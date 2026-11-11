# Journal de bord

> Une entrée par séance de travail, la plus récente en haut.
> Le « pourquoi » des décisions vit ici. `REPRENDRE-ICI.md` ne garde que l'état courant.

---

## 11 novembre 2026 — Mots clés dans le texte, puis les animations au défilement

Deux sujets. Le matin, vérifier le référencement et combler le trou des mots clés. Ensuite, à la demande d'Augustin qui trouvait le site « assez banal », des animations au défilement qui jouent avec le logo.

### Référencement

Le SEO technique était complet sur les 12 pages. Le manque était dans le texte : les requêtes visées par `CADRAGE.md` figuraient dans les `title` et presque pas dans les pages. « Coach » n'apparaissait ni dans le `title` ni dans le H1 de la page dirigeant.

| Fait | Détail |
|---|---|
| Sous-titre sous le H1 | Sur les 5 pages d'offre, dans un `<hgroup>`. Le H1 ne bouge pas |
| H2 précisés | « Comment est-ce que ça se passe ? » devient « Comment se déroule un séminaire d'équipe », etc. |
| FAQ en bas de page | 3 à 4 questions par page d'offre, uniquement à partir de faits déjà écrits sur le site. Aucun chiffre nouveau |
| `title` de deux pages | Séminaire et dirigeant |

Écarté : la balise `meta keywords`, ignorée par Google depuis 2009, et le texte caché, que Google classe comme spam.

### Animations

Cinq versions de prototype dans la journée, dans `Claude outputs/prototype-animation-*.html`. Ce qui a été retenu, et pourquoi :

| Décision | Raison |
|---|---|
| La scène de la méthode sur l'accueil | La seule idée où l'animation explique quelque chose : désordre, table, plan. L'image finale est le logo exact, positions relevées dans `logo.svg` |
| Des pauses dans la scène | Sans elles, tout changeait dès que la section se figeait. Demande d'Augustin |
| La planche qui se redresse, abandonnée | Jugée ridicule sur la page d'offre |
| La bille fil conducteur sur toutes les pages | Elle a remplacé la planche. Elle part du O du logo et finit dans le bouton de rendez-vous |
| La page se fige quand la bille traverse | Pour que le lecteur ne regarde la bille qu'à des moments choisis. Arrêt complet plutôt que ralenti : l'arrêt est fait par le navigateur en `position: sticky`, un ralenti aurait dû être simulé en JavaScript et aurait saccadé sur téléphone |
| Arrêt et latence sur le bouton final | Pour donner envie de cliquer. Demande d'Augustin |
| Sur l'accueil, la bille du haut repart du logo | Pour qu'elle finisse elle aussi dans le bouton |
| Carré à droite sur ordinateur | Conséquence du point précédent : la bille entre et sort par la marge de droite sans survoler le texte |
| La bille bouge aussi en hauteur | À hauteur fixe elle paraissait morte. Elle tombe après une traversée, descend doucement, puis se pose sur l'arête suivante qui la remonte |
| Une arête n'est un palier que s'il y a de la place sous le texte | Trouvé en vérifiant les 12 pages : sur trois d'entre elles le texte touche le bloc violet, la bille aurait roulé dessus |

Deux bugs corrigés en route, de même nature : la hauteur de la bille était lue sur le défilement réel et ses déplacements sur un défilement lissé, en retard de quelques images. Aux transitions elle sautait. Tout ce qui est mouvement propre de la bille suit maintenant la même horloge.

Corrigé au passage : le titre « On en parle quinze minutes ? » était collé au bloc « Et aussi » sur les pages qui en ont un.

Vérifié par script sur les 12 pages, ordinateur et téléphone : aucune erreur, aucun débordement, arrêt sur le bouton partout, bille jamais sur du texte, mise en page d'origine sans JavaScript ou avec les animations réduites. **Pas vérifié** : le rendu au doigt sur un vrai téléphone.

### Réponses d'Anne-Sophie, appliquées le soir même

| Réponse | Ce qui a été fait |
|---|---|
| Lien LinkedIn | Pied de page des 12 pages et `sameAs` de l'accueil |
| Quinze ans, de 1999 à 2014 | Page À propos : frise « 2002 à 2014 », description « Quinze ans » au lieu de « Douze ans » |
| Phrase sur le reclassement | « j'ai participé au reclassement… ». Elle avait écrit « aidé participé », « participé » a été retenu |
| Son vrai logo | En-tête des 12 pages, en version horizontale. Voir la décision dans `REPRENDRE-ICI-1.md` |
| Dix avis, mais on n'ajoute pas le dixième | Décision d'Augustin. La description de la page ne dit plus « les dix avis » |
| Lien pour demander des avis | Lien « Laisser un avis sur Google » sur la page témoignages |
| Médiateur | Voir ci-dessous |

