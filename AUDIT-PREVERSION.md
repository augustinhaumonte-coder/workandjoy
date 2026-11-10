# Audit de la préversion

> 26 octobre 2026. Préversion `reliable-druid-e56775.netlify.app`, 12 pages.
> Complète l'étape 5 de `REPRENDRE-ICI.md` (recette). À relire avant la bascule DNS.

---

## Méthode, et ce qu'elle ne dit pas

Analyse statique des 12 fichiers HTML, du CSS, du `robots.txt`, du `sitemap.xml` et du `_headers`, plus Lighthouse en mobile sur quatre pages.

Lighthouse a tourné sur une copie servie en local, pas sur Netlify. Conséquence : **les constats sur les en-têtes de cache et sur le temps de réponse serveur ne comptent pas**, Netlify s'en charge via son CDN. Tout le reste vient du code et vaut à l'identique en ligne. La version en ligne correspond bien aux fichiers locaux, vérifié sur l'accueil et sur la page témoignages.

### Scores Lighthouse, mobile

| Page | Performance | Accessibilité | SEO | Bonnes pratiques | LCP |
|---|---|---|---|---|---|
| Accueil | 94 | 94 | 100 | 96 | 3,0 s |
| À propos | 97 | 98 | 100 | 96 | 2,6 s |
| Contact | 99 | 98 | 100 | 96 | 1,8 s |
| Témoignages | 99 | 98 | 100 | 96 | 1,7 s |

CLS à 0 partout sauf témoignages (0,018), TBT à 0 ms partout. Le site est rapide et stable. Les problèmes sont ailleurs.

---

## 1. Bloquant avant la bascule

### 1.1 Deux chiffres faux

**Témoignages.** L'en-tête annonce « 5,0 ★ 10 avis Google ». Neuf avis sont affichés. La meta description dit « Les dix avis Google reçus par Work and Joy ». Les deux recommandations LinkedIn sont dans une section séparée, elles ne comblent pas l'écart.

Soit il manque un avis à recopier, soit il faut écrire neuf. Un visiteur qui compte se dira que le reste est à l'avenant.

**Durée d'ingénierie.** L'accueil affiche « 15 ans d'ingénierie en microélectronique » et, plus bas, « quinze ans de conception de puces wifi et bluetooth ». La meta description de la page À propos dit « Douze ans de conception de puces électroniques [...] puis quinze ans à accompagner ».

Le site se contredit lui-même. Le CV dit 1999 à 2011, soit douze ans d'ingénierie, et 2011 à aujourd'hui, soit quinze ans d'accompagnement. La version de la meta description est la bonne, c'est l'accueil qu'il faut corriger. À trancher avec Anne-Sophie, c'est son parcours.

### 1.2 Le lien LinkedIn ne mène nulle part

Dans le pied de page des **12 pages** : `<a href="https://www.linkedin.com/">LinkedIn</a>`. Il ouvre l'accueil de LinkedIn, pas son profil. Sur un site B2B, c'est le lien le plus cliqué après « Prendre rendez-vous ».

### 1.3 Les restes de préversion

Déjà listés en étape 7 de `REPRENDRE-ICI.md`, confirmés présents :

- `_headers` : `X-Robots-Tag: noindex` sur `/*`
- `assets/js/review.js` et les 12 balises `<script defer src="...review.js">`
- le formulaire caché `avis-maquette` dans `index.html`, lignes 151-152

### 1.4 Les trois trous légaux

- `mentions-legales/index.html:70` : raison sociale, adresse et téléphone de l'hébergeur
- `mentions-legales/index.html:74` : médiateur de la consommation
- `accessibilite-et-handicap/index.html:57` : accessibilité du 121 avenue Clot Bey

---

## 2. SEO

### 2.1 Aucune balise canonical, et chaque page a deux adresses

Impact : élevé.

Aucune des 12 pages n'a de `<link rel="canonical">`. En parallèle, les liens internes pointent tous vers `/contact/index.html` plutôt que `/contact/` : **224 liens** dans ce format.

