# Reprendre le projet

> Mis à jour le 3 novembre 2026. Point d'entrée du dossier.
> Refonte du site de Work and Joy, Anne-Sophie Haumonté, Marseille.
> Les autres documents : `CADRAGE.md` pour la stratégie, `AUDIT-PREVERSION.md` pour la recette
> détaillée du 26 octobre, `DNS-avant-bascule.md` pour tout ce qui touche au domaine,
> `JOURNAL.md` pour le pourquoi des décisions, séance par séance.

---

## En deux phrases

Le site Wix actuel, `workandjoy.org`, est remplacé par un site statique écrit à la main, dans `site/`. Douze pages sont écrites, relues et auditées, une préversion tourne sur Netlify, rien n'est encore sur le domaine de production.

Le positionnement a changé en cours de route : le site s'adresse désormais aux **dirigeants de PME industrielles et tech**, le bilan de compétences passe en page secondaire.

---

## Ce qui existe

```
site/
├── index.html                         accueil
├── seminaire-equipe/                  offre 1
├── accompagnement-dirigeant/          offre 2
├── accompagnement-equipes/            offre 3
├── formation-management/              offre 4
├── bilan-de-competences/              particuliers
├── a-propos/                          le parcours d'Anne-Sophie
├── temoignages/                       9 avis Google + 2 LinkedIn
├── contact/                           formulaire + coordonnées
├── mentions-legales/
├── politique-de-confidentialite/
├── accessibilite-et-handicap/
├── robots.txt  sitemap.xml  _headers  favicon.svg  favicon.ico  apple-touch-icon.png
└── assets/  css/style.css · js/ · fonts/ (6 woff2) · img/ (7 fichiers)

ressources/logos-work-and-joy/         SVG, PNG et PDF des trois déclinaisons + fiche de charte
CERTIFICATION/                         certificat Qualiopi, chartes d'usage et graphique, logos
LOGO et Charte/                        logo UPE13 adhérent 2026 et sa charte
LOGO/                                  masters du logo W&J (.ai, .eps, .jpg) et doublons
```

Pas de framework, pas d'étape de compilation. Un fichier CSS pour tout le site. Mode sombre inclus. Liens internes vérifiés, aucun cassé.

---

## Les décisions, et pourquoi

| Décision | Raison |
|---|---|
| Site B2B, bilan en secondaire | Demande explicite d'Anne-Sophie dans le questionnaire |
| On garde `workandjoy.org` | Elle l'a depuis dix ans et ne veut pas changer. Supprime la migration SEO, l'étape la plus risquée |
| On garde le DNS chez Wix | On ne modifie que 3 enregistrements A et le CNAME `www`. Les 10 lignes Microsoft ne sont jamais touchées, risque nul sur sa messagerie |
| On quitte l'hébergement Wix pour Netlify | Netlify accepte un domaine dont le DNS est ailleurs, Cloudflare Pages non. Économise 360 € TTC par an |
| Montserrat et Jost | Avenir et Century Gothic de sa charte sont payantes, budget nul. Substituts très proches, validés par elle sur une planche comparative |
| Polices auto-hébergées | Évite le transfert d'IP vers Google que le RGPD sanctionne |
| Couleurs du fichier logo, pas du questionnaire | Le SVG contient `#424193 #FFED00 #E94B63`, elle avait noté `#4335B1 #FFDB00 #FF4860`. Suivre le fichier pour que logo et page s'accordent. **À faire confirmer** |
| Pas d'animation au défilement | `animation-timeline: view()` masque le contenu tant que l'animation n'a pas tourné. Risque disproportionné pour de la décoration |
| Menu déroulant pour les offres | Le menu mélangeait ancres et destinations. « Méthode » est sorti du menu |
| Avis reproduits mot pour mot | Y compris les fautes. Décision explicite d'Augustin |
| Badge Qualiopi sur l'accueil seulement | La charte interdit le logo sur un support dédié à une seule action de formation. Les pages d'offre n'en portent que la mention en texte |
| Logo UPE13 sur disque blanc | Sa moitié haute est transparente et « UPE13 » y est écrit en violet : sans disque, il disparaît dans le pied de page |
| Texte avant photo sur mobile | Le portrait en `order: -1` remplissait tout le premier écran et repoussait le titre et les boutons sous la ligne de flottaison |
| Téléphone masqué de 921 à 1200 px | La barre de navigation est déjà pleine sur cette plage. Il reste dans le menu burger en dessous |
| Pas encore de 11ty | Reporté. Conséquence : l'en-tête et le pied de page sont dupliqués dans 12 fichiers |