**Le médiateur a changé de nom.** Ses CGV citent CNPM MÉDIATION CONSOMMATION à Saint-Chamond. Vérification faite sur le site du médiateur : l'ancienne adresse redirige vers `www.medconsodev.eu`, l'entité s'appelle MÉDIATION CONSOMMATION DÉVELOPPEMENT et elle est à Saint-Étienne. La mention des mentions légales reprend ces coordonnées, avec la formule que le médiateur demande à ses adhérents. Le texte exact est dans son espace adhérent, rubrique « Mes mentions obligatoires » : c'est lui qui fait foi.

**Correction du 11 novembre au soir : elle n'adhère à aucun médiateur.** Sa réponse : « je ne suis pas adhérente, j'ai dû recopier ça quelque part ». La rubrique est retirée des mentions légales et l'article 12 des CGV aussi, l'ancien article 13 devient le 12. Un commentaire HTML marque l'endroit dans les deux fichiers. Elle doit adhérer à un médiateur de la consommation parce que le bilan de compétences se vend à des particuliers. Tant que ce n'est pas fait, le site n'en cite aucun : c'est un manque, mais ce n'est plus une affirmation fausse.

**Hébergeur.** Netlify, Inc., 101 2nd Street, San Francisco, CA 94105. Netlify ne publie pas de téléphone, son adresse de contact le remplace.

**Menu.** Le vrai logo fait 171 px de large contre 134 pour l'ancien mot-symbole. Le burger passe de 920 à 1100 px et le téléphone s'efface jusqu'à 1280 px. Au passage, ça corrige un débordement qui existait déjà entre 921 et 980 px.

**Vu et non corrigé.** Sur l'accueil, en dessous de 366 px de large, le bouton « Voir les accompagnements » est trop long et la page déborde de 4 px. Sur un écran de 320 px, c'est le bouton « Prendre rendez-vous » du bas de chaque page qui déborde.

### Téléphone retiré, et passage en version de production

À la demande d'Augustin, le numéro de téléphone sort du site : en-tête des 12 pages, page contact, page accessibilité. Il reste dans les mentions légales, où il est obligatoire pour une société. La fiche officielle « Mentions obligatoires sur le site internet d'une entreprise » le liste avec l'adresse mail, et annonce jusqu'à 375 000 € d'amende pour une société en cas de manquement.

Dans la foulée, les éléments de préversion sont retirés des fichiers : plus de `noindex` dans `site/_headers`, plus de balise `review.js`, plus de formulaire `avis-maquette`. Le fichier `review.js` lui-même reste à supprimer à la main, les outils fichier ne savent pas supprimer.

**Piège d'outillage découvert.** Une écriture dans le dossier depuis un même chemin de préparation renvoie parfois l'ancien contenu : les notes de reprise écrites en fin d'après-midi n'avaient pas été mises à jour, alors que l'outil annonçait le contraire. Depuis, chaque écriture part d'un chemin neuf, et la taille du fichier est relue après coup. Les copies des prototypes dans `Claude outputs/` sont probablement restées à leur première version pour la même raison ; elles ne servent plus.

### CGV et CGU reprises du site Wix, défauts d'affichage corrigés

**CGV et CGU.** Lues sur `workandjoy.org/cgv` et `/cgu`, recopiées mot pour mot dans deux nouvelles pages aux mêmes adresses, donc sans redirection à prévoir. Une seule retouche : la phrase « Ce modèle est à adapter selon les services et les spécificités de ton activité », qui était publiée telle quelle à la fin des CGU, est retirée. Les contradictions entre les CGV et le nouveau site sont listées dans `REPRENDRE-ICI-1.md`, point 2 : elles ne sont pas corrigées, c'est un texte contractuel.

**Défauts d'affichage.** Un balayage des 14 pages à six largeurs de 320 à 414 px en a trouvé plus que les trois signalés :

