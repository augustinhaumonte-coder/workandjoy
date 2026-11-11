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
└── assets/  css/style.css · js/scene.js (animations) · fonts/ (6 woff2) · img/ (9 fichiers, dont 2 webp)

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
| Couleurs du fichier logo, pas du questionnaire | Le SVG contient `#424193 #FFED00 #E94B63`, elle avait noté `#4335B1 #FFDB00 #FF4860`. Suivre le fichier pour que logo et page s'accordent. Validé par Anne-Sophie le 11 novembre |
| Son vrai logo dans l'en-tête, en version horizontale | Demandé deux fois par Anne-Sophie. Le logo complet est trop haut pour une barre de 70 px : l'en-tête porte son carré, puis « WORK & JOY » dans le dessin d'origine, en SVG dans la page. La signature « ENJOY YOUR JOB » serait illisible à cette taille, elle reste sur le logo du pied de page |
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
| Menu burger sous 1100 px | Seuil relevé le 11 novembre : le vrai logo est plus large que l'ancien mot-symbole. L'ancien seuil de 920 px débordait déjà entre 921 et 980 px |
| Plus de téléphone sur le site, sauf dans les mentions légales | Demande d'Augustin le 11 novembre. Retiré de l'en-tête, de la page contact et de la page accessibilité. Gardé dans les mentions légales : pour une société, le numéro fait partie des mentions obligatoires |
| Pas encore de 11ty | Reporté. Conséquence : l'en-tête et le pied de page sont dupliqués dans 12 fichiers |

---

## Ce qui bloque, et sur qui

**Anne-Sophie**

1. **Médiateur de la consommation.** Elle y adhère : ses CGV citent CNPM MÉDIATION CONSOMMATION. Mais l'entité a changé de nom et d'adresse : elle s'appelle MÉDIATION CONSOMMATION DÉVELOPPEMENT, à Saint-Étienne, et son site est `www.medconsodev.eu`. La mention est rédigée dans les mentions légales avec ces coordonnées, sous un commentaire `À CONFIRMER`. **Reste à faire** : qu'elle copie le texte officiel depuis son espace adhérent, rubrique « Mes mentions obligatoires », ce qui confirmera aussi que l'adhésion est active, et qu'elle corrige ses CGV. Ensuite la page bilan peut être publiée.
2. **CGV et CGU.** Les CGU sont reçues : sept articles génériques, avec une phrase de modèle à retirer en fin de texte. **Les CGV manquent encore**, Augustin les lui redemande. Pages à créer et liens à remettre dans le pied de page quand les deux textes sont là.
3. ~~Quinze ans ou douze ans d'ingénierie.~~ Tranché le 11 novembre : quinze ans, de 1999 à 2014. Elle précise qu'à la fin elle était salariée sans plus travailler. La page À propos affiche maintenant « 2002 à 2014 ».
4. ~~Les neuf entreprises nommées sur la page À propos.~~ Validées le 11 novembre.
5. **Page formation, conformité Qualiopi.** Prérequis validés le 11 novembre. Elle n'a pas trouvé les modalités d'évaluation : elles sont dans le tableau « En pratique », ligne « Évaluation ». À lui montrer pour validation, avec le délai d'accès.
6. ~~Accès à sa fiche Google.~~ Augustin l'a. Le lien pour demander des avis est posé sur la page témoignages.
7. ~~L'adresse de son profil LinkedIn.~~ Fait le 11 novembre : `linkedin.com/in/haumonte` dans le pied de page des 12 pages.
8. ~~Neuf ou dix avis.~~ Il y en a bien dix sur Google. Décision d'Augustin : la page en affiche neuf, on n'ajoute pas le dixième. L'encart garde « 10 avis Google », la description ne dit plus « les dix avis ».

Ajouts du 11 novembre, à lui faire valider :

- **Le mot « coaching »** apparaît maintenant en clair sur les pages dirigeant et équipes, y compris dans le `title` de la page dirigeant. Elle disait « accompagnement » partout.
- **« Aix-en-Provence »** est cité une fois, dans la FAQ du séminaire. C'est dans sa zone, mais le site ne nommait pas la ville.
- **Les FAQ des pages formation et bilan** s'ajoutent aux engagements opposables en audit Qualiopi. Elles ne reprennent que des faits déjà écrits sur le site.
- **Bilan, heures annoncées.** 8 rendez-vous de 1h30 font 12 h, les formules affichent 13 h et 24 h. À clarifier.
- **Texte collé au bloc violet du témoignage** sur trois pages : formation et dirigeant (« Ce que vous y gagnez »), bilan (note sous les deux formules). Défaut d'espacement d'origine, non corrigé.

**Augustin**

