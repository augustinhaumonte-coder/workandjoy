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
