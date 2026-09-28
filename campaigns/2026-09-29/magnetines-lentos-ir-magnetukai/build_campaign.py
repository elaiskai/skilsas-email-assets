from pathlib import Path
import html, json
ROOT=Path(__file__).resolve().parent
SOURCE=json.loads((ROOT/'sources/products-2026-09-28.json').read_text())
PRODUCTS=json.loads((ROOT/'campaign-copy.json').read_text())
FONT='Montserrat,Arial,sans-serif'
GREEN,MINT,INK='#188348','#E5FCEF','#104C3E'
UTM='?utm_source=omnisend&utm_medium=email&utm_campaign=skilsas_20260929_magnetines_lentos_ir_magnetukai'
PUBLIC='https://raw.githubusercontent.com/elaiskai/skilsas-email-assets/codex/skilsas-creative-play-20260928/campaigns/2026-09-29/magnetines-lentos-ir-magnetukai/'
CATEGORY='https://www.skilsas.lt/lavinamosios-priemones/magnetines-lentos-ir-magnetai-yes-for-skills'
SUBJECT='Mažas kampelis. Daug istorijų. 🧲'
PREHEADER='Magnetinės lentos, magnetukai ir 3 idėjos žaidimų kampeliui namuose.'

def esc(s): return html.escape(str(s), quote=True)
def url(key): return SOURCE[key]['offers']['url'] + UTM
def price(key):
    v = SOURCE[key]['offers']['price']
    return (str(int(v)) if v == int(v) else f'{v:.2f}'.replace('.', ',')) + ' €'
def table(body, extra=''):
    return f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" {extra}>{body}</table>'
def row(body, style='', extra=''):
    return f'<tr><td {extra} style="{style}">{body}</td></tr>\n'
def p(text, margin='0 0 16px', size=17, color=INK, cls=''):
    return f'<p class="{cls}" style="margin:{margin};font-family:{FONT};font-size:{size}px;line-height:{round(size*1.5)}px;color:{color};">{text}</p>'
def eyebrow(text):
    return f'<p style="margin:0 0 10px;font-family:{FONT};font-size:11px;line-height:17px;letter-spacing:1px;font-weight:700;color:{GREEN};">{text}</p>'
def heading(text):
    return f'<h2 style="margin:0 0 12px;font-family:{FONT};font-size:28px;line-height:35px;color:{INK};font-weight:700;">{text}</h2>'
def button(text, href, inverse=False):
    bg, fg = (MINT, INK) if inverse else (GREEN, '#FFFFFF')
    return table(row(f'<a href="{esc(href)}" style="display:inline-block;padding:14px 20px;border:1px solid {bg};border-radius:28px;font-family:{FONT};font-size:15px;line-height:22px;font-weight:700;text-decoration:none;color:{fg};">{text}&nbsp; →</a>', f'background-color:{bg};border-radius:28px;mso-padding-alt:14px 20px;', f'align="center" bgcolor="{bg}"'))
def section(label, title):
    return row(eyebrow(label)+heading(title), 'padding:20px 24px 20px;')
def card(product):
    key, label, title, desc = product
    a = esc(url(key))
    image = f'<a href="{a}"><img src="assets/products/{key}.jpg" width="92" height="92" alt="{esc(SOURCE[key]["name"])}" style="display:block;width:92px;max-width:100%;height:auto;border:0;border-radius:12px;"></a>'
    title_html = f'<p style="margin:0 0 6px;font-family:{FONT};font-size:10px;line-height:15px;letter-spacing:0.35px;font-weight:700;color:{GREEN};">{label}</p><h3 style="margin:0;font-family:{FONT};font-size:18px;line-height:24px;font-weight:700;color:{INK};">{title}</h3>'
    top = table(f'<tr><td width="108" valign="middle" style="width:108px;padding:0;">{image}</td><td valign="middle" style="padding:0;text-align:left;word-break:normal;">{title_html}</td></tr>', 'width="100%" style="width:100%;table-layout:fixed;"')
    desc_html = p(desc, '14px 0 16px',16,cls='product-description')
    cta = f'<a href="{a}" style="display:inline-block;padding:10px 14px;background-color:{GREEN};border:1px solid {GREEN};border-radius:22px;font-family:{FONT};font-size:14px;line-height:20px;font-weight:700;text-decoration:none;color:#FFFFFF;white-space:nowrap;">Apžiūrėti&nbsp;→</a>'
    bottom = table(f'<tr><td width="40%" valign="middle" style="padding:0;font-family:{FONT};font-size:23px;line-height:30px;font-weight:700;color:{INK};white-space:nowrap;">{price(key).replace(" ", "&nbsp;")}</td><td width="60%" align="right" valign="middle" style="padding:0;">{cta}</td></tr>', 'width="100%" style="width:100%;table-layout:fixed;"')
    return row(table(row(top+desc_html+bottom,'padding:20px;'),'class="product-card" width="100%" bgcolor="#FFFFFF" style="width:100%;background-color:#FFFFFF;border-radius:22px;table-layout:fixed;"'),'padding:0 18px 16px;')


