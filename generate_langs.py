#!/usr/bin/env python3
"""Regenerate /en/, /es/, /ru/, /zh/ index.html from root index.html."""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE, 'index.html'), 'r', encoding='utf-8') as f:
    root_html = f.read()

LANGS = {
    'en': {
        'html_lang': 'en',
        'title': 'Immigration Services Riviera Maya | Visa & Residency Experts',
        'description': 'Get Mexican residency in 2–4 weeks. Temporary & permanent visas, work permits, citizenship. Cancún, Playa del Carmen, Tulum. 2,500+ approved.',
        'keywords': 'immigration services Riviera Maya, Mexico visa consultant, temporary residency Mexico, permanent residency Mexico, work permit Mexico, Mexican citizenship naturalization, immigration lawyer Cancun, immigration Playa del Carmen, visa services Tulum, INM appointment Quintana Roo, digital nomad visa Mexico, investor visa Mexico, retirement visa Mexico, family reunification visa Mexico, expat relocation Mexico, residency card Mexico, Mexico immigration consultant 2026, how to get residency in Mexico, Mexico visa application process, best immigration lawyer Riviera Maya',
        'og_title': 'Immigration Services Riviera Maya — Visa & Residency Experts',
        'og_locale': 'en_US',
        'twitter_title': 'Immigration Services Riviera Maya — Get Residency in 2–4 Weeks',
        'faq': [
            ('How long does it take to get temporary residency in Mexico?', 'The process typically takes 2-4 weeks from document submission to card issuance, depending on the INM office workload in the Riviera Maya.'),
            ('Do I need to be in Mexico to start the immigration process?', 'For most visa types, you can start the process at a Mexican consulate in your home country. We coordinate everything remotely until you arrive.'),
            ('Can I work in Mexico with a temporary residency?', 'Temporary residency alone does not grant work permission. You need a specific work authorization added to your temporary resident card, which we can arrange.'),
            ('What documents do I need for Mexican residency?', 'Requirements vary by visa type but typically include a valid passport, proof of income or employment (bank statements showing ~$2,500 USD/month), photographs, and completed application forms.'),
            ('How much does it cost to get residency in Mexico?', 'Government fees for temporary residency are approximately $4,000-6,000 MXN. Our consulting services start from $500 USD. Contact us for a personalized quote.'),
            ('Can I get Mexican residency as a digital nomad?', 'Yes. Mexico offers temporary residency for remote workers who can prove sufficient income from abroad (~$2,500 USD/month). We handle the entire application.'),
            ('What is the difference between temporary and permanent residency?', 'Temporary residency is valid for 1-4 years and must be renewed. Permanent residency never expires. After 4 years of temporary, you can apply for permanent.'),
            ('How long does it take to get Mexican citizenship?', 'After 5 years of legal residency (2 years if married to a Mexican citizen), you can apply for naturalization. The process takes 6-12 months including the language exam.'),
            ('Can my family get residency with me?', 'Yes. Mexico offers family reunification visas. Your spouse and dependent children can obtain residency based on your immigration status.'),
            ('Do you offer services in languages other than Spanish?', 'Yes. MexVisa Pro provides full immigration consulting in English, Spanish, Russian, and Chinese. All consultants are multilingual.'),
        ],
    },
    'es': {
        'html_lang': 'es',
        'title': 'Servicios Migratorios Riviera Maya | Visa y Residencia',
        'description': 'Obtén tu residencia mexicana en 2–4 semanas. Visa temporal, permanente, permisos de trabajo, ciudadanía en Cancún, Playa del Carmen, Tulum. 2,500+ aprobados.',
        'keywords': 'servicios migratorios Riviera Maya, consultor migratorio México, residencia temporal México, residencia permanente México, permiso de trabajo México, ciudadanía mexicana naturalización, abogado migratorio Cancún, inmigración Playa del Carmen, servicios de visa Tulum, cita INM Quintana Roo, visa nómada digital México, visa inversionista México, visa jubilado México, visa reunificación familiar México, reubicación expatriados México, tarjeta de residencia México, trámite migratorio México 2026, cómo obtener residencia en México, proceso de solicitud de visa México, mejor abogado migratorio Riviera Maya',
        'og_title': 'Servicios Migratorios Riviera Maya — Expertos en Visa y Residencia',
        'og_locale': 'es_MX',
        'twitter_title': 'Servicios Migratorios Riviera Maya — Residencia en 2–4 Semanas',
        'faq': [
            ('¿Cuánto tarda obtener la residencia temporal en México?', 'El proceso toma de 2 a 4 semanas desde la presentación de documentos hasta la emisión de la tarjeta, dependiendo de la oficina del INM en Riviera Maya.'),
            ('¿Necesito estar en México para iniciar el trámite migratorio?', 'Para la mayoría de los tipos de visa, puede iniciar el proceso en un consulado mexicano en su país. Coordinamos todo a distancia hasta su llegada.'),
            ('¿Puedo trabajar en México con residencia temporal?', 'La residencia temporal por sí sola no otorga permiso de trabajo. Necesita una autorización específica añadida a su tarjeta de residente temporal, que nosotros gestionamos.'),
            ('¿Qué documentos necesito para la residencia mexicana?', 'Los requisitos varían según el tipo de visa: pasaporte vigente, comprobante de ingresos (~$2,500 USD/mes), fotografías y formularios. Nosotros preparamos todo.'),
            ('¿Cuánto cuesta obtener la residencia en México?', 'Los derechos gubernamentales para residencia temporal son aproximadamente $4,000-6,000 MXN. Nuestros servicios de consultoría desde $500 USD. Contáctenos para una cotización.'),
            ('¿Puedo obtener residencia como nómada digital?', 'Sí. México ofrece residencia temporal para trabajadores remotos con ingresos suficientes del extranjero (~$2,500 USD/mes). Manejamos toda la solicitud.'),
            ('¿Cuál es la diferencia entre residencia temporal y permanente?', 'La temporal es válida por 1-4 años y se renueva. La permanente no caduca. Después de 4 años de temporal, puede solicitar la permanente.'),
            ('¿Cuánto tarda obtener la ciudadanía mexicana?', 'Después de 5 años de residencia legal (2 si está casado con mexicano/a), puede solicitar naturalización. El proceso toma 6-12 meses incluyendo el examen.'),
            ('¿Mi familia puede obtener residencia conmigo?', 'Sí. México ofrece visas de reunificación familiar. Su cónyuge e hijos dependientes pueden obtener residencia basada en su estatus migratorio.'),
            ('¿Ofrecen servicios en otros idiomas además del español?', 'Sí. MexVisa Pro ofrece consultoría migratoria completa en español, inglés, ruso y chino. Todos nuestros consultores son multilingües.'),
        ],
    },
    'ru': {
        'html_lang': 'ru',
        'title': 'Иммиграция в Ривьеру-Майя | Виза и ВНЖ Мексика — MexVisa Pro',
        'description': 'Получите ВНЖ Мексики за 2–4 недели. Временное и постоянное резидентство, рабочая виза, гражданство в Канкуне, Плайя-дель-Кармен, Тулуме. 2500+ одобрений.',
        'keywords': 'иммиграционные услуги Ривьера-Майя, иммиграционный консультант Мексика, ВНЖ Мексика, ПМЖ Мексика, рабочая виза Мексика, гражданство Мексики натурализация, иммиграционный юрист Канкун, иммиграция Плайя-дель-Кармен, визовые услуги Тулум, запись INM Кинтана-Роо, виза цифрового кочевника Мексика, инвестиционная виза Мексика, пенсионная виза Мексика, виза воссоединение семьи Мексика, переезд в Мексику, резидентская карта Мексика, иммиграция Мексика 2026, как получить ВНЖ в Мексике, процесс подачи на визу Мексика, лучший иммиграционный юрист Ривьера-Майя',
        'og_title': 'Иммиграция в Ривьеру-Майя — Эксперты по визам и ВНЖ',
        'og_locale': 'ru_RU',
        'twitter_title': 'Иммиграция Ривьера-Майя — ВНЖ Мексики за 2–4 недели',
        'faq': [
            ('Сколько времени занимает получение ВНЖ в Мексике?', 'Процесс занимает 2-4 недели с момента подачи документов до выдачи карты, в зависимости от загруженности офиса INM в Ривьере-Майя.'),
            ('Нужно ли находиться в Мексике для начала иммиграционного процесса?', 'Для большинства типов виз можно начать процесс в мексиканском консульстве в вашей стране. Мы координируем всё удалённо до вашего приезда.'),
            ('Можно ли работать в Мексике с временным ВНЖ?', 'Временное резидентство само по себе не даёт права на работу. Необходимо разрешение на работу, которое мы можем оформить.'),
            ('Какие документы нужны для ВНЖ в Мексике?', 'Зависит от типа визы: действующий паспорт, подтверждение дохода (~$2500 в месяц), фотографии и заполненные анкеты. Мы подготовим весь пакет.'),
            ('Сколько стоит получение ВНЖ в Мексике?', 'Госпошлина за временное резидентство — примерно $4000-6000 MXN. Наши услуги от $500 USD. Свяжитесь для индивидуального расчёта.'),
            ('Можно ли получить ВНЖ как цифровой кочевник?', 'Да. Мексика предоставляет временное резидентство удалённым работникам с подтверждённым доходом из-за рубежа (~$2500/мес). Мы ведём весь процесс.'),
            ('В чём разница между временным и постоянным ВНЖ?', 'Временное — на 1-4 года с продлением. Постоянное — бессрочное. После 4 лет временного можно подать на постоянное.'),
            ('Сколько времени занимает получение гражданства Мексики?', 'После 5 лет легального проживания (2 года при браке с мексиканцем) можно подать на натурализацию. Процесс — 6-12 месяцев, включая языковой экзамен.'),
            ('Может ли семья получить ВНЖ вместе со мной?', 'Да. Мексика предлагает визы воссоединения семьи. Супруг/а и дети-иждивенцы могут получить резидентство на основании вашего статуса.'),
            ('Предоставляете ли услуги на русском языке?', 'Да. MexVisa Pro оказывает полное иммиграционное сопровождение на русском, английском, испанском и китайском языках.'),
        ],
    },
    'zh': {
        'html_lang': 'zh',
        'title': '里维埃拉玛雅移民服务 | 签证与居留 — MexVisa Pro',
        'description': '2-4周获得墨西哥居留权。临时和永久签证、工作许可、公民身份。坎昆、普拉亚德尔卡门、图卢姆。2500+成功案例。免费咨询。',
        'keywords': '里维埃拉玛雅移民服务, 墨西哥签证顾问, 墨西哥临时居留, 墨西哥永久居留, 墨西哥工作许可, 墨西哥公民身份归化, 坎昆移民律师, 普拉亚德尔卡门移民, 图卢姆签证服务, 金塔纳罗奥INM预约, 墨西哥数字游民签证, 墨西哥投资签证, 墨西哥退休签证, 墨西哥家庭团聚签证, 外籍人士搬迁墨西哥, 墨西哥居留卡, 墨西哥移民顾问2026, 如何获得墨西哥居留权, 墨西哥签证申请流程, 最佳里维埃拉玛雅移民律师',
        'og_title': '里维埃拉玛雅移民服务 — 签证与居留专家',
        'og_locale': 'zh_CN',
        'twitter_title': '里维埃拉玛雅移民服务 — 2-4周获得居留权',
        'faq': [
            ('在墨西哥获得临时居留需要多长时间？', '从提交文件到发卡，整个过程通常需要2至4周，具体取决于里维埃拉玛雅INM办公室的工作量。'),
            ('我需要在墨西哥才能开始移民流程吗？', '大多数签证类型可以在您所在国家的墨西哥领事馆开始办理。我们远程协调一切，直到您抵达。'),
            ('持有临时居留可以在墨西哥工作吗？', '仅凭临时居留不能获得工作许可。您需要添加专门的工作授权到临时居民卡上，我们可以为您办理。'),
            ('墨西哥居留需要什么文件？', '根据签证类型不同：有效护照、收入证明（约$2,500美元/月）、照片和填写完整的申请表。我们帮您准备全部材料。'),
            ('获得墨西哥居留权要多少钱？', '临时居留的政府费用约为$4,000-6,000墨西哥比索。我们的咨询服务从$500美元起。联系我们获取个性化报价。'),
            ('数字游民可以获得墨西哥居留权吗？', '可以。墨西哥为能证明海外收入（约$2,500美元/月）的远程工作者提供临时居留。我们处理整个申请流程。'),
            ('临时居留和永久居留有什么区别？', '临时居留有效期1-4年，需要续签。永久居留没有期限。临时居留满4年后可以申请永久居留。'),
            ('获得墨西哥公民身份需要多长时间？', '合法居住5年后（与墨西哥公民结婚则为2年），可以申请归化入籍。过程需要6-12个月，包括语言考试。'),
            ('我的家人可以和我一起获得居留权吗？', '可以。墨西哥提供家庭团聚签证。您的配偶和受抚养子女可以基于您的移民身份获得居留权。'),
            ('你们提供中文服务吗？', '是的。MexVisa Pro提供中文、英文、西班牙文和俄文的完整移民咨询服务。所有顾问都是多语种。'),
        ],
    },
}

