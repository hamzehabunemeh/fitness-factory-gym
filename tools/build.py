#!/usr/bin/env python3
"""
FITNESS FACTORY website generator.

All site content lives in this file (branch info, prices, trainers, services,
classes). Edit the data below, then run:

    python3 tools/build.py

and every HTML page is regenerated in the repository root.
Items marked SAMPLE are placeholder data waiting for the real details.
"""
import json, os, html as H

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_URL = "https://hamzehabunemeh.github.io/fitness-factory-gym/"

FACEBOOK = "https://www.facebook.com/share/19qZiuS7ze/"

# ---------------------------------------------------------------- helpers
def t(en, ar):
    """Bilingual inline text."""
    return f'<span class="l-en">{en}</span><span class="l-ar">{ar}</span>'

def esc(s):
    return H.escape(s, quote=True)

ICONS = {
 "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
 "pin": '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
 "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "x": '<path d="M18 6 6 18M6 6l12 12"/>',
 "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
 "dumbbell": '<path d="M6.5 6.5v11M17.5 6.5v11M3 9v6M21 9v6M6.5 12h11"/>',
 "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
 "user": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
 "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
 "card": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>',
 "image": '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/>',
 "heart": '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.6 1-1.1a5.5 5.5 0 0 0 0-7.7z"/>',
 "bolt": '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
 "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
 "flame": '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.4-.5-2-1-3-1.1-2.1-.2-4 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.2.4-2.3 1-3.3.3 1.8 1.4 2.8 2.5 2.8z"/>',
 "scale": '<path d="M12 3v18M5 7h14M5 7l-3 7a4 4 0 0 0 6 0L5 7zM19 7l-3 7a4 4 0 0 0 6 0l-3-7z"/>',
 "glove": '<path d="M7 11V6a3 3 0 0 1 3-3h4a4 4 0 0 1 4 4v6a6 6 0 0 1-6 6H9a2 2 0 0 1-2-2v-6z"/><path d="M7 11h6M7 21h8"/>',
 "apple": '<path d="M12 7c-2-2-6-1.5-6 3.5S9 21 12 19c3 2 6-3.5 6-8.5S14 5 12 7z"/><path d="M12 7c0-2 1-4 3-4"/>',
 "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
 "trophy": '<path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6M18 9h1.5a2.5 2.5 0 0 0 0-5H18M4 22h16M10 14.7V17c0 .6-.5 1-1 1.2C7.8 18.8 7 20.2 7 22M14 14.7V17c0 .6.5 1 1 1.2 1.2.6 2 2 2 3.8M18 2H6v7a6 6 0 0 0 12 0V2z"/>',
 "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/>',
}
FILLED = {
 "whatsapp": '<path fill="currentColor" d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zm8.4-18.2A11.8 11.8 0 0 0 1.7 17.8L0 24l6.3-1.7a11.8 11.8 0 0 0 5.7 1.4A11.8 11.8 0 0 0 20.4 3.6z"/>',
 "facebook": '<path fill="currentColor" d="M24 12a12 12 0 1 0-13.9 11.9v-8.4H7.1V12h3V9.4c0-3 1.8-4.7 4.5-4.7 1.3 0 2.7.2 2.7.2v3h-1.5c-1.5 0-2 .9-2 1.9V12h3.4l-.5 3.5h-2.9v8.4A12 12 0 0 0 24 12z"/>',
}
def icon(name):
    if name in FILLED:
        return f'<svg viewBox="0 0 24 24" aria-hidden="true">{FILLED[name]}</svg>'
    if name == "instagram":
        return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">'
                '<rect x="2" y="2" width="20" height="20" rx="5.5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.6" cy="6.4" r="1" fill="currentColor"/></svg>')
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')

# ---------------------------------------------------------------- data
DAYS = [  # Jordan week order: Saturday first. (js_index, en, ar)
    (6, "Saturday", "السبت"), (0, "Sunday", "الأحد"), (1, "Monday", "الاثنين"),
    (2, "Tuesday", "الثلاثاء"), (3, "Wednesday", "الأربعاء"), (4, "Thursday", "الخميس"),
    (5, "Friday", "الجمعة"),
]
FULL = ("6:00 AM – 12:30 AM", "6:00 صباحاً – 12:30 بعد منتصف الليل")