---

## Ce qui bloque, et sur qui

**Anne-Sophie**

1. **Médiateur de la consommation.** Elle n'y adhère pas. Obligatoire dès lors qu'on vend à des particuliers, ce qui est le cas du bilan même financé par le CPF. Tant que ce n'est pas réglé, la page bilan ne doit pas être publiée. Son auditeur Qualiopi saura confirmer.
2. **CGV et CGU.** Elles existent sur le site Wix, il faut les textes avant de résilier. Les liens ont été retirés du pied de page en attendant.
3. **Quinze ans ou douze ans d'ingénierie.** Son CV dit 1999 à 2011, elle écrit « quinze ans » partout. L'accueil affiche quinze. À trancher.
4. **Les neuf entreprises nommées** sur la page À propos viennent de son CV. Un CV circule en main propre, un site est public. À valider.
5. **Page formation, conformité Qualiopi.** Prérequis, modalités d'évaluation et délai d'accès sont des propositions. Ce sont des engagements opposables en audit, elle doit les relire.
6. **Accès à sa fiche Google**, et le lien « Demander des avis ».
7. **L'adresse de son profil LinkedIn.** Le pied de page des 12 pages pointe encore sur `https://www.linkedin.com/`, l'accueil du réseau. Sur un site B2B c'est le lien le plus cliqué après « Prendre rendez-vous ».
8. **Neuf ou dix avis.** L'en-tête de la page témoignages annonce dix, neuf sont affichés.

**Augustin**

9. Trois trous marqués par des commentaires `À COMPLÉTER` dans le HTML : adresse complète de l'hébergeur, coordonnées du médiateur, accessibilité précise des locaux.
10. **Mettre le dossier sous git.** Aujourd'hui le site n'existe qu'en un seul exemplaire sur le Mac, déployé par dépôt manuel de dossier. Pas de sauvegarde, pas d'historique, aucun retour en arrière possible après une fausse manœuvre. Un dépôt GitHub privé branché sur Netlify règle la sauvegarde, l'historique et le déploiement automatique d'un coup, et conditionne le choix d'une interface d'édition pour Anne-Sophie (Decap ou Sveltia tournent sur dépôt git). **Demande un `git init` sur place**, voir la note sur le montage plus bas.
11. Exporter de Wix avant toute résiliation : CGV, CGU, messages du formulaire, clients et rendez-vous Wix Bookings.
12. Désactiver le renouvellement automatique du forfait Wix avant le **21 mai 2027**, sans toucher au domaine qui se renouvelle le 11 juin.

---

## Prochaines étapes, dans l'ordre

1. Mettre le dossier sous git, avant tout le reste. Tout ce qui suit modifie des fichiers.
2. Recueillir les retours d'Anne-Sophie sur la préversion, corriger.
3. Combler les trous légaux, régler le médiateur, obtenir le lien LinkedIn.
4. Dérouler le plan d'action de `AUDIT-PREVERSION.md` : liens internes sans `index.html`, contraste des `<dt>`, `h4` du pied de page, portrait en WebP, `Person` et `BreadcrumbList` en JSON-LD.
5. Décider de 11ty, qui conditionne le blog et l'interface d'édition.
6. Recette : Lighthouse, mobile réel, formulaire de contact, lien Bookings, relecture des textes.
7. Brancher le formulaire sur Netlify Forms.
8. **Retirer les éléments de préversion** : le fichier `site/_headers` qui interdit l'indexation, le fichier `site/assets/js/review.js`, les douze balises `<script ... review.js>`, et le formulaire caché `avis-maquette` dans `index.html`. Supprimer aussi `assets/js/main.js`, qui ne contient qu'un commentaire et n'est référencé nulle part.
9. Bascule DNS : 3 enregistrements A et le CNAME `www` dans le panneau Wix. Ne toucher à rien d'autre.
10. Search Console, et mise à jour du lien du site sur la fiche Google.
11. Résilier le forfait Wix.

---

## Recueillir les retours d'Anne-Sophie