| Défaut | Correction |
|---|---|
| Texte collé au bloc violet du témoignage, pages formation, dirigeant et bilan | De l'air sous le bloc qui précède. Sur formation et dirigeant, par une classe `gains--avant-bloc`, parce que le même bloc est suivi d'autre chose sur deux autres pages |
| Titre « Accompagnement » trop large sous 386 px, pages dirigeant et équipes | La taille du titre suit la largeur de l'écran en dessous de 427 px. C'était le plus sérieux : un iPhone de 375 px débordait de 11 px |
| Bouton « Voir les accompagnements » trop large sous 366 px, accueil | Sous 400 px, les boutons ont moins de marge intérieure et peuvent passer sur deux lignes |
| Bouton « Prendre rendez-vous » du bas trop large sous 343 px, toutes les pages | Même correction |
| Peu d'air entre le texte et « On en parle quinze minutes ? » sur les pages légales, sur téléphone | Marge basse des pages légales relevée |

Après correction : aucun débordement sur les 14 pages de 320 à 414 px.

**Le O du logo.** Une fois la bille partie, le O vide était tracé trop épais. Il devient un trait fin et atténué, à l'intérieur du rond d'origine.

**Animations.** Une arête séparée du bloc voisin par une marge n'est plus retenue comme palier : la ligne d'arrêt ne tomberait pas sur le bord visible.

---

## 3 novembre 2026 — Certifications, logos, et passage de la checklist

Trois sujets dans la journée : poser les logos Qualiopi et UPE13 correctement, ranger les déclinaisons du logo Work and Joy, puis passer le site au crible d'une checklist de 55 points.

### Qualiopi

Le badge était déjà le bon fichier, `LogoQualiopi-300dpi-Avec Marianne.png`, posé sur fond blanc par `.creds__badge`. Deux règles de la charte étaient donc déjà tenues sans qu'on l'ait cherché : le bandeau « Marianne + République française », obligatoire dès lors que l'émetteur n'est pas l'État, et le cartouche blanc, obligatoire quel que soit le fond.

Ce qui manquait, c'est la **mention obligatoire**. La charte graphique de mars 2023 impose qu'elle accompagne le logo mot pour mot, et qu'elle soit « de taille équivalente ou légèrement plus petite que *processus certifié* ». Le site se contentait d'une reformulation dans la liste de crédibilité. Ajoutée sous le badge, à 0,7 rem, avec les deux catégories réellement certifiées :

> La certification qualité a été délivrée au titre des catégories d'actions suivantes :
> **ACTIONS DE FORMATION** — **BILANS DE COMPÉTENCES**

Les deux catégories viennent du certificat `QUA25030046` lui-même, émis par Activcert le 3 mai 2025, cycle du 02/05/2025 au 01/05/2028. Ne pas en ajouter une troisième : VAE et apprentissage ne sont pas couverts.

**Ce que la charte interdit, et qu'il ne faut pas « améliorer » plus tard** : sortir le logo de son cartouche blanc, retirer le bandeau Marianne, changer une couleur ou une typo, le déformer, lui appliquer un effet ou une transparence. Et côté supports, l'interdiction qui nous concerne directement : pas de logo sur un support dédié à une seule action de formation. C'est la raison pour laquelle le badge reste sur l'accueil et n'est pas descendu sur `formation-management/` ni `bilan-de-competences/`, qui n'en portent que la mention en texte. La page d'accueil est une présentation de structure, elle est dans les usages conformes, au même titre que les réseaux sociaux, les brochures générales et la signature mail.

### UPE13

Logo « adhérent 2026 » ajouté au pied de page des 12 pages, sous le logo Work and Joy. Sa charte réserve explicitement l'usage au site web et aux signatures d'e-mail, interdit la déformation, le changement de couleur et tout effet ajouté, et rappelle que le droit d'usage tombe si la cotisation n'est plus à jour. **À vérifier chaque début d'année**, le logo porte le millésime.

Détail technique qui a décidé de la mise en forme : le PNG fourni a toute sa moitié haute en transparent, et le mot « UPE13 » y est écrit en violet. Posé tel quel sur le violet du pied de page, il disparaissait. Il est donc posé sur un disque blanc, `border-radius: 50%`, ce qui ne touche ni ses proportions ni ses couleurs.

### Logos Work and Joy

Les SVG, PNG et PDF des trois déclinaisons, plus `Logo_Bleu_Seul.png` et la fiche de charte, rangés dans `ressources/logos-work-and-joy/`. Les masters lourds (`.ai`, `.eps`, `.jpg`) et les doublons `[27]`, `[54]`… sont restés dans `LOGO/`.

**Piste explorée et abandonnée : le logo jaune en pied de page.** L'idée était de le poser directement sur le violet, sans cartouche blanc. Elle ne marche pas. « Jaune » ne désigne pas une version claire du logo, mais la version dont le carré est jaune au lieu d'être violet. Dans les trois déclinaisons, la signature « WORK & JOY / ENJOY YOUR JOB » reste en violet : sur fond violet elle disparaît, et il ne reste qu'un carré jaune flottant. Avec le cartouche blanc, elle revient, mais le jaune entre alors en concurrence avec celui des intitulés de colonnes juste à côté.

