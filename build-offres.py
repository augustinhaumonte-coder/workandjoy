#!/usr/bin/env python3
"""Génère les quatre pages d'offres depuis une coquille commune.

Script jetable : les fichiers HTML produits sont la source. Quand le site
passera sous 11ty, l'en-tête et le pied de page deviendront des includes et
ce script disparaîtra.
"""
import html, pathlib

BOOKING = ("https://bookings.cloud.microsoft/bookwithme/user/"
           "a25ae09279404c6988d7f9df4378557e@workandjoy.org/meetingtype/"
           "o_2nV1khmUG8mVr6vYahlA2?anonymous&amp;ismsaljsauthenabled&amp;ep=mcard")

NAV = """<header class="nav">
  <div class="nav__in">
    <a class="mark" href="../index.html" aria-label="Work and Joy, accueil">
      <span>WORK</span><span class="mark__amp">&amp;</span><span>J<span class="mark__o"></span>Y</span>
    </a>
    <input type="checkbox" id="menu" class="nav__toggle">
    <label for="menu" class="nav__burger" aria-hidden="true"><span></span><span></span><span></span></label>
    <nav class="nav__links">
      <a href="../index.html#accompagnements">Accompagnements</a>
      <a href="../index.html#methode">Méthode</a>
      <a href="../a-propos/index.html">À propos</a>
      <a href="../temoignages/index.html">Témoignages</a>
      <a class="btn btn--sm" href="#contact">Prendre rendez-vous</a>
    </nav>
  </div>
</header>"""

FOOT = """<footer class="foot">
  <div class="foot__in">
    <img class="foot__logo" src="../assets/img/logo.svg" width="160" height="197" alt="Work and Joy" loading="lazy">
    <div class="foot__col">
      <h4>Work and Joy</h4>
      <p>121 avenue Clot Bey<br>13008 Marseille</p>
      <p><a href="tel:+33624310759">06 24 31 07 59</a><br><a href="mailto:contact@workandjoy.org">contact@workandjoy.org</a></p>
    </div>
    <div class="foot__col">
      <h4>Accompagnements</h4>
      <p>
        <a href="../seminaire-equipe/index.html">Séminaire d'équipe</a><br>
        <a href="../accompagnement-dirigeant/index.html">Accompagnement du dirigeant</a><br>
        <a href="../accompagnement-equipes/index.html">Accompagnement des équipes</a><br>
        <a href="../formation-management/index.html">Formation</a><br>
        <a href="../bilan-de-competences/">Bilan de compétences</a>
      </p>
    </div>
    <div class="foot__col">
      <h4>Work and Joy</h4>
      <p>
        <a href="../a-propos/index.html">À propos</a><br>
        <a href="../temoignages/index.html">Témoignages</a><br>
        <a href="https://www.linkedin.com/">LinkedIn</a><br>
        <a href="../mentions-legales/">Mentions légales</a><br>
        <a href="../cgv/">CGV</a> et <a href="../cgu/">CGU</a><br>
        <a href="../accessibilite-et-handicap/">Accessibilité et handicap</a>
      </p>
    </div>
  </div>
  <p class="foot__legal">Work and Joy, SASU au capital de 1 000 €. SIRET 940 982 432 00012. Déclaration d'activité 93132365213 auprès du préfet de région Provence-Alpes-Côte d'Azur, qui ne vaut pas agrément de l'État.</p>
</footer>"""

FINAL = f"""  <section class="final" id="contact">
    <h2>On en parle quinze minutes ?</h2>
    <p>Un premier échange en visio, gratuit et sans engagement, pour voir si le sujet est le bon et si on a envie de travailler ensemble.</p>
    <a class="btn btn--lg" href="{BOOKING}">Prendre rendez-vous</a>
    <p class="final__alt">Ou par e-mail : <a href="mailto:contact@workandjoy.org">contact@workandjoy.org</a></p>
  </section>"""

