# DNS de workandjoy.org, relevé avant toute modification

> Relevé le 16 octobre 2026 depuis l'extérieur, via les résolveurs publics Google.
> Ce fichier est la photo de l'état actuel. En cas de problème pendant la bascule, on remet ces valeurs.

## Hébergeur DNS

Les serveurs de noms sont ceux de Wix, donc c'est Wix qui répond pour tout le domaine.

```
NS    workandjoy.org    ns0.wixdns.net
NS    workandjoy.org    ns1.wixdns.net
```

## Site web, à modifier le jour de la bascule

```
A      workandjoy.org        185.230.63.186
A      workandjoy.org        185.230.63.107
A      workandjoy.org        185.230.63.171
CNAME  www.workandjoy.org    cdn3.wixdns.net
```

Ce sont les adresses des serveurs Wix. Ce sont les seules lignes à changer.

## Messagerie Microsoft 365, à ne surtout pas toucher

```
MX     workandjoy.org                  10 workandjoy-org.mail.protection.outlook.com
TXT    workandjoy.org                  v=spf1 include:spf.protection.outlook.com -all
TXT    workandjoy.org                  MS=ms95720206
CNAME  autodiscover.workandjoy.org     autodiscover.outlook.com
```

Si une seule de ces quatre lignes disparaît, sa messagerie tombe. Le MX fait arriver le courrier, le SPF empêche que ses mails partent en spam, le `MS=` est la preuve de propriété du domaine pour Microsoft, et `autodiscover` est ce qui permet à Outlook de se configurer tout seul.

## Absents aujourd'hui

- **DKIM** : `selector1._domainkey` et `selector2._domainkey` n'existent pas, la signature DKIM n'est pas activée dans Microsoft 365.
- **DMARC** : `_dmarc` n'existe pas.

Sans ces deux-là, ses mails passent plus facilement en spam chez certains destinataires, et n'importe qui peut usurper son adresse. À activer un jour depuis la console Microsoft 365, ce n'est pas lié à la refonte et ça peut attendre.

## Stratégie de bascule

**On ne change pas les serveurs de noms.** On garde le DNS chez Wix et on modifie uniquement les enregistrements A et le CNAME `www`. Les quatre lignes de messagerie ne sont alors jamais touchées, et le risque de couper ses mails tombe à zéro.

C'est aussi ce qui dicte le choix de l'hébergeur : il faut un hébergeur qui accepte un domaine dont le DNS est géré ailleurs. **Netlify** le fait sans difficulté, avec un enregistrement A vers leur répartiteur de charge et un CNAME pour `www`. Cloudflare Pages préfère que le domaine soit chez Cloudflare, ce qui obligerait à déplacer tout le DNS, messagerie comprise. Netlify, donc.

## Reste à vérifier dans le panneau Wix

Des enregistrements peuvent exister sur des sous-domaines sans être visibles depuis l'extérieur tant qu'on ne connaît pas leur nom. Relever la liste complète dans le panneau DNS de Wix, en particulier :

- `sip`, `lyncdiscover`, `_sip._tls`, `_sipfederationtls._tcp` si Teams est utilisé pour la téléphonie
- `enterpriseregistration`, `enterpriseenrollment` si des appareils sont inscrits à Intune
- tout CNAME de vérification laissé par un autre service
