# SKILSAS: visi 16 automatizacijų laiškų

Ši versija pakeičia ankstesnius automatizacijų HTML. Tai vietiniai failai, į Omnisend dar neįkelti.

Atidaryk index.html. Prie kiekvieno laiško yra peržiūra ir „Kopijuoti HTML“. TXT failuose tas pats pilnas kodas, jei naršyklė HTML failą rodo kaip laišką.

Welcome W1–W5 ir Winback WB1–WB3: visas HTML šablonas.
Cart AC1–AC3, Checkout CH1–CH2, Abandoned Product AP1–AP2 ir Review PR1: top.html į HTML bloką prieš Omnisend dinaminį prekių bloką, bottom.html į HTML bloką po juo. Preview failai nėra skirti importui.

HTML bloko išorinius tarpus Omnisend nustatyk į 0. Šablono plotis 600 px. Nenaudok seno papildomo styles.css. Naujos versijos bazinis persirikiavimas įrašytas tiesiai elementuose; jei klientas nepalaiko skaičiuojamo pločio, atsarginis išdėstymas yra vienas stulpelis.

Išsaugok Omnisend atsisakymo ir paskyros laukus. Patikrink srauto grįžimo nuorodą su tikru bandomuoju įvykiu. Dinaminio bloko mobilų išdėstymą nustato Omnisend, jis nėra šio HTML dalis.

Patikrintos 600, 320, 390 ir 430 px versijos su head stiliais ir be jų, iš viso 128 švieži atvaizdavimai. Vizualiai peržiūrėti visi laiškai, patikros rezultatai su HTML SHA256 yra QA.json. Tai Chromium peržiūros, ne patvirtintas Gmail, Outlook ar Omnisend pristatymas. Prieš siuntimą reikalingas naujas Omnisend testas telefone ir kompiuteryje, įskaitant tikrą dinaminį bloką. Jokie srautai neįjungti.
