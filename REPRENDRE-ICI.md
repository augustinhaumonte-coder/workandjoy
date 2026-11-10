# Reprendre le projet

> Mis à jour le 16 octobre 2026. Point d'entrée du dossier.
> Refonte du site de Work and Joy, Anne-Sophie Haumonté, Marseille.
> Les deux autres documents : `CADRAGE.md` pour la stratégie, `DNS-avant-bascule.md` pour tout ce qui touche au domaine.

---

## En deux phrases

Le site Wix actuel, `workandjoy.org`, est remplacé par un site statique écrit à la main, dans `site/`. Douze pages sont écrites et relues, rien n'est encore en ligne.

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
├── robots.txt  sitemap.xml  _headers
└── assets/  css/style.css · js/review.js · fonts/ (6 woff2) · img/ (4 fichiers)
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

**Augustin**

7. Trois trous marqués par des commentaires `À COMPLÉTER` dans le HTML : adresse complète de l'hébergeur, coordonnées du médiateur, accessibilité précise des locaux.
8. Exporter de Wix avant toute résiliation : CGV, CGU, messages du formulaire, clients et rendez-vous Wix Bookings.
9. Désactiver le renouvellement automatique du forfait Wix avant le **21 mai 2027**, sans toucher au domaine qui se renouvelle le 11 juin.

---

## Prochaines étapes, dans l'ordre

1. **Mettre en ligne une préversion** sur Netlify pour qu'Anne-Sophie voie le site sur son téléphone. Voir plus bas.
2. Recueillir ses retours, corriger.
3. Combler les trous légaux, régler le médiateur.
4. Décider de 11ty, qui conditionne le blog.
5. Recette : Lighthouse, mobile réel, formulaire de contact, relecture des textes.
6. Brancher le formulaire sur Netlify Forms.
7. **Retirer les éléments de préversion** : le fichier `site/_headers` qui interdit l'indexation, le fichier `site/assets/js/review.js`, les douze balises `<script ... review.js>`, et le formulaire caché `avis-maquette` dans `index.html`.
8. Bascule DNS : 3 enregistrements A et le CNAME `www` dans le panneau Wix. Ne toucher à rien d'autre.
9. Search Console, et mise à jour du lien du site sur la fiche Google.
10. Résilier le forfait Wix.

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

**Formes.** Tout est carré, sauf les boutons qui sont en pilule. Règle à tenir.

**Classes réutilisables** : `.btn`, `.btn--sm`, `.btn--lg`, `.btn--ghost` pour les boutons, `.temps` pour une rangée de trois blocs à filet jaune, `.quote` pour une citation pleine largeur sur violet, `.final` pour l'appel à l'action de fin, `.pratique__list` pour un tableau de caractéristiques, `.legal` pour une page de texte.

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
