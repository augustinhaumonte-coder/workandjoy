/* Bloc-notes de relecture, pour la préversion uniquement.
 *
 * Ajoute un bouton flottant qui permet de laisser un commentaire sur la page
 * en cours. Si du texte est sélectionné au moment du clic, il est joint au
 * commentaire, ce qui évite les retours du type "il y a une faute quelque part".
 *
 * Les commentaires partent dans Netlify Forms, formulaire "avis-maquette".
 * Rien à installer, rien à payer, et aucune inscription pour la relectrice.
 *
 * Le script refuse de s'afficher sur le domaine public, pour ne jamais
 * apparaître devant un vrai visiteur même si on oublie de le retirer.
 * Partout ailleurs il s'affiche : fichier ouvert en local, serveur local,
 * préversion Netlify. À supprimer malgré tout le jour de la mise en ligne.
 */
(function () {
  if (/(^|\.)workandjoy\.org$/.test(location.hostname)) return;

  var css = document.createElement("style");
  css.textContent = [
    ".rv-btn{position:fixed;right:18px;bottom:18px;z-index:9000;font-family:inherit;font-weight:700;",
    "font-size:.85rem;letter-spacing:.06em;text-transform:uppercase;padding:.8rem 1.3rem;border-radius:999px;",
    "border:2px solid #16152e;background:#ffed00;color:#16152e;cursor:pointer;box-shadow:0 8px 24px rgba(0,0,0,.22)}",
    ".rv-btn:active{transform:translateY(1px)}",
    ".rv-panel{position:fixed;right:18px;bottom:76px;z-index:9001;width:min(380px,calc(100vw - 36px));",
    "background:#fff;color:#16152e;border:1px solid #d8d2c8;box-shadow:0 18px 50px rgba(0,0,0,.25);padding:1.1rem}",
    ".rv-panel[hidden]{display:none}",
    ".rv-panel h2{font-size:1rem;margin:0 0 .25rem}",
    ".rv-panel p{font-size:.82rem;color:#4d4b63;margin:0 0 .8rem;line-height:1.45}",
    ".rv-panel label{display:block;font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;",
    "font-weight:800;margin:0 0 .25rem}",
    ".rv-panel input,.rv-panel textarea{font:inherit;font-size:.9rem;width:100%;box-sizing:border-box;",
    "border:1px solid #9b99ad;padding:.5rem .6rem;margin:0 0 .7rem;background:#fff;color:#16152e}",
    ".rv-panel textarea{resize:vertical}",
    ".rv-quote{background:#f4f1ec;border-left:4px solid #ffed00;padding:.5rem .7rem;margin:0 0 .8rem;",
    "font-size:.82rem;font-style:italic;max-height:5.5rem;overflow:auto}",
    ".rv-row{display:flex;gap:.6rem;align-items:center}",
    ".rv-drop{display:block;margin-top:.4rem;font:inherit;font-size:.72rem;font-style:normal;background:none;",
    "border:0;padding:0;color:#4d4b63;text-decoration:underline;cursor:pointer}",
    ".rv-send{font:inherit;font-weight:800;font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;",
    "padding:.6rem 1.1rem;border-radius:999px;border:2px solid #16152e;background:#ffed00;cursor:pointer}",
    ".rv-cancel{font:inherit;font-size:.82rem;background:none;border:0;color:#4d4b63;cursor:pointer;text-decoration:underline}",
    ".rv-msg{font-size:.82rem;margin:.6rem 0 0}"
  ].join("");
  document.head.appendChild(css);

  var btn = document.createElement("button");
  btn.className = "rv-btn";
  btn.type = "button";
  btn.textContent = "Commenter";

  var panel = document.createElement("div");
  panel.className = "rv-panel";
  panel.hidden = true;
  panel.innerHTML =
    '<h2>Votre remarque</h2>' +
    '<p>Sélectionnez un passage avant de cliquer et il sera joint automatiquement.</p>' +
    '<div class="rv-quote" hidden></div>' +
    '<label for="rv-nom">Qui écrit</label>' +
    '<input id="rv-nom" type="text" autocomplete="name">' +
    '<label for="rv-txt">Ce qui ne va pas, ou ce qui manque</label>' +
    '<textarea id="rv-txt" rows="4"></textarea>' +
    '<div class="rv-row"><button class="rv-send" type="button">Envoyer</button>' +
    '<button class="rv-cancel" type="button">Annuler</button></div>' +
    '<p class="rv-msg" role="status"></p>';

  document.body.appendChild(btn);
  document.body.appendChild(panel);

  var quote = panel.querySelector(".rv-quote");
  var nom = panel.querySelector("#rv-nom");
  var txt = panel.querySelector("#rv-txt");
  var msg = panel.querySelector(".rv-msg");
  var selection = "";
  var derniere = "";

  // Sur téléphone, toucher le bouton efface la sélection avant que le clic
  // ne soit traité. On retient donc la dernière sélection non vide.
  document.addEventListener("selectionchange", function () {
    var t = String(window.getSelection()).trim();
    if (t) derniere = t.slice(0, 600);
  });

  try { nom.value = localStorage.getItem("rv-nom") || ""; } catch (e) {}

  function montrerCitation() {
    quote.hidden = !selection;
    quote.innerHTML = "";
    if (!selection) return;
    quote.appendChild(document.createTextNode("« " + selection + " »"));
    var del = document.createElement("button");
    del.type = "button";
    del.className = "rv-drop";
    del.textContent = "retirer ce passage";
    del.addEventListener("click", function () { selection = ""; montrerCitation(); });
    quote.appendChild(del);
  }

  btn.addEventListener("click", function () {
    if (!panel.hidden) { panel.hidden = true; return; }
    selection = String(window.getSelection()).trim().slice(0, 600) || derniere;
    montrerCitation();
    msg.textContent = "";
    panel.hidden = false;
    txt.focus();
  });

  panel.querySelector(".rv-cancel").addEventListener("click", function () {
    panel.hidden = true;
  });

  panel.querySelector(".rv-send").addEventListener("click", function () {
    if (!txt.value.trim()) { msg.textContent = "Il manque la remarque."; return; }
    try { localStorage.setItem("rv-nom", nom.value); } catch (e) {}
    msg.textContent = "Envoi...";
    // le passage sélectionné est intégré au message plutôt qu'envoyé à part :
    // un seul champ, donc rien qui puisse se perdre en route
    var corps = selection
      ? "Passage visé :\n« " + selection + " »\n\nRemarque :\n" + txt.value
      : txt.value;
    var data = new URLSearchParams({
      "form-name": "avis-maquette",
      nom: nom.value || "anonyme",
      page: document.title + "  (" + location.pathname + ")",
      message: corps
    });
    fetch("/", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: data.toString()
    }).then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      msg.textContent = "C'est noté, merci.";
      txt.value = "";
      selection = ""; derniere = ""; montrerCitation();
      setTimeout(function () { panel.hidden = true; }, 1200);
    }).catch(function (err) {
      var local = location.protocol === "file:" || location.hostname === "localhost";
      msg.textContent = local
        ? "Envoi impossible en local, c'est normal. Le formulaire ne fonctionne qu'une fois le site en ligne."
        : "Échec de l'envoi (" + err.message + "). Votre texte est conservé, ne fermez pas.";
    });
  });
})();