BRANCHES = {
 "khalda": dict(
    slug="khalda", platinum=True,
    name=("Khalda Branch", "فرع خلدا"),
    short=("Khalda", "خلدا"),
    title=("Fitness Factory Platinum", "فيتنس فاكتوري بلاتينيوم"),
    tagline=("The premium Fitness Factory experience — elevated spaces, a dedicated combat zone and professional coaching in the heart of Khalda.",
             "تجربة فيتنس فاكتوري المميّزة — مساحات راقية، ومنطقة مخصّصة للفنون القتالية، وتدريب احترافي في قلب خلدا."),
    phone_display="07 9001 5690", phone_intl="+962790015690", wa="962790015690",
    maps="https://maps.app.goo.gl/WFHZ137YwgKfXsUcA",
    instagram="https://www.instagram.com/fitnessfactorykhalda", ig_handle="@fitnessfactorykhalda",
    hero="khalda-hero.jpg", photos=[("khalda-hero.jpg", ("Main training floor", "صالة التدريب الرئيسية")),
                                    ("khalda-cage.jpg", ("Combat & functional zone", "منطقة الفنون القتالية والتدريب الوظيفي")),
                                    ("khalda-reception.jpg", ("Reception & InBody station", "الاستقبال وجهاز InBody"))],
    # js day index 0=Sun..6=Sat -> [open, close] minutes; close > 1440 means after midnight
    hours_js=[[360,1470],[360,1470],[360,1470],[360,1470],[360,1320],[960,1260],[360,1470]],
    hours_rows={6:FULL,0:FULL,1:FULL,2:FULL,3:FULL,
                4:("6:00 AM – 10:00 PM","6:00 صباحاً – 10:00 مساءً"),
                5:("4:00 PM – 9:00 PM","4:00 عصراً – 9:00 مساءً")},
    hours_summary=[("Sat – Wed","السبت – الأربعاء",FULL),
                   ("Thursday","الخميس",("6:00 AM – 10:00 PM","6:00 ص – 10:00 م")),
                   ("Friday","الجمعة",("4:00 PM – 9:00 PM","4:00 م – 9:00 م"))],
    intro=[("Fitness Factory Platinum is our flagship branch in Khalda — built for members who want more from every session. Dark, focused interiors, premium equipment and a dedicated combat cage create an atmosphere designed for serious training.",
            "فيتنس فاكتوري بلاتينيوم هو فرعنا الرئيسي في خلدا — صُمّم لمن يريد أكثر من كل تمرين. تصميم داخلي مركّز، وأجهزة مميّزة، وقفص مخصّص للفنون القتالية يصنعون أجواءً مثالية للتدريب الجاد."),
           ("From strength and conditioning to boxing, MMA and body composition tracking, everything you need to build a stronger version of yourself is under one roof.",
            "من تدريب القوة واللياقة إلى الملاكمة والفنون القتالية وقياس مكوّنات الجسم، كل ما تحتاجه لتبني نسخة أقوى من نفسك تحت سقف واحد.")],
    highlights=[("Premium strength & cardio equipment","أجهزة قوة وكارديو مميّزة"),
                ("Dedicated combat & functional cage","قفص مخصّص للفنون القتالية والتدريب الوظيفي"),
                ("InBody body composition analysis","تحليل مكوّنات الجسم بجهاز InBody"),
                ("Certified professional coaches","مدربون محترفون معتمدون")],
    # SAMPLE: placeholder prices (JOD)
    plans=[("1 Month","شهر واحد",45,("per month","للشهر"),False),
           ("3 Months","3 أشهر",120,("40 JD / month","40 د.أ / شهرياً"),False),
           ("6 Months","6 أشهر",210,("35 JD / month","35 د.أ / شهرياً"),True),
           ("12 Months","12 شهراً",380,("≈ 31.7 JD / month","≈ 31.7 د.أ / شهرياً"),False)],
    plan_features=[("Full access to the Platinum floor","دخول كامل لصالة بلاتينيوم"),
                   ("Combat & functional zone","منطقة الفنون القتالية والتدريب الوظيفي"),
                   ("Free InBody assessment","قياس InBody مجاني"),
                   ("Lockers & changing rooms","خزائن وغرف تبديل")],
    extras=[("Day Pass","تذكرة يوم واحد","7 JD","7 د.أ"),
            ("Personal Training – 12 sessions","تدريب شخصي – 12 جلسة","240 JD","240 د.أ"),
            ("Boxing / MMA – monthly add-on","ملاكمة / فنون قتالية – إضافة شهرية","35 JD","35 د.أ"),
            ("InBody assessment (non-members)","قياس InBody (لغير المشتركين)","5 JD","5 د.أ"),
            ("Nutrition plan","برنامج تغذية","30 JD","30 د.أ")],
    trainers=[("Khaled Mansour","خالد منصور",("Head Coach · Strength & Powerlifting","المدرب الرئيسي · القوة ورفع الأثقال"),12,["Powerlifting","Strength"]),
              ("Sara Haddadin","سارة حدادين",("Women's Fitness & Body Recomposition","لياقة السيدات وإعادة تشكيل الجسم"),8,["Fat loss","Toning"]),
              ("Yousef Al-Masri","يوسف المصري",("Boxing & MMA Coach","مدرب ملاكمة وفنون قتالية"),10,["Boxing","MMA"]),
              ("Laith Obeidat","ليث عبيدات",("Functional & Athletic Performance","التدريب الوظيفي والأداء الرياضي"),7,["Functional","Mobility"]),
              ("Dana Qasem","دانا قاسم",("Nutrition & InBody Specialist","أخصائية تغذية وقياس InBody"),6,["Nutrition","InBody"]),
              ("Hamza Tamimi","حمزة التميمي",("Bodybuilding & Hypertrophy","كمال الأجسام وبناء العضلات"),9,["Bodybuilding","Prep"])],
    services=[("dumbbell","Strength & Free Weights","القوة والأوزان الحرة","Premium racks, plate-loaded machines and a full dumbbell range.","رفوف مميّزة، وأجهزة بأوزان حرة، ومجموعة كاملة من الدمبلز."),
              ("glove","Combat Zone","منطقة الفنون القتالية","A dedicated cage with red mat flooring for boxing, kickboxing and MMA.","قفص مخصّص بأرضية حمراء للملاكمة والكيك بوكسينغ والفنون القتالية المختلطة."),
              ("bolt","Functional Training","التدريب الوظيفي","Open space for conditioning, mobility and athletic performance work.","مساحة مفتوحة لتمارين اللياقة والمرونة والأداء الرياضي."),
              ("heart","Cardio Zone","منطقة الكارديو","Treadmills, bikes and ellipticals for endurance and fat loss.","أجهزة جري ودراجات وإليبتيكال لتحسين التحمّل وحرق الدهون."),
              ("user","Personal Training","التدريب الشخصي","One-to-one programmes with certified coaches built around your goals.","برامج فردية مع مدربين معتمدين مبنية حول أهدافك."),
              ("scale","InBody Analysis","تحليل InBody","Track muscle, fat and water with professional body composition scans.","تابع العضلات والدهون ونسبة الماء بقياسات احترافية لمكوّنات الجسم."),
              ("apple","Nutrition Guidance","الإرشاد الغذائي","Practical meal plans to support training, cutting or bulking.","خطط غذائية عملية تدعم التدريب أو التنشيف أو زيادة الكتلة."),
              ("star","Premium Reception","استقبال مميّز","A welcoming lounge and front desk ready to help every member.","استقبال وصالة انتظار مريحة لخدمة كل مشترك.")],
    classes={6:[("7:00 AM","Morning HIIT","هيت صباحي","Laith"),("6:00 PM","Boxing Fundamentals","أساسيات الملاكمة","Yousef"),("8:00 PM","Strength Circuit","دائرة القوة","Khaled")],
             0:[("7:00 AM","Mobility & Core","مرونة وتمارين البطن","Laith"),("7:00 PM","MMA Basics","أساسيات الفنون القتالية","Yousef")],
             1:[("7:00 AM","Morning HIIT","هيت صباحي","Laith"),("5:00 PM","Ladies Toning","تنحيف وشد للسيدات","Sara"),("8:00 PM","Kickboxing","كيك بوكسينغ","Yousef")],
             2:[("6:00 PM","Functional Conditioning","لياقة وظيفية","Laith"),("8:00 PM","Powerlifting Clinic","ورشة رفع الأثقال","Khaled")],
             3:[("7:00 AM","Mobility & Core","مرونة وتمارين البطن","Laith"),("5:00 PM","Ladies Toning","تنحيف وشد للسيدات","Sara"),("7:00 PM","Boxing Sparring","تدريب نزالات ملاكمة","Yousef")],
             4:[("6:00 PM","Strength Circuit","دائرة القوة","Hamza")],
             5:[("6:00 PM","Open Mat","تدريب حر على البساط","Yousef")]},
 ),
 "dahyet-alrasheed": dict(
    slug="dahyet-alrasheed", platinum=False,
    name=("Dahyet Al Rasheed Branch", "فرع ضاحية الرشيد"),
    short=("Dahyet Al Rasheed", "ضاحية الرشيد"),
    title=("Fitness Factory", "فيتنس فاكتوري"),
    tagline=("Your neighbourhood strength gym — fully equipped, open early till late every day, with coaches ready to push you further.",
             "نادي القوة في منطقتك — مجهّز بالكامل، ويفتح من الصباح الباكر حتى ما بعد منتصف الليل كل يوم، مع مدربين جاهزين لدفعك للأمام."),
    phone_display="07 9566 9931", phone_intl="+962795669931", wa="962795669931",
    maps="https://maps.app.goo.gl/wNn2uRRDCoDbDNJo6",
    instagram="https://www.instagram.com/fitness.factory.jo", ig_handle="@fitness.factory.jo",
    hero="dahyet-hero.jpg", photos=[("dahyet-hero.jpg", ("Machine & cardio floor", "صالة الأجهزة والكارديو")),
                                    ("dahyet-2.jpg", ("Free weights area", "منطقة الأوزان الحرة")),
                                    ("dahyet-1.jpg", ("Strength racks", "رفوف القوة"))],
    hours_js=[[360,1470]]*7,
    hours_rows={d[0]:FULL for d in DAYS},
    hours_summary=[("Every day","يومياً",FULL)],
    intro=[("Our Dahyet Al Rasheed branch is where Fitness Factory started building strength in the community. A complete gym floor with selectorised machines, free weights, power racks and cardio — open from 6 AM until after midnight, seven days a week.",
            "فرع ضاحية الرشيد هو المكان الذي بدأت منه فيتنس فاكتوري بناء القوة في المجتمع. صالة متكاملة فيها أجهزة مقاومة وأوزان حرة ورفوف قوة وكارديو — مفتوحة من 6 صباحاً حتى ما بعد منتصف الليل، طوال أيام الأسبوع."),
           ("Whether you're starting out or chasing a new personal best, our coaches and community will keep you consistent.",
            "سواء كنت مبتدئاً أو تسعى لتحقيق رقم شخصي جديد، مدربونا ومجتمعنا سيساعدونك على الاستمرار.")],
    highlights=[("Open every day, 6:00 AM – 12:30 AM","مفتوح يومياً من 6:00 صباحاً حتى 12:30 بعد منتصف الليل"),
                ("Full machine circuit & free weights","دائرة أجهزة كاملة وأوزان حرة"),
                ("Power racks & Smith machines","رفوف قوة وأجهزة سميث"),
                ("Friendly coaches & great value","مدربون ودودون وأسعار مناسبة")],
    plans=[("1 Month","شهر واحد",30,("per month","للشهر"),False),
           ("3 Months","3 أشهر",80,("≈ 26.7 JD / month","≈ 26.7 د.أ / شهرياً"),False),
           ("6 Months","6 أشهر",145,("≈ 24.2 JD / month","≈ 24.2 د.أ / شهرياً"),True),
           ("12 Months","12 شهراً",260,("≈ 21.7 JD / month","≈ 21.7 د.أ / شهرياً"),False)],
    plan_features=[("Full gym floor access","دخول كامل للصالة"),
                   ("Cardio & machine circuit","الكارديو ودائرة الأجهزة"),
                   ("Free introductory program","برنامج تمارين تعريفي مجاني"),
                   ("Lockers & changing rooms","خزائن وغرف تبديل")],
    extras=[("Day Pass","تذكرة يوم واحد","4 JD","4 د.أ"),
            ("Personal Training – 12 sessions","تدريب شخصي – 12 جلسة","150 JD","150 د.أ"),
            ("Student offer – 1 month","عرض الطلاب – شهر واحد","25 JD","25 د.أ"),
            ("Nutrition plan","برنامج تغذية","20 JD","20 د.أ")],
    trainers=[("Omar Haddad","عمر حداد",("Head Coach · Strength & Conditioning","المدرب الرئيسي · القوة واللياقة"),10,["Strength","Conditioning"]),
              ("Rami Nasser","رامي ناصر",("Bodybuilding & Hypertrophy","كمال الأجسام وبناء العضلات"),8,["Bodybuilding","Programs"]),
              ("Lina Khoury","لينا خوري",("Women's Fitness & Weight Loss","لياقة السيدات وإنقاص الوزن"),6,["Weight loss","Toning"]),
              ("Yazan Saleh","يزن صالح",("Circuit & HIIT Coach","مدرب الدوائر والهيت"),5,["HIIT","Cardio"])],
    services=[("dumbbell","Strength & Free Weights","القوة والأوزان الحرة","Power racks, Smith machines, benches and a full barbell & dumbbell range.","رفوف قوة وأجهزة سميث ومقاعد ومجموعة كاملة من البارات والدمبلز."),
              ("target","Machine Circuit","دائرة الأجهزة","Selectorised machines covering every muscle group — ideal for beginners.","أجهزة مقاومة تغطي كل مجموعات العضلات — مثالية للمبتدئين."),
              ("heart","Cardio Zone","منطقة الكارديو","Treadmills, bikes and ellipticals for endurance and fat loss.","أجهزة جري ودراجات وإليبتيكال لتحسين التحمّل وحرق الدهون."),
              ("user","Personal Training","التدريب الشخصي","One-to-one coaching with a programme built around your goals.","تدريب فردي ببرنامج مبني حول أهدافك."),
              ("users","Group Classes","الحصص الجماعية","HIIT, circuits and core classes through the week.","حصص هيت ودوائر وتمارين بطن على مدار الأسبوع."),
              ("apple","Nutrition Guidance","الإرشاد الغذائي","Simple, practical meal plans to match your training.","خطط غذائية بسيطة وعملية تناسب تدريبك.")],
    classes={6:[("7:00 PM","Full-Body Circuit","دائرة الجسم الكامل","Yazan")],
             0:[("6:30 PM","HIIT Burn","هيت لحرق الدهون","Yazan"),("8:30 PM","Strength Basics","أساسيات القوة","Omar")],
             1:[("5:00 PM","Ladies Cardio & Core","كارديو وبطن للسيدات","Lina")],
             2:[("7:00 PM","Full-Body Circuit","دائرة الجسم الكامل","Yazan"),("8:30 PM","Bodybuilding Clinic","ورشة كمال الأجسام","Rami")],
             3:[("5:00 PM","Ladies Cardio & Core","كارديو وبطن للسيدات","Lina")],
             4:[("6:30 PM","HIIT Burn","هيت لحرق الدهون","Yazan")],
             5:[]},
 ),
}
BRANCH_ORDER = ["khalda", "dahyet-alrasheed"]

