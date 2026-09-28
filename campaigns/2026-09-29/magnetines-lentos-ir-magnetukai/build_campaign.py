from pathlib import Path
import html, json
ROOT=Path(__file__).resolve().parent
SOURCE=json.loads((ROOT/'sources/products-2026-09-28.json').read_text())
PRODUCTS=json.loads((ROOT/'campaign-copy.json').read_text())
FONT='Montserrat,Arial,sans-serif'
GREEN,MINT,INK='#188348','#E5FCEF','#104C3E'
UTM='?utm_source=omnisend&utm_medium=email&utm_campaign=skilsas_20260929_magnetines_lentos_ir_magnetukai'
PUBLIC='https://raw.githubusercontent.com/elaiskai/skilsas-email-assets/19a1500d2e2392f753aa012ba908d6ce61e46754/campaigns/2026-09-29/magnetines-lentos-ir-magnetukai/'
CATEGORY='https://www.skilsas.lt/lavinamosios-priemones/magnetines-lentos-ir-magnetai-yes-for-skills'
SUBJECT='Mažas kampelis. Daug istorijų. 🧲'
PREHEADER='Išsirinkite lentą, pridėkite magnetukų ir išbandykite naują žaidimą.'

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
def section(label, title, subtitle=''):
    return row(eyebrow(label)+heading(title)+(p(subtitle,'0',16) if subtitle else ''), 'padding:24px 24px 18px;')
def card(product):
    key, label, title, desc = product
    a = esc(url(key))
    image = f'<a href="{a}"><img src="assets/products/{key}.jpg" width="124" height="124" alt="{esc(SOURCE[key]["name"])}" style="display:block;width:124px;max-width:100%;height:auto;border:0;border-radius:12px;"></a>'
    title_html = eyebrow(label)+f'<h3 style="margin:0;font-family:{FONT};font-size:20px;line-height:26px;font-weight:700;color:{INK};">{title}</h3>'
    cta = f'<a href="{a}" style="display:inline-block;padding:10px 9px;background-color:{GREEN};border:1px solid {GREEN};border-radius:22px;font-family:{FONT};font-size:13px;line-height:20px;font-weight:700;text-decoration:none;color:#FFFFFF;white-space:nowrap;">Apžiūrėti&nbsp;→</a>'
    purchase = f'<p style="margin:0 0 14px;font-family:{FONT};font-size:26px;line-height:34px;font-weight:700;color:{INK};white-space:nowrap;">{price(key).replace(" ", "&nbsp;")}</p>'+cta
    visual = table(f'<tr><td width="132" valign="middle" style="width:132px;padding:0;">{image}</td><td valign="middle" align="right" style="padding:0;">{purchase}</td></tr>', 'width="100%" style="width:100%;table-layout:fixed;"')
    content = row(title_html,'padding:16px 16px 12px;vertical-align:top;', 'height="86" class="product-title-cell"')
    content += row(visual,'padding:0 16px;')
    content += row(p(desc,'0',16,cls='product-description'),'padding:14px 15px 18px;vertical-align:top;', 'height="72" class="product-desc-cell"')
    return table(content,'class="product-card" width="100%" bgcolor="#FFFFFF" style="width:100%;background-color:#FFFFFF;border:1px solid #C7E5D4;border-radius:20px;table-layout:fixed;"')

def grid(products):
    # Fluid columns wrap without media queries; Outlook gets a fixed two-column table.
    columns=[]
    for i,product in enumerate(products):
        if i % 2 == 0: columns.append('<!--[if mso]><table role="presentation" width="576" cellpadding="0" cellspacing="0" border="0"><tr><![endif]-->')
        columns.append('<!--[if mso]><td width="288" valign="top"><![endif]--><div class="product-column" style="display:inline-block;vertical-align:top;width:100%;max-width:288px;text-align:left;">'+table(row(card(product),'padding:0 6px 12px;'),'width="100%" style="width:100%;table-layout:fixed;"')+'</div><!--[if mso]></td><![endif]-->')
        if i % 2 == 1 or i == len(products)-1: columns.append('<!--[if mso]></tr></table><![endif]-->')
    return row(''.join(columns),'padding:0 12px;font-size:0;line-height:0;','align="center"')