9. Un trou `À COMPLÉTER` reste dans le HTML : l'accessibilité précise des locaux, qui dépend d'elle. L'adresse de l'hébergeur est remplie. La mention du médiateur est rédigée mais porte un `À CONFIRMER`, voir le point 1.
10. Exporter de Wix avant toute résiliation : CGV, CGU, messages du formulaire, clients et rendez-vous Wix Bookings.
11. Désactiver le renouvellement automatique du forfait Wix avant le **21 mai 2027**, sans toucher au domaine qui se renouvelle le 11 juin.
12. **Vérifier le budget de crédits Netlify avant la bascule.** Le plan gratuit donne 300 crédits par mois, plafond strict. Un déploiement en production en coûte 15, la bande passante 20 par gigaoctet. Une vingtaine de pushs par mois suffit donc à épuiser le quota. Si ça serre, OVH redevient une option sérieuse, au prix d'un script PHP à écrire pour le formulaire.

*Réglé le 10 novembre : le dossier est sous git et poussé sur GitHub, Netlify est branché sur le dépôt.*

---

## Prochaines étapes, dans l'ordre

1. ~~Recueillir les retours d'Anne-Sophie, corriger.~~ Fait le 11 novembre, par mail.
2. Combler les trous légaux : LinkedIn et hébergeur faits. Restent le texte officiel du médiateur, les CGV, l'accessibilité des locaux.
3. Décider de 11ty, qui conditionne le blog et l'interface d'édition.
4. Recette sur la préversion : **téléphone réel** (les animations n'y ont jamais été essayées au doigt), formulaire de contact, lien Bookings, relecture des textes.
5. Brancher le formulaire sur Netlify Forms : activer la détection des formulaires dans Netlify, redéployer, régler l'adresse de notification, puis envoyer un message d'essai.
6. ~~Retirer les éléments de préversion.~~ Fait le 11 novembre dans les fichiers : `site/_headers` ne contient plus de `noindex`, les douze balises `review.js` et le formulaire caché `avis-maquette` sont retirés. **Reste un geste à la main** : `git rm site/assets/js/review.js`, le fichier n'est plus utilisé mais il est encore là.
7. Bascule DNS : 3 enregistrements A et le CNAME `www` dans le panneau Wix. Ne toucher à rien d'autre.
8. Search Console, et mise à jour du lien du site sur la fiche Google.
9. Résilier le forfait Wix.

---

## Recueillir les retours d'Anne-Sophie

Le bouton « Commenter » de la préversion a été retiré le 11 novembre, avec la mise en production. Ses retours passent désormais par mail.

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
- **`site/_headers` ne bloque plus Google** depuis le 11 novembre. Tant que le DNS n'est pas basculé, l'adresse en `.netlify.app` est donc indexable. Les balises canonical pointent vers `workandjoy.org`, le risque est faible, mais il ne faut pas laisser traîner cet état des semaines.
- **Le bloc-notes de relecture n'est plus chargé.** Le fichier `assets/js/review.js` reste à supprimer avec `git rm`.
- **La dette des douze en-têtes.** Modifier le menu, c'est modifier douze fichiers. C'est le prix du report de 11ty.
- **Les logos Qualiopi et UPE13 sont sous charte.** Ne pas sortir le badge Qualiopi de son cartouche blanc, ne pas retirer le bandeau Marianne, ne pas toucher aux couleurs ni aux proportions des deux logos, ne pas descendre le badge Qualiopi sur une page dédiée à une seule action de formation. Le logo UPE13 porte un millésime : il tombe si la cotisation n'est pas renouvelée.
- **Les animations enveloppent les sections.** Une fois `scene.js` lancé, les sections ne sont plus des enfants directs de `<main>` ni forcément voisines. Un sélecteur CSS du type `main > section` ou `.a + .b` entre deux sections cesserait de s'appliquer. Aucun n'existe aujourd'hui, ne pas en ajouter.
- **Les animations allongent le défilement.** Une page d'offre passe d'environ 6,5 à 8,5 écrans, l'accueil de 6,5 à 12. Jamais testé au doigt sur un vrai téléphone : à faire avant la bascule.
- **`git push` publie.** Tant qu'on est sur la préversion c'est sans conséquence. Après la bascule DNS, pousser c'est mettre en ligne. Soit travailler sur une branche fusionnée quand c'est prêt, soit pousser moins souvent, d'autant que chaque déploiement coûte 15 crédits.
- **`Documents demandés/` n'est plus sauvegardé.** Il est exclu du dépôt. Les originaux sont chez Anne-Sophie, mais si tu y ajoutes quoi que ce soit d'unique, il faudra une copie ailleurs.
- **Le dossier ne se monte pas dans le shell distant.** Google Drive a été écarté comme cause, le montage échoue quand même, côté application. Les outils fichier marchent, le shell non : les commandes git se lancent donc à la main dans le Terminal, pas à distance.