INTRO = 'Žaidimų kampelis neturi užimti viso kambario. Vieta lentai ir keli mėgstami magnetukai – jau gera pradžia. Šįkart dalijuosi lentomis, magnetukais ir trimis paprastomis idėjomis, ką su jais nuveikti namuose.'
IDEAS = [
    ('Sugrupuokime', 'Sudėliokite magnetukus grupelėmis pagal spalvas ar pasirinktą temą.'),
    ('Sukurkime istoriją', 'Pasirinkite kelis magnetukus ir pakaitomis pridėkite po sakinį prie pasakojimo.'),
    ('Kas pasikeitė?', 'Vienam užsimerkus, pakeiskite magnetukų vietas – ar pavyks pastebėti skirtumą?'),
]
CLOSING = 'Pradėkite nuo kelių magnetukų, o naujas žaidimo taisykles sugalvokite kartu.'

parts=[]
parts.append(row(f'<a href="{esc("https://www.skilsas.lt/"+UTM)}"><img src="assets/brand/logo.png" width="112" height="65" alt="SKILSAS" style="display:block;width:112px;height:auto;border:0;"></a>','padding:24px 24px 20px;','align="center"'))
parts.append(row(eyebrow('ŽAIDIMŲ KAMPELIS NAMUOSE')+f'<h1 class="hero-title" style="margin:0 0 16px;font-family:{FONT};font-size:33px;line-height:40px;font-weight:700;letter-spacing:-1px;color:{INK};">Mažas kampelis.<br>Daug istorijų.</h1>'+p('Lenta, magnetukai ir vieta vaiko sumanymams.','0',18),'padding:4px 20px 24px;','align="center"'))
parts.append(row(f'<a href="{esc(url("arka"))}"><img src="assets/campaign/hero.jpg" width="564" height="564" alt="Žalsvai melsva magnetinė lenta „Arka“ su miško magnetukais jaukiame žaidimų kampelyje" style="display:block;width:100%;height:auto;border:1px solid #BCDCCB;border-radius:24px;box-sizing:border-box;"></a>','padding:0 18px;font-size:0;line-height:0;'))
parts.append(row(eyebrow('ŽALSVAI MELSVA · 95 × 76 CM')+heading('Magnetinė lenta „Arka“')+p('Priklijuojama lenta lengviems magnetukams ir kasdien naujoms istorijoms.','0 0 10px',16)+p('Magnetukai parduodami atskirai.','0 0 18px',13)+f'<p style="margin:0 0 18px;font-family:{FONT};font-size:30px;line-height:38px;font-weight:700;color:{INK};">{price("arka")}</p>'+button('Apžiūrėti lentą',url('arka')),'padding:24px 24px 32px;','align="center"'))
parts.append(row(p('<strong>Labas!</strong>')+p(INTRO,'0'),'padding:0 24px 20px;'))
parts.append(section('PIRMIAUSIA – LENTA','O gal namelis ant sienos?'))
parts.append(card(PRODUCTS[1]))
parts.append(row(p('Lentos ir magnetukų rinkiniai parduodami atskirai.','0',13),'padding:0 24px 14px;'))
parts.append(section('TOLIAU – JŪSŲ ISTORIJOS','Kuo ją pripildysime?'))
parts.extend(card(x) for x in PRODUCTS[2:5])
parts.append(section('DAR DAUGIAU BŪDŲ ŽAISTI','Dėlioti, derinti, atrasti.'))
parts.extend(card(x) for x in PRODUCTS[5:])
ideas=eyebrow('3 IDĖJOS ŽAIDIMŲ KAMPELIUI')+heading('Išbandykite kartu.')
for i,(title,desc) in enumerate(IDEAS,1):
    ideas+=p(f'<strong>{i}. {title}</strong>','0 0 5px',17)+p(desc,'0' if i==3 else '0 0 20px',16)
parts.append(row(table(row(ideas,'padding:22px;'),'width="100%" bgcolor="#D4EFDE" style="background-color:#D4EFDE;border-radius:20px;table-layout:fixed;"'),'padding:8px 18px 24px;'))
parts.append(row(p(CLOSING)+p('Su meile,<br><strong>Ingrida</strong>','0'),'padding:0 24px 30px;'))
parts.append(row(f'<h2 style="margin:0 0 22px;font-family:{FONT};font-size:28px;line-height:35px;font-weight:700;color:{MINT};">Kokią istoriją<br>kursite šiandien?</h2>'+button('Kurti savo kampelį',CATEGORY+UTM,True),f'padding:34px 22px;background-color:{INK};',f'align="center" bgcolor="{INK}"'))

