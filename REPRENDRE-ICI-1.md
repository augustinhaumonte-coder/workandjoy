# Reprendre le projet

> Mis à jour le 11 novembre 2026 à 18 h 50, juste après la bascule du domaine. Point d'entrée du dossier.
> Refonte du site de Work and Joy, Anne-Sophie Haumonté, Marseille.
> Les autres documents : `CADRAGE.md` pour la stratégie, `AUDIT-PREVERSION.md` pour la recette
> détaillée du 26 octobre, dont le plan d'action est déroulé sauf la suppression de `main.js`, `DNS-avant-bascule.md` pour tout ce qui touche au domaine,
> `JOURNAL.md` pour le pourquoi des décisions, séance par séance.

---

## En deux phrases

Le site Wix de `workandjoy.org` est remplacé par un site statique écrit à la main, dans `site/`. Quatorze pages, hébergées sur Netlify à l'adresse `reliable-druid-e56775.netlify.app`.

**La bascule du domaine a été faite le 11 novembre 2026 vers 18 h 30** : le DNS, resté chez Wix, pointe maintenant vers Netlify. La mise en ligne n'est pas terminée pour autant, voir « Où on en est » juste en dessous.

Depuis le 10 novembre le dossier est sous git, poussé sur un dépôt GitHub privé, et Netlify redéploie le site à chaque `push`. Le dépôt est `github.com/augustinhaumonte-coder/workandjoy`.

Le positionnement a changé en cours de route : le site s'adresse désormais aux **dirigeants de PME industrielles et tech**, le bilan de compétences passe en page secondaire.

---

## Où on en est, le 11 novembre au soir

**Fait**

- La version de production est poussée et déployée. Vérifié de l'extérieur à 18 h 47 sur l'adresse `.netlify.app` : pied de page avec les liens CGV et CGU, plus de téléphone ailleurs que dans les mentions légales, plus de rubrique médiateur, CGV à 12 articles.
- Les animations ont été essayées au doigt par Augustin sur son téléphone : ça marche.
- Le domaine est déclaré dans Netlify, en DNS externe.
- Dans le panneau DNS de Wix, Augustin a remplacé les trois enregistrements A par un seul vers `75.2.60.5`, et modifié le CNAME `www`. Détail dans `DNS-avant-bascule.md`.

**À vérifier, dans l'ordre.** Rien de ce qui suit n'a été confirmé.

1. **Le nouveau site s'affiche** sur `https://www.workandjoy.org` et `https://workandjoy.org`, avec le cadenas. À 18 h 47, `www` montrait encore l'ancien site Wix vu de l'extérieur : normal, les anciens réglages restent en mémoire une heure, parfois jusqu'à 24. L'adresse sans `www` n'a pas pu être contrôlée.
2. **La valeur du CNAME `www`.** Elle doit être `reliable-druid-e56775.netlify.app`. Augustin l'a saisie seul, elle n'a pas été relue. Si `www` n'affiche pas le nouveau site demain, c'est la première chose à regarder.
3. **Netlify, Domain management.** La mention « Pending DNS verification » doit avoir disparu et le certificat HTTPS doit être actif.
4. **`www.workandjoy.org` en domaine principal.** Le réglage a été refusé pendant que Netlify créait le certificat (« you cannot change custom domains until that process completes »). À refaire : ligne `www.workandjoy.org`, **Options**, **Set as primary domain**. Tant que ce n'est pas fait, `www` redirige vers l'adresse nue, à l'inverse de ce que déclarent les balises canonical et le plan du site.
5. **Le formulaire de contact. État inconnu.** Il dépend de Netlify Forms : **Forms**, **Enable form detection**, relancer un déploiement, puis **Forms**, **Submission notifications**, **Add notification** avec l'adresse d'Anne-Sophie, et envoyer un message d'essai depuis la page Contact. Augustin n'a pas confirmé l'avoir fait. **Tant que ce n'est pas fait, les messages des visiteurs sont perdus.**
6. **La messagerie d'Anne-Sophie.** Lui écrire à son adresse `@workandjoy.org` et lui demander de répondre. Les lignes Microsoft n'ont pas été touchées, c'est un contrôle de principe.
7. **`review.js`.** Devait partir avec `git rm site/assets/js/review.js`. Non confirmé. Sans gravité : plus aucune page ne le charge.

**Ensuite**

8. Search Console : déclarer `www.workandjoy.org`, envoyer `sitemap.xml`. Vérifier le lien du site sur la fiche Google.
9. Exporter de Wix les messages du formulaire et les clients Wix Bookings.
10. Ne pas résilier le forfait Wix avant d'être sûr du nouveau site. Ne jamais résilier le domaine : il est acheté chez Wix et fait vivre le site et la messagerie.