DOMAIN = 'https://mexvisapro.com'

for lang, cfg in LANGS.items():
    html = root_html

    # Fix asset paths: assets/ → ../assets/
    html = html.replace('href="assets/', 'href="../assets/')
    html = html.replace('src="assets/', 'src="../assets/')
    html = html.replace('href="manifest.json"', 'href="../manifest.json"')

    # Set <html lang>
    html = re.sub(r'<html lang="[^"]*">', f'<html lang="{cfg["html_lang"]}">', html)

    # Replace <title>
    html = re.sub(r'<title>[^<]+</title>', f'<title>{cfg["title"]}</title>', html)

    # Replace meta description
    html = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{cfg["description"]}">',
        html
    )

    # Replace meta keywords
    html = re.sub(
        r'<meta name="keywords" content="[^"]*">',
        f'<meta name="keywords" content="{cfg["keywords"]}">',
        html
    )

    # Replace canonical
    html = html.replace(
        f'<link rel="canonical" href="{DOMAIN}/">',
        f'<link rel="canonical" href="{DOMAIN}/{lang}/">'
    )

    # Replace OG tags
    html = re.sub(
        r'<meta property="og:title" content="[^"]*">',
        f'<meta property="og:title" content="{cfg["og_title"]}">',
        html
    )
    html = re.sub(
        r'<meta property="og:url" content="[^"]*">',
        f'<meta property="og:url" content="{DOMAIN}/{lang}/">',
        html
    )
    html = re.sub(
        r'<meta property="og:locale" content="[^"]*">',
        f'<meta property="og:locale" content="{cfg["og_locale"]}">',
        html
    )

    # Replace Twitter title
    html = re.sub(
        r'<meta name="twitter:title" content="[^"]*">',
        f'<meta name="twitter:title" content="{cfg["twitter_title"]}">',
        html
    )

    # Replace Schema.org FAQPage
    faq_items = []
    for q, a in cfg['faq']:
        faq_items.append(f'{{"@type": "Question", "name": "{q}", "acceptedAnswer": {{"@type": "Answer", "text": "{a}"}}}}')
    faq_json = ',\n      '.join(faq_items)
    faq_block = f'''{{"@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {faq_json}
    ]
  }}'''
    html = re.sub(
        r'\{"@context": "https://schema\.org",\s*"@type": "FAQPage".*?\}(?=\s*</script>)',
        faq_block,
        html,
        flags=re.DOTALL
    )

    # Remove auto-redirect script (only root needs it)
    html = re.sub(
        r'\s*<!-- Auto-detect browser language.*?</script>',
        '',
        html,
        flags=re.DOTALL
    )

    # Add localStorage pre-set script before </head>
    lang_script = f'\n  <script>localStorage.setItem(\'lang\',\'{lang}\');localStorage.setItem(\'lang_redirect\',\'done\')</script>'
    html = html.replace('</head>', f'{lang_script}\n</head>')

    # Write
    out_dir = os.path.join(BASE, lang)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'index.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  ✓ {lang}/index.html ({len(html):,} bytes)')

print('Done — all 4 language pages regenerated.')