footer=p(f'<a href="{esc("https://www.skilsas.lt/"+UTM)}" style="color:{MINT};text-decoration:none;">skilsas.lt</a>&nbsp; · &nbsp;<a href="https://www.facebook.com/skilsaslietuva" style="color:{MINT};text-decoration:none;">Facebook</a>&nbsp; · &nbsp;<a href="https://www.instagram.com/skilsas.lt/" style="color:{MINT};text-decoration:none;">Instagram</a>','0 0 16px',13,MINT)
footer+=p('MB SKILSAS<br>S. Stanevičiaus g. 61, LT-07114 Vilnius','0 0 12px',11,'#C6DCD3')+p('Šį laišką gavote, nes užsisakėte SKILSAS naujienas.','0 0 12px',11,'#C6DCD3')
footer+=p('<a href="https://www.skilsas.lt/privatumo-politika" style="color:#C6DCD3;">Privatumas</a>&nbsp; · &nbsp;<a href="[[preference_link]]" style="color:#C6DCD3;">Keisti nuostatas</a>&nbsp; · &nbsp;<a href="[[unsubscribe_link]]" style="color:#C6DCD3;">Atsisakyti naujienų</a>','0',11,'#C6DCD3')
parts.append(row(table(row(footer,'padding-top:22px;border-top:1px solid #477769;','align="center"'),'width="100%"'),f'padding:0 22px 30px;background-color:{INK};',f'align="center" bgcolor="{INK}"'))
content=table(''.join(parts),'class="wrap" width="600" bgcolor="#E5FCEF" style="width:100%;max-width:600px;table-layout:fixed;background-color:#E5FCEF;"')

doc='''<!doctype html>
<html lang="lt" xmlns:o="urn:schemas-microsoft-com:office:office">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="x-apple-disable-message-reformatting"><meta name="format-detection" content="telephone=no,address=no,email=no,date=no"><meta name="color-scheme" content="light"><title>Mažas kampelis. Daug istorijų.</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<style>
@font-face{font-family:Montserrat;font-weight:400;src:url('assets/brand/Montserrat-Regular.ttf') format('truetype');}
@font-face{font-family:Montserrat;font-weight:700;src:url('assets/brand/Montserrat-Bold.ttf') format('truetype');}
body{margin:0!important;padding:0!important;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;}
table{border-spacing:0;mso-table-lspace:0pt;mso-table-rspace:0pt;}
img{border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;}
a[x-apple-data-detectors]{color:inherit!important;text-decoration:none!important;}
@media screen and (min-width:481px){.hero-title{font-size:46px!important;line-height:52px!important;}}
</style>
<!--[if mso]><style>body,table,td,p,a,h1,h2,h3{font-family:Arial,sans-serif!important;}</style><![endif]-->
</head><body style="margin:0;padding:0;background-color:#EDF3ED;">
'''
doc+=f'<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">{PREHEADER}</div>'
doc+=table(row('<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->'+content+'<!--[if mso]></td></tr></table><![endif]-->','','align="center"'),'width="100%" bgcolor="#EDF3ED"')+'</body></html>\n'

(ROOT/'preview.html').write_text(doc)
(ROOT/'newsletter.html').write_text(doc.replace('src="assets/',f'src="{PUBLIC}assets/').replace("url('assets/",f"url('{PUBLIC}assets/"))
text=[f'TEMA: {SUBJECT}',f'PREHEADER: {PREHEADER}','','Mažas kampelis. Daug istorijų.','Lenta, magnetukai ir vieta vaiko sumanymams.','','Labas!',INTRO,'']
for key,label,title,desc in PRODUCTS:
    text.extend([f'{label} | {title} – {price(key)}',desc])
    if key in ('arka','naira'):text.append('Magnetukai parduodami atskirai.')
    text.extend([url(key),''])
text.extend(['3 IDĖJOS ŽAIDIMŲ KAMPELIUI',''])
for i,(title,desc) in enumerate(IDEAS,1):text.extend([f'{i}. {title}',desc,''])
text.extend([CLOSING,'','Su meile,','Ingrida','','Kurti savo kampelį:',CATEGORY+UTM,'','MB SKILSAS | S. Stanevičiaus g. 61, LT-07114 Vilnius','Šį laišką gavote, nes užsisakėte SKILSAS naujienas.','Privatumas: https://www.skilsas.lt/privatumo-politika','Keisti nuostatas: [[preference_link]]','Atsisakyti naujienų: [[unsubscribe_link]]'])
(ROOT/'newsletter.txt').write_text('\n'.join(text)+'\n')
print(json.dumps({'products':len(PRODUCTS),'html_bytes':len(doc.encode()),'subject':SUBJECT},ensure_ascii=False))
