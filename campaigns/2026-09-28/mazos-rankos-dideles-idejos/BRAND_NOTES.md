# SKILSAS · Mažos rankos. Didelės idėjos.

Parengta 2026-09-28. Siuntimo data nepasirinkta. Kampanija neišsiųsta.

Tema: Mažos rankos. Didelės idėjos. 🎨
Preheaderis: 8 idėjos kūrybos popietei: nuo šviečiančių piešinių iki spalvų ant vandens.

## Kryptis

Kūrybos popietė: 3 SKILSAS / Yes For Skills produktai ir 5 parduotuvės Tookyland produktai. Tookyland gamintojas nurodytas produktų kortelėse, šie produktai nepristatomi kaip pagaminti SKILSAS. Išlaikyta žalia ir mėtinė brando kryptis, oficialus logotipas ir Montserrat su Arial atsarga. Trumpi produktų aprašai atskira eilute, išnaudojant visą kortelės plotį.

## Patikrinti šaltiniai

Visi puslapiai tiesiogiai patikrinti 2026-09-28. Struktūriniuose duomenyse visiems 8 nurodyta InStock. Rodomos tik patikrintos dabartinės kainos, be išgalvotų nuolaidų, terminų ar skubos.

- LED šviečianti piešimo lenta SKILSAS su markerių laikikliu — 39 EUR
  https://www.skilsas.lt/led-sviecianti-piesimo-lenta-skilsas-su-markeriu-laikikliu
- LED šviečianti piešimo lenta SKILSAS — 35 EUR
  https://www.skilsas.lt/led-sviecianti-piesimo-lenta-skilsas
- Yes For Skills lietuviškai įgarsintos Šnekančios kortelės „Mokausi piešti“ su garsiniais kortelių apibūdinimais, kalbančios lietuviškai — 36 EUR
  https://www.skilsas.lt/yes-for-skills-lietuviskai-igarsintos-snekancios-korteles-mokausi-piesti-kalbancios-lietuviskai
- Tookyland lengvai nuplaunamų šilkinių kreidelių rinkinys – 24 spalvos (LT138A) — 13.93 EUR
  https://www.skilsas.lt/tookyland-lengvai-nuplaunamu-silkiniu-kreideliu-rinkinys-24-spalvos-lt138a
- Tookyland didelis spalvinimo rulonas „Gyvūnų pasaulis“ (LT342) — 8.33 EUR
  https://www.skilsas.lt/tookyland-didelis-spalvinimo-rulonas-gyvunu-pasaulis-lt342
- Tookyland spalvinimo knygelė su akvarele ir teptuku „Dinozaurai“ (LT206) — 9.03 EUR
  https://www.skilsas.lt/tookyland-spalvinimo-knygele-su-akvarele-ir-teptuku-dinozaurai-lt206
- Tookyland kūrybinis marmuravimo rinkinys – 12 spalvų (LT150) — 17.5 EUR
  https://www.skilsas.lt/tookyland-kurybinis-marmuravimo-rinkinys-12-spalvu-lt150
- Tookyland kūrybinis langų piešimo rinkinys „Kosmoso pasaulis“ (LT123C) — 14 EUR
  https://www.skilsas.lt/tookyland-kurybinis-langu-piesimo-rinkinys-kosmoso-pasaulis-lt123c

## Vizualas

Hero generuotas integruotu image_gen įrankiu pagal tikrą LED lentos su markerių laikikliu nuotrauką. Tai reklaminė vizualizacija. Produktų kortelėms naudojamos oficialios autentiškos svetainės nuotraukos, sumažintos ir suspaustos. Hero promptas išsaugotas sources/hero-prompt.txt; originalas sources/hero-original.png; laiške assets/campaign/hero.jpg.

## Mobilioji struktūra

Produkto nuotrauka 92 px, pirmas stulpelis 108 px, pavadinimas šalia. Aprašas 16 px, 24 px eilutė, atskirai per visą kortelės plotį. Kaina ir CTA atskiroje eilutėje. Pagrindinei struktūrai nereikalingos media queries. Numatoma patikra 600, 390 ir 320 px, taip pat pašalinus style blokus.

## Patikra ir failai

Patikrinti 600, 390 ir 320 px pločiai su įprastais stiliais bei pašalinus visus style blokus – iš viso 6 variantai. Visuose įsikrauna 9 vaizdai, yra alt tekstai, nėra horizontalaus slinkimo ar pavadinimų išlindimo. 390 px lange produktų aprašai yra 314 px pločio ir 2 eilučių; 320 px lange – 244 px pločio ir 2–3 eilučių. Patikra yra naršyklės atvaizdavimo ir stilių pašalinimo modeliavimas, ne realus pristatymo Gmail ar Outlook klientams bandymas.

- newsletter.html: galutinis laiškas su absoliučiais HTTPS vaizdų ir šriftų adresais šioje GitHub saugykloje.
- preview.html: vietinė peržiūra su santykiniais assets keliais.
- newsletter.txt: teksto versija.
- subject-lines.md: 5 temos ir preheaderio variantai.
- preview-desktop.jpg: 600 × 4110 px pilnas laiškas.
- preview-mobile.jpg: 390 × 4270 px mobilioji versija.
- preview-mobile-320.jpg: 320 × 4400 px siauriausia patikrinta versija.
- preview-*-no-style.jpg: tie patys pločiai pašalinus style blokus.
- qa-results.json: patikros matavimai.
- build_campaign.py: atkuriami HTML ir teksto failai.

Saugyklos vieta: https://github.com/elaiskai/skilsas-email-assets/tree/codex/skilsas-creative-play-20260928/campaigns/2026-09-28/mazos-rankos-dideles-idejos

Aplanko data yra parengimo data, ne patvirtinta siuntimo data. Laiškas neįkeltas į Omnisend, nesuplanuotas ir neišsiųstas. Prieš siunčiant reikia patikrinti platformos prenumeratos nuorodų žymas ir atlikti bandomąjį pristatymą. 2026-09-28 patvirtintos kainos nėra pažadas, kad jos nesikeis vėliau.

GitHub publikuojami laiškui reikalingi suspausti assets, HTML, JPG peržiūros, šaltinių duomenys ir hero promptas. Dideli originalūs referenciniai vaizdai bei pradinis hero PNG išsaugoti vietiniame kampanijos sources aplanke.

Vaizdų adresai newsletter.html pririšti prie kampanijos failų commit 555185a195bfeafd7ec59875550651f667c7c3c4, todėl jie veikia ir kol kampanija dar neįjungta į main. Vieši įmonės rekvizitai pakartotinai patikrinti https://www.skilsas.lt/kontaktai ir ankstesniame tos pačios viešos saugyklos laiške.