SUBPAGES = [  # file, en, ar, icon, description en, description ar
    ("index.html", "Overview", "نظرة عامة", "info", "", ""),
    ("memberships.html", "Memberships", "الاشتراكات", "card", "Plans, prices and add-ons.", "الباقات والأسعار والإضافات."),
    ("trainers.html", "Trainers", "المدربون", "users", "Meet the coaching team.", "تعرّف على فريق المدربين."),
    ("hours.html", "Opening Hours", "أوقات الدوام", "clock", "Weekly opening times.", "مواعيد الدوام الأسبوعية."),
    ("services.html", "Services", "الخدمات", "dumbbell", "Facilities and services.", "المرافق والخدمات."),
    ("classes.html", "Class Schedule", "جدول الحصص", "calendar", "Weekly group classes.", "الحصص الجماعية الأسبوعية."),
    ("gallery.html", "Gallery", "معرض الصور", "image", "Take a look inside.", "ألقِ نظرة من الداخل."),
]

# ---------------------------------------------------------------- layout
def head(depth, title_en, title_ar, desc, og_image="khalda-hero.jpg"):
    p = "../" * depth
    return f'''<!DOCTYPE html>
<html lang="en" dir="ltr" data-title-en="{esc(title_en)}" data-title-ar="{esc(title_ar)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title_en)}</title>
<script>(function(){{var l='en';try{{l=localStorage.getItem('ff-lang')||'en'}}catch(e){{}}var q=new URLSearchParams(location.search).get('lang');if(q==='ar'||q==='en')l=q;var h=document.documentElement;h.lang=l;h.dir=l==='ar'?'rtl':'ltr';}})();</script>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#09090a">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title_en)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{SITE_URL}assets/img/{og_image}">
<link rel="icon" type="image/png" href="{p}assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<meta name="color-scheme" content="dark">
<style>html,body{{background:#09090a;color:#e9e9ec}}a,a:visited{{color:inherit;text-decoration:none}}</style>
<link rel="stylesheet" href="{p}assets/css/style.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Inter:wght@400;500;600;700&family=Oswald:wght@400;500;600;700&display=swap" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Inter:wght@400;500;600;700&family=Oswald:wght@400;500;600;700&display=swap"></noscript>
</head>
'''

MAIN_NAV = [
    ("home", "index.html", "Home", "الرئيسية"),
    ("khalda", "khalda/index.html", "Khalda Branch", "فرع خلدا"),
    ("dahyet-alrasheed", "dahyet-alrasheed/index.html", "Dahyet Al Rasheed Branch", "فرع ضاحية الرشيد"),
    ("about", "about.html", "About Us", "من نحن"),
    ("contact", "contact.html", "Contact Us", "تواصل معنا"),
]

