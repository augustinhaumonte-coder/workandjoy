# Reprendre le projet

> Mis à jour le 11 novembre 2026. Point d'entrée du dossier.
> Refonte du site de Work and Joy, Anne-Sophie Haumonté, Marseille.
> Les autres documents : `CADRAGE.md` pour la stratégie, `AUDIT-PREVERSION.md` pour la recette
> détaillée du 26 octobre, dont le plan d'action est déroulé sauf la suppression de `main.js`, `DNS-avant-bascule.md` pour tout ce qui touche au domaine,
> `JOURNAL.md` pour le pourquoi des décisions, séance par séance.

---

## En deux phrases

Le site Wix actuel, `workandjoy.org`, est remplacé par un site statique écrit à la main, dans `site/`. Douze pages sont écrites, relues et auditées, une préversion tourne sur Netlify, rien n'est encore sur le domaine de production.

Depuis le 10 novembre le dossier est sous git, poussé sur un dépôt GitHub privé, et Netlify redéploie la préversion à chaque `push`. Le dépôt est `github.com/augustinhaumonte-coder/workandjoy`.

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
└── assets/  css/style.css · js/scene.js (animations) et review.js (relecture) · fonts/ (6 woff2) · img/ (9 fichiers, dont 2 webp)

.gitignore                             exclut Documents demandés/, voir plus bas
netlify.toml                           dit à Netlify de ne publier que site/

ressources/logos-work-and-joy/         SVG, PNG et PDF des trois déclinaisons + fiche de charte
CERTIFICATION/                         certificat Qualiopi, chartes d'usage et graphique, logos
LOGO et Charte/                        logo UPE13 adhérent 2026 et sa charte
LOGO/                                  masters du logo W&J (.ai, .eps, .jpg) et doublons
```

Pas de framework, pas d'étape de compilation. Un fichier CSS pour tout le site. Mode sombre inclus. Liens internes vérifiés, aucun cassé, et désormais tous en forme de dossier, sans `index.html`.

**Conséquence du point précédent** : un double-clic sur `site/index.html` en `file://` affiche la liste du dossier au lieu de la page. Passer par `cd site && python3 -m http.server 8787`.

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
| Animations au défilement, en JavaScript | Décision du 11 novembre, qui remplace le « pas d'animation » d'origine. `animation-timeline: view()` reste écarté : il masquait le contenu. Ici aucun texte n'est jamais masqué, le script n'ajoute que des dessins. Sans JavaScript ou avec « réduire les animations », les pages gardent leur mise en page d'origine |
| Arrêts de défilement en `position: sticky`, pas en JavaScript | C'est le navigateur qui fige la page. Un arrêt simulé en JavaScript tremble sur téléphone |
| Carré de la scène à droite, texte à gauche | Pour que la bille entre et sorte par la marge sans survoler le texte |
| Sous-titre sous le H1 et FAQ sur les 5 pages d'offre | Les mots clés visés par `CADRAGE.md` étaient dans les `title` mais presque absents du texte. Pas de texte caché : Google le sanctionne |
| Menu déroulant pour les offres | Le menu mélangeait ancres et destinations. « Méthode » est sorti du menu |
| Avis reproduits mot pour mot | Y compris les fautes. Décision explicite d'Augustin |
| Dépôt GitHub privé, pas public | Le dossier contient le CV d'Anne-Sophie, ses certificats et des portraits |
| `Documents demandés/` hors du dépôt | 215 Mo de scans et de portraits bruts, dont un PDF de 95,9 Mo à quatre mégaoctets de la limite stricte de GitHub. Rien ne sert au site, les originaux sont chez Anne-Sophie. Le dossier reste sur le disque mais n'est sauvegardé nulle part |
| `LOGO/` et `CERTIFICATION/` gardés dans le dépôt | 27 Mo au total, et ils servent au site |
| Déploiement depuis git, plus par glisser-déposer | Supprime l'écart entre ce qui est en ligne et ce qui est commité, et c'est un prérequis de Decap ou Sveltia |
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

Ajouts du 11 novembre, à lui faire valider :

- **Le mot « coaching »** apparaît maintenant en clair sur les pages dirigeant et équipes, y compris dans le `title` de la page dirigeant. Elle disait « accompagnement » partout.
- **« Aix-en-Provence »** est cité une fois, dans la FAQ du séminaire. C'est dans sa zone, mais le site ne nommait pas la ville.
- **Les FAQ des pages formation et bilan** s'ajoutent aux engagements opposables en audit Qualiopi. Elles ne reprennent que des faits déjà écrits sur le site.
- **Bilan, heures annoncées.** 8 rendez-vous de 1h30 font 12 h, les formules affichent 13 h et 24 h. À clarifier.
- **Texte collé au bloc violet du témoignage** sur trois pages : formation et dirigeant (« Ce que vous y gagnez »), bilan (note sous les deux formules). Défaut d'espacement d'origine, non corrigé.

**Augustin**