def feature(label,title,body,bg='#D4EFDE',dark=False):
    color=MINT if dark else INK
    title_html=f'<h2 style="margin:0 0 12px;font-family:{FONT};font-size:27px;line-height:34px;color:{color};font-weight:700;">{title}</h2>'
    label_html=f'<p style="margin:0 0 10px;font-family:{FONT};font-size:11px;line-height:17px;letter-spacing:1px;font-weight:700;color:{color};">{label}</p>'
    return row(table(row(label_html+title_html+body,'padding:24px;'),'width="100%" bgcolor="'+bg+'" style="width:100%;background-color:'+bg+';border-radius:22px;table-layout:fixed;"'),'padding:14px 18px 16px;')


INTRO = 'Žaidimų kampelis gali prasidėti nuo mažo sienos lopinėlio. Parinkau dvi lentas ir šešis magnetukų rinkinius – išsirinkite savąjį derinį, o istorijas kurkite kartu.'
RECIPE = [('Lenta','Vieta mažoms istorijoms.'),('Magnetukai','Tema, kuri įdomi šiandien.'),('Fantazija','Žaidimo taisykles kuriate jūs.')]
CHALLENGE = 'Išsirinkite tris magnetukus. Sugalvokite istoriją, kurioje jie visi susitinka.'
PROMPT = '„Vieną dieną jie išsiruošė į kelionę…“'
ROTATION = 'Dalį magnetukų atidėkite į dėžutę. Kitą kartą juos sukeiskite ir pradėkite naują žaidimą.'
CLOSING = 'Pradėkite nuo kelių magnetukų, o naujas žaidimo taisykles sugalvokite kartu.'

parts=[]
parts.append(row(f'<a href="{esc("https://www.skilsas.lt/"+UTM)}"><img src="assets/brand/logo.png" width="112" height="65" alt="SKILSAS" style="display:block;width:112px;height:auto;border:0;"></a>','padding:24px 24px 20px;','align="center"'))
parts.append(row(eyebrow('ŽAIDIMŲ KAMPELIS NAMUOSE')+f'<h1 class="hero-title" style="margin:0 0 16px;font-family:{FONT};font-size:33px;line-height:40px;font-weight:700;letter-spacing:-1px;color:{INK};">Mažas kampelis.<br>Daug istorijų.</h1>'+p('Lenta, magnetukai ir vieta vaiko sumanymams.','0',18),'padding:4px 20px 24px;','align="center"'))
parts.append(row(f'<a href="{esc(url("arka"))}"><img src="assets/campaign/hero.jpg" width="564" height="564" alt="Žalsvai melsva magnetinė lenta „Arka“ su miško magnetukais jaukiame žaidimų kampelyje" style="display:block;width:100%;height:auto;border:1px solid #BCDCCB;border-radius:24px;box-sizing:border-box;"></a>','padding:0 18px;font-size:0;line-height:0;'))
parts.append(row(p('Kampelio idėja: lenta „Arka“ ir magnetukai „Miškas“.','0 0 4px',12)+p('Lenta ir magnetukai parduodami atskirai.','0',12),'padding:12px 24px 4px;','align="center"'))
parts.append(row(p('<strong>Labas!</strong>','0 0 10px')+p(INTRO,'0'),'padding:24px 24px 4px;'))
parts.append(section('01 / LENTA','Išsirinkite pagrindą.','Dvi formos jūsų kampeliui: arka arba namelis.'))
parts.append(grid(PRODUCTS[:2]))
parts.append(row(p('Magnetukai į lentų kainą neįskaičiuoti.','0',13),'padding:0 24px 4px;'))
recipe=''
for i,(title,desc) in enumerate(RECIPE,1):
    recipe+=f'<tr><td width="36" valign="top" style="padding:0 0 14px;font-family:{FONT};font-size:26px;line-height:32px;font-weight:700;color:{GREEN};">{i:02d}</td><td style="padding:0 0 14px 10px;">'+p(f'<strong>{title}</strong>','0',17)+p(desc,'0',15)+'</td></tr>'