OFFRES = [
dict(
  slug="seminaire-equipe",
  title="Séminaire d'équipe pour PME industrielles et tech",
  desc="Une journée pour aligner une équipe de direction sur un cap commun, clarifier les rôles et repartir avec un plan d'action partagé. À partir de 2 000 € HT, à Marseille et partout en France.",
  h1="Séminaire<br>d'équipe",
  lede="Aligner une équipe sur un cap commun, clarifier les rôles et la façon de décider, et repartir avec un plan d'action que tout le monde a construit.",
  keys=[("Format", "1 journée, à partir de 5 personnes"), ("Tarif", "à partir de 2 000 € HT")],
  pourqui_h="Quand ce séminaire a du sens",
  pourqui=[
    "Vous dirigez une PME industrielle ou tech de moins de 250 salariés et votre équipe traverse un moment charnière.",
    "Une croissance rapide qui bouscule les façons de faire, une réorganisation, l'arrivée d'un nouveau management. Ou simplement le besoin de faire un point collectif structuré, parce que les réunions hebdomadaires n'y suffisent plus.",
    "Le point commun de ces situations, c'est que le sujet réel est rarement celui que l'on annonce.",
  ],
  temps=[
    ("Avant", "Des entretiens courts, trente minutes, avec vous et deux ou trois membres clés de l'équipe. C'est là que se trouve le sujet à travailler, et il n'est presque jamais celui du départ."),
    ("Le jour J", "Une journée ou une demi-journée. Bilan collectif en ouverture, travail approfondi sur le sujet identifié, puis construction d'un plan d'action partagé."),
    ("Après", "Une restitution écrite avec les points clés et les recommandations, pour que rien ne se perde la semaine suivante."),
  ],
  gains_h="Ce que vous y gagnez",
  gains=[
    ("Un plan, pas un souvenir", "L'équipe repart avec des actions nommées et attribuées, pas avec le sentiment d'avoir passé une bonne journée."),
    ("Un cap clarifié en un jour", "Sans immobiliser l'équipe plusieurs semaines et sans processus interminable."),
    ("Les non-dits sur la table", "Identifiés en amont pendant les entretiens, puis amenés par un regard extérieur. C'est précisément ce que personne de l'intérieur ne peut faire."),
  ],
  extra_h="Formule tout inclus",
  extra="Pour un séminaire clé en main, Work and Joy travaille avec une agence événementielle partenaire. Chacun sur son métier : Work and Joy conçoit et anime, l'agence prend en charge la logistique. Vous n'avez plus qu'à réunir votre équipe. Le forfait comprend l'animation telle que décrite ci-dessus, la recherche et la réservation d'un lieu avec salle équipée, les pauses et le déjeuner, et une activité de cohésion. Le tarif est établi sur devis avec l'agence, selon l'effectif, le lieu et l'activité retenus.",
  pratique=[("Groupe", "à partir de 5 personnes"), ("Durée", "1 journée, demi-journée possible"),
            ("Lieu", "chez vous, ou dans un lieu que nous trouvons pour vous"),
            ("Zone", "PACA, Lyon et Paris"), ("Tarif", "à partir de 2 000 € HT")],
  quote=("Anne-Sophie est intervenue à plusieurs reprises pour nous accompagner sur différents sujets. Les sujets les plus difficiles sont abordés et résolus toujours dans la bonne humeur, sans jamais perdre le cap. Elle a la particularité de rendre les process de travail ludiques et donc d'embarquer avec elle toutes les équipes.",
         "Clémentine Moulin, 2024"),
),
dict(
  slug="accompagnement-dirigeant",
  title="Accompagnement de dirigeant de PME | Work and Joy",
  desc="Un espace de recul régulier pour clarifier vos décisions stratégiques et affiner votre posture. Six à douze séances sur trois à six mois, forfait de 2 000 à 5 000 € HT.",
  h1="Accompagnement<br>du dirigeant",
  lede="Un espace confidentiel et régulier pour prendre du recul, tester vos décisions avant de les annoncer, et affiner votre posture face à l'équipe.",
  keys=[("Format", "6 à 12 séances sur 3 à 6 mois"), ("Tarif", "forfait 2 000 à 5 000 € HT")],
  pourqui_h="Quand cet accompagnement a du sens",
  pourqui=[
    "Vous dirigez une PME industrielle ou tech, seul ou avec des associés, et vous traversez une période où les décisions comptent plus que d'habitude.",
    "Un changement de direction, une phase de croissance, une réorganisation. Ou le moment où vous commencez à vous demander si votre façon de piloter tient encore.",
    "Diriger est un métier où l'on a peu d'endroits pour penser à voix haute sans que cela ait des conséquences. C'est ce que cet accompagnement fournit.",
  ],
  temps=[
    ("Cadrage", "Une première séance pour poser ce sur quoi nous travaillons, et à quoi nous saurons que ça a servi."),
    ("Les séances", "Une heure à une heure trente, toutes les trois à quatre semaines, en présentiel ou en visio. Le rythme compte autant que le contenu."),
    ("Étapes", "Un point à mi-parcours, puis un bilan final pour mesurer ce qui a bougé."),
  ],
  gains_h="Ce que vous y gagnez",
  gains=[
    ("Un endroit pour penser", "Un espace confidentiel pour tester une décision avant de l'annoncer à l'équipe, au conseil ou aux clients."),
    ("Une posture plus assurée", "Particulièrement dans les moments où l'équipe cherche des signaux et interprète tout."),
    ("Un rythme, pas une urgence", "Des rendez-vous réguliers qui évitent d'attendre la crise pour prendre du recul."),
  ],
  extra_h=None, extra=None,
  pratique=[("Format", "séances de 1h à 1h30"), ("Modalité", "présentiel à Marseille ou visio"),
            ("Durée", "3 à 6 mois, soit 6 à 12 séances"), ("Rythme", "toutes les 3 à 4 semaines"),
            ("Tarif", "forfait 2 000 à 5 000 € HT, ou 250 € HT de l'heure")],
  quote=("Merci Anne-Sophie pour ton efficacité redoutable !!!! En très peu de temps tu m'as beaucoup aidé dans mes réflexions business et cela m'a amené de la clarté pour le futur. On ressort de ton coaching avec un plan d'actions clair et programmé dans le temps, ce qui rend les choses encore plus simples.",
         "Ingrid Prost, avis Google, avril 2025"),
),
dict(
  slug="accompagnement-equipes",
  title="Accompagnement d'équipe en réorganisation | Work and Joy",
  desc="Traverser une période de tension ou de transformation avec un suivi resserré sur quatre à six mois, plutôt qu'une intervention isolée. 1 500 à 2 000 € HT la journée.",
  h1="Accompagnement<br>des équipes",
  lede="Traverser une période de tension ou de transformation avec un suivi dans la durée, plutôt qu'une intervention isolée vite oubliée.",
  keys=[("Format", "3 à 4 sessions sur 4 à 6 mois"), ("Tarif", "1 500 à 2 000 € HT la journée")],
  pourqui_h="Quand cet accompagnement a du sens",
  pourqui=[
    "Votre équipe est en réorganisation, intègre un nouveau management, ou grandit assez vite pour que les habitudes de fonctionnement ne suivent plus.",
    "Ou alors quelque chose s'est installé. Une personne en tension avec le reste du groupe, une démotivation diffuse, un turn-over qui ne s'explique pas tout seul.",
    "Ces situations ne se règlent pas en une journée. Elles demandent du temps et des rendez-vous espacés, pour que les choses bougent entre les séances.",
  ],
  temps=[
    ("Diagnostic", "Des entretiens individuels avec les membres clés de l'équipe. On y entend ce qui ne se dit pas en réunion."),
    ("Les sessions", "Trois à quatre temps collectifs, demi-journée ou journée selon le sujet, espacés sur plusieurs mois."),
    ("Entre les sessions", "Un point téléphonique régulier avec vous, pour ajuster et ne pas découvrir les choses à la session suivante."),
  ],
  gains_h="Ce que vous y gagnez",
  gains=[
    ("Une dynamique retrouvée", "Une équipe qui retravaille en bonne intelligence après une période de tension."),
    ("Un suivi, pas un coup d'éclat", "Les effets se mesurent entre les sessions, pas pendant."),
    ("Un dirigeant moins seul", "Vous n'êtes plus le seul à porter la cohésion de l'équipe au quotidien."),
  ],
  extra_h="Un cas, anonymisé",
  extra="Une entreprise d'informatique. Une équipe démotivée et peu proactive, une personne en tension avec le reste du groupe, un dirigeant à bout, un turn-over très élevé. Des entretiens individuels, un diagnostic partagé, une refonte de l'équipe, et un travail sur le relais des messages du dirigeant vers ses collaborateurs. Aujourd'hui l'équipe fonctionne et travaille en bonne intelligence, les managers sont outillés, et les nouveaux arrivants sont accueillis par des gens qui savent gérer une équipe.",
  pratique=[("Groupe", "l'équipe accompagnée par son dirigeant ou son directeur, taille variable"),
            ("Durée", "4 à 6 mois"), ("Rythme", "3 à 4 sessions espacées"),
            ("Tarif", "1 500 à 2 000 € HT la journée, forfait dégressif à partir de 3 sessions")],
  quote=("Une expérience riche et constructive. J'ai fait appel à elle pour deux de mes clients artisans et elle a su à chaque fois débloquer des situations qui m'ont ensuite permis de faire mon travail ! Je la recommande vivement pour toutes les questions qui touchent au personnel, à la relation humaine avec une logique tournée vers des solutions pragmatiques qui fonctionnent !",
         "Samir Brikci, avis Google"),
),
dict(
  slug="formation-management",
  title="Formation management pour PME industrielles et tech | Work and Joy",
  desc="Formation sur mesure au management, construite avec vous à partir de vos situations réelles. Un à deux jours, de 1 à 15 personnes, à partir de 1 700 € HT la journée. Organisme certifié Qualiopi.",
  h1="Formation<br>management",
  lede="Outiller vos managers avec des méthodes applicables dès le lendemain, sur un contenu construit à partir de vos situations réelles.",
  keys=[("Format", "1 à 2 jours, de 1 à 15 personnes"), ("Tarif", "à partir de 1 700 € HT la journée")],
  pourqui_h="Pour qui",
  pourqui=[
    "Managers de proximité, responsables d'équipe et dirigeants de PME industrielles et tech qui veulent monter en compétence sur un sujet précis.",
    "Les thèmes les plus demandés : la prise de poste de manager, la gestion des tensions, la communication managériale, l'organisation du travail en période de changement, et la qualité de vie et des conditions de travail.",
    "Il n'y a pas de catalogue. Le contenu est construit avec le commanditaire à partir de ce qui se passe réellement dans l'entreprise.",
  ],
  temps=[
    ("Cadrage", "Un échange en amont avec vous, direction ou RH, pour ajuster le contenu aux situations que vivent vos managers."),
    ("La session", "Un format participatif en présentiel. Apports méthodologiques, mises en situation, études de cas tirés de votre contexte."),
    ("Après", "Un support remis aux participants, et un langage commun qui reste dans l'équipe de management."),
  ],
  gains_h="Ce que vous y gagnez",
  gains=[
    ("Applicable dès le lendemain", "Des méthodes concrètes, pas un exposé sur le leadership."),
    ("Un langage commun", "Toute l'équipe de management sort avec les mêmes repères, ce qui change les réunions d'après."),
    ("Rien de générique", "Le programme est écrit pour vous. C'est ce qui fait la différence avec un stage sur étagère."),
  ],
  extra_h=None, extra=None,
  pratique=[("Public", "managers, responsables d'équipe, dirigeants"),
            ("Groupe", "de 1 à 15 personnes, en intra"), ("Durée", "1 à 2 jours selon la thématique"),
            ("Modalité", "présentiel"),
            ("Prérequis", "encadrer une équipe ou être sur le point de le faire"),
            ("Délai d'accès", "nous consulter, selon le calendrier"),
            ("Évaluation", "mises en situation pendant la session, questionnaire de satisfaction à l'issue"),
            ("Accessibilité", "Anne-Sophie Haumonté est la référente handicap, contactez-la pour étudier les adaptations possibles"),
            ("Tarif", "à partir de 1 700 € HT la journée, hors déplacement")],
  quote=("Une experte en bonheurologie d'entreprise.<br>A recommander vivement sur la région de Marseille.<br>Anne-Sophie Haumonté saura auditer dans les moindres détails vos problématiques ou difficultés RH de votre entreprise et mettra une stratégie efficace qui vous permettra de repartir sein d'esprit et plein d'envies dans votre Business...",
         "Matthieu Dellwing, avis Google, février 2020"),
  qualiopi=True,
),
]