def header(depth, active):
    p = "../" * depth
    items = "".join(
        f'<li><a href="{p}{href}"{" aria-current=\"page\"" if key == active else ""}>{t(en, ar)}</a></li>'
        for key, href, en, ar in MAIN_NAV)
    return f'''<header class="site-header">
 <div class="wrap">
  <a class="brand" href="{p}index.html" aria-label="Fitness Factory home">
   <img src="{p}assets/img/logo-icon.webp" alt="" width="44" height="44">
   <span class="brand-name metal">FITNESS FACTORY<small>AMMAN · JORDAN</small></span>
  </a>
  <nav class="main-nav" aria-label="Main"><ul>{items}</ul></nav>
  <div class="header-tools">
   <button class="lang-btn" type="button" data-lang-toggle aria-label="Switch language">{icon("globe")}<span class="l-en">عربي</span><span class="l-ar">EN</span></button>
   <button class="menu-btn" type="button" aria-label="Menu" aria-expanded="false">{icon("menu")}</button>
  </div>
 </div>
</header>
'''

def branch_nav(b, active_file):
    items = "".join(
        f'<li><a href="{f}"{" aria-current=\"page\"" if f == active_file else ""}>{t(en, ar)}</a></li>'
        for f, en, ar, *_ in SUBPAGES)
    plat = ' <span class="badge-platinum" style="margin:0;padding:3px 9px;font-size:10px;letter-spacing:.2em">PLATINUM</span>' if b["platinum"] else ""
    return f'''<nav class="branch-nav" aria-label="{esc(b["name"][0])}">
 <div class="wrap">
  <div class="branch-tag"><span class="dot"></span>{t(*b["short"])}{plat}</div>
  <ul>{items}</ul>
 </div>
</nav>
'''

def footer(depth, branch=None):
    p = "../" * depth
    # Instagram icon(s): the current branch's account on branch pages, both accounts elsewhere
    ig_keys = [branch] if branch else BRANCH_ORDER
    ig_icons = "".join(
        f'<a class="social" href="{BRANCHES[k]["instagram"]}" target="_blank" rel="noopener" '
        f'aria-label="Instagram {esc(BRANCHES[k]["name"][0])}" title="Instagram – {esc(BRANCHES[k]["short"][0])}">{icon("instagram")}</a>'
        for k in ig_keys)
    cols = ""
    for key in BRANCH_ORDER:
        b = BRANCHES[key]
        cols += f'''<div>
   <h4>{t(*b["name"])}</h4>
   <ul>
    <li><a href="tel:{b["phone_intl"]}"><span class="ltr">{b["phone_display"]}</span></a></li>
    <li><a href="https://wa.me/{b["wa"]}" target="_blank" rel="noopener">WhatsApp</a></li>
    <li><a href="{b["maps"]}" target="_blank" rel="noopener">{t("Get directions", "الموقع على الخريطة")}</a></li>
    <li><a href="{b["instagram"]}" target="_blank" rel="noopener"><span class="ltr">{b["ig_handle"]}</span></a></li>
    <li><a href="{p}{b["slug"]}/hours.html">{t("Opening hours", "أوقات الدوام")}</a></li>
   </ul>
  </div>'''
    return f'''<footer class="site-footer">
 <div class="wrap">
  <div class="foot-grid">
   <div>
    <img class="foot-logo" src="{p}assets/img/logo.webp" alt="Fitness Factory" width="120" height="139" loading="lazy">
    <p class="muted" style="max-width:34ch;margin:0 0 20px">{t("Built for Strength. Driven by Excellence.", "صُنع للقوة. مدفوع بالتميّز.")}</p>
    <div class="socials">
     <a class="social" href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook">{icon("facebook")}</a>
     {ig_icons}
    </div>
   </div>
   {cols}
   <div>
    <h4>{t("Explore", "تصفّح")}</h4>
    <ul>
     <li><a href="{p}index.html">{t("Home", "الرئيسية")}</a></li>
     <li><a href="{p}about.html">{t("About Us", "من نحن")}</a></li>
     <li><a href="{p}contact.html">{t("Contact Us", "تواصل معنا")}</a></li>
     <li><a href="{p}khalda/memberships.html">{t("Khalda memberships", "اشتراكات خلدا")}</a></li>
     <li><a href="{p}dahyet-alrasheed/memberships.html">{t("Dahyet Al Rasheed memberships", "اشتراكات ضاحية الرشيد")}</a></li>
    </ul>
   </div>
  </div>
  <div class="foot-bottom">
   <span>© <span data-year>2026</span> Fitness Factory. {t("All rights reserved.", "جميع الحقوق محفوظة.")}</span>
   <span>{t("Amman, Jordan", "عمّان، الأردن")}</span>
  </div>
 </div>
</footer>
'''

def wa_float(branch=None):
    if branch:
        b = BRANCHES[branch]
        return f'<div class="wa-float"><a class="wa-btn" href="https://wa.me/{b["wa"]}" target="_blank" rel="noopener" aria-label="WhatsApp {esc(b["name"][0])}">{icon("whatsapp")}</a></div>\n'
    links = "".join(
        f'<a href="https://wa.me/{BRANCHES[k]["wa"]}" target="_blank" rel="noopener">{icon("whatsapp")}<span>{t(*BRANCHES[k]["name"])}<small class="ltr">{BRANCHES[k]["phone_display"]}</small></span></a>'
        for k in BRANCH_ORDER)
    return f'''<div class="wa-float">
 <div class="wa-menu" role="menu">{links}</div>
 <button class="wa-btn" type="button" data-wa-toggle aria-label="WhatsApp" aria-expanded="false">{icon("whatsapp")}</button>
</div>
'''

def page(path, depth, active, title, desc, body, branch=None, sub=None, og="khalda-hero.jpg"):
    p = "../" * depth
    body_cls = ' class="platinum"' if branch and BRANCHES[branch]["platinum"] else ""
    out = head(depth, title[0], title[1], desc, og)
    out += f"<body{body_cls}>\n" + header(depth, active)
    if branch:
        out += branch_nav(BRANCHES[branch], sub)
    out += "<main>\n" + body + "</main>\n" + footer(depth, branch) + wa_float(branch)
    out += f'<script src="{p}assets/js/main.js" defer></script>\n</body>\n</html>\n'
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", path)

def sample_note():
    return (f'<div class="sample-note">{icon("info")}<span>'
            + t("Sample information for preview — final details will be updated soon.",
                "معلومات تجريبية للعرض — سيتم تحديث التفاصيل النهائية قريباً.")
            + '</span></div>')

def sec_head(kicker, title, sub=None, center=False):
    s = f'<div class="sec-head{" center" if center else ""} reveal"><p class="kicker">{kicker}</p><h2>{title}</h2>'
    if sub:
        s += f"<p>{sub}</p>"
    return s + "</div>"

def page_hero(depth, img, kicker, title, lead=None, size="tiny", extra=""):
    p = "../" * depth
    l = f'<p class="lead">{lead}</p>' if lead else ""
    return f'''<section class="hero {size}">
 <div class="hero-bg"><img src="{p}assets/img/{img}" alt="" fetchpriority="high"></div>
 <div class="wrap">{extra}<p class="kicker">{kicker}</p><h1 class="metal">{title}</h1>{l}</div>
</section>
'''

def cta(depth, b=None):
    p = "../" * depth
    if b:
        btns = (f'<a class="btn btn-red" href="https://wa.me/{b["wa"]}" target="_blank" rel="noopener">{icon("whatsapp")}{t("WhatsApp us", "راسلنا واتساب")}</a>'
                f'<a class="btn btn-ghost" href="tel:{b["phone_intl"]}">{icon("phone")}<span class="ltr">{b["phone_display"]}</span></a>')
        title = t(f"Ready to train at {b['short'][0]}?", f"جاهز للتمرين في {b['short'][1]}؟")
    else:
        btns = (f'<a class="btn btn-red" href="{p}contact.html">{t("Contact us", "تواصل معنا")}{icon("arrow")}</a>'
                f'<a class="btn btn-ghost" href="{p}about.html">{t("About Fitness Factory", "عن فيتنس فاكتوري")}</a>')
        title = t("Your stronger self starts today", "نسختك الأقوى تبدأ اليوم")
    return f'''<section class="sec tight"><div class="wrap"><div class="cta reveal">
 <img class="wm" src="{p}assets/img/logo-icon.webp" alt="">
 <div><h2>{title}</h2><p>{t("Visit us, call or send a WhatsApp message — our team will help you choose the right plan.", "زرنا أو اتصل بنا أو أرسل رسالة واتساب — فريقنا سيساعدك في اختيار الاشتراك المناسب.")}</p></div>
 <div class="btns">{btns}</div>
</div></div></section>
'''