Google peut donc découvrir chaque page sous deux URLs, avec et sans `index.html`, et devra choisir seul laquelle garder. Sur un site neuf qui démarre son indexation, autant ne pas lui laisser le choix.

Deux corrections, à faire ensemble :

1. Ajouter sur chaque page sa canonical, en absolu :
   ```html
   <link rel="canonical" href="https://www.workandjoy.org/contact/">
   ```
2. Réécrire les liens internes sans `index.html`. Un `sed` sur les 12 fichiers :
   ```bash
   cd site
   sed -i '' -E 's|href="([^"]*)index\.html"|href="\1"|g' index.html */index.html
   ```
   Attention, cela transforme `href="index.html"` en `href=""`. Reprendre ensuite ces cas-là en `href="/"` ou `href="../"` selon la page.

Vérifier aussi, dans Netlify, que l'option **Pretty URLs** est active : elle redirige `/contact/index.html` vers `/contact/` et ferme le sujet côté serveur.

### 2.2 Pas d'Open Graph, pas de Twitter Card

Impact : élevé, pour ce site précisément.

Aucune balise `og:title`, `og:description`, `og:image` sur aucune page. Quand Anne-Sophie partage le lien sur LinkedIn, le post affiche une vignette grise sans titre ni visuel. Pour une activité B2B dont LinkedIn est le canal principal, c'est la correction au meilleur rapport effort/résultat du lot.

À ajouter dans le `<head>` de chaque page, avec une image dédiée en 1200×630 :

```html
<meta property="og:type" content="website">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="https://www.workandjoy.org/assets/img/og.jpg">
<meta property="og:url" content="https://www.workandjoy.org/contact/">
<meta name="twitter:card" content="summary_large_image">
```

### 2.3 Données structurées limitées à l'accueil

Impact : moyen.

L'accueil porte un bloc `ProfessionalService` correct et valide. Les 11 autres pages n'ont rien. Manquent :

- `Person` sur À propos, avec `jobTitle`, `alumniOf`, `sameAs` vers son LinkedIn
- `Service` sur les quatre pages d'offres, rattaché au `ProfessionalService` par `provider`
- `BreadcrumbList` sur toutes les pages internes

Ne pas ajouter de `AggregateRating` ni de `Review` pour les avis Google : Google n'affiche pas les avis qu'un site publie sur lui-même en extrait enrichi. Les laisser en texte.

### 2.4 Pas de favicon

Impact : faible en référencement, visible partout ailleurs.

Aucun `<link rel="icon">`, et la requête `/favicon.ico` renvoie 404. Pas d'icône dans l'onglet, dans les favoris, ni à côté du résultat Google sur mobile. Le logo SVG existe déjà, il suffit d'en dériver un `favicon.svg` et un `apple-touch-icon.png` de 180×180.

### 2.5 Deux titres à retoucher

- Accueil, 73 caractères : tronqué dans les résultats. Viser 60.
- `seminaire-equipe` : seul titre du site sans « | Work and Joy ».

Les dix autres titres et les douze meta descriptions sont uniques, bien calibrés et écrits pour être lus. Rien d'autre à y faire.

---

## 3. Accessibilité

Le score de 94 à 98 est bon. Trois points restent, et la page « Accessibilité et handicap » du site rend le premier un peu gênant.

### 3.1 Contraste insuffisant sur les étiquettes de tarifs

Les `<dt>` des blocs format et tarif affichent `#b3b3d4` sur fond violet `#424193`, soit un rapport de **4,28:1**. Le seuil WCAG AA est 4,5:1. Texte petit, 10,9 px, et en gras.

Éclaircir la couleur suffit : `#c2c2de` passe à 4,9:1. Les sélecteurs concernés, dans `style.css` : `.specs dt` ligne 310, `.offre-head__keys dt` ligne 635, `.pratique__list dt` ligne 685.

### 3.2 Saut de niveau dans le pied de page

Sur les 12 pages, la hiérarchie passe de `h2` à `h4` au moment du pied de page. Les lecteurs d'écran annoncent un niveau manquant. Passer ces trois `<h4>` en `<h3>`, ou en `<p class="foot__titre">` puisqu'ils ne structurent pas le contenu.

