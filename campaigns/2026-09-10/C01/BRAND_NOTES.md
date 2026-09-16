# C01 · Ką veiksime po darželio?

Atnaujinta 2026 m. rugsėjo 16 d. pagal vartotojo komentarus būtent C01. Išsaugota pasirinkto V3 hero kompozicija, penki produktai, trys veiklų grupės ir šeimos istorija.

## HTML versija

Hero lieka vienas paveikslėlis. Pasisveikinimas, veiklų antraštės, produktų pavadinimai, aprašai, kainos, mygtukai, brando istorija ir poraštė yra HTML. Produktų iliustracijos ir šeimos nuotrauka iškirptos iš vartotojo pasirinkto V3, todėl išsaugotos anksčiau patvirtinto generuoto maketo smulkios detalės. Originalas campaign-01-v3.png ir senos vaizdų juostos nepakeisti.

Pagrindinis tekstas 18 px, eilutės aukštis 29 px. Pavadinimai 22–34 px. Padidinti tarpai, aprašai papildyti veiklų idėjomis. Telefone iki 480 px produktai persirikiuoja į vieną stulpelį. Montserrat nepalaikančiose pašto programose naudojamas Arial.

Fonas #E5FCEF, tekstas #07554C, mygtukai #00964F, poraštė #005735. Hero apačios 24 px juosta tiksliai sutampa su HTML fonu. Nukirpti po hero prasidedančių dekoracijų fragmentai pašalinti, hero turinys ir CTA išsaugoti. Dekoratyvinė banga pereina į poraštės spalvą.

## Failai

* newsletter.html: siuntimo platformai, vaizdai viešais HTTPS adresais.
* preview.html: vietinė peržiūra, naudojanti assets/live.
* newsletter.txt: tema, preheaderis, visi tekstai ir nuorodos.
* preview-desktop.png ir preview-mobile.png: viso atnaujinto HTML peržiūros; preview-mobile-320.png: 320 px pločio viršutinės dalies patikros vaizdas.
* assets/live: hero, penki produktai, šeimos nuotrauka, banga ir Montserrat šriftai.

## Šaltiniai

Visų penkių produktų kainos ir InStock būsena patikrintos rugsėjo 16 d.: SK10 49 €, SK9 24 €, knyga 30 €, logikos žaidimas 39,20 €, LED lenta 35 €. Visos aštuonios unikalios svetainės nuorodos grąžino HTTP 200. Tą pačią dieną dar kartą patikrinta šeimos istorija. Kainos ir likučiai gali keistis.

* https://www.skilsas.lt/yes-for-skills-garso-kolonele-vaikams-su-irasytomis-lietuviskomis-dainomis-ir-pasakomis
* https://www.skilsas.lt/yes-for-skills-lietuviskai-igarsintos-korteles-snekancios-korteles
* https://www.skilsas.lt/mano-pirma-lavinamoji-veiklos-knyga-su-daugkartinio-naudojimo-lipdukais
* https://www.skilsas.lt/interaktyvus-logikos-lavinimo-zaidimas-skilsas-su-uzduociu-kortelemis
* https://www.skilsas.lt/led-sviecianti-piesimo-lenta-skilsas
* https://www.skilsas.lt/apie-mus

## Siuntimas

Po vizualinės korekcijos patikrinta 600, 390 ir 320 px pločiais: nėra horizontalaus slinkimo, visi 8 vaizdai įsikrauna, produktų aprašai išlieka 18 px. Hero ir poraštės spalvinės ribos patikrintos pagal pikselius. HTML failas yra apie 21 KB ir nenaudoja base64 vaizdų.

Omnisend turi užpildyti [[account.address]], [[account.city]], [[account.zipCode]], [[account.country]], [[preference_link]] ir [[unsubscribe_link]]. Naršyklėje šie laukai neužpildyti. Prieš siuntimą reikalingas bandomasis laiškas iš siuntimo platformos. Naršyklės patikra nėra Gmail ar Outlook pristatymo testas. Kampanija nesuplanuota ir neišsiųsta.
