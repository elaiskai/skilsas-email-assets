# C02 · Pasakų vakaras

Parengta 2026 m. rugsėjo 17 d. pagal 8 laiškų plano antrą temą. Planuojama data rugsėjo 18 d. yra plano žyma; kampanija siuntimo platformoje nesuplanuota.

Tema: „Kokios pasakos klausysimės šįvakar?“

Preheaderis: „Išsirinkite istoriją, o tada pasikalbėkite apie jos veikėjus.“

## Kūrybinė kryptis

Atnaujintas hero turi ramesnę fotografijos estetiką: tamsiai žalia siena, natūrali lango šviesa, šeima fone ir SK10 ant medinio stalo. Tai generuota scena pagal tikrą SK10 produkto nuotrauką, ne dokumentinė fotografija. Oficialaus PNG logotipo juodos dalys mechaniškai pakeistos šviesiomis, išsaugant originalią geometriją, skaidrumą ir žalią akcentą. Logotipas negeneruotas. Modelio pavadinimo įrankio rezultatas nepatvirtina. Hero produkto detalės paremtos originalu, bet nėra originalaus packshot pikselių kopija. Dekoratyvinių knygų užrašai nėra parduodamų ar įrašytų pasakų pavadinimai.

Hero yra vienas 1200 × 1100 px JPG (apie 255 KB) su antrašte ir CTA. Visi tekstai žemiau hero, kainos, mygtukai, veiklos žingsniai ir poraštė yra HTML. Šešių produktų nuotraukos yra autentiški svetainės ar perduotos bibliotekos failai, tik sumažinti ir apkirpti. Išsaugotas realių pakuočių Yes For Skills ženklinimas.

Šriftas Montserrat, atsarginis Arial. Pagrindinis tekstas 18 px / 29 px. Spalvos: #E5FCEF šviesus fonas, #104C3E tekstas, #188348 mygtukai, #D5F1DF veiklos blokas, #084B38 poraštė. Žalia kryptis atitinka kliento patikslinimus. Fonų spalvos yra maketo sprendimai, ne oficialaus brandbook specifikacija.

Laiškas pirmuoju asmeniu, su atskiru „Labas!“ ir „Su meile, Ingrida“. Šeimos kilmės istorija nekartojama. Pateikiami trys klausymosi žingsniai ir atskiras HTML žaidimas „Sukurkite savo pasaką“ su veikėjo, vietos ir tikslo pasirinkimais. Nepridedama nuolaida, skuba, nepatikrinti pasakų pavadinimai ar vystymosi garantijos.

## Patikrinti produktai

Visos šešios kainos ir InStock būsena patikrintos oficialiuose produktų puslapiuose 2026 m. rugsėjo 17 d. Vieša būsena nenurodo sandėlio vienetų kiekio. Kainos gali keistis.

| Produktas | Kaina | Šaltinis |
| --- | --- | --- |
| Garso kolonėlė SK10 | 49 € | https://www.skilsas.lt/yes-for-skills-garso-kolonele-vaikams-su-irasytomis-lietuviskomis-dainomis-ir-pasakomis |
| Šnekančios kortelės SK9 | 24 € | https://www.skilsas.lt/yes-for-skills-lietuviskai-igarsintos-korteles-snekancios-korteles |
| Pirma veiklos knyga | 30 € | https://www.skilsas.lt/mano-pirma-lavinamoji-veiklos-knyga-su-daugkartinio-naudojimo-lipdukais |
| Antra veiklos knyga | 30 € | https://www.skilsas.lt/mano-antra-lavinamoji-veiklos-knyga-su-daugkartinio-naudojimo-lipdukais |
| LED piešimo lenta | 35 € | https://www.skilsas.lt/led-sviecianti-piesimo-lenta-skilsas |
| Logikos žaidimas | 39,20 € | https://www.skilsas.lt/interaktyvus-logikos-lavinimo-zaidimas-skilsas-su-uzduociu-kortelemis |

SK10 turi 30 lietuviškų dainų ir 30 pasakų. Knyga turi daugkartinio naudojimo lipdukus, jos apraše siūloma pasakoti pagal gyvūnų paveikslėlius. Antroje knygoje yra užduotis „Kaip aš jaučiuosi?“. Logikos žaidimo instrukcijos įgarsintos lietuviškai. Pasakojimo ir pokalbio idėjos yra kampanijos pasiūlymai, ne naujos produktų funkcijos.

Oficialus logotipas: https://www.skilsas.lt/styles/montessorikorteles/images/logo.png

## Failai ir siuntimas