FINANCEMENT = """  <section class="finance">
    <h2>Financement</h2>
    <p>Cette prestation est finançable par votre OPCO, jusqu'à 100 % sous conditions, dans le cadre de la prestation de conseil en ressources humaines. Work and Joy est référencée auprès de Constructys, OPCO Santé et Uniformation, et vous aide à monter le dossier.</p>
  </section>"""

QUALIOPI = """  <section class="finance finance--qualiopi">
    <h2>Organisme de formation certifié</h2>
    <p>Work and Joy est certifiée Qualiopi au titre des actions de formation et des bilans de compétences, certificat QUA25030046 délivré par Activcert, valable jusqu'en mai 2028. Déclaration d'activité enregistrée sous le numéro 93132365213 auprès du préfet de région Provence-Alpes-Côte d'Azur, ce qui ne vaut pas agrément de l'État.</p>
  </section>"""


def page(o):
    keys = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in o["keys"])
    pourqui = "".join(f"<p>{p}</p>" for p in o["pourqui"])
    temps = "".join(
        f'<div class="temps__item"><h3>{t}</h3><p>{d}</p></div>' for t, d in o["temps"])
    gains = "".join(
        f'<div class="temps__item"><h3>{t}</h3><p>{d}</p></div>' for t, d in o["gains"])
    prat = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in o["pratique"])
    extra = ""
    if o.get("extra"):
        extra = (f'  <section class="extra">\n    <h2>{o["extra_h"]}</h2>\n'
                 f'    <p>{o["extra"]}</p>\n  </section>\n\n')
    q, qa = o["quote"]
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(o['title'])}</title>
<meta name="description" content="{html.escape(o['desc'])}">
<link rel="stylesheet" href="../assets/css/style.css">
<link rel="preload" href="../assets/fonts/montserrat-latin-900-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="../assets/fonts/jost-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
</head>
<body>