### 3.3 Logo, libellé accessible décalé

`<a class="mark" aria-label="Work and Joy, accueil">` : l'`aria-label` ne reprend pas exactement le texte visible, ce qui gêne la commande vocale. Soit « Work and Joy » tout court, soit retirer l'attribut, le texte visible suffit.

---

## 4. Performance

Déjà très bon. Deux choses seulement.

### 4.1 Le portrait de l'accueil

`portrait-hero.jpg` est servi en 1000×1250 pour un affichage mobile de 371×464. C'est l'élément LCP de la page, et ce qui la met à 3,0 s contre 1,7 s pour les autres.

Produire une version 800 px de large en WebP, et servir les deux :

```html
<picture>
  <source srcset="assets/img/portrait-hero.webp" type="image/webp">
  <img src="assets/img/portrait-hero.jpg" width="1000" height="1250"
       alt="Anne-Sophie Haumonté, fondatrice de Work and Joy" fetchpriority="high">
</picture>
```

Même traitement pour `portrait-histoire.jpg`, en lazy.

### 4.2 Détails

- `style.css`, 33 ko non minifiés et bloquant le rendu. Sur un seul fichier déjà petit, le gain est marginal. À faire le jour où 11ty arrive, pas avant.
- `assets/js/main.js` contient un commentaire et rien d'autre, et n'est référencé par aucune page. À supprimer.

---

## 5. À tester à la main

Ce que l'analyse du code ne peut pas trancher :

1. **Le formulaire de contact.** Il est correctement déclaré (`data-netlify="true"`, champ `form-name`, pot de miel `societe-bis`). Reste à envoyer un vrai message et à vérifier qu'il arrive dans Netlify, onglet Forms, puis à activer la notification par e-mail. L'étape 6 de `REPRENDRE-ICI.md` peut passer en « à vérifier » plutôt qu'en « à faire ».
2. **Le lien Bookings Microsoft**, présent sur les 12 pages. Un lien mort sur le bouton principal coûte plus cher que tout le reste de cette liste.
3. **Le mode sombre**, sur une vraie machine en thème sombre.
4. **Un vrai téléphone**, en 4G, pas l'émulateur.

---

## 6. Ce qui est déjà en place

Pour mémoire, et pour ne pas y retoucher :

- Les 12 titres et les 12 meta descriptions sont uniques, de bonne longueur, et ne récitent pas des mots-clés
- Un seul `h1` par page, pertinent
- Toutes les images ont un `alt` descriptif, des dimensions explicites, et `loading="lazy"` ou `fetchpriority="high"` selon leur place
- Aucun lien interne cassé sur les 224 liens
- `lang="fr"`, `viewport`, encodage : corrects partout
- CLS à 0, TBT à 0 ms
- Polices auto-hébergées et préchargées
- `robots.txt` et `sitemap.xml` propres, les 12 URLs y sont, en absolu, sur le domaine de production

---

## Plan d'action

**Avant la bascule, sans exception**

1. Trancher 15 ou 12 ans avec Anne-Sophie, corriger l'accueil
2. Corriger le nombre d'avis, neuf ou dix
3. Mettre le vrai lien LinkedIn dans les 12 pieds de page
4. Combler les trois `À COMPLÉTER`
5. Retirer `_headers`, `review.js`, les 12 balises script, le formulaire `avis-maquette`
6. Tester le formulaire de contact et le lien Bookings pour de vrai

**Dans la foulée, avant l'indexation**

7. Canonicals sur les 12 pages, liens internes sans `index.html`, vérifier Pretty URLs
8. Open Graph sur les 12 pages, avec une image 1200×630
9. Favicon

**Quand le site est en ligne**

10. Contraste des `<dt>`, `h4` du pied de page, `aria-label` du logo
11. Portrait de l'accueil en WebP redimensionné
12. `Person`, `Service` et `BreadcrumbList` en JSON-LD
13. Supprimer `main.js`
14. Search Console, et revérifier les Core Web Vitals sur données réelles au bout d'un mois