**Pour revenir en arrière** : remettre dans Wix les trois enregistrements A et le CNAME `www` d'origine, notés dans `DNS-avant-bascule.md`. L'ancien site Wix n'a pas été supprimé.

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
├── cgv/                               reprises du site Wix le 11 novembre, mêmes adresses qu'avant
├── cgu/
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
| `www.workandjoy.org` est l'adresse principale | C'est celle des balises canonical et du plan du site, et c'est ce que Netlify recommande quand le DNS est ailleurs. L'adresse nue doit rediriger vers elle |
| Un enregistrement A, pas d'ALIAS | Netlify préfère un ALIAS vers `apex-loadbalancer.netlify.com`. Le panneau Wix n'en propose pas : on a pris la solution de repli, un A vers `75.2.60.5` |
| On ne supprime pas l'ancien site Wix | Il reste rangé dans le compte Wix, invisible, et sert de secours. La bascule se fait par le DNS, pas par une suppression |
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
| Pas encore de 11ty | Reporté. Conséquence : l'en-tête et le pied de page sont dupliqués dans 14 fichiers |

---

## Ce qui bloque, et sur qui

**Anne-Sophie**

1. **Médiateur de la consommation.** Réponse d'Anne-Sophie le 11 novembre : elle n'adhère à aucun médiateur, le texte de ses CGV avait été recopié ailleurs. La mention fausse est donc retirée des mentions légales et des CGV (article 12 supprimé, l'ancien article 13 devient le 12), un commentaire HTML marque l'endroit dans les deux fichiers. L'ancien site Wix l'affichait. **Le nouveau site est donc en ligne sans mention de médiateur. Reste à faire** : qu'elle adhère à un médiateur de la consommation, obligatoire dès qu'elle vend à des particuliers, ce qui est le cas du bilan de compétences (article L.612-1 du code de la consommation). Une fois l'adhésion faite, remettre la mention aux deux endroits avec le texte que le médiateur fournit.
2. **CGV et CGU.** Reprises du site Wix le 11 novembre, aux mêmes adresses `/cgv` et `/cgu`, liens remis dans le pied de page. La phrase de modèle qui terminait les CGU est retirée. **Les CGV sont reprises mot pour mot et contredisent le nouveau site sur plusieurs points, à lui faire relire** : bilan à 2 202 € net de TVA alors que la page bilan affiche 1 750 et 2 700 € HT ; paiement en trois mensualités de 1 000 € ; 12 heures sur 6 mois au plus alors que la page annonce 8 à 12 semaines ; une « formation en bilan de compétences » de 35 heures à 3 000 € HT qui n'existe pas sur le nouveau site ; tribunaux de Paris compétents pour une société de Marseille. La clause sur le médiateur est retirée, voir le point 1.
3. ~~Quinze ans ou douze ans d'ingénierie.~~ Tranché le 11 novembre : quinze ans, de 1999 à 2014. Elle précise qu'à la fin elle était salariée sans plus travailler. La page À propos affiche maintenant « 2002 à 2014 ».
4. ~~Les neuf entreprises nommées sur la page À propos.~~ Validées le 11 novembre.
5. **Page formation, conformité Qualiopi.** Prérequis validés le 11 novembre. Elle n'a pas trouvé les modalités d'évaluation : elles sont dans le tableau « En pratique », ligne « Évaluation ». À lui montrer pour validation, avec le délai d'accès.
6. ~~Accès à sa fiche Google.~~ Augustin l'a. Le lien pour demander des avis est posé sur la page témoignages.
7. ~~L'adresse de son profil LinkedIn.~~ Fait le 11 novembre : `linkedin.com/in/haumonte` dans le pied de page de toutes les pages.
8. ~~Neuf ou dix avis.~~ Il y en a bien dix sur Google. Décision d'Augustin : la page en affiche neuf, on n'ajoute pas le dixième. L'encart garde « 10 avis Google », la description ne dit plus « les dix avis ».

Ajouts du 11 novembre, à lui faire valider :

- **Le mot « coaching »** apparaît maintenant en clair sur les pages dirigeant et équipes, y compris dans le `title` de la page dirigeant. Elle disait « accompagnement » partout.
- **« Aix-en-Provence »** est cité une fois, dans la FAQ du séminaire. C'est dans sa zone, mais le site ne nommait pas la ville.
- **Les FAQ des pages formation et bilan** s'ajoutent aux engagements opposables en audit Qualiopi. Elles ne reprennent que des faits déjà écrits sur le site.
- **Bilan, heures annoncées.** 8 rendez-vous de 1h30 font 12 h, les formules affichent 13 h et 24 h. À clarifier.
- ~~Texte collé au bloc violet du témoignage~~ sur trois pages : corrigé le 11 novembre.

**Augustin**

9. Un trou `À COMPLÉTER` reste dans le HTML : l'accessibilité précise des locaux, qui dépend d'elle. L'adresse de l'hébergeur est remplie. La mention du médiateur est retirée, voir le point 1.
10. Exporter de Wix avant toute résiliation : les CGV et CGU sont reprises. Restent les messages du formulaire, les clients et les rendez-vous Wix Bookings.
11. Désactiver le renouvellement automatique du forfait Wix avant le **21 mai 2027**, sans toucher au domaine qui se renouvelle le 11 juin.
12. **Vérifier le budget de crédits Netlify avant la bascule.** Le plan gratuit donne 300 crédits par mois, plafond strict. Un déploiement en production en coûte 15, la bande passante 20 par gigaoctet. Une vingtaine de pushs par mois suffit donc à épuiser le quota. Si ça serre, OVH redevient une option sérieuse, au prix d'un script PHP à écrire pour le formulaire.

*Réglé le 10 novembre : le dossier est sous git et poussé sur GitHub, Netlify est branché sur le dépôt.*

---

## Prochaines étapes, dans l'ordre

Le détail de la mise en ligne est dans « Où on en est », en haut.

1. ~~Recueillir les retours d'Anne-Sophie, corriger.~~ Fait le 11 novembre, par mail.
2. ~~Retirer les éléments de préversion.~~ Fait le 11 novembre : plus de `noindex` dans `site/_headers`, plus de balise `review.js`, plus de formulaire caché `avis-maquette`.
3. ~~Recette sur téléphone réel.~~ Faite par Augustin le 11 novembre, animations comprises.
4. ~~Bascule DNS.~~ Faite le 11 novembre vers 18 h 30.
5. **Finir la mise en ligne** : les points 1 à 7 de « Où on en est ». Le formulaire de contact en premier.
6. Search Console, plan du site, lien de la fiche Google.
7. Combler les trous légaux : l'adhésion à un médiateur, la relecture des CGV, l'accessibilité des locaux.
8. Faire valider par Anne-Sophie les ajouts du 11 novembre listés plus haut.
9. Exporter de Wix, puis arrêter le forfait Wix avant le 21 mai 2027, sans toucher au domaine.
10. Décider de 11ty, qui conditionne le blog et l'interface d'édition.

---

## Recueillir les retours d'Anne-Sophie

Le bouton « Commenter » de la préversion a été retiré le 11 novembre, avec la mise en production. Ses retours passent désormais par mail.

---

## Travailler sur le site

Un double-clic sur `site/index.html` ne suffit pas, les liens visent des dossiers. Il faut un serveur local :

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

Tout tient dans `assets/js/scene.js` et dans le dernier bloc de `style.css`. Le script est chargé par les quatorze pages.

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
- **L'adresse `.netlify.app` reste ouverte.** Le site y répond toujours, en double de `www.workandjoy.org`. Les balises canonical désignent `www.workandjoy.org`, donc Google sait laquelle retenir. Ne pas remettre de `noindex` dans `site/_headers` : il s'appliquerait aussi au vrai domaine.
- **Le bloc-notes de relecture n'est plus chargé.** Si le fichier `assets/js/review.js` est encore dans le dossier, le supprimer avec `git rm`.
- **La dette des quatorze en-têtes.** Modifier le menu, c'est modifier quatorze fichiers. C'est le prix du report de 11ty.
- **Les logos Qualiopi et UPE13 sont sous charte.** Ne pas sortir le badge Qualiopi de son cartouche blanc, ne pas retirer le bandeau Marianne, ne pas toucher aux couleurs ni aux proportions des deux logos, ne pas descendre le badge Qualiopi sur une page dédiée à une seule action de formation. Le logo UPE13 porte un millésime : il tombe si la cotisation n'est pas renouvelée.
- **Les animations enveloppent les sections.** Une fois `scene.js` lancé, les sections ne sont plus des enfants directs de `<main>` ni forcément voisines. Un sélecteur CSS du type `main > section` ou `.a + .b` entre deux sections cesserait de s'appliquer. Aucun n'existe aujourd'hui, ne pas en ajouter.
- **Les animations allongent le défilement.** Une page d'offre passe d'environ 6,5 à 8,5 écrans, l'accueil de 6,5 à 12. Essayé au doigt le 11 novembre sur le téléphone d'Augustin, sans problème. Un seul téléphone a été essayé.
- **`git push` publie.** Depuis la bascule du 11 novembre, pousser c'est mettre en ligne sur `workandjoy.org`. Soit travailler sur une branche fusionnée quand c'est prêt, soit pousser moins souvent, d'autant que chaque déploiement coûte 15 crédits.
- **`Documents demandés/` n'est plus sauvegardé.** Il est exclu du dépôt. Les originaux sont chez Anne-Sophie, mais si tu y ajoutes quoi que ce soit d'unique, il faudra une copie ailleurs.
- **Netlify verrouille les domaines pendant qu'il crée un certificat.** Tout changement de domaine est refusé pendant ce temps. Attendre quelques minutes et recommencer.
- **Wix réserve le nom `www` à ses propres sites.** On ne peut pas ajouter un second CNAME `www`, seulement modifier celui qui existe.
- **Une écriture à distance peut renvoyer un ancien contenu.** Quand un fichier est écrit dans le dossier depuis un chemin de préparation déjà utilisé, l'outil annonce un succès et dépose parfois l'ancienne version. Toujours partir d'un chemin neuf et relire la taille du fichier après coup.
- **Le dossier ne se monte pas dans le shell distant.** Google Drive a été écarté comme cause, le montage échoue quand même, côté application. Les outils fichier marchent, le shell non : les commandes git se lancent donc à la main dans le Terminal, pas à distance.