Ce qui marcherait vraiment : une version en réserve, signature blanche sur fond transparent. La charte du logo n'en fournit pas, mais sa dernière page montre le sigle sur aplat violet avec les filets en blanc, donc l'esprit y est. À demander à qui a fait le logo, ou à dériver du SVG avec l'accord d'Anne-Sophie.

### Passage de la checklist des 55 points

Checklist générique trouvée en ligne, passée en revue intégralement. Sept corrections retenues, six faites dans la journée.

**Fait**

| Quoi | Pourquoi |
|---|---|
| Texte avant photo sur mobile | `.hero__media` était en `order: -1` sous 860 px. Sur un téléphone, le portrait remplissait tout le premier écran : le titre, le chapô et les deux boutons tombaient sous la ligne de flottaison. Supprimé |
| Téléphone dans l'en-tête | `06 24 31 07 59` en `tel:` cliquable sur les 12 pages. Il n'existait que sur la page contact |
| Blocs « Et aussi » | Trois passerelles contextuelles avant l'appel à l'action final, sur les 5 offres plus À propos et Témoignages. Les pages d'offre ne portaient qu'**un seul** lien interne dans leur contenu, le bouton de rendez-vous |
| Six méta-descriptions raccourcies | Elles allaient jusqu'à 222 caractères et auraient été coupées dans Google. Toutes entre 151 et 155 |
| JSON-LD `Service` | Un bloc par page d'offre, `provider` rattaché au `ProfessionalService` de l'accueil. Répond au point 2.3 de `AUDIT-PREVERSION.md`, partiellement : `Person` et `BreadcrumbList` restent à faire |
| `white-space: nowrap` sur le menu | Les libellés se cassaient en deux lignes vers 1100 px, avant même l'ajout du téléphone |

Le téléphone s'efface entre 921 et 1200 px, où la barre est déjà pleine. Il reste dans le menu burger en dessous de 921 px.

**Points de la checklist écartés, et pourquoi**

- *Live-chat.* Aucun sens pour du coaching à 2 000 € vendu par visio de quinze minutes.
- *Horaires d'ouverture.* L'agenda Microsoft Bookings fait déjà le travail, et mieux.
- *Newsletter.* Pas tant qu'il n'y a rien à envoyer. Un champ d'inscription vide dessert.
- *Carte d'accès.* Oui sur le principe, mais **pas en iframe Google Maps** : ce serait exactement le transfert de données vers Google qu'on a évité en auto-hébergeant les polices. Un lien vers la fiche Google, déjà présente dans le JSON-LD en `sameAs`, suffit.
- *Fil d'Ariane.* Douze pages sur deux niveaux, le menu suffit. Le `BreadcrumbList` en JSON-LD garde un intérêt pour les résultats Google, pas le fil visuel.
- *Moyens de paiement, blog et ses six sous-points.* Sans objet, ou reportés avec 11ty.

**Ce que la checklist rate**, et qui compte bien plus ici : le RGPD, l'accessibilité réelle, et la conformité Qualiopi. Elle est écrite pour un site e-commerce ou un commerce de proximité.

### Contrastes, mesurés

Pour mémoire, le site passe largement. Le plus faible rapport mesuré est 5,32:1 (texte doux sur violet), le reste va de 7 à 17:1. Clair et sombre passent AA, l'essentiel passe AAA. Attention, ce calcul ne couvre pas les `<dt>` relevés au point 3.1 de `AUDIT-PREVERSION.md`, qui restent à corriger.

### Problème d'outillage rencontré

Le dossier `workandjoy-refonte` ne se monte plus dans le shell distant. Les outils fichier fonctionnent, le shell non. Cause probable : le dossier contient un répertoire `.tmp.drivedownload`, trace de Google Drive pour ordinateur, et les fichiers ajoutés portent tous la même date à la milliseconde près, signature d'un téléchargement en masse. Si `~/Documents` est synchronisé par Drive, c'est un système de fichiers virtuel, pas un dossier local ordinaire.

Conséquence pratique : on travaille par copies aller-retour. Ça marche, c'est plus lent, et **il devient impossible de déplacer, renommer ou supprimer un fichier à distance**, seulement d'en écrire. C'est aussi ce qui bloque la mise en place du dépôt git, qui demande un `git init` sur place.
