#!/usr/bin/env python3
"""Crée les pages restantes en reprenant la coquille d'une page existante.

L'en-tête et le pied de page sont lus dans a-propos/index.html pour qu'ils
restent strictement identiques partout. Script jetable, les HTML sont la source.
"""
import re, pathlib, html

ROOT = pathlib.Path(__file__).parent / "site"
src = (ROOT / "a-propos" / "index.html").read_text(encoding="utf-8")
NAV = re.search(r'<header class="nav">.*?</script>', src, re.S).group(0)
FOOT = re.search(r'<footer class="foot">.*?</footer>', src, re.S).group(0)

BOOKING = ("https://bookings.cloud.microsoft/bookwithme/user/"
           "a25ae09279404c6988d7f9df4378557e@workandjoy.org/meetingtype/"
           "o_2nV1khmUG8mVr6vYahlA2?anonymous&amp;ismsaljsauthenabled&amp;ep=mcard")

FINAL = f"""  <section class="final" id="contact">
    <h2>On en parle quinze minutes ?</h2>
    <p>Un premier échange en visio, gratuit et sans engagement, pour voir si le sujet est le bon et si on a envie de travailler ensemble.</p>
    <a class="btn btn--lg" href="{BOOKING}">Prendre rendez-vous</a>
    <p class="final__alt">Ou par e-mail : <a href="mailto:contact@workandjoy.org">contact@workandjoy.org</a></p>
  </section>"""


def shell(slug, title, desc, body, current=None):
    nav = NAV
    nav = nav.replace(' aria-current="page"', '')
    if current:
        nav = nav.replace(f'href="../{current}/index.html"',
                          f'href="../{current}/index.html" aria-current="page"', 1)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="stylesheet" href="../assets/css/style.css">
<link rel="preload" href="../assets/fonts/montserrat-latin-900-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="../assets/fonts/jost-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
</head>
<body>

<a class="skip" href="#contenu">Aller au contenu</a>

{nav}

<main id="contenu">

{body}

{FINAL}

</main>

{FOOT}