Un bouton « Commenter » flotte en bas à droite de chaque page de la préversion. Elle sélectionne un passage, clique, écrit sa remarque, et le passage sélectionné part avec le commentaire. Les retours arrivent dans Netlify, onglet **Forms**, formulaire `avis-maquette`, et Netlify peut envoyer un e-mail à chaque dépôt (Site configuration, Forms, Form notifications).

Cent dépôts par mois sur le plan gratuit, largement de quoi faire.

---

## Travailler sur le site

Les liens sont relatifs, donc un double-clic sur `site/index.html` fonctionne. Pour être au plus près du rendu final, mieux vaut un serveur local :

```bash
cd site && python3 -m http.server 8787
# puis http://localhost:8787/
```

### Conventions

**Couleurs**, définies en variables CSS sur `:root`, redéfinies pour le mode sombre.

| | |
|---|---|
| `--violet` | `#424193`, fond des sections fortes |
| `--jaune` | `#FFED00`, **seule couleur d'accent** de la page |
| `--corail` | `#E94B63`, n'apparaît que dans le logo |

**Polices.** Montserrat 600/800/900 pour les titres et les étiquettes, Jost 400/500/600 pour le texte. Servies depuis `assets/fonts/`.

**Formes.** Tout est carré, sauf les boutons qui sont en pilule, et le badge UPE13 qui est rond par nature.

**Classes réutilisables** : `.btn`, `.btn--sm`, `.btn--lg`, `.btn--ghost` pour les boutons, `.temps` pour une rangée de trois blocs à filet jaune, `.quote` pour une citation pleine largeur sur violet, `.final` pour l'appel à l'action de fin, `.pratique__list` pour un tableau de caractéristiques, `.legal` pour une page de texte, `.voisins` pour le bloc « Et aussi » de fin de page, qui réutilise la grille `.temps`.

**Une page type** reprend la coquille d'une page existante : copier `a-propos/index.html`, remplacer `<main>`. L'en-tête et le pied de page doivent rester strictement identiques partout.

### Les scripts

`build-offres.py` et `build-pages.py` ont servi à générer les pages depuis une coquille commune. Ils sont jetables : **les fichiers HTML sont la source**, pas les scripts. Ne pas les relancer, ils écraseraient les corrections faites depuis.

---

## Les pièges à ne pas oublier

- **Le DNS.** Les dix enregistrements Microsoft font vivre sa messagerie, Teams et ses appareils. Ne toucher qu'aux A et au `www`. Tout est relevé dans `DNS-avant-bascule.md`.
- **Le forfait Wix et le domaine sont deux factures distinctes.** Résilier le premier ne doit pas emporter le second.
- **Ne jamais inventer un chiffre.** C'est arrivé une fois : « 100 % de projets valides à six mois » était fabriqué à partir d'un « Oui ». Retiré.
- **`site/_headers`** empêche Google d'indexer la préversion. À supprimer le jour de la mise en ligne, sans quoi le site restera invisible.
- **Le bloc-notes de relecture** (`assets/js/review.js`) ne s'affiche que sur `localhost` et sur une adresse en `.netlify.app`. Il ne peut donc pas apparaître par accident sur `workandjoy.org`, mais il reste à supprimer.
- **La dette des douze en-têtes.** Modifier le menu, c'est modifier douze fichiers. C'est le prix du report de 11ty.
- **Les logos Qualiopi et UPE13 sont sous charte.** Ne pas sortir le badge Qualiopi de son cartouche blanc, ne pas retirer le bandeau Marianne, ne pas toucher aux couleurs ni aux proportions des deux logos, ne pas descendre le badge Qualiopi sur une page dédiée à une seule action de formation. Le logo UPE13 porte un millésime : il tombe si la cotisation n'est pas renouvelée.
- **Les liens internes contiennent encore `index.html`.** Le `sed` prévu au point 2.1 de `AUDIT-PREVERSION.md` devra aussi passer sur les blocs « Et aussi » ajoutés le 3 novembre.
- **Le dossier ne se monte plus dans le shell distant**, probablement parce qu'il est synchronisé par Google Drive (il contient un `.tmp.drivedownload`). Les outils fichier marchent, le shell non : impossible de déplacer, renommer ou supprimer un fichier à distance, et impossible de lancer `git init`. Le sortir de la zone synchronisée par Drive réglerait les deux.