<a class="skip" href="#contenu">Aller au contenu</a>

{NAV}

<main id="contenu">

  <section class="offre-head">
    <h1>{o['h1']}</h1>
    <p class="lede">{o['lede']}</p>
    <dl class="offre-head__keys">{keys}</dl>
    <a class="btn" href="#contact">Prendre rendez-vous</a>
  </section>

  <section class="pourqui">
    <h2>{o['pourqui_h']}</h2>
    <div class="pourqui__col">{pourqui}</div>
  </section>

  <section class="methode">
    <h2>Comment ça se passe</h2>
    <div class="temps">{temps}</div>
  </section>

  <section class="gains">
    <h2>{o['gains_h']}</h2>
    <div class="temps">{gains}</div>
  </section>

{extra}  <section class="quote">
    <blockquote>
      <p>{q}</p>
      <footer>{qa}</footer>
    </blockquote>
  </section>

  <section class="pratique">
    <h2>En pratique</h2>
    <dl class="pratique__list">{prat}</dl>
  </section>

{QUALIOPI if o.get("qualiopi") else FINANCEMENT}

{FINAL}

</main>

{FOOT}

</body>
</html>
"""


root = pathlib.Path(__file__).parent / "site"
for o in OFFRES:
    d = root / o["slug"]
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(page(o), encoding="utf-8")
    print("écrit", d / "index.html")
