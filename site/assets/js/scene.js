/* Animations au défilement de Work and Joy.

   1. Le fil conducteur, sur toutes les pages : le O jaune du logo quitte
      l'en-tête et descend la page dans la marge. À des moments choisis (les
      paliers), la page se fige et la bille traverse d'une marge à l'autre en
      roulant sur l'arête d'une section. Elle finit dans le bouton « Prendre
      rendez-vous » du bas de page : la page se fige jusqu'à son arrivée, puis
      reste figée encore un peu.
   2. La scène de la méthode, sur l'accueil : la bille entre dans le carré et
      devient la grosse bille du logo, qui se construit en trois temps séparés
      par des pauses. À la fin, la bille en haut à droite tombe de sa planche
      et reprend la descente jusqu'au bouton.

   Les arrêts sont obtenus par du positionnement « sticky » natif : c'est le
   navigateur qui fige la page, pas du JavaScript, donc rien ne tremble sur
   téléphone. Aucun contenu n'est masqué. Sans ce script, ou si le visiteur a
   demandé moins d'animations, la page garde sa mise en page d'origine. */
(function () {
  "use strict";
  if (!window.requestAnimationFrame || !document.querySelector) return;
  if (window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  /* ---------- réglages, en hauteurs d'écran ---------- */
  var LINE = 0.42;          /* hauteur à l'écran de l'arête pendant un palier */
  var HOLD_ROLL = 0.55;     /* défilement pendant lequel la page reste figée à un palier */
  var HOLD_CTA = 1.0;       /* idem à l'arrivée sur le bouton : moitié trajet, moitié latence */
  var GAP = 1.2;            /* distance minimale entre deux paliers */
  var MEET = 0.80;          /* hauteur à l'écran où la bille se pose sur l'arête qui monte */
  var DROP = 0.40;          /* défilement pendant lequel elle tombe vite, juste après une traversée */
  /* la scène : les pauses sont des zones où l'on défile sans que rien ne bouge */
  var SEGMENTS = [
    { pause: 0.40 },  /* arrêt sur le désordre, la bille arrive dans le carré */
    { act: 0.45 },    /* étape 1 : la grosse bille roule au centre */
    { pause: 0.35 },
    { act: 0.60 },    /* étape 2 : la table se pose, trois billes sautent dessus */
    { pause: 0.35 },
    { act: 0.55 },    /* étape 3 : la seconde planche et les dernières billes */
    { pause: 0.75 }   /* arrêt sur le logo terminé, puis la bille du haut repart */
  ];

  var NS = "http://www.w3.org/2000/svg", docEl = document.documentElement;
  function el(name, attrs) {
    var n = document.createElementNS(NS, name);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    return n;
  }
  function div(cls) { var d = document.createElement("div"); d.className = cls; return d; }
  function clamp(v, a, b) { a = a === undefined ? 0 : a; b = b === undefined ? 1 : b; return v < a ? a : v > b ? b : v; }
  function lerp(a, b, t) { return a + (b - a) * t; }
  function io(t) { return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }
  function back(t) { var c = 1.9; return 1 + (c + 1) * Math.pow(t - 1, 3) + c * Math.pow(t - 1, 2); }
  function docTop(n) { return n.getBoundingClientRect().top + window.pageYOffset; }

  /* ==================================================================
     La scène de la méthode
     ================================================================== */
  var TOTAL = SEGMENTS.reduce(function (s, g) { return s + (g.pause || g.act); }, 0);

  /* Coordonnées relevées dans logo.svg, ramenées au carré violet (290 x 290).
     « w » est la fenêtre de mouvement de la pièce, en temps du récit :
     0 à 1 pour l'étape 1, 1 à 2 pour l'étape 2, 2 à 3 pour l'étape 3. */
  var PIECES = [
    { id: "Y0", k: "bj", r: 30.01, to: [143.16, 208.23, 0],    from: [240, 258, 0],  w: [0.05, 0.95], hop: 0 },
    { id: "Y1", k: "bj", r: 23.09, to: [116.36, 152.60, 0],    from: [52, 84, 0],    w: [1.56, 1.98], hop: 34 },
    { id: "C1", k: "bc", r: 10.27, to: [167.71, 162.87, 0],    from: [252, 146, 0],  w: [1.28, 1.66], hop: 46 },
    { id: "C2", k: "bc", r: 10.27, to: [194.88, 162.87, 0],    from: [28, 277, 0],   w: [1.42, 1.80], hop: 40 },
    { id: "P1", k: "pl",           to: [143.47, 175.63, 0],    from: [94, 236, 27],  w: [1.00, 1.42], hop: 0 },
    { id: "Y2", k: "bj", r: 17.95, to: [191.10, 118.36, 0],    from: [38, 176, 0],   w: [2.34, 2.76], hop: 40 },
    { id: "C3", k: "bc", r: 10.27, to: [84.70, 107.26, 0],     from: [124, 34, 0],   w: [2.52, 2.98], hop: 26 },
    { id: "P2", k: "pl",           to: [139.45, 129.47, 10.5], from: [198, 66, -54], w: [2.00, 2.48], hop: 0 }
  ];
  var PLANK = { l: 152.54, h: 2.53 };
  var Y0 = PIECES[0], Y2 = PIECES[5];
  var PLANK_END = [221.6, 124.0];   /* centre de la bille du haut quand elle arrive au bout de sa planche */

  /* avancement du défilement (0 à 1) -> temps du récit (0 à 3) */
  var CUTS = [], STEP_AT = [0];
  (function () {
    var acc = 0, act = 0;
    SEGMENTS.forEach(function (g) {
      var len = (g.pause || g.act) / TOTAL;
      CUTS.push({ a: acc, b: acc + len, act: g.act ? act : -1, t: act });
      /* l'étape suivante s'allume au milieu de la pause qui la précède */
      if (g.pause && act > 0 && act < 3) STEP_AT.push(acc + len / 2);
      if (g.act) act++;
      acc += len;
    });
  })();
  function story(p) {
    for (var i = 0; i < CUTS.length; i++) {
      var c = CUTS[i];
      if (p <= c.b || i === CUTS.length - 1) return c.act < 0 ? c.t : c.act + clamp((p - c.a) / (c.b - c.a));
    }
    return 3;
  }
  var LASTP = CUTS[CUTS.length - 1];
  var ARRIVAL = [CUTS[0].b * 0.12, CUTS[0].b * 0.85];                                   /* la bille entre dans le carré */
  var DEPART = [lerp(LASTP.a, LASTP.b, 0.32), lerp(LASTP.a, LASTP.b, 0.9)];             /* la bille du haut en repart */

  function buildScene(sec) {
    var h2 = sec.querySelector("h2"), temps = sec.querySelector(".temps");
    if (!h2 || !temps) return null;
    var pin = div("scene__pin"), art = div("scene__art"), copy = div("scene__copy");
    art.setAttribute("aria-hidden", "true");
    var svg = el("svg", { viewBox: "0 0 290 290", focusable: "false" });
    PIECES.forEach(function (p, i) {
      p.n = p.k === "pl"
        ? el("rect", { "class": "pl", x: -PLANK.l / 2, y: -PLANK.h / 2, width: PLANK.l, height: PLANK.h })
        : el("circle", { "class": p.k, r: p.r });
      p.ph = i * 1.7 + 0.4; /* déphasage du flottement */
      svg.appendChild(p.n);
    });
    art.appendChild(svg);
    copy.appendChild(h2); copy.appendChild(temps);
    pin.appendChild(art); pin.appendChild(copy);
    sec.appendChild(pin);
    sec.classList.add("scene", "is-live");
    sec.style.height = "calc(100svh * " + (1 + TOTAL).toFixed(2) + ")";
    return { sec: sec, pin: pin, art: art, items: temps.querySelectorAll(".temps__item"), p: 0, step: -1, S0: 0, travel: 1 };
  }

  function drawScene(s, time, hide) {
    var T = story(s.p);
    for (var i = 0; i < PIECES.length; i++) {
      var q = PIECES[i];
      var t = clamp((T - q.w[0]) / (q.w[1] - q.w[0]));
      var e = io(t), x, y, a;
      x = lerp(q.from[0], q.to[0], e);
      y = lerp(q.from[1], q.to[1], e) - q.hop * Math.sin(Math.PI * t);
      a = lerp(q.from[2], q.to[2], q.k === "pl" ? back(t) : e);
      /* tant qu'une pièce n'est pas posée, elle flotte un peu. La grosse bille, elle, roule au sol. */
      var loose = q === Y0 ? 0 : 1 - e;
      if (loose > 0.001) {
        x += loose * 2.6 * Math.sin(time * 0.0011 + q.ph);
        y += loose * 2.2 * Math.cos(time * 0.0013 + q.ph * 1.3);
        if (q.k === "pl") a += loose * 3.5 * Math.sin(time * 0.0009 + q.ph);
      }
      q.n.setAttribute("transform", "translate(" + x.toFixed(2) + " " + y.toFixed(2) + ") rotate(" + a.toFixed(2) + ")");
    }
    Y0.n.style.visibility = hide.y0 ? "hidden" : "";
    Y2.n.style.visibility = hide.y2 ? "hidden" : "";
    var step = s.p >= STEP_AT[2] ? 2 : s.p >= STEP_AT[1] ? 1 : 0;
    if (step !== s.step) {
      s.step = step;
      for (var j = 0; j < s.items.length; j++) s.items[j].classList.toggle("is-on", j === step);
    }
  }

  /* ==================================================================
     Le fil conducteur et les paliers
     ================================================================== */
  var scene = null, F = null, P = null, V = {};
  var main = document.querySelector("main"), foot = document.querySelector("body > footer");
  var probe = div("pal__probe"); document.body.appendChild(probe);

  function buildFil() {
    var o = document.querySelector(".nav .mark__o"), nav = document.querySelector(".nav"), navIn = document.querySelector(".nav__in");
    if (!o || !nav || !navIn || !main) return null;
    var n = div("fil"); n.setAttribute("aria-hidden", "true");
    document.body.appendChild(n);
    return { n: n, o: o, nav: nav, navIn: navIn, shown: false, out: false, top: false, calling: false };
  }

  /* bas du dernier élément visible d'une section (texte, image, bouton), en coordonnées d'écran */
  function inkBottom(sec) {
    var m = -Infinity, k, r, n, rg = document.createRange();
    var w = document.createTreeWalker(sec, NodeFilter.SHOW_TEXT, null, false);
    while ((n = w.nextNode())) {
      if (!n.nodeValue.trim()) continue;
      rg.selectNodeContents(n);
      var rs = rg.getClientRects();
      for (k = 0; k < rs.length; k++) if (rs[k].bottom > m) m = rs[k].bottom;
    }
    var els = sec.querySelectorAll("img, svg, .btn, input, textarea");
    for (k = 0; k < els.length; k++) { r = els[k].getBoundingClientRect(); if (r.height && r.bottom > m) m = r.bottom; }
    return m;
  }

  /* remet la page dans son état d'origine (avant de recalculer les paliers) */
  function teardown() {
    if (!P) return;
    P.kids.forEach(function (k) { main.appendChild(k); });
    P.boxes.forEach(function (b) { if (b.parentNode) b.parentNode.removeChild(b); });
    if (P.footBox) {
      P.footBox.parentNode.insertBefore(foot, P.footBox);
      P.footBox.parentNode.removeChild(P.footBox);
      foot.classList.remove("pal__foot"); foot.style.top = "";
    }
    P = null;
  }

  /* Choisit les paliers et enveloppe les sections. Chaque palier fige deux
     blocs en même temps : celui du dessus (son bas reste sur la ligne) et
     celui du dessous (son haut reste sur la ligne). */
  function setup() {
    teardown();
    var vh = probe.offsetHeight || window.innerHeight, W = docEl.clientWidth;
    V = { vh: vh, W: W, T: Math.round(LINE * vh), pinTop: 0 };
    if (scene) V.pinTop = parseFloat(getComputedStyle(scene.pin).top) || 0;
    if (!F) { refresh(); return; }

    var contentLeft = F.navIn.getBoundingClientRect().left + parseFloat(getComputedStyle(F.navIn).paddingLeft);
    var o = F.o.getBoundingClientRect();
    F.navB = F.nav.offsetHeight - 1;
    F.r = clamp(contentLeft / 2 - 3, 5, 9);
    F.xL = contentLeft - Math.min(contentLeft / 2, 44); F.xR = W - F.xL;
    F.sA = 0.2 * vh;                       /* défilement pendant lequel elle quitte l'en-tête */
    F.yb = V.T - F.r - 1;                  /* hauteur à l'écran où elle se tient : posée sur la ligne */
    F.ox = o.left + o.width / 2; F.oy = o.top + o.height / 2; F.or = o.width / 2;

    var kids = Array.prototype.slice.call(main.children);
    var tops = kids.map(docTop);
    var btn = main.querySelector(".final .btn");
    var cta = !!(btn && foot);
    var yBtn = cta ? docTop(btn) + btn.offsetHeight / 2 : Infinity;
    var sceneTop = scene ? docTop(scene.sec) : Infinity;

    /* les arêtes : là où le fond change entre deux sections, ou une bordure.
       On n'en garde que quelques-unes, bien espacées : ce sont les paliers. */
    var L = [], prev = -Infinity;
    for (var i = 1; i < kids.length; i++) {
      var a = getComputedStyle(kids[i - 1]), b = getComputedStyle(kids[i]);
      if (!(a.backgroundColor !== b.backgroundColor || parseFloat(b.borderTopWidth) > 0 || parseFloat(a.borderBottomWidth) > 0)) continue;
      var y = tops[i];
      if (y - V.T < F.sA + 0.05 * vh) continue;        /* trop tôt : la bille n'a pas fini de quitter l'en-tête */
      if (y - prev < GAP * vh) continue;               /* trop près du palier précédent */
      if (scene && y > sceneTop - GAP * vh) continue;  /* rien juste avant la scène, ni après */
      if (yBtn - y < 0.9 * vh) continue;               /* trop près du bouton final */
      /* la bille roule sur l'arête, donc dans le bas de la section du dessus : il lui faut de la place sous le texte */
      if (kids[i - 1].getBoundingClientRect().bottom - inkBottom(kids[i - 1]) < 2 * F.r + 12) continue;
      L.push(i); prev = y;
    }
    /* sur l'accueil, la bille doit arriver du côté du carré, pour ne pas survoler le texte */
    if (scene) {
      var art = scene.art.getBoundingClientRect(), mid = art.left + art.width / 2;
      var want = Math.abs(mid - W / 2) < 20 ? -1 : mid < W / 2 ? 0 : 1;
      if (want >= 0 && L.length % 2 !== want && L.length) L.pop();
    }

    var Hroll = Math.round(HOLD_ROLL * vh), Hc = Math.round(HOLD_CTA * vh);
    P = { kids: kids, boxes: [], groups: [], holds: [], cta: null, footBox: null, Hroll: Hroll, Hc: Hc, btn: cta ? btn : null };
    var cuts = [0].concat(L, [kids.length]), n = L.length;
    for (var g = 0; g <= n; g++) {
      var G = { low: div("pal__low"), up: div("pal__up"), box: div("pal__box") };
      kids.slice(cuts[g], cuts[g + 1]).forEach(function (k) { G.low.appendChild(k); });
      if (g > 0) {
        var lowbox = div("pal__lowbox"), sp = div("pal__sp");
        sp.style.height = Hroll + "px";
        lowbox.appendChild(G.low); lowbox.appendChild(sp); G.up.appendChild(lowbox);
        G.low.style.top = V.T + "px";
        G.box.style.marginTop = -Hroll + "px";
      } else { G.up.appendChild(G.low); }
      G.box.appendChild(G.up);
      if (g < n || cta) {
        var sp2 = div("pal__sp"); sp2.style.height = (g < n ? Hroll : Hc) + "px";
        G.box.appendChild(sp2);
      }
      main.appendChild(G.box);
      P.boxes.push(G.box); P.groups.push(G);
    }
    if (cta) {
      /* le pied de page se fige lui aussi pendant l'arrêt sur le bouton */
      var fb = div("pal__box"), sp3 = div("pal__sp");
      sp3.style.height = Hc + "px"; fb.style.marginTop = -Hc + "px";
      foot.parentNode.insertBefore(fb, foot);
      fb.appendChild(foot); fb.appendChild(sp3);
      foot.classList.add("pal__foot");
      P.footBox = fb;
    }
    refresh();
  }

  /* Recalcule ce qui dépend des hauteurs (elles bougent quand les polices arrivent) :
     les crans « sticky » et les positions de défilement de chaque événement. */
  function refresh() {
    if (!P) {
      if (scene) {
        scene.S0 = docTop(scene.sec) - V.pinTop;
        scene.travel = Math.max(1, scene.sec.offsetHeight - scene.pin.offsetHeight);
      }
      return;
    }
    var yNat = docTop(main), sumH = 0, n = P.groups.length - 1;
    P.holds = [];
    P.groups.forEach(function (G, g) {
      var h = G.low.offsetHeight;
      G.yNat = yNat; G.before = sumH;
      if (scene && G.low.contains(scene.sec)) {
        scene.S0 = yNat + (scene.sec.getBoundingClientRect().top - G.low.getBoundingClientRect().top) + sumH - V.pinTop;
        scene.travel = Math.max(1, scene.sec.offsetHeight - scene.pin.offsetHeight);
        /* après la scène, la bille se tient plus bas : sous le bout de la planche d'où elle tombe */
        var art = scene.art, sc = art.offsetWidth / 290;
        var artTop = V.pinTop + (art.getBoundingClientRect().top - scene.pin.getBoundingClientRect().top);
        V.y2 = Math.max(0.6 * V.vh, artTop + (PLANK_END[1] + Y2.r) * sc + 24);
      }
      if (g < n) {
        G.up.style.top = (V.T - G.up.offsetHeight) + "px";
        P.holds.push({ s: yNat + h - V.T + sumH, len: P.Hroll });
        sumH += P.Hroll;
      } else if (P.btn) {
        var r = P.btn.getBoundingClientRect();
        var cy = r.top + r.height / 2 - G.low.getBoundingClientRect().top;   /* le bouton, mesuré dans son bloc */
        var below = (h - cy) + foot.offsetHeight;
        var ride = scene ? V.y2 : F.yb;
        /* le bouton s'arrête à la hauteur de la bille ; plus bas si la fin de page est trop courte pour remplir l'écran */
        var sec = P.btn.closest ? P.btn.closest("section") : null;
        var head = sec ? r.top + r.height / 2 - sec.getBoundingClientRect().top : 0;   /* le titre du bloc doit rester sous l'en-tête */
        var Tb = Math.min(Math.max(ride, V.vh - below, F.navB + 28 + head), V.vh - 70);
        if (scene) V.y2 = Tb;
        G.up.style.top = (Tb - (G.up.offsetHeight - h) - cy) + "px";
        foot.style.top = (Tb + (h - cy)) + "px";
        P.cta = { s: yNat + cy - Tb + sumH, len: P.Hc, Tb: Tb };
      }
      yNat += h;
    });
    /* les jalons du trajet, dans l'ordre : paliers, scène, bouton */
    var miles = P.holds.map(function (hd) { return { s: hd.s, len: hd.len, line: V.T, off: F.r + 1 }; });
    if (scene) miles.push({ s: scene.S0, len: scene.travel, scene: true, out: V.y2 });
    if (P.cta) miles.push({ s: P.cta.s, len: P.cta.len, line: P.cta.Tb, off: 0 });
    P.miles = miles.sort(function (a, b) { return a.s - b.s; });
    /* si la première arête est proche, la bille tombe de l'en-tête directement dessus, d'un seul mouvement */
    F.sFall = F.sA;
    var m0 = P.miles[0];
    if (m0 && !m0.scene) {
      var sm0 = m0.s - (Math.max(MEET * V.vh, m0.line) - m0.line);
      if (sm0 > F.sA && sm0 < F.sA + 0.6 * V.vh) F.sFall = sm0;
    }
  }

  /* Hauteur de la bille à l'écran quand elle est dans la marge.
     Après une traversée elle tombe, puis descend doucement ; quand l'arête suivante
     monte jusqu'à elle, elle s'y pose et se laisse porter jusqu'au palier.
     « ss » (défilement lissé) rythme ses mouvements propres, pour qu'ils restent calés sur
     ses traversées ; « s » (défilement réel) donne la position de l'arête, qui bouge avec la page. */
  function rideY(s, ss) {
    var sa = F.sFall, ya = F.yb, vh = V.vh;
    function fall(sEnd, yEnd) {
      if (sEnd <= sa) return yEnd;
      var u = clamp((ss - sa) / (sEnd - sa)), q = clamp((ss - sa) / Math.min(DROP * vh, sEnd - sa));
      return ya + (yEnd - ya) * (0.5 * (1 - (1 - q) * (1 - q)) + 0.5 * u);
    }
    for (var i = 0; i < P.miles.length; i++) {
      var m = P.miles[i];
      if (ss < m.s) {
        if (m.scene) return fall(m.s, 0.72 * vh);          /* rien à rejoindre : elle descend jusqu'à son entrée dans le carré */
        var M = Math.max(MEET * vh, m.line);
        /* elle ne peut pas être plus bas que l'arête qui monte : dès qu'elles se touchent, l'arête la porte */
        return Math.min(fall(m.s - (M - m.line), M - m.off), Math.max(m.line, m.line + (m.s - s)) - m.off);
      }
      if (ss <= m.s + m.len) return m.scene ? m.out : m.line - m.off;   /* page figée */
      sa = m.s + m.len; ya = m.scene ? m.out : m.line - m.off;
    }
    return ya;
  }

  /* position de défilement qui amène un élément sous l'en-tête, paliers compris */
  function scrollPosFor(target) {
    if (!P || target === main || target.contains(main)) return null;
    if (P.cta && P.btn && target.contains(P.btn)) return P.cta.s + 0.55 * P.cta.len;  /* le bloc final : bille arrivée, bouton en place */
    for (var g = 0; g < P.groups.length; g++) {
      var G = P.groups[g];
      if (G.low.contains(target)) {
        return G.yNat + (target.getBoundingClientRect().top - G.low.getBoundingClientRect().top) + G.before - F.navB - 12;
      }
    }
    return null;
  }

  function X(side) { return side ? F.xR : F.xL; }

  /* s : défilement réel ; ss : défilement lissé, qui rythme les déplacements de la bille */
  function drawFil(s, ss, hide) {
    var x = F.xL, y = rideY(Math.max(s, F.sFall), Math.max(ss, F.sFall)), r = F.r, show = true, top = false, calling = false, side = 0, t, u, e;
    hide.y0 = !!scene; hide.y2 = false;
    if (ss < 1) {
      show = false;                                   /* elle est dans le logo de l'en-tête */
    } else if (ss < F.sFall) {
      /* elle tombe sur le bord de l'en-tête, roule jusqu'à la marge, puis se laisse tomber */
      var rm = Math.min(F.r, 6.5), sB = 0.2 * F.sA, sC = 0.6 * F.sA;
      top = true;
      if (ss < sB) { u = ss / sB; x = F.ox; y = lerp(F.oy, F.navB - rm, u * u); r = lerp(F.or, rm, u); }
      else if (ss < sC) { u = (ss - sB) / (sC - sB); x = lerp(F.ox, F.xL, io(u)); y = F.navB - rm; r = rm; }
      else { u = (ss - sC) / (F.sFall - sC); x = F.xL; y = lerp(F.navB - rm, rideY(Math.max(s, F.sFall), F.sFall), u * u); r = lerp(rm, F.r, Math.min(1, u * 2)); top = u < 0.15; }
    } else {
      /* les paliers : la page est figée, la bille traverse sur l'arête */
      for (var k = 0; k < P.holds.length; k++) {
        t = (ss - P.holds[k].s) / P.holds[k].len;
        if (t <= 0) break;
        u = clamp((t - 0.06) / 0.76);
        x = lerp(X(side), X(1 - side), u * u * (3 - 2 * u));
        side = 1 - side;
      }
      if (scene && ss > scene.S0 + scene.travel) {
        /* la scène est passée : la bille du haut a quitté le logo, elle descend dans la marge de droite */
        hide.y0 = false; hide.y2 = true; side = 1; x = F.xR;
      } else if (scene && ss >= scene.S0) {
        var a = scene.art.getBoundingClientRect(), sc = a.width / 290;
        var arr = clamp((scene.p - ARRIVAL[0]) / (ARRIVAL[1] - ARRIVAL[0]));
        if (arr < 1) {
          /* elle entre dans le carré et devient la grosse bille du logo */
          e = io(arr);
          x = lerp(X(side), a.left + Y0.from[0] * sc, e);
          y = lerp(rideY(scene.S0 - 0.01, scene.S0 - 0.01), a.top + Y0.from[1] * sc, e);
          r = lerp(F.r, Y0.r * sc, e);
        } else {
          hide.y0 = false;
          var dep = clamp((scene.p - DEPART[0]) / (DEPART[1] - DEPART[0]));
          if (dep <= 0) {
            show = false;                             /* elle est dans le logo */
          } else {
            /* la bille du haut roule au bout de sa planche, tombe, et rejoint la marge de droite */
            hide.y2 = true;
            var ex = a.left + PLANK_END[0] * sc, ey = a.top + PLANK_END[1] * sc, R = Y2.r * sc;
            if (dep < 0.3) {
              u = dep / 0.3; u = u * u;
              x = lerp(a.left + Y2.to[0] * sc, ex, u); y = lerp(a.top + Y2.to[1] * sc, ey, u); r = R;
            } else {
              u = (dep - 0.3) / 0.7;
              x = lerp(ex, F.xR, u); y = ey + (V.y2 - ey) * u * u; r = lerp(R, F.r, u);
            }
          }
          side = 1;
        }
      }
      /* l'arrivée : la page est figée, la bille roule jusqu'au bouton et y entre */
      if (P.cta && show) {
        t = (ss - P.cta.s) / P.cta.len;
        if (t > 0) {
          u = clamp((t - 0.05) / 0.45); e = io(u);
          var rb = P.btn.getBoundingClientRect();
          x = lerp(x, side ? rb.right - F.r - 6 : rb.left + F.r + 6, e);
          y = lerp(y, rb.top + rb.height / 2, e);
          if (u >= 1) { show = false; calling = t < 1.5; }
        }
      }
    }

    if (show !== F.shown) { F.shown = show; F.n.style.visibility = show ? "visible" : "hidden"; }
    if (top !== F.top) { F.top = top; F.n.classList.toggle("is-top", top); }
    var out = ss >= 1;
    if (out !== F.out) { F.out = out; docEl.classList.toggle("fil-out", out); }
    if (P.btn && calling !== F.calling) { F.calling = calling; P.btn.classList.toggle("is-calling", calling); }
    if (show) {
      F.n.style.width = F.n.style.height = (2 * r).toFixed(1) + "px";
      F.n.style.transform = "translate(" + (x - r).toFixed(1) + "px," + (y - r).toFixed(1) + "px)";
    }
  }

  /* ==================================================================
     Mise en route
     ================================================================== */
  var m = document.getElementById("methode");
  if (m && m.hasAttribute("data-scene")) scene = buildScene(m);
  F = buildFil();
  if (!scene && !F) return;

  var ss = window.pageYOffset, running = false, sceneOn = false, hide = { y0: false, y2: false };
  function frame(time) {
    var s = window.pageYOffset;
    /* lissage : doux quand on défile lentement, plus nerveux quand le retard grandit, pour que la bille ne traîne pas */
    ss += (s - ss) * (0.16 + Math.min(0.6, Math.abs(s - ss) / 500));
    if (Math.abs(s - ss) < 0.3) ss = s;
    if (scene) scene.p = clamp((ss - scene.S0) / scene.travel);
    if (F && P) drawFil(s, ss, hide);
    if (scene) drawScene(scene, time, hide);
    /* la boucle s'arrête dès que plus rien ne bouge */
    if (ss !== s || sceneOn) requestAnimationFrame(frame); else running = false;
  }
  function start() { if (!running) { running = true; requestAnimationFrame(frame); } }

  setup();
  var lastW = V.W, lastVh = V.vh, pending = 0, full = false;
  /* regroupe les recalculs sur une image ; une reconstruction complète demandée entre-temps n'est jamais perdue */
  function later(fn) {
    if (fn === setup) full = true;
    if (pending) return;
    pending = 1;
    requestAnimationFrame(function () { pending = 0; if (full) { full = false; setup(); } else refresh(); start(); });
  }
  window.addEventListener("scroll", start, { passive: true });
  window.addEventListener("resize", function () {
    /* sur téléphone la barre d'adresse fait varier la hauteur en permanence : on ne refait tout que si l'écran change vraiment */
    var vh = probe.offsetHeight || window.innerHeight, W = docEl.clientWidth;
    if (W !== lastW || vh !== lastVh) { lastW = W; lastVh = vh; later(setup); } else later(refresh);
  });
  window.addEventListener("load", function () { later(refresh); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { later(refresh); });
  if ("ResizeObserver" in window && main) new ResizeObserver(function () { later(refresh); }).observe(main);
  if (scene && "IntersectionObserver" in window) {
    new IntersectionObserver(function (en) { sceneOn = en[0].isIntersecting; if (sceneOn) start(); }, { rootMargin: "200px 0px" }).observe(scene.sec);
  } else if (scene) { sceneOn = true; }

  /* les liens internes (#contact, etc.) visent une position qui tient compte des paliers */
  function goTo(hash, ev) {
    if (!hash || hash.length < 2) return;
    var target = null;
    try { target = document.querySelector(hash); } catch (err) { return; }
    var pos = target && scrollPosFor(target);
    if (pos === null || pos === undefined) return;
    if (ev) ev.preventDefault();
    window.scrollTo(0, Math.max(0, pos));
  }
  document.addEventListener("click", function (ev) {
    var a = ev.target.closest ? ev.target.closest('a[href^="#"]') : null;
    if (a) goTo(a.getAttribute("href"), ev);
  });
  if (location.hash) window.addEventListener("load", function () { setTimeout(function () { goTo(location.hash); }, 60); });
  start();
})();