</body>
</html>
"""


# ---------------------------------------------------------------- bilan

BILAN = """  <section class="offre-head">
    <h1>Bilan de<br>compétences</h1>
    <p class="lede">Faire le point sur votre parcours, construire un projet qui vous ressemble, et repartir avec un plan d'action concret.</p>
    <dl class="offre-head__keys">
      <div><dt>Durée</dt><dd>8 à 12 semaines, 8 rendez-vous de 1h30</dd></div>
      <div><dt>Tarif</dt><dd>1 750 ou 2 700 € HT selon la formule</dd></div>
    </dl>
    <a class="btn" href="#contact">Prendre rendez-vous</a>
  </section>

  <section class="pourqui">
    <h2>À qui ça s'adresse</h2>
    <div class="pourqui__col">
      <p>À toute personne, salariée ou non, qui veut faire le point sur son parcours professionnel.</p>
      <p>Une reconversion envisagée, un changement de poste, une évolution à préparer. Ou simplement le besoin de comprendre ce qu'on sait faire, ce qu'on aime faire, et ce vers quoi on veut aller.</p>
      <p>Le bilan n'est pas un test qui donne une réponse. C'est un travail structuré, accompagné, au terme duquel vous avez un projet et les étapes pour l'atteindre.</p>
    </div>
  </section>

  <section class="methode">
    <h2>Les cinq phases</h2>
    <div class="temps">
      <div class="temps__item"><h3>Faire le point</h3><p>Le parcours, les compétences, les valeurs, les aptitudes, la personnalité, les besoins, les passions. Et les projets rêvés, même ceux qu'on n'ose pas formuler.</p></div>
      <div class="temps__item"><h3>Quel métier ?</h3><p>Définir le projet, vérifier qu'il correspond vraiment à vos aspirations, et identifier ce qu'il faudra pour y arriver.</p></div>
      <div class="temps__item"><h3>Action</h3><p>Passer au concret. Recherche d'emploi, préparation aux entretiens, ou création d'entreprise selon le projet.</p></div>
      <div class="temps__item"><h3>Synthèse</h3><p>Un document personnel et confidentiel vous est remis en fin de parcours. Il n'appartient qu'à vous.</p></div>
      <div class="temps__item"><h3>Suivi à six mois</h3><p>Un rendez-vous pour vérifier que le projet tient toujours, et l'ajuster si la situation a changé.</p></div>
    </div>
  </section>

  <section class="formules">
    <h2>Deux formules</h2>
    <div class="formules__grid">
      <article>
        <h3>Exploration</h3>
        <p class="formules__prix">1 750 € HT</p>
        <p>13 heures d'accompagnement. Pour faire le point sur le parcours, les envies et les talents, et explorer des pistes de projet réalistes.</p>
      </article>
      <article>
        <h3>Complet</h3>
        <p class="formules__prix">2 700 € HT</p>
        <p>24 heures d'accompagnement. La démarche entière, du bilan au plan d'action, pour avancer vers la suite avec de la clarté.</p>
      </article>
    </div>
    <p class="formules__note">Ces tarifs sont ceux affichés sur Mon Compte Formation. Le bilan est finançable par le CPF, par votre OPCO, par votre employeur, ou à titre personnel. Un entretien préalable gratuit et sans engagement permet de vérifier que le dispositif correspond à votre besoin avant toute inscription.</p>
  </section>

  <section class="quote">
    <blockquote>
      <p>Ses conseils avisés m'ont permis de réfléchir hors du cadre, de reprendre confiance, de croire à des projets qui me semblaient difficilement atteignables. Quelques semaines après nos dernières séances, j'ai décroché un poste répondant largement à mes attentes.</p>
      <footer>Florence</footer>
    </blockquote>
  </section>

  <section class="pratique">
    <h2>En pratique</h2>
    <dl class="pratique__list">
      <div><dt>Durée</dt><dd>8 à 12 semaines selon vos disponibilités</dd></div>
      <div><dt>Rythme</dt><dd>8 rendez-vous individuels de 1h30, environ 24 h de travail personnel</dd></div>
      <div><dt>Lieu</dt><dd>présentiel à Marseille 8e, ou visio depuis partout en France</dd></div>
      <div><dt>Outils</dt><dd>une plateforme en ligne sert de fil conducteur, avec des tests selon les besoins : TLP, MBTI, Ennéagramme, IIP</dd></div>
      <div><dt>Livrable</dt><dd>une synthèse personnelle et confidentielle</dd></div>
      <div><dt>Délai d'accès</dt><dd>15 jours minimum après la signature</dd></div>
      <div><dt>Confidentialité</dt><dd>les séances à distance ne sont jamais enregistrées</dd></div>
      <div><dt>Accessibilité</dt><dd>Anne-Sophie Haumonté est la référente handicap, contactez-la pour étudier les adaptations possibles</dd></div>
    </dl>
  </section>

  <section class="indic">
    <h2>Résultats</h2>
    <ul class="indic__grid">
      <li><b>11</b><span>bénéficiaires accompagnés depuis 2025</span></li>
      <li><b>5/5</b><span>satisfaction, contenus et accompagnement</span></li>
      <li><b>0</b><span>abandon en cours de parcours</span></li>
      <li><b>100 %</b><span>de projets toujours valides au suivi à six mois</span></li>
    </ul>
    <p class="indic__note">Indicateurs établis à partir des questionnaires remplis en fin de bilan, sur les parcours réalisés en 2025 et 2026.</p>
  </section>

  <section class="finance finance--qualiopi">
    <h2>Organisme certifié</h2>
    <p>Work and Joy est certifiée Qualiopi au titre des actions de formation et des bilans de compétences, certificat QUA25030046 délivré par Activcert, valable jusqu'en mai 2028. Déclaration d'activité enregistrée sous le numéro 93132365213 auprès du préfet de région Provence-Alpes-Côte d'Azur, ce qui ne vaut pas agrément de l'État. Le document de synthèse est élaboré pendant la phase de conclusions, conformément au code du travail.</p>
  </section>"""


# ---------------------------------------------------------------- contact

CONTACT = f"""  <section class="offre-head">
    <h1>Contact</h1>
    <p class="lede">Le plus simple est un premier échange en visio de quinze minutes, gratuit et sans engagement. Vous choisissez le créneau, je m'adapte.</p>
    <dl class="offre-head__keys">
      <div><dt>Téléphone</dt><dd><a href="tel:+33624310759">06 24 31 07 59</a></dd></div>
      <div><dt>E-mail</dt><dd><a href="mailto:contact@workandjoy.org">contact@workandjoy.org</a></dd></div>
    </dl>
    <a class="btn" href="{BOOKING}">Réserver un créneau</a>
  </section>

  <section class="contact-grid">
    <div class="contact-form">
      <h2>Ou écrivez-moi</h2>
      <form name="contact" method="POST" data-netlify="true" netlify-honeypot="societe-bis">
        <input type="hidden" name="form-name" value="contact">
        <p class="pot"><label>Ne remplissez pas ce champ <input name="societe-bis"></label></p>

        <div class="field">
          <label for="nom">Nom et prénom</label>
          <input id="nom" name="nom" type="text" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="email">E-mail</label>
          <input id="email" name="email" type="email" autocomplete="email" required>
          <p class="hint">Pour que je puisse vous répondre.</p>
        </div>
        <div class="field">
          <label for="entreprise">Entreprise <span>facultatif</span></label>
          <input id="entreprise" name="entreprise" type="text" autocomplete="organization">
        </div>
        <div class="field">
          <label for="message">Votre message</label>
          <textarea id="message" name="message" rows="6" required></textarea>
          <p class="hint">En deux lignes, la situation et ce que vous cherchez.</p>
        </div>
        <button class="btn" type="submit">Envoyer</button>
        <p class="hint">Vos données servent uniquement à vous répondre. Voir la <a href="../politique-de-confidentialite/index.html">politique de confidentialité</a>.</p>
      </form>
    </div>

    <aside class="contact-info">
      <h2>Où</h2>
      <p><strong>Work and Joy</strong><br>121 avenue Clot Bey<br>13008 Marseille</p>
      <p>Accès facile en voiture, desservi par le bus.</p>
      <p>Les locaux sont accessibles dans de nombreuses situations. Contactez la référente handicap, Anne-Sophie Haumonté, pour que nous trouvions ensemble la solution adaptée.</p>
      <h2>Zone d'intervention</h2>
      <p>Les accompagnements d'entreprise se font en Provence-Alpes-Côte d'Azur, à Lyon et à Paris. Le bilan de compétences se fait en présentiel à Marseille, ou en visio depuis partout en France.</p>
      <h2>En anglais</h2>
      <p>Les accompagnements peuvent se dérouler en anglais.</p>
    </aside>
  </section>"""


# ---------------------------------------------------------------- légal

MENTIONS = """  <section class="legal">
    <h1>Mentions légales</h1>

    <h2>Éditeur du site</h2>
    <p>
      <strong>Work and Joy</strong>, société par actions simplifiée unipersonnelle au capital de 1 000 €.<br>
      Siège social : 121 avenue Clot Bey, 13008 Marseille, France.<br>
      SIRET : 940 982 432 00012. RCS Marseille.<br>
      Numéro de TVA intracommunautaire : FR55 940 982 432.<br>
      Code APE : 70.22Z, conseil pour les affaires et autres conseils de gestion.<br>
      Téléphone : <a href="tel:+33624310759">06 24 31 07 59</a>. E-mail : <a href="mailto:contact@workandjoy.org">contact@workandjoy.org</a>.
    </p>

    <h2>Directrice de la publication</h2>
    <p>Anne-Sophie Haumonté, présidente.</p>

    <h2>Organisme de formation</h2>
    <p>
      Déclaration d'activité enregistrée sous le numéro 93132365213 auprès du préfet de région Provence-Alpes-Côte d'Azur. Cet enregistrement ne vaut pas agrément de l'État.<br>
      Certification Qualiopi n° QUA25030046, délivrée par Activcert, au titre des actions de formation et des bilans de compétences, valable jusqu'au 1er mai 2028.
    </p>

    <h2>Assurance</h2>
    <p>Responsabilité civile professionnelle souscrite auprès d'AXA, police n° 0000022213912504.</p>

    <h2>Hébergement</h2>
    <!-- À COMPLÉTER une fois l'hébergeur retenu : raison sociale, adresse postale complète et téléphone. -->
    <p>Le site est hébergé par Netlify, Inc., San Francisco, Californie, États-Unis.</p>

    <h2>Médiation de la consommation</h2>
    <!-- À COMPLÉTER : adhésion à un médiateur agréé obligatoire dès lors que des prestations sont
         vendues à des particuliers. Remplacer ce paragraphe par le nom, l'adresse postale et
         l'adresse du site du médiateur retenu. -->
    <p>Conformément au code de la consommation, un médiateur de la consommation peut être saisi gratuitement en cas de litige non résolu avec un client particulier. Les coordonnées du médiateur seront précisées ici.</p>

    <h2>Propriété intellectuelle</h2>
    <p>L'ensemble des contenus de ce site, textes, images et identité visuelle, est la propriété de Work and Joy, sauf mention contraire. Les portraits photographiques sont l'œuvre de Studio Café. Toute reproduction sans autorisation est interdite.</p>

    <h2>Avis publiés</h2>
    <p>Les avis reproduits sur ce site proviennent de la fiche Google de Work and Joy et des recommandations publiées sur LinkedIn. Ils sont repris sans modification du texte. Work and Joy ne rémunère pas les auteurs d'avis et ne pratique aucune sélection visant à masquer des avis défavorables.</p>
  </section>"""

CONFID = """  <section class="legal">
    <h1>Politique de confidentialité</h1>

    <p class="legal__intro">Ce site collecte très peu de données, et uniquement pour vous répondre. Cette page explique lesquelles, pourquoi, et combien de temps elles sont conservées.</p>

    <h2>Qui est responsable</h2>
    <p>Work and Joy, 121 avenue Clot Bey, 13008 Marseille, représentée par Anne-Sophie Haumonté. Pour toute question sur vos données, écrivez à <a href="mailto:contact@workandjoy.org">contact@workandjoy.org</a>.</p>

    <h2>Le formulaire de contact</h2>
    <p>Lorsque vous utilisez le formulaire, les informations que vous saisissez, nom, adresse e-mail, nom de l'entreprise et message, sont transmises par e-mail à Work and Joy. Elles servent uniquement à traiter votre demande. La base légale est votre démarche volontaire vers nous. Ces données sont conservées trois ans après le dernier échange, puis supprimées.</p>

    <h2>La prise de rendez-vous</h2>
    <p>Le bouton de prise de rendez-vous ouvre Microsoft Bookings, un service de Microsoft. Les informations que vous y renseignez sont traitées par Microsoft selon ses propres conditions. Work and Joy n'y accède que pour organiser le rendez-vous.</p>

    <h2>Mesure d'audience</h2>
    <!-- À CONFIRMER une fois l'outil installé. Rédigé pour une mesure sans cookie. -->
    <p>La fréquentation du site est mesurée sans cookie et sans identifiant individuel. Aucun profil n'est constitué, aucune donnée n'est revendue, et rien ne permet de vous reconnaître d'une visite à l'autre. C'est la raison pour laquelle ce site ne vous demande pas de consentement aux cookies : il n'en dépose aucun.</p>

    <h2>Les polices de caractères</h2>
    <p>Les polices du site sont servies depuis le site lui-même et non depuis un service tiers. Votre adresse IP n'est donc transmise à personne d'autre que l'hébergeur.</p>

    <h2>Vos droits</h2>
    <p>Vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation et d'opposition sur vos données. Écrivez à <a href="mailto:contact@workandjoy.org">contact@workandjoy.org</a>, une réponse vous sera apportée sous un mois. Si la réponse ne vous satisfait pas, vous pouvez saisir la CNIL.</p>

    <h2>Les données des personnes accompagnées</h2>
    <p>Les informations échangées pendant un accompagnement, un bilan de compétences ou une formation sont confidentielles. Elles ne sont jamais communiquées à un tiers, y compris à l'employeur ou au financeur, sauf obligation légale ou accord écrit de la personne concernée. Les séances à distance ne sont jamais enregistrées.</p>
  </section>"""

ACCESS = """  <section class="legal">
    <h1>Accessibilité et handicap</h1>

    <p class="legal__intro">Une situation de handicap ne doit pas empêcher de suivre une formation ou un bilan de compétences. Voici comment nous procédons.</p>

    <h2>Votre interlocutrice</h2>
    <p>Anne-Sophie Haumonté est la référente handicap de Work and Joy. Vous pouvez la joindre directement au <a href="tel:+33624310759">06 24 31 07 59</a> ou à <a href="mailto:contact@workandjoy.org">contact@workandjoy.org</a>.</p>

    <h2>Comment ça se passe</h2>
    <p>Signalez votre situation le plus tôt possible, idéalement lors de l'entretien préalable. Nous examinons ensemble ce qui est nécessaire : l'aménagement du rythme et de la durée des séances, le choix du lieu, le passage en visio, l'adaptation des supports, ou le recours à un intervenant spécialisé.</p>
    <p>Si une adaptation dépasse ce que Work and Joy peut mettre en place, nous vous orientons vers les ressources compétentes, notamment l'Agefiph et les structures du réseau Ressource Handicap Formation.</p>

    <h2>Les locaux</h2>
    <!-- À COMPLÉTER : décrire précisément l'accessibilité du 121 avenue Clot Bey, marches, ascenseur, sanitaires. -->
    <p>Les accompagnements en présentiel ont lieu à Marseille, 121 avenue Clot Bey. Contactez la référente handicap pour vérifier que le lieu convient à votre situation. La visio reste possible dans tous les cas et sans surcoût.</p>

    <h2>Accessibilité du site</h2>
    <p>Ce site a été conçu pour être lisible au clavier, compatible avec les lecteurs d'écran, et respecter des contrastes suffisants. Si vous rencontrez une difficulté pour accéder à un contenu, signalez-la, elle sera corrigée.</p>
  </section>"""


PAGES = [
 ("bilan-de-competences",
  "Bilan de compétences à Marseille et à distance | Work and Joy",
  "Bilan de compétences accompagné par Anne-Sophie Haumonté, à Marseille ou en visio. Huit rendez-vous sur huit à douze semaines, 1 750 ou 2 700 € HT, finançable par le CPF. Organisme certifié Qualiopi.",
  BILAN),
 ("contact",
  "Contact | Work and Joy, Marseille",
  "Prendre rendez-vous avec Anne-Sophie Haumonté. Quinze minutes en visio, gratuit et sans engagement. Work and Joy, 121 avenue Clot Bey, 13008 Marseille.",
  CONTACT),
 ("mentions-legales",
  "Mentions légales | Work and Joy",
  "Mentions légales de Work and Joy, SASU basée à Marseille, organisme de formation certifié Qualiopi.",
  MENTIONS),
 ("politique-de-confidentialite",
  "Politique de confidentialité | Work and Joy",
  "Quelles données ce site collecte, pourquoi, combien de temps elles sont conservées, et comment exercer vos droits.",
  CONFID),
 ("accessibilite-et-handicap",
  "Accessibilité et handicap | Work and Joy",
  "Référente handicap, adaptations possibles et accessibilité des formations et bilans de compétences de Work and Joy.",
  ACCESS),
]

for slug, title, desc, body in PAGES:
    d = ROOT / slug
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(shell(slug, title, desc, body, current=slug), encoding="utf-8")
    print("écrit", d / "index.html")