* newsletter.html: siuntimo platformai su viešomis HTTPS nuotraukų nuorodomis.
* preview.html: vietinė peržiūra su assets aplanku.
* newsletter.txt: tema, preheaderis, visas tekstas ir nuorodos.
* preview-desktop.png ir preview-mobile.png: viso HTML peržiūros.
* preview-mobile-320.png: 320 px pločio viršaus patikros vaizdas.

Naujas hero-v2.jpg pakeičia ankstesnį hero.png, kuris išsaugotas istorijai. Korekcijos metu SK10 produkto nuotraukai pridėtas pločio apribojimas: 320 px ekrane ji telpa 224 px stulpelyje. Patikrinta naršyklėje 600, 390 ir 320 px pločiais: nėra horizontalaus slinkimo, visi aštuoni vaizdai įsikrauna, aprašų tekstas lieka 18 px. Hero apatinės 24 px juostos skirtumas nuo #E5FCEF yra tik 1 RGB reikšmė, kraštų patikra praeita. Poraštės banga nepakeista. HTML apie 26 KB, be JavaScript, vietinių vaizdų adresų ar base64.

Omnisend turi užpildyti siuntėjo adreso, nuostatų ir atsisakymo laukus: [[account.address]], [[account.city]], [[account.zipCode]], [[account.country]], [[preference_link]], [[unsubscribe_link]]. Naršyklėje jie lieka neužpildyti. Prieš siuntimą reikia bandomojo laiško iš siuntimo platformos. Naršyklės peržiūra nėra Gmail ar Outlook laiško pristatymo testas. Kampanija neišsiųsta.

## Naujo hero generavimas

Įrankis: integruotas image_gen.imagegen. Nuorodos vaizdas: assets/products/sk10-pack.png. Originalas nukopijuotas į hero-concept-v2.png darbo aplanke. Galutinis failas: assets/hero-v2.jpg.

Tikslus generavimo tekstas:

Create a premium PHOTOGRAPHIC EMAIL HERO for Lithuanian family learning brand SKILSAS. Art direction: understated real lifestyle campaign shot by a human photographer for a Scandinavian home magazine, NOT an illustration or a 3D render. Attached image is the exact white SK10 player product reference: preserve its mint green arch handle and feet, oval white body, front horizontal grille and exact four top buttons (purple minus, orange plus, red, mint). One player only, realistic small tabletop scale. Setting: an ordinary beautiful lived-in Lithuanian apartment in late afternoon, muted deep forest green plaster wall, a simple walnut side table, a softly creased linen curtain, subdued green sofa behind. At the far right background a mother and preschool child are comfortably sitting close together seen only partially from the side/back, authentic candid moment, faces not focal, no posing or smiles to camera. Product sits on table in the lower right half, fully visible and physically grounded with a believable contact shadow. Human skin, fabric, wood grain and product plastic must look imperfect and real, slightly fine photographic grain, restrained natural colors, gentle real window light, 50mm lens, moderate depth of field. Do not use fairy tale scenery, oversized product, floating objects, fantasy glowing windows, giant chunky knits, yellow blown-out lamp, extreme bokeh, plastic-smooth CGI or HDR. No decorative stars, moons, hearts, leaves, doodles, clipart, stickers or cartoon motifs. Compose a complete single raster email hero about 1200 by 1100 proportions. Upper left and upper middle have calm dark green wall negative space for refined typesetting. Leave a clean empty space at very top center about 130px tall for the exact official logo to be added later; do not draw any logo. Exact Lithuanian headline on the upper-left, clean adult editorial Montserrat/Sans type, medium/semibold weight, not extra bold or rounded: 'Kokios pasakos' on first line, 'klausysimės' second line, 'šįvakar?' third line. Well-spaced but readable headline, warm white, 72px equivalent at 1200 width, left margin 90px. Beneath it a small 30px equivalent white subline: 'Viena istorija. Laikas kartu.' The type must be beautifully integrated over the actual dark photographic wall, no pale mint blob behind it. Near lower-left include a restrained off-white rounded rectangle button with DARK FOREST GREEN exact text 'Apžiūrėti SK10 →', about 360px wide, 74px high at1200 width; no gradient/bevel/glow. Keep text away from physical product. Bottom of photographic scene fades very subtly into pale mint #E5FCEF over the last100px; final28px band is solid #E5FCEF for email continuation. Sophisticated calm real photography and generous whitespace. This is an ad addressed to adults, not a children's book cover. Absolutely legible Lithuanian diacritics and physically accurate product reference.