# ---------------------------------------------------------------- pages: general
def build_home():
    d = 0
    cards = ""
    for key in BRANCH_ORDER:
        b = BRANCHES[key]
        plat = b["platinum"]
        logo = f'<img class="logo-mini" src="assets/img/{"logo-platinum" if plat else "logo"}.webp" alt="">'
        hrs = b["hours_summary"][0]
        cards += f'''<a class="branch-card{" plat" if plat else ""} reveal" href="{key}/index.html">
 <img class="bg" src="assets/img/{b["hero"]}" alt="{esc(b["name"][0])}" loading="lazy">
 {logo}
 <div class="inner">
  {'<span class="badge-platinum">Platinum</span>' if plat else ''}
  <h3 class="metal">{t(*b["name"])}</h3>
  <p>{t(*b["tagline"])}</p>
  <div class="meta">
   <span>{icon("clock")}<span class="status" data-hours='{json.dumps(b["hours_js"])}'>&nbsp;</span></span>
   <span>{icon("phone")}<span class="ltr">{b["phone_display"]}</span></span>
  </div>
  <span class="btn {"btn-metal" if plat else "btn-red"}">{t("Explore branch", "استكشف الفرع")}{icon("arrow")}</span>
 </div>
</a>'''
    why = [("dumbbell", "Strength Training", "تدريب القوة", "Complete free-weight and machine areas built for real progress.", "مناطق أوزان حرة وأجهزة متكاملة مصمّمة لتقدّم حقيقي."),
           ("bolt", "Physical Conditioning", "اللياقة البدنية", "Cardio, functional and conditioning work to improve performance.", "كارديو وتدريب وظيفي ولياقة لتحسين الأداء."),
           ("user", "Professional Coaching", "تدريب احترافي", "Coaches who build programmes around your goals and keep you on track.", "مدربون يبنون برامج حول أهدافك ويتابعون تقدّمك."),
           ("flame", "Motivating Environment", "بيئة محفّزة", "A focused atmosphere and a community that pushes you to stay consistent.", "أجواء مركّزة ومجتمع يدفعك للاستمرار.")]
    why_html = "".join(f'<div class="card reveal"><div class="icon">{icon(i)}</div><h3>{t(a, b_)}</h3><p>{t(c, d_)}</p></div>' for i, a, b_, c, d_ in why)
    body = f'''<section class="hero">
 <div class="hero-bg"><img src="assets/img/khalda-hero.jpg" alt="" fetchpriority="high"></div>
 <div class="wrap">
  <img class="hero-logo" src="assets/img/logo.webp" alt="Fitness Factory logo" width="180" height="208">
  <p class="kicker">{t("Fitness Factory · Amman", "فيتنس فاكتوري · عمّان")}</p>
  <h1 class="metal">{t("Built for Strength.<br>Driven by Excellence.", "صُنع للقوة.<br>مدفوع بالتميّز.")}</h1>
  <p class="lead">{t("Two branches across Amman, one mission: helping you become a stronger version of yourself through strength training, conditioning and a motivating environment.", "فرعان في عمّان وهدف واحد: أن نساعدك لتصبح نسخة أقوى من نفسك من خلال تدريب القوة واللياقة البدنية وبيئة تدريب محفّزة.")}</p>
  <div class="btns">
   <a class="btn btn-red" href="#branches">{t("Choose your branch", "اختر فرعك")}{icon("arrow")}</a>
   <a class="btn btn-ghost" href="contact.html">{t("Contact us", "تواصل معنا")}</a>
  </div>
 </div>
</section>
<section class="sec tight"><div class="wrap">
 <div class="stats reveal">
  <div class="stat"><b class="metal">2</b><span>{t("Branches in Amman", "فرعان في عمّان")}</span></div>
  <div class="stat"><b class="metal">18.5</b><span>{t("Hours open daily", "ساعة دوام يومياً")}</span></div>
  <div class="stat"><b class="metal">7</b><span>{t("Days a week", "أيام في الأسبوع")}</span></div>
  <div class="stat"><b class="metal">1</b><span>{t("Goal: a stronger you", "هدف واحد: نسخة أقوى منك")}</span></div>
 </div>
</div></section>
<section class="sec" id="branches" style="padding-top:40px"><div class="wrap">
 {sec_head(t("Our branches", "فروعنا"), t("Two branches. <span class='red'>Different experiences.</span>", "فرعان. <span class='red'>تجربتان مختلفتان.</span>"), t("Each branch has its own memberships, trainers, opening hours and services. Choose your branch to see its details.", "لكل فرع اشتراكاته ومدربوه وأوقات دوامه وخدماته الخاصة. اختر فرعك لتشاهد تفاصيله."))}
 <div class="grid g2">{cards}</div>
</div></section>
<section class="sec alt"><div class="wrap">
 <div class="split">
  <div class="reveal">
   <p class="kicker">{t("About us", "من نحن")}</p>
   <div class="sec-head" style="margin-bottom:24px"><h2 class="metal">{t("More than a gym", "أكثر من مجرد نادٍ رياضي")}</h2></div>
   <div class="prose">
    <p class="big">{t("Fitness Factory is a fitness and wellness brand based in Amman, Jordan, dedicated to helping individuals achieve their fitness goals.", "فيتنس فاكتوري علامة رياضية وصحية مقرّها عمّان، الأردن، تهدف إلى مساعدة الأفراد على تحقيق أهدافهم الرياضية.")}</p>
    <p>{t("Our focus is on building strength, improving performance, encouraging consistency, and creating an environment where every individual can work towards becoming a stronger version of themselves.", "نركّز على بناء القوة وتحسين الأداء وتعزيز الاستمرارية، وعلى خلق بيئة يستطيع فيها كل فرد أن يعمل ليصبح نسخة أقوى من نفسه.")}</p>
   </div>
   <a class="btn btn-ghost" href="about.html" style="margin-top:12px">{t("Read our story", "اقرأ قصتنا")}{icon("arrow")}</a>
  </div>
  <div class="photo reveal"><img src="assets/img/dahyet-hero.jpg" alt="Fitness Factory training floor" loading="lazy"></div>
 </div>
</div></section>
<section class="sec"><div class="wrap">
 {sec_head(t("Why Fitness Factory", "لماذا فيتنس فاكتوري"), t("Everything you need to get stronger", "كل ما تحتاجه لتصبح أقوى"), center=True)}
 <div class="grid g4">{why_html}</div>
</div></section>
{cta(0)}'''
    page("index.html", d, "home", ("Fitness Factory | Gym in Amman – Khalda & Dahyet Al Rasheed", "فيتنس فاكتوري | نادي رياضي في عمّان – خلدا وضاحية الرشيد"),
         "Fitness Factory gym in Amman, Jordan — two branches in Khalda (Platinum) and Dahyet Al Rasheed. Strength training, conditioning and professional coaching.", body)

