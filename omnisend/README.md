# SKILSAS · naujausi 16 laiškų

Šiame aplanke pateiktos naujausios šiame projekte redaguotos versijos. Senesni failai repozitorijos šaknyje nėra šio rinkinio dalis.

| Serija | Laiškai | Failai |
|---|---|---|
| Welcome | W1–W5 | welcome/W1.html ir t. t. |
| Abandoned cart | AC1–AC3 | cart/AC1-top.html + AC1-bottom.html ir t. t. |
| Abandoned checkout | CH1–CH2 | checkout/CH1-top.html + CH1-bottom.html |
| Winback | WB1–WB3 | winback/WB1.html ir t. t. |
| Abandoned product | AP1–AP2 | abandoned-product/AP1-top.html + AP1-bottom.html |
| Product review | PR1 | product-review/PR1-top.html + PR1-bottom.html |

## Įkėlimas į Omnisend

Welcome ir winback: naudoti pagrindinį .html failą kaip pilną HTML šabloną. Temos, preheader ir siuntėjo nustatymai yra manifest.json.

Kitoms serijoms: top.html HTML blokas → Omnisend dinaminis prekių blokas → bottom.html HTML blokas. Prie šablono pridėti atitinkamo laiško styles.css taisykles mobiliajam vaizdui. Cart / checkout bloke rodyti paliktas prekes; abandoned product bloke peržiūrėtas; review bloke nupirktas prekes ir atsiliepimų nuorodas.

Failai su -preview.html skirti peržiūrai. Juose esanti dinaminio bloko žyma nėra siunčiamo laiško dalis. Jos nekopijuoti į Omnisend.

Paveikslėlių adresai visuose įkėlimo HTML yra vieši HTTPS adresai. Nauji ir senesni paveikslėliai surinkti assets aplanke. Nepalikta vietinių failų nuorodų ar base64 paveikslėlių.

## Prieš įjungiant

Išsaugoti Omnisend paskyros, atsisakymo ir nuostatų personalizavimo laukus. Cart / checkout CTA naudoja jau projekte buvusį [[event.abandonedCheckoutURL]] lauką: redaktoriuje parinkti konkretaus srauto grįžimo nuorodą ir patikrinti su bandomuoju įvykiu. Įprastoje naršyklės peržiūroje šie laukai neveikia.

CH1 be nuolaidos. CH2 ir AC3: 10 % su KREPSELIS10. Welcome: SKILSAS10. Winback WB2 ir WB3: DOVANA10. Galiojimas ir realus pritaikymas parduotuvėje šiame įkėlime netikrinti.

Tai HTML failų publikavimas, ne Omnisend automatizacijų paleidimas. Dinaminiai blokai, laikai, auditorijos, išėjimai po pirkimo ir cart / checkout prioritetai nustatomi Omnisend. Prieš siunčiant patikrinti testinį laišką telefone ir kompiuteryje.