parts.append(feature('KAMPELIO RECEPTAS','Užtenka trijų dalykų.',table(recipe,'width="100%" style="table-layout:fixed;"')))
parts.append(section('02 / MAGNETUKAI','Pridėkite savo istoriją.','Gyvūnų nuotykiai ar drabužių deriniai?'))
parts.append(grid(PRODUCTS[2:6]))
parts.append(feature('PABANDYKITE KARTU','3 magnetukų iššūkis',p(CHALLENGE,'0 0 18px',16,MINT)+table(row(p(PROMPT,'0',18,MINT),'padding:0 0 0 16px;border-left:3px solid #94DAB1;'),'width="100%"'),bg=INK,dark=True))
parts.append(section('DAR DU PASIRINKIMAI','Dėlioti ir atrasti.','Kūno dalys, spalvos ir nauji deriniai.'))
parts.append(grid(PRODUCTS[6:]))
parts.append(feature('MAŽA IDĖJA RYTOJUI','Ta pati lenta.<br>Naujas žaidimas.',p(ROTATION,'0',16),bg='#FFF2DB'))
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
@media screen and (max-width:599px){.product-column{max-width:100%!important;}.product-title-cell,.product-desc-cell{height:auto!important;}}
</style>
<!--[if mso]><style>body,table,td,p,a,h1,h2,h3{font-family:Arial,sans-serif!important;}</style><![endif]-->
</head><body style="margin:0;padding:0;background-color:#EDF3ED;">
'''
doc+=f'<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">{PREHEADER}</div>'
doc+=table(row('<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->'+content+'<!--[if mso]></td></tr></table><![endif]-->','','align="center"'),'width="100%" bgcolor="#EDF3ED"')+'</body></html>\n'

(ROOT/'preview.html').write_text(doc)
(ROOT/'newsletter.html').write_text(doc.replace('src="assets/',f'src="{PUBLIC}assets/').replace("url('assets/",f"url('{PUBLIC}assets/"))
text=[f'TEMA: {SUBJECT}',f'PREHEADER: {PREHEADER}','','Mažas kampelis. Daug istorijų.','Lenta, magnetukai ir vieta vaiko sumanymams.','','Labas!',INTRO,'']
for i,(key,label,title,desc) in enumerate(PRODUCTS):
    if i==0:text.extend(['01 / LENTA – Išsirinkite pagrindą.','Dvi formos jūsų kampeliui: arka arba namelis.',''])
    if i==2:
        text.extend(['KAMPELIO RECEPTAS – Užtenka trijų dalykų.'])
        for name,line in RECIPE:text.append(f'{name}: {line}')
        text.extend(['','02 / MAGNETUKAI – Pridėkite savo istoriją.','Gyvūnų nuotykiai ar drabužių deriniai?',''])
    if i==6:text.extend(['PABANDYKITE KARTU – 3 magnetukų iššūkis',CHALLENGE,PROMPT,'','DAR DU PASIRINKIMAI – Dėlioti ir atrasti.','Kūno dalys, spalvos ir nauji deriniai.',''])
    text.extend([f'{label} | {title} – {price(key)}',desc])
    if key in ('arka','naira'):text.append('Magnetukai parduodami atskirai.')
    text.extend([url(key),''])
text.extend(['MAŽA IDĖJA RYTOJUI – Ta pati lenta. Naujas žaidimas.',ROTATION,''])
text.extend([CLOSING,'','Su meile,','Ingrida','','Kurti savo kampelį:',CATEGORY+UTM,'','MB SKILSAS | S. Stanevičiaus g. 61, LT-07114 Vilnius','Šį laišką gavote, nes užsisakėte SKILSAS naujienas.','Privatumas: https://www.skilsas.lt/privatumo-politika','Keisti nuostatas: [[preference_link]]','Atsisakyti naujienų: [[unsubscribe_link]]'])
(ROOT/'newsletter.txt').write_text('\n'.join(text)+'\n')
print(json.dumps({'products':len(PRODUCTS),'html_bytes':len(doc.encode()),'subject':SUBJECT},ensure_ascii=False))