def build_about():
    vals = [("dumbbell", "Strength", "القوة", "Building real, lasting strength is at the core of everything we do.", "بناء قوة حقيقية ودائمة هو جوهر كل ما نقوم به."),
            ("trophy", "Performance", "الأداء", "Training that improves how you move, lift and live.", "تدريب يحسّن طريقة حركتك ورفعك للأوزان وحياتك اليومية."),
            ("calendar", "Consistency", "الاستمرارية", "Results come from showing up — we make it easier to keep going.", "النتائج تأتي من الالتزام — ونحن نجعل الاستمرار أسهل."),
            ("users", "Community", "المجتمع", "A motivating environment where members push each other forward.", "بيئة محفّزة يدفع فيها المشتركون بعضهم للأمام.")]
    vals_html = "".join(f'<div class="card reveal"><div class="icon">{icon(i)}</div><h3>{t(a, b)}</h3><p>{t(c, d)}</p></div>' for i, a, b, c, d in vals)
    br = ""
    for key in BRANCH_ORDER:
        b = BRANCHES[key]
        br += f'<a class="card reveal" href="{key}/index.html"><span class="arrow">{icon("arrow")}</span><div class="icon">{icon("pin")}</div><h3>{t(*b["name"])}</h3><p>{t(*b["tagline"])}</p></a>'
    body = page_hero(0, "khalda-reception.jpg", t("About us", "من نحن"), "FITNESS FACTORY",
                     t("Built for Strength. Driven by Excellence.", "صُنع للقوة. مدفوع بالتميّز."), size="short") + f'''
<section class="sec"><div class="wrap">
 <div class="split">
  <div class="prose reveal">
   <p class="kicker">{t("Our story", "قصتنا")}</p>
   <p class="big">{t("Fitness Factory is a fitness and wellness brand based in Amman, Jordan, dedicated to helping individuals achieve their fitness goals through strength training, physical conditioning, and a motivating training environment.", "فيتنس فاكتوري علامة رياضية وصحية مقرّها عمّان، الأردن، تهدف إلى مساعدة الأفراد على تحقيق أهدافهم الرياضية من خلال تدريب القوة واللياقة البدنية وبيئة تدريب محفّزة.")}</p>
   <p>{t("With two branches serving different communities across Amman, Fitness Factory brings together fitness facilities, professional training support, and a range of fitness-related services designed to support an active and healthy lifestyle.", "من خلال فرعين يخدمان مجتمعات مختلفة في عمّان، تجمع فيتنس فاكتوري بين المرافق الرياضية والدعم التدريبي الاحترافي ومجموعة من الخدمات الرياضية المصمّمة لدعم أسلوب حياة نشيط وصحي.")}</p>
   <p>{t("Our focus is on building strength, improving performance, encouraging consistency, and creating an environment where every individual can work towards becoming a stronger version of themselves.", "نركّز على بناء القوة وتحسين الأداء وتعزيز الاستمرارية، وعلى خلق بيئة يستطيع فيها كل فرد أن يعمل ليصبح نسخة أقوى من نفسه.")}</p>
  </div>
  <div class="photo reveal"><img src="assets/img/khalda-hero.jpg" alt="Fitness Factory Platinum, Khalda" loading="lazy"></div>
 </div>
</div></section>
<section class="sec alt"><div class="wrap">
 {sec_head(t("What drives us", "ما يحرّكنا"), t("Our values", "قيمنا"), center=True)}
 <div class="grid g4">{vals_html}</div>
</div></section>
<section class="sec"><div class="wrap">
 {sec_head(t("Our branches", "فروعنا"), t("Two communities across Amman", "مجتمعان في عمّان"))}
 <div class="grid g2">{br}</div>
</div></section>
{cta(0)}'''
    page("about.html", 0, "about", ("About Us | Fitness Factory", "من نحن | فيتنس فاكتوري"),
         "Fitness Factory is a fitness and wellness brand based in Amman, Jordan, with branches in Khalda and Dahyet Al Rasheed.", body, og="khalda-reception.jpg")

def build_contact():
    cards = ""
    for key in BRANCH_ORDER:
        b = BRANCHES[key]
        hours = "".join(f'<div>{t(en, ar)}: <span class="muted">{t(*h)}</span></div>' for en, ar, h in b["hours_summary"])
        cards += f'''<div class="card contact-card reveal">
 <div class="top"><img src="assets/img/{b["hero"]}" alt="{esc(b["name"][0])}" loading="lazy"></div>
 <div class="body">
  {'<span class="badge-platinum">Platinum</span>' if b["platinum"] else ''}
  <h3 class="metal">{t(*b["name"])}</h3>
  <ul class="c-list">
   <li><span class="ic">{icon("phone")}</span><span><small>{t("Call", "اتصال")}</small><a href="tel:{b["phone_intl"]}"><span class="ltr">{b["phone_display"]}</span></a></span></li>
   <li><span class="ic">{icon("whatsapp")}</span><span><small>WhatsApp</small><a href="https://wa.me/{b["wa"]}" target="_blank" rel="noopener"><span class="ltr">{b["phone_display"]}</span></a></span></li>
   <li><span class="ic">{icon("pin")}</span><span><small>{t("Location", "الموقع")}</small><a href="{b["maps"]}" target="_blank" rel="noopener">{t("Open in Google Maps", "افتح في خرائط جوجل")}</a></span></li>
   <li><span class="ic">{icon("instagram")}</span><span><small>Instagram</small><a href="{b["instagram"]}" target="_blank" rel="noopener"><span class="ltr">{b["ig_handle"]}</span></a></span></li>
   <li><span class="ic">{icon("clock")}</span><span><small>{t("Opening hours", "أوقات الدوام")} · <span class="status" data-hours='{json.dumps(b["hours_js"])}'>&nbsp;</span></small>{hours}</span></li>
  </ul>
  <div class="btns">
   <a class="btn btn-red btn-sm" href="https://wa.me/{b["wa"]}" target="_blank" rel="noopener">{icon("whatsapp")}WhatsApp</a>
   <a class="btn btn-ghost btn-sm" href="tel:{b["phone_intl"]}">{icon("phone")}{t("Call", "اتصال")}</a>
   <a class="btn btn-ghost btn-sm" href="{b["maps"]}" target="_blank" rel="noopener">{icon("pin")}{t("Directions", "الاتجاهات")}</a>
  </div>
 </div>
</div>'''
    body = page_hero(0, "dahyet-2.jpg", t("Contact us", "تواصل معنا"), t("Get in touch", "تواصل معنا"),
                     t("Call, message us on WhatsApp or visit the branch nearest to you.", "اتصل بنا أو راسلنا على واتساب أو زر الفرع الأقرب إليك.")) + f'''
<section class="sec"><div class="wrap">
 <div class="grid g2">{cards}</div>
</div></section>
<section class="sec alt tight"><div class="wrap">
 <div class="split follow">
  <div class="reveal"><p class="kicker">{t("Follow us", "تابعنا")}</p><div class="sec-head mb-0" style="margin:0"><h2 class="metal" style="margin:0">{t("Stay connected", "ابقَ على تواصل")}</h2></div></div>
  <div class="btns reveal">
   <a class="btn btn-ghost" href="{FACEBOOK}" target="_blank" rel="noopener">{icon("facebook")}Facebook</a>
   <a class="btn btn-ghost" href="{BRANCHES["khalda"]["instagram"]}" target="_blank" rel="noopener">{icon("instagram")}{t("Instagram – Khalda", "انستغرام – خلدا")}</a>
   <a class="btn btn-ghost" href="{BRANCHES["dahyet-alrasheed"]["instagram"]}" target="_blank" rel="noopener">{icon("instagram")}{t("Instagram – Dahyet Al Rasheed", "انستغرام – ضاحية الرشيد")}</a>
  </div>
 </div>
</div></section>
'''
    page("contact.html", 0, "contact", ("Contact Us | Fitness Factory", "تواصل معنا | فيتنس فاكتوري"),
         "Contact Fitness Factory Khalda and Dahyet Al Rasheed branches — phone, WhatsApp, location and Instagram.", body, og="dahyet-2.jpg")