9. Trois trous marqués par des commentaires `À COMPLÉTER` dans le HTML : adresse complète de l'hébergeur, coordonnées du médiateur, accessibilité précise des locaux. Les deux derniers dépendent d'elle.
10. Exporter de Wix avant toute résiliation : CGV, CGU, messages du formulaire, clients et rendez-vous Wix Bookings.
11. Désactiver le renouvellement automatique du forfait Wix avant le **21 mai 2027**, sans toucher au domaine qui se renouvelle le 11 juin.
12. **Vérifier le budget de crédits Netlify avant la bascule.** Le plan gratuit donne 300 crédits par mois, plafond strict. Un déploiement en production en coûte 15, la bande passante 20 par gigaoctet. Une vingtaine de pushs par mois suffit donc à épuiser le quota. Si ça serre, OVH redevient une option sérieuse, au prix d'un script PHP à écrire pour le formulaire.

*Réglé le 10 novembre : le dossier est sous git et poussé sur GitHub, Netlify est branché sur le dépôt.*

---

## Prochaines étapes, dans l'ordre

1. Recueillir les retours d'Anne-Sophie sur la préversion, corriger.
2. Combler les trous légaux, régler le médiateur, obtenir le lien LinkedIn.
3. Décider de 11ty, qui conditionne le blog et l'interface d'édition.
4. Recette : Lighthouse, mobile réel, formulaire de contact, lien Bookings, relecture des textes.
5. Brancher le formulaire sur Netlify Forms.
6. **Retirer les éléments de préversion** : le fichier `site/_headers` qui interdit l'indexation, le fichier `site/assets/js/review.js`, les douze balises `<script ... review.js>`, et le formulaire caché `avis-maquette` dans `index.html`. Supprimer aussi `assets/js/main.js`, qui ne contient qu'un commentaire et n'est référencé nulle part.
7. Bascule DNS : 3 enregistrements A et le CNAME `www` dans le panneau Wix. Ne toucher à rien d'autre.
8. Search Console, et mise à jour du lien du site sur la fiche Google.
9. Résilier le forfait Wix.

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

### Les animations au défilement

Tout tient dans `assets/js/scene.js` et dans le dernier bloc de `style.css`. Le script est chargé par les douze pages.

- **La bille fil conducteur**, sur toutes les pages. Le O jaune du logo quitte l'en-tête, descend dans la marge, et finit dans le bouton « Prendre rendez-vous » du bas de page.
- **Les paliers.** À une arête entre deux sections, la page se fige et la bille traverse d'une marge à l'autre. Le script choisit seul les arêtes : un changement de fond ou une bordure, à au moins 1,2 écran du palier précédent, et avec de la place sous le texte pour que la bille roule sans le toucher.
- **L'arrêt sur le bouton.** La page se fige, la bille entre dans le bouton, puis la page reste figée encore un demi-écran pendant que le bouton « respire ». Les liens `#contact` amènent directement à cet état.
- **La scène de la méthode**, sur l'accueil seulement, activée par l'attribut `data-scene` sur `#methode`. La bille devient la grosse bille du logo, qui se construit en trois temps séparés par des pauses, puis la bille du haut retombe et repart vers le bouton.

Les réglages sont des constantes en tête de `scene.js`, en hauteurs d'écran : `LINE`, `HOLD_ROLL`, `HOLD_CTA`, `GAP`, `MEET`, `DROP`, et le tableau `SEGMENTS` pour les durées de la scène.

Pour une nouvelle page, rien à faire : il suffit que la coquille soit la même (en-tête avec `.mark__o`, sections directement dans `<main>`, bloc `.final` avec son bouton, pied de page).

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
- **Les animations enveloppent les sections.** Une fois `scene.js` lancé, les sections ne sont plus des enfants directs de `<main>` ni forcément voisines. Un sélecteur CSS du type `main > section` ou `.a + .b` entre deux sections cesserait de s'appliquer. Aucun n'existe aujourd'hui, ne pas en ajouter.
- **Les animations allongent le défilement.** Une page d'offre passe d'environ 6,5 à 8,5 écrans, l'accueil de 6,5 à 12. Jamais testé au doigt sur un vrai téléphone : à faire avant la bascule.
- **`git push` publie.** Tant qu'on est sur la préversion c'est sans conséquence. Après la bascule DNS, pousser c'est mettre en ligne. Soit travailler sur une branche fusionnée quand c'est prêt, soit pousser moins souvent, d'autant que chaque déploiement coûte 15 crédits.
- **`Documents demandés/` n'est plus sauvegardé.** Il est exclu du dépôt. Les originaux sont chez Anne-Sophie, mais si tu y ajoutes quoi que ce soit d'unique, il faudra une copie ailleurs.
- **Le dossier ne se monte pas dans le shell distant.** Google Drive a été écarté comme cause, le montage échoue quand même, côté application. Les outils fichier marchent, le shell non : les commandes git se lancent donc à la main dans le Terminal, pas à distance.