# ---------------------------------------------------------------- pages: branch
def bhero(b, kicker_en, kicker_ar, title, lead=None, size="tiny", img=None):
    extra = '<span class="badge-platinum">Platinum</span><br>' if b["platinum"] else ""
    return page_hero(1, img or b["hero"], t(kicker_en, kicker_ar), title, lead, size, extra)

def branch_page(b, file, title_en, title_ar, desc, body):
    full_title = (f"{title_en} | {b['name'][0]} – Fitness Factory", f"{title_ar} | {b['name'][1]} – فيتنس فاكتوري")
    page(f"{b['slug']}/{file}", 1, b["slug"], full_title, desc, body, branch=b["slug"], sub=file, og=b["hero"])

def build_branch(key):
    b = BRANCHES[key]
    plat = b["platinum"]
    btn_main = "btn-metal" if plat else "btn-red"
    status = f'<span class="status" data-hours=\'{json.dumps(b["hours_js"])}\'>&nbsp;</span>'
    name_en, name_ar = b["name"]

    # ---- overview
    logo = f'<img class="hero-logo" src="../assets/img/{"logo-platinum" if plat else "logo"}.webp" alt="" width="160">'
    hero = f'''<section class="hero short">
 <div class="hero-bg"><img src="../assets/img/{b["hero"]}" alt="" fetchpriority="high"></div>
 <div class="wrap">
  {logo}
  <p class="kicker">{t(*b["title"])}</p>
  <h1 class="metal">{t(name_en, name_ar)}</h1>
  <p class="lead">{t(*b["tagline"])}</p>
  <div class="btns">
   <a class="btn {btn_main}" href="memberships.html">{t("View memberships", "عرض الاشتراكات")}{icon("arrow")}</a>
   <a class="btn btn-ghost" href="https://wa.me/{b["wa"]}" target="_blank" rel="noopener">{icon("whatsapp")}WhatsApp</a>
  </div>
 </div>
</section>'''
    today_list = "".join(f'<span>{t(en, ar)}: {t(*h)}</span><br>' for en, ar, h in b["hours_summary"])
    quick = f'''<div class="wrap"><div class="quick">
 <a href="hours.html"><span class="ic">{icon("clock")}</span><span><small>{t("Opening hours", "أوقات الدوام")}</small><strong>{status}</strong></span></a>
 <a href="tel:{b["phone_intl"]}"><span class="ic">{icon("phone")}</span><span><small>{t("Call / WhatsApp", "اتصال / واتساب")}</small><strong class="ltr">{b["phone_display"]}</strong></span></a>
 <a href="{b["maps"]}" target="_blank" rel="noopener"><span class="ic">{icon("pin")}</span><span><small>{t("Location", "الموقع")}</small><strong>{t("Get directions", "احصل على الاتجاهات")}</strong></span></a>
</div></div>'''
    checks = "".join(f'<li>{icon("check")}<span>{t(*h)}</span></li>' for h in b["highlights"])
    intro = "".join(f"<p>{t(*p)}</p>" for p in b["intro"])
    explore = "".join(
        f'<a class="card reveal" href="{f}"><span class="arrow">{icon("arrow")}</span><div class="icon">{icon(ic)}</div><h3>{t(en, ar)}</h3><p>{t(de, da)}</p></a>'
        for f, en, ar, ic, de, da in SUBPAGES[1:])
    body = hero + quick + f'''
<section class="sec"><div class="wrap">
 <div class="split">
  <div class="reveal">
   <p class="kicker">{t("Welcome", "أهلاً بك")}</p>
   <div class="sec-head" style="margin-bottom:22px"><h2 class="metal">{t("Welcome to " + b["short"][0], "أهلاً بك في " + b["short"][1])}</h2></div>
   <div class="prose">{intro}</div>
   <ul class="checks">{checks}</ul>
  </div>
  <div class="photo reveal"><img src="../assets/img/{b["photos"][1][0]}" alt="{esc(b["photos"][1][1][0])}" loading="lazy"><span class="tag">{t(*b["photos"][1][1])}</span></div>
 </div>
</div></section>
<section class="sec alt"><div class="wrap">
 {sec_head(t("Explore the branch", "استكشف الفرع"), t("Everything about " + b["short"][0], "كل ما يخص " + b["short"][1]))}
 <div class="grid g3">{explore}</div>
</div></section>
{cta(1, b)}'''
    branch_page(b, "index.html", "Overview", "نظرة عامة",
                f"Fitness Factory {name_en}, Amman — memberships, trainers, opening hours, services and classes.", body)

    # ---- memberships
    cards = ""
    feats = "".join(f'<li>{icon("check")}<span>{t(*f)}</span></li>' for f in b["plan_features"])
    for en, ar, price, per, featured in b["plans"]:
        rib = f'<span class="ribbon">{t("Best value", "الأفضل قيمة")}</span>' if featured else ""
        cards += f'''<div class="card price-card{" featured" if featured else ""} reveal">{rib}
 <p class="name">{t(en, ar)}</p>
 <div class="price"><b class="metal">{price}</b><span>{t("JD", "د.أ")}</span></div>
 <div class="per">{t(*per)}</div>
 <ul>{feats}</ul>
 <a class="btn {btn_main if featured else "btn-ghost"}" href="https://wa.me/{b["wa"]}?text={esc("Hi, I'd like to join Fitness Factory " + b["short"][0] + " – " + en + " membership")}" target="_blank" rel="noopener">{t("Join now", "اشترك الآن")}</a>
</div>'''
    rows = "".join(f'<tr><td>{t(en, ar)}</td><td class="num">{t(pe, pa)}</td></tr>' for en, ar, pe, pa in b["extras"])
    body = bhero(b, "Memberships", "الاشتراكات", t("Memberships & prices", "الاشتراكات والأسعار"),
                 t(f"Choose the plan that fits your goals at our {b['short'][0]} branch.", f"اختر الاشتراك المناسب لأهدافك في فرع {b['short'][1]}.")) + f'''
<section class="sec"><div class="wrap">
 {sample_note()}
 <div class="grid g4" style="padding-top:14px">{cards}</div>
 <p class="note">{t("Prices in Jordanian Dinar (JD). Visit the branch or contact us on WhatsApp to subscribe.", "الأسعار بالدينار الأردني. زر الفرع أو تواصل معنا عبر واتساب للاشتراك.")}</p>
</div></section>
<section class="sec alt"><div class="wrap">
 {sec_head(t("Add-ons & extras", "إضافات وخدمات أخرى"), t("More options", "خيارات إضافية"))}
 <div class="table-wrap reveal"><table>
  <thead><tr><th>{t("Service", "الخدمة")}</th><th>{t("Price", "السعر")}</th></tr></thead>
  <tbody>{rows}</tbody>
 </table></div>
</div></section>
{cta(1, b)}'''
    branch_page(b, "memberships.html", "Memberships", "الاشتراكات",
                f"Membership plans and prices at Fitness Factory {name_en}, Amman.", body)

    # ---- trainers
    tc = ""
    for en, ar, role, yrs, chips in b["trainers"]:
        initials = "".join(w[0] for w in en.replace("Al-", "").split()[:2])
        chips_h = "".join(f'<span class="chip">{c}</span>' for c in chips)
        tc += f'''<div class="card trainer reveal">
 <div class="avatar"><span class="metal">{initials}</span><img class="mark" src="../assets/img/logo-icon.webp" alt=""></div>
 <div class="body">
  <h3>{t(en, ar)}</h3>
  <div class="role">{t(*role)}</div>
  <p>{t(f"{yrs} years of coaching experience", f"خبرة {yrs} سنوات في التدريب" if yrs <= 10 else f"خبرة {yrs} سنة في التدريب")}</p>
  <div class="chips">{chips_h}</div>
 </div>
</div>'''
    body = bhero(b, "Trainers", "المدربون", t("Meet our coaches", "تعرّف على مدربينا"),
                 t(f"The coaching team at {b['short'][0]} — here to guide, correct and motivate you.", f"فريق المدربين في {b['short'][1]} — هنا لتوجيهك وتصحيح أدائك وتحفيزك.")) + f'''
<section class="sec"><div class="wrap">
 {sample_note()}
 <div class="grid {"g3" if len(b["trainers"]) % 3 == 0 else "g4"}">{tc}</div>
</div></section>
{cta(1, b)}'''
    branch_page(b, "trainers.html", "Trainers", "المدربون",
                f"Personal trainers and coaches at Fitness Factory {name_en}, Amman.", body)

    # ---- hours
    rows = ""
    for js, en, ar in DAYS:
        h = b["hours_rows"][js]
        rows += f'<tr data-day="{js}"><td>{t(en, ar)}<span class="today-pill" hidden>{t("Today", "اليوم")}</span></td><td class="num">{t(*h)}</td></tr>'
    body = bhero(b, "Opening hours", "أوقات الدوام", t("Opening hours", "أوقات الدوام"),
                 t(f"When you can train at our {b['short'][0]} branch.", f"مواعيد التدريب في فرع {b['short'][1]}.")) + f'''
<section class="sec"><div class="wrap" style="max-width:860px">
 <div class="card reveal" style="display:flex;gap:16px;align-items:center;margin-bottom:22px">
  <div class="icon" style="margin:0">{icon("clock")}</div>
  <div><small class="muted">{t("Right now (Amman time)", "الآن (بتوقيت عمّان)")}</small><div style="font-size:20px">{status}</div></div>
 </div>
 <div class="table-wrap reveal"><table>
  <thead><tr><th>{t("Day", "اليوم")}</th><th>{t("Hours", "الدوام")}</th></tr></thead>
  <tbody>{rows}</tbody>
 </table></div>
 <p class="note">{t("Hours may change during public holidays and Ramadan — follow our Instagram for updates.", "قد تتغيّر المواعيد خلال العطل الرسمية وشهر رمضان — تابع حسابنا على انستغرام للتحديثات.")} <a class="red" href="{b["instagram"]}" target="_blank" rel="noopener"><span class="ltr">{b["ig_handle"]}</span></a></p>
</div></section>
{cta(1, b)}'''
    branch_page(b, "hours.html", "Opening Hours", "أوقات الدوام",
                f"Opening hours of Fitness Factory {name_en}, Amman.", body)

    # ---- services
    sv = "".join(f'<div class="card reveal"><div class="icon">{icon(i)}</div><h3>{t(a, b_)}</h3><p>{t(c, d)}</p></div>'
                 for i, a, b_, c, d in b["services"])
    ph = b["photos"][1]
    body = bhero(b, "Services", "الخدمات", t("Services & facilities", "الخدمات والمرافق"),
                 t(f"What's available at our {b['short'][0]} branch.", f"ما يقدّمه فرع {b['short'][1]}."),
                 img=b["photos"][1][0]) + f'''
<section class="sec"><div class="wrap">
 {sample_note()}
 <div class="grid {"g4" if len(b["services"]) % 4 == 0 else "g3"}">{sv}</div>
</div></section>
<section class="sec alt"><div class="wrap">
 <div class="split rev">
  <div class="photo reveal"><img src="../assets/img/{b["photos"][2][0]}" alt="{esc(b["photos"][2][1][0])}" loading="lazy"><span class="tag">{t(*b["photos"][2][1])}</span></div>
  <div class="reveal">
   <p class="kicker">{t("Personal training", "التدريب الشخصي")}</p>
   <div class="sec-head" style="margin-bottom:18px"><h2 class="metal">{t("Train with a coach", "تدرّب مع مدرب")}</h2></div>
   <div class="prose"><p>{t("Get a programme built around your body and your goals, with a coach who corrects your technique and keeps you accountable.", "احصل على برنامج مبني حول جسمك وأهدافك، مع مدرب يصحّح أداءك ويتابع التزامك.")}</p></div>
   <div class="btns" style="margin-top:20px"><a class="btn {btn_main}" href="trainers.html">{t("Meet the trainers", "تعرّف على المدربين")}{icon("arrow")}</a><a class="btn btn-ghost" href="memberships.html">{t("See prices", "شاهد الأسعار")}</a></div>
  </div>
 </div>
</div></section>
{cta(1, b)}'''
    branch_page(b, "services.html", "Services", "الخدمات",
                f"Services and facilities at Fitness Factory {name_en}, Amman.", body)

    # ---- classes
    days_html = ""
    for js, en, ar in DAYS:
        items = b["classes"].get(js, [])
        if items:
            lis = "".join(f'<li><time class="ltr">{tm}</time><b>{t(ce, ca)}</b><small>{t("Coach", "المدرب")}: {c}</small></li>' for tm, ce, ca, c in items)
        else:
            lis = f'<li class="none">{t("No classes — open gym", "لا توجد حصص — تدريب حر")}</li>'
        days_html += f'<div class="day reveal" data-day="{js}"><h4>{t(en, ar)}<span class="today-pill" hidden>{t("Today", "اليوم")}</span></h4><ul>{lis}</ul></div>'
    body = bhero(b, "Class schedule", "جدول الحصص", t("Weekly class schedule", "جدول الحصص الأسبوعي"),
                 t("Group classes are included with membership unless stated otherwise.", "الحصص الجماعية مشمولة مع الاشتراك ما لم يُذكر غير ذلك."),
                 img=b["photos"][1][0] if plat else b["hero"]) + f'''
<section class="sec"><div class="wrap">
 {sample_note()}
 <div class="days">{days_html}</div>
 <p class="note">{t("Class times may change — contact the branch on WhatsApp to confirm your spot.", "قد تتغيّر مواعيد الحصص — تواصل مع الفرع عبر واتساب لتأكيد مكانك.")}</p>
</div></section>
{cta(1, b)}'''
    branch_page(b, "classes.html", "Class Schedule", "جدول الحصص",
                f"Weekly group class schedule at Fitness Factory {name_en}, Amman.", body)

    # ---- gallery
    g = ""
    for i, (img, cap) in enumerate(b["photos"]):
        g += f'<button type="button" class="{"wide" if i == 0 else ""} reveal" data-full="../assets/img/{img}" aria-label="{esc(cap[0])}"><img src="../assets/img/{img}" alt="{esc(cap[0])}" loading="lazy"></button>'
    body = bhero(b, "Gallery", "معرض الصور", t("Inside the branch", "من داخل الفرع"),
                 t(f"A look inside Fitness Factory {b['short'][0]}.", f"نظرة من داخل فيتنس فاكتوري {b['short'][1]}."),
                 img=b["photos"][-1][0]) + f'''
<section class="sec"><div class="wrap">
 <div class="gallery">{g}</div>
</div></section>
<div class="lightbox" role="dialog" aria-modal="true" aria-label="Photo"><button type="button" aria-label="Close">{icon("x")}</button><img src="" alt=""></div>
{cta(1, b)}'''
    branch_page(b, "gallery.html", "Gallery", "معرض الصور",
                f"Photos of Fitness Factory {name_en}, Amman.", body)


if __name__ == "__main__":
    build_home()
    build_about()
    build_contact()
    for k in BRANCH_ORDER:
        build_branch(k)
