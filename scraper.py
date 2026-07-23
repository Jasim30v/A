#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                            ║
║  💜  VØID_X SUPREME v2 - Complete Platform               ║
║     Cloudinary: dmqyd0haj / s3_gok                        ║
║     Database: europe-west1                                ║
║     Admin: jasim28v@gmail.com                             ║
║     Bottom Nav: Profile | Chat | Upload | Notifications   ║
║                                                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import shutil

# ═══════════════════════════════════════════════════════════
# 💜 CONFIGURATION
# ═══════════════════════════════════════════════════════════

FIREBASE_CONFIG = {
    "apiKey": "AIzaSyCqDvG98pEqmZHKZienquJEq6gS1kNjK8M",
    "authDomain": "muvg-42126.firebaseapp.com",
    "databaseURL": "https://muvg-42126-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "muvg-42126",
    "storageBucket": "muvg-42126.firebasestorage.app",
    "messagingSenderId": "514075097173",
    "appId": "1:514075097173:web:6fab4e9598549691cc7cdc",
    "measurementId": "G-4VP8E6WJ48"
}

CLOUD_NAME = "dmqyd0haj"
UPLOAD_PRESET = "s3_gok"
CLOUDINARY_COLLECTION_URL = "https://collection.cloudinary.com/dmqyd0haj"
ADMIN_EMAILS_JS = "['jasim28v@gmail.com']"
DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg"
APP_NAME = "VØID_X"
WATERMARK_TEXT = "VØID_X SUPREME"
OUTPUT_DIR = "voidx_supreme_v2"
TOTAL_LINES = 0

COVER_COLORS_JS = """[
    "linear-gradient(135deg, #1a000d, #2d0020, #4a0030)",
    "linear-gradient(135deg, #0d001a, #200030, #350050)",
    "linear-gradient(135deg, #1a0020, #2d0040, #4a0060)",
    "linear-gradient(135deg, #150020, #280040, #3d0060)",
    "linear-gradient(135deg, #200030, #3d0060, #5a0090)",
    "linear-gradient(135deg, #0a0a1a, #1a1040, #2d1a60)"
]"""

def write(filename, content):
    global TOTAL_LINES
    filepath = os.path.join(OUTPUT_DIR, filename)
    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else OUTPUT_DIR, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n') + 1
    TOTAL_LINES += lines
    print(f"  ✅ {filename} ({lines} lines)")

def section(title):
    print(f"\n{'='*60}\n  💜  {title}\n{'='*60}")

# ═══════════════════════════════════════════════════════════
# 💜 COMMON CSS
# ═══════════════════════════════════════════════════════════

COMMON_CSS = """
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;900&family=Cairo:wght@400;700&display=swap');
    :root {
        --neon: #ff007f;
        --bg: #050002;
        --glass: rgba(255, 255, 255, 0.03);
        --border: rgba(255, 255, 255, 0.08);
        --card: rgba(255, 255, 255, 0.05);
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
        font-family: 'Cairo', sans-serif;
        background: var(--bg);
        color: #fff;
        -webkit-tap-highlight-color: transparent;
        user-select: none;
        -webkit-user-select: none;
    }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes fadeUp { from { opacity: 0; transform: translateY(40px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes spin { to { transform: rotate(360deg); } }
    @keyframes slideUp { from { transform: translateY(100%); } to { transform: translateY(0); } }
    @keyframes glowPulse { 0%,100% { box-shadow: 0 0 20px var(--neon); } 50% { box-shadow: 0 0 40px var(--neon), 0 0 60px rgba(255,0,127,0.5); } }
    @keyframes floatMark { 0%,100% { transform: translate(0,0); } 50% { transform: translate(-20px, 40px); } }
    .spinner {
        width: 36px; height: 36px;
        border: 3px solid rgba(255,0,127,0.2);
        border-top-color: var(--neon);
        border-radius: 50%;
        animation: spin 0.7s linear infinite;
        margin: 30px auto;
    }
    .toast-msg {
        position: fixed; bottom: 120px; left: 50%; transform: translateX(-50%);
        background: rgba(5,0,2,0.95); padding: 12px 24px; border-radius: 30px;
        z-index: 10000; border: 1px solid rgba(255,0,127,0.4); font-size: 13px;
        opacity: 0; transition: opacity 0.3s; pointer-events: none; white-space: nowrap;
        box-shadow: 0 8px 32px rgba(255,0,127,0.2);
    }
    .toast-msg.show { opacity: 1; }
    .overlay {
        position: fixed; inset: 0; background: rgba(5,0,2,0.97);
        backdrop-filter: blur(40px); z-index: 400; overflow-y: auto;
        animation: fadeIn 0.3s ease;
    }
    .btn-close-overlay {
        background: rgba(255,0,127,0.1); border: 1px solid rgba(255,255,255,0.1);
        color: #fff; width: 36px; height: 36px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        cursor: pointer; font-size: 16px; transition: all 0.3s;
    }
"""

# ═══════════════════════════════════════════════════════════
# 1. firebase-config.js
# ═══════════════════════════════════════════════════════════

def build_config():
    return f"""// 💜 VØID_X SUPREME v2 Configuration
// Cloudinary: dmqyd0haj | Upload Preset: s3_gok
// Database: europe-west1

const firebaseConfig = {{
    apiKey: "{FIREBASE_CONFIG['apiKey']}",
    authDomain: "{FIREBASE_CONFIG['authDomain']}",
    databaseURL: "{FIREBASE_CONFIG['databaseURL']}",
    projectId: "{FIREBASE_CONFIG['projectId']}",
    storageBucket: "{FIREBASE_CONFIG['storageBucket']}",
    messagingSenderId: "{FIREBASE_CONFIG['messagingSenderId']}",
    appId: "{FIREBASE_CONFIG['appId']}",
    measurementId: "{FIREBASE_CONFIG['measurementId']}"
}};

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

const CLOUD_NAME = "{CLOUD_NAME}";
const UPLOAD_PRESET = "{UPLOAD_PRESET}";
const CLOUDINARY_UPLOAD_URL = `https://api.cloudinary.com/v1_1/${{CLOUD_NAME}}/auto/upload`;
const CLOUDINARY_COLLECTION_URL = "{CLOUDINARY_COLLECTION_URL}";

const ADMIN_EMAILS = {ADMIN_EMAILS_JS};
const DICEBEAR_URL = "{DICEBEAR_URL}";
const COVER_COLORS = {COVER_COLORS_JS};

const APP_NAME = "{APP_NAME}";
const WATERMARK_TEXT = "{WATERMARK_TEXT}";

console.log('%c💜 %c'+APP_NAME+' v2 Ready ✨', 'color: #ff007f; font-size: 16px;');
"""

# ═══════════════════════════════════════════════════════════
# 2. auth.html
# ═══════════════════════════════════════════════════════════

def build_auth():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💜 VØID_X | دخول</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body {{
            min-height: 100vh;
            background: radial-gradient(ellipse at top, #1a000d, #0d0015, #050002);
            display: flex; align-items: center; justify-content: center;
            overflow: hidden; position: relative;
        }}
        .bg-orb {{
            position: fixed; border-radius: 50%; filter: blur(130px); opacity: 0.3;
            animation: orbFloat 20s infinite alternate; pointer-events: none;
        }}
        .bg-orb:nth-child(1) {{ width: 400px; height: 400px; background: var(--neon); top: -100px; left: -100px; }}
        .bg-orb:nth-child(2) {{ width: 350px; height: 350px; background: #ff00aa; bottom: -100px; right: -100px; animation-delay: 5s; }}
        .bg-orb:nth-child(3) {{ width: 300px; height: 300px; background: #ff007f; top: 50%; left: 50%; animation-delay: 10s; }}
        @keyframes orbFloat {{ 0% {{ transform: translate(0,0) scale(1) }} 100% {{ transform: translate(50px,-50px) scale(1.3) }} }}

        .card {{
            position: relative; z-index: 1; width: 90%; max-width: 420px;
            background: rgba(255,255,255,0.03); backdrop-filter: blur(40px);
            border-radius: 32px; padding: 36px 24px;
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 30px 70px rgba(255,0,127,0.2), 0 0 60px rgba(255,0,127,0.1);
            animation: fadeUp 0.8s ease;
        }}
        .logo {{
            width: 70px; height: 70px; margin: 0 auto 20px;
            background: linear-gradient(135deg, rgba(255,0,127,0.4), rgba(255,0,170,0.4));
            border-radius: 20px; display: flex; align-items: center; justify-content: center;
            font-size: 36px; border: 1px solid rgba(255,0,127,0.3);
            animation: glowPulse 3s ease-in-out infinite;
            box-shadow: 0 0 30px rgba(255,0,127,0.5);
        }}
        h1 {{
            text-align: center; font-size: 36px; font-weight: 900;
            background: linear-gradient(135deg, #ff007f, #ff00aa);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            margin-bottom: 4px; font-family: 'Orbitron', sans-serif; letter-spacing: 2px;
        }}
        .sub {{ text-align: center; color: rgba(255,255,255,0.5); font-size: 13px; margin-bottom: 20px; }}
        .tabs {{ display: flex; gap: 4px; background: rgba(255,255,255,0.05); border-radius: 40px; padding: 4px; margin-bottom: 24px; border: 1px solid rgba(255,255,255,0.1); }}
        .tab {{ flex: 1; padding: 12px; background: none; border: none; color: rgba(255,255,255,0.5); cursor: pointer; border-radius: 40px; font-size: 14px; transition: all 0.3s; font-weight: 500; }}
        .tab.active {{ background: linear-gradient(135deg, #ff007f, #ff00aa); color: #fff; box-shadow: 0 8px 25px rgba(255,0,127,0.5); }}
        .form {{ display: none; animation: fadeIn 0.4s ease; }}
        .form.active {{ display: block; }}
        input {{
            width: 100%; padding: 15px 18px; margin: 8px 0;
            border-radius: 50px; background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.15); color: #fff;
            font-size: 14px; outline: none; transition: all 0.4s;
        }}
        input:focus {{ border-color: var(--neon); box-shadow: 0 0 25px rgba(255,0,127,0.3); background: rgba(255,255,255,0.08); }}
        input::placeholder {{ color: rgba(255,255,255,0.3); }}
        button {{
            width: 100%; padding: 15px; margin-top: 18px;
            background: linear-gradient(135deg, #ff007f, #ff00aa);
            border: none; border-radius: 50px; color: #fff;
            font-weight: bold; font-size: 15px; cursor: pointer;
            transition: all 0.3s; box-shadow: 0 10px 35px rgba(255,0,127,0.5);
        }}
        button:hover {{ transform: translateY(-2px); box-shadow: 0 20px 50px rgba(255,0,127,0.7); }}
        button:active {{ transform: scale(0.97); }}
        button:disabled {{ opacity: 0.5; pointer-events: none; }}
        .msg {{ text-align: center; color: #fca5a5; font-size: 13px; margin-top: 12px; min-height: 20px; }}
        .msg.success {{ color: #4ade80; }}
    </style>
</head>
<body>
    <div class="bg-orb"></div><div class="bg-orb"></div><div class="bg-orb"></div>
    <div class="card">
        <div class="logo">💜</div>
        <h1>VØID_X</h1>
        <p class="sub">Neon Glass Supreme ✨</p>
        <div class="tabs">
            <button class="tab active" id="tabLogin" onclick="switchTab('login')"><i class="fas fa-sign-in-alt"></i> دخول</button>
            <button class="tab" id="tabRegister" onclick="switchTab('register')"><i class="fas fa-user-plus"></i> اشتراك</button>
        </div>
        <div id="formLogin" class="form active">
            <input type="email" id="loginEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email" dir="ltr">
            <input type="password" id="loginPass" placeholder="🔒 كلمة المرور" autocomplete="current-password">
            <button id="btnLogin" onclick="doLogin()"><i class="fas fa-arrow-right-to-bracket"></i> تسجيل الدخول</button>
            <div class="msg" id="loginMsg"></div>
        </div>
        <div id="formRegister" class="form">
            <input type="text" id="regName" placeholder="👤 اسم المستخدم">
            <input type="email" id="regEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email" dir="ltr">
            <input type="password" id="regPass" placeholder="🔒 كلمة المرور (6 أحرف على الأقل)" autocomplete="new-password">
            <button id="btnRegister" onclick="doRegister()"><i class="fas fa-heart"></i> إنشاء حساب</button>
            <div class="msg" id="regMsg"></div>
        </div>
    </div>
    <script src="firebase-config.js"></script>
    <script>
        function switchTab(type) {{
            document.getElementById('tabLogin').classList.remove('active');
            document.getElementById('tabRegister').classList.remove('active');
            document.getElementById('formLogin').classList.remove('active');
            document.getElementById('formRegister').classList.remove('active');
            document.getElementById('loginMsg').innerText = '';
            document.getElementById('regMsg').innerText = '';
            if(type === 'login') {{
                document.getElementById('tabLogin').classList.add('active');
                document.getElementById('formLogin').classList.add('active');
            }} else {{
                document.getElementById('tabRegister').classList.add('active');
                document.getElementById('formRegister').classList.add('active');
            }}
        }}

        async function doLogin() {{
            const email = document.getElementById('loginEmail').value.trim();
            const password = document.getElementById('loginPass').value;
            const msg = document.getElementById('loginMsg');
            const btn = document.getElementById('btnLogin');
            if(!email || !password) {{ msg.innerText = '❌ الرجاء ملء جميع الحقول'; return; }}
            btn.disabled = true; btn.innerHTML = '⏳ جاري الدخول...'; msg.innerText = ''; msg.className = 'msg';
            try {{
                await auth.signInWithEmailAndPassword(email, password);
                window.location.replace('index.html');
            }} catch(error) {{
                btn.disabled = false; btn.innerHTML = '<i class="fas fa-arrow-right-to-bracket"></i> تسجيل الدخول';
                switch(error.code) {{
                    case 'auth/user-not-found': msg.innerText = '❌ لا يوجد حساب بهذا البريد'; break;
                    case 'auth/wrong-password': case 'auth/invalid-credential': msg.innerText = '❌ كلمة المرور غير صحيحة'; break;
                    case 'auth/invalid-email': msg.innerText = '❌ بريد إلكتروني غير صالح'; break;
                    case 'auth/too-many-requests': msg.innerText = '❌ محاولات كثيرة، حاول لاحقاً'; break;
                    default: msg.innerText = '❌ خطأ: ' + error.message;
                }}
            }}
        }}

        async function doRegister() {{
            const username = document.getElementById('regName').value.trim();
            const email = document.getElementById('regEmail').value.trim();
            const password = document.getElementById('regPass').value;
            const msg = document.getElementById('regMsg');
            const btn = document.getElementById('btnRegister');
            if(!username || !email || !password) {{ msg.innerText = '❌ الرجاء ملء جميع الحقول'; return; }}
            if(username.length < 3) {{ msg.innerText = '❌ اسم المستخدم 3 أحرف على الأقل'; return; }}
            if(password.length < 6) {{ msg.innerText = '❌ كلمة المرور 6 أحرف على الأقل'; return; }}
            if(!email.includes('@') || !email.includes('.')) {{ msg.innerText = '❌ بريد إلكتروني غير صالح'; return; }}
            btn.disabled = true; btn.innerHTML = '⏳ جاري إنشاء الحساب...'; msg.innerText = ''; msg.className = 'msg';
            try {{
                const userCredential = await auth.createUserWithEmailAndPassword(email, password);
                const uid = userCredential.user.uid;
                const avatarUrl = DICEBEAR_URL + '?seed=' + uid;
                const coverColor = COVER_COLORS[Math.floor(Math.random() * COVER_COLORS.length)];
                const userData = {{
                    username: username, email: email, bio: '',
                    website: '', location: '', contactEmail: '',
                    avatarUrl: avatarUrl, hasCustomAvatar: false,
                    coverImageUrl: '', hasCustomCover: false,
                    coverColor: coverColor, followers: {{}}, following: {{}},
                    totalLikes: 0, isVerified: false, verifiedAt: null, verifiedBy: null,
                    banned: false, createdAt: Date.now(), lastSeen: Date.now()
                }};
                await db.ref('users/' + uid).set(userData);
                msg.innerText = '✅ تم إنشاء الحساب بنجاح! جاري التوجيه...';
                msg.className = 'msg success';
                setTimeout(() => {{ window.location.replace('index.html'); }}, 800);
            }} catch(error) {{
                btn.disabled = false; btn.innerHTML = '<i class="fas fa-heart"></i> إنشاء حساب'; msg.className = 'msg';
                switch(error.code) {{
                    case 'auth/email-already-in-use': msg.innerText = '❌ البريد الإلكتروني مستخدم بالفعل'; break;
                    case 'auth/weak-password': msg.innerText = '❌ كلمة المرور ضعيفة جداً'; break;
                    case 'auth/invalid-email': msg.innerText = '❌ بريد إلكتروني غير صالح'; break;
                    case 'auth/operation-not-allowed': msg.innerText = '❌ التسجيل غير مفعل'; break;
                    default: msg.innerText = '❌ خطأ: ' + error.message;
                }}
            }}
        }}

        document.querySelectorAll('input').forEach(input => {{
            input.addEventListener('keydown', function(e) {{
                if(e.key === 'Enter') {{
                    e.preventDefault();
                    if(document.getElementById('formLogin').classList.contains('active')) {{ doLogin(); }}
                    else {{ doRegister(); }}
                }}
            }});
        }});

        auth.onAuthStateChanged(user => {{
            if(user) {{ window.location.replace('index.html'); }}
        }});

        console.log('💜 VØID_X Auth Ready');
    </script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 3. index.html - VØID_X Main Feed (UPDATED BOTTOM NAV)
# ═══════════════════════════════════════════════════════════

def build_index():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>💜 VØID_X | الرئيسية</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body {{ height: 100vh; }}

        #loaderScreen {{
            position: fixed; inset: 0; z-index: 9999;
            background: radial-gradient(ellipse at top, #1a000d, #0d0015, #050002);
            display: flex; align-items: center; justify-content: center;
            flex-direction: column; gap: 16px;
        }}
        .spinner-big {{
            width: 50px; height: 50px;
            border: 4px solid rgba(255,0,127,0.2);
            border-top-color: var(--neon);
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
        }}

        #mainApp {{ display: none; height: 100vh; position: relative; }}

        header {{
            position: fixed; top: 25px; left: 20px; right: 20px; z-index: 500;
            display: flex; justify-content: space-between; align-items: center;
            pointer-events: none;
        }}
        .brand-box {{
            padding: 8px 22px; border-radius: 20px;
            border-left: 4px solid var(--neon);
            background: rgba(255,255,255,0.03); backdrop-filter: blur(15px);
            border: 1px solid rgba(255,255,255,0.1);
            pointer-events: auto;
        }}
        .brand-name {{
            font-family: 'Orbitron', sans-serif; font-weight: 900;
            letter-spacing: 2px; color: #fff;
            text-shadow: 0 0 15px var(--neon);
        }}
        .clock {{
            font-family: 'Orbitron', sans-serif; font-size: 11px;
            color: rgba(255,255,255,0.8); padding: 6px 16px;
            border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);
            background: rgba(255,255,255,0.03); backdrop-filter: blur(10px);
        }}

        .videos-wrap {{
            height: 100vh; overflow-y: scroll;
            scroll-snap-type: y mandatory;
            scrollbar-width: none; -ms-overflow-style: none;
        }}
        .videos-wrap::-webkit-scrollbar {{ display: none; }}
        .vid-card {{
            height: 100vh; width: 100vw; scroll-snap-align: start;
            scroll-snap-stop: always; position: relative; overflow: hidden;
            background: #000;
        }}
        .vid-card video {{
            width: 100%; height: 100%; object-fit: cover;
            opacity: 0; transform: translateY(60px);
            transition: opacity 0.6s ease, transform 0.6s cubic-bezier(0.16,1,0.3,1);
        }}
        .vid-card.active video {{ opacity: 1; transform: translateY(0); }}

        .watermark-overlay {{
            position: absolute; top: 20%; right: 10%;
            font-family: 'Orbitron', sans-serif; font-size: 0.8rem;
            color: rgba(255,255,255,0.15); z-index: 20;
            letter-spacing: 4px; animation: floatMark 10s infinite;
            text-shadow: 0 0 5px var(--neon);
        }}

        .side-actions {{
            position: absolute; left: 20px; bottom: 180px;
            display: flex; flex-direction: column; gap: 15px; z-index: 100;
        }}
        .action-btn {{
            width: 55px; height: 55px; border-radius: 20px;
            display: flex; flex-direction: column; align-items: center;
            justify-content: center;
            background: rgba(255,255,255,0.05); backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.1);
            transition: 0.3s;
        }}
        .action-btn i {{
            font-size: 1.3rem; color: var(--neon);
            filter: drop-shadow(0 0 8px var(--neon)); transition: 0.3s;
        }}
        .btn-label {{
            font-size: 9px; font-weight: bold; margin-top: 2px;
            color: #fff; opacity: 0.7; font-family: 'Orbitron', sans-serif;
        }}
        .action-btn.liked i {{ color: #fff; filter: drop-shadow(0 0 15px var(--neon)); animation: likePop 0.4s ease; }}
        @keyframes likePop {{
            0% {{ transform: scale(1); }} 50% {{ transform: scale(1.4); }} 100% {{ transform: scale(1); }}
        }}

        /* ===== UPDATED BOTTOM NAV ===== */
        nav {{
            position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%);
            width: 92%; max-width: 450px; height: 70px; border-radius: 35px;
            background: rgba(5, 0, 10, 0.5); backdrop-filter: blur(30px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            display: flex; justify-content: space-around; align-items: center;
            z-index: 200; padding: 0 5px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8), 0 0 30px rgba(255, 0, 127, 0.1);
        }}
        .nav-item {{
            display: flex; flex-direction: column; align-items: center;
            justify-content: center; gap: 4px; cursor: pointer;
            transition: all 0.3s ease; padding: 10px 12px; border-radius: 20px;
            position: relative; color: rgba(255, 255, 255, 0.5);
            min-width: 55px; text-decoration: none;
        }}
        .nav-item i {{
            font-size: 1.5rem; transition: all 0.3s ease;
            filter: drop-shadow(0 0 5px transparent);
        }}
        .nav-item span {{
            font-size: 9px; font-weight: 700; letter-spacing: 0.5px;
            font-family: 'Orbitron', sans-serif; transition: all 0.3s ease;
        }}
        .nav-item.active {{
            color: var(--neon);
            text-shadow: 0 0 15px var(--neon);
        }}
        .nav-item.active i {{
            filter: drop-shadow(0 0 10px var(--neon));
        }}
        .nav-item.active span {{
            opacity: 1;
        }}
        /* Center Upload Button */
        #upload-nav-btn {{
            background: var(--neon); box-shadow: 0 0 30px var(--neon);
            cursor: pointer; width: 65px; height: 65px; border-radius: 22px;
            display: flex; align-items: center; justify-content: center;
            transform: translateY(-18px); border: 4px solid var(--bg);
            color: #fff; font-size: 1.6rem; transition: all 0.3s ease;
            margin: 0 5px;
        }}
        #upload-nav-btn:hover {{
            box-shadow: 0 0 45px var(--neon); transform: translateY(-20px) scale(1.05);
        }}
        #upload-nav-btn i {{
            filter: drop-shadow(0 0 10px #fff);
        }}

        /* Notification Badge */
        .notification-badge {{
            position: absolute; top: 0; right: 5px;
            background: #ff0040; color: #fff; font-size: 9px;
            font-weight: bold; width: 18px; height: 18px;
            border-radius: 50%; display: flex; align-items: center;
            justify-content: center; border: 2px solid var(--bg);
            box-shadow: 0 0 10px rgba(255, 0, 64, 0.7);
            font-family: 'Orbitron', sans-serif;
        }}
    </style>
</head>
<body>

<div id="loaderScreen">
    <div class="spinner-big"></div>
    <p style="color: rgba(255,255,255,0.5); font-size: 15px; font-family: 'Orbitron';">💜 VØID_X LOADING...</p>
</div>

<div id="mainApp">
    <header>
        <div class="brand-box"><span class="brand-name">VØID_X</span></div>
        <div class="clock" id="clock">00:00:00</div>
    </header>

    <div class="videos-wrap" id="videosWrap">
        <div style="display: flex; align-items: center; justify-content: center; height: 100vh; color: rgba(255,255,255,0.5); flex-direction: column; gap: 12px;">
            <i class="fas fa-video" style="font-size: 48px; opacity: 0.3; color: var(--neon);"></i>
            <p>لا توجد فيديوهات بعد</p>
            <p style="font-size: 12px; opacity: 0.5;">ارفع أول فيديو! 💜</p>
        </div>
    </div>

    <!-- Fullscreen Player -->
    <div class="fullscreen-player" id="fullscreenPlayer" onclick="if(event.target===this)closePlayer()">
        <button class="close-player" onclick="closePlayer()"><i class="fas fa-times"></i></button>
        <video id="fullscreenVideo" controls playsinline></video>
    </div>

    <!-- Share Panel -->
    <div class="share-panel" id="sharePanel">
        <h3 style="text-align:center;margin-bottom:15px;color:var(--neon)"><i class="fas fa-share-alt"></i> مشاركة</h3>
        <div class="share-grid" style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:20px;">
            <div class="share-item" onclick="shareTo('whatsapp')"><div class="share-icon" style="width:56px;height:56px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:24px;background:rgba(37,211,102,0.15);color:#25D366;margin:0 auto;"><i class="fab fa-whatsapp"></i></div><span style="font-size:11px;">WhatsApp</span></div>
            <div class="share-item" onclick="shareTo('telegram')"><div class="share-icon" style="width:56px;height:56px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:24px;background:rgba(0,136,204,0.15);color:#0088cc;margin:0 auto;"><i class="fab fa-telegram"></i></div><span style="font-size:11px;">Telegram</span></div>
            <div class="share-item" onclick="shareTo('facebook')"><div class="share-icon" style="width:56px;height:56px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:24px;background:rgba(24,119,242,0.15);color:#1877F2;margin:0 auto;"><i class="fab fa-facebook"></i></div><span style="font-size:11px;">Facebook</span></div>
            <div class="share-item" onclick="shareTo('copy')"><div class="share-icon" style="width:56px;height:56px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:24px;background:rgba(255,0,127,0.15);color:#ff007f;margin:0 auto;"><i class="fas fa-link"></i></div><span style="font-size:11px;">نسخ الرابط</span></div>
        </div>
        <div style="display:flex;gap:8px;background:rgba(255,255,255,0.05);border-radius:16px;padding:8px;border:1px solid rgba(255,255,255,0.1);">
            <input type="text" id="shareUrlInput" value="" readonly dir="ltr" style="flex:1;padding:12px;border-radius:12px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;font-size:13px;outline:none;">
            <button onclick="shareTo('copy')" style="background:linear-gradient(135deg, #ff007f, #ff00aa);border:none;color:#fff;padding:12px 20px;border-radius:12px;font-weight:700;cursor:pointer;box-shadow:0 0 20px rgba(255,0,127,0.4);"><i class="fas fa-copy"></i> نسخ</button>
        </div>
    </div>
    <div class="overlay" id="shareOverlay" style="display:none;z-index:499" onclick="closeSharePanel()"></div>

    <!-- Comments Panel -->
    <div class="comments-panel" id="commentsPanel" style="position:fixed;bottom:0;left:0;right:0;background:rgba(5,0,2,0.98);backdrop-filter:blur(40px);border-top:2px solid var(--neon);border-radius:24px 24px 0 0;z-index:500;max-height:70vh;display:flex;flex-direction:column;transform:translateY(100%);transition:transform 0.4s cubic-bezier(0.4,0,0.2,1);">
        <div class="comments-header" style="display:flex;justify-content:space-between;align-items:center;padding:16px 20px;border-bottom:1px solid rgba(255,255,255,0.1);">
            <h3 style="color:#fff"><i class="fas fa-comments" style="color:var(--neon)"></i> التعليقات <span id="commentsCount" style="font-size:13px;opacity:0.5"></span></h3>
            <button class="btn-close-overlay" onclick="closeCommentsPanel()"><i class="fas fa-times"></i></button>
        </div>
        <div class="comments-list" id="commentsList" style="flex:1;overflow-y:auto;padding:12px 16px;"></div>
        <div class="comment-input-row" style="display:flex;gap:8px;padding:12px 16px;border-top:1px solid rgba(255,255,255,0.1);background:rgba(5,0,2,0.95);">
            <input type="text" id="commentInput" placeholder="أضف تعليقاً..." onkeydown="if(event.key==='Enter')addComment()" style="flex:1;padding:12px 16px;border-radius:30px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;font-size:13px;outline:none;">
            <button onclick="addComment()" style="background:linear-gradient(135deg, #ff007f, #ff00aa);border:none;color:#fff;padding:10px 18px;border-radius:30px;font-weight:700;cursor:pointer;white-space:nowrap;"><i class="fas fa-paper-plane"></i> نشر</button>
        </div>
    </div>
    <div class="overlay" id="commentsOverlay" style="display:none;z-index:499" onclick="closeCommentsPanel()"></div>

    <!-- ===== UPDATED BOTTOM NAVIGATION ===== -->
    <nav id="main-nav">
        <div class="nav-item" id="nav-profile" onclick="window.location.href='profile.html'">
            <i class="fas fa-user"></i>
            <span>PROFILE</span>
        </div>
        <div class="nav-item" id="nav-chat" onclick="window.location.href='chat.html'">
            <i class="fas fa-comment-dots"></i>
            <span>CHAT</span>
        </div>
        <div id="upload-nav-btn" onclick="window.location.href='upload.html'">
            <i class="fas fa-plus"></i>
        </div>
        <div class="nav-item" id="nav-explore" onclick="window.location.href='explore.html'">
            <i class="fas fa-compass"></i>
            <span>EXPLORE</span>
        </div>
        <div class="nav-item" id="nav-notifications" onclick="window.location.href='notifications.html'">
            <i class="fas fa-bell"></i>
            <span>ALERTS</span>
            <span class="notification-badge" id="notifBadge" style="display:none;">0</span>
        </div>
    </nav>

    <div class="toast-msg" id="toast">✅ تم</div>
</div>

<script src="firebase-config.js"></script>
<script>
    let currentUser = null, currentUserData = null, allUsers = {{}}, allVideos = [], isMuted = true;
    let currentShareUrl = null, currentCommentVideoId = null;

    function closePlayer() {{
        const player = document.getElementById('fullscreenPlayer');
        const video = document.getElementById('fullscreenVideo');
        video.pause(); video.src=''; player.classList.remove('active');
    }}

    function openSharePanel(url) {{
        currentShareUrl = url;
        document.getElementById('shareUrlInput').value = url;
        document.getElementById('sharePanel').classList.add('show');
        document.getElementById('shareOverlay').style.display = 'block';
    }}
    function closeSharePanel() {{
        document.getElementById('sharePanel').classList.remove('show');
        document.getElementById('shareOverlay').style.display = 'none';
    }}
    function shareTo(platform) {{
        const url = encodeURIComponent(currentShareUrl);
        const text = encodeURIComponent('شاهد هذا الفيديو على VØID_X 💜');
        let shareUrl = '';
        switch(platform) {{
            case 'whatsapp': shareUrl = 'https://wa.me/?text=' + text + '%20' + url; break;
            case 'telegram': shareUrl = 'https://t.me/share/url?url=' + url + '&text=' + text; break;
            case 'facebook': shareUrl = 'https://www.facebook.com/sharer/sharer.php?u=' + url; break;
            case 'copy':
                navigator.clipboard.writeText(currentShareUrl).then(() => {{
                    showToast('✅ تم نسخ الرابط');
                    closeSharePanel();
                }});
                return;
        }}
        if(shareUrl) window.open(shareUrl, '_blank');
        closeSharePanel();
    }}

    async function openCommentsPanel(videoId) {{
        currentCommentVideoId = videoId;
        document.getElementById('commentsPanel').style.transform = 'translateY(0)';
        document.getElementById('commentsOverlay').style.display = 'block';
        await loadComments();
    }}
    function closeCommentsPanel() {{
        document.getElementById('commentsPanel').style.transform = 'translateY(100%)';
        document.getElementById('commentsOverlay').style.display = 'none';
        currentCommentVideoId = null;
    }}
    async function loadComments() {{
        if(!currentCommentVideoId) return;
        const snap = await db.ref('videos/' + currentCommentVideoId + '/comments').get();
        const comments = snap.val() || {{}};
        const commentsArr = Object.entries(comments).map(([id, c]) => ({{id, ...c}}));
        commentsArr.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
        document.getElementById('commentsCount').innerText = '(' + commentsArr.length + ')';
        const list = document.getElementById('commentsList');
        if(!commentsArr.length) {{
            list.innerHTML = '<div style="text-align:center;opacity:0.5;padding:30px"><i class="fas fa-comment-slash" style="font-size:32px;color:var(--neon);margin-bottom:8px;display:block"></i>لا توجد تعليقات</div>';
            return;
        }}
        list.innerHTML = commentsArr.map(c => {{
            const user = allUsers[c.userId] || {{username: c.username || 'مستخدم'}};
            const avatar = user.avatarUrl || (DICEBEAR_URL + '?seed=' + c.userId);
            return `<div style="display:flex;gap:10px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,0.05);"><div style="width:36px;height:36px;border-radius:50%;overflow:hidden;flex-shrink:0;border:2px solid rgba(255,0,127,0.3);"><img src="${{avatar}}" style="width:100%;height:100%;object-fit:cover;"></div><div style="flex:1;min-width:0;"><div style="font-weight:600;font-size:13px;color:#fff;">@${{user.username}} ${{user.isVerified ? '<span style="color:var(--neon);font-size:10px"><i class="fas fa-check-circle"></i></span>' : ''}}</div><div style="font-size:13px;color:rgba(255,255,255,0.8);">${{c.text}}</div></div></div>`;
        }}).join('');
    }}
    async function addComment() {{
        const input = document.getElementById('commentInput');
        const text = input.value.trim();
        if(!text || !currentCommentVideoId || !currentUser) return;
        const commentData = {{
            userId: currentUser.uid,
            username: currentUserData?.username || 'مستخدم',
            text: text,
            timestamp: Date.now()
        }};
        await db.ref('videos/' + currentCommentVideoId + '/comments').push(commentData);
        input.value = '';
        await loadComments();
    }}

    auth.onAuthStateChanged(async (user) => {{
        if(!user) {{ window.location.replace('auth.html'); return; }}
        currentUser = user;
        try {{
            const snap = await db.ref('users/' + user.uid).get();
            if(snap.exists()) currentUserData = {{uid: user.uid, ...snap.val()}};
        }} catch(e) {{ console.error('Error loading user:', e); }}

        db.ref('users').on('value', s => {{ allUsers = s.val() || {{}}; }});
        db.ref('videos').on('value', s => {{
            const data = s.val();
            if(!data) {{ allVideos = []; }}
            else {{
                allVideos = Object.entries(data).map(([key, value]) => ({{id: key, ...value}}));
                allVideos.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
            }}
            renderVideos();
        }});

        // Check notifications
        db.ref('notifications/' + user.uid).on('value', s => {{
            const ns = s.val() || {{}};
            const unread = Object.values(ns).filter(n => !n.read).length;
            const badge = document.getElementById('notifBadge');
            if(unread > 0) {{
                badge.style.display = 'flex';
                badge.innerText = unread > 99 ? '99+' : unread;
            }} else {{
                badge.style.display = 'none';
            }}
        }});

        db.ref('presence/' + user.uid).set(true);
        db.ref('presence/' + user.uid).onDisconnect().remove();
        db.ref('users/' + user.uid + '/lastSeen').set(Date.now());

        document.getElementById('loaderScreen').style.display = 'none';
        document.getElementById('mainApp').style.display = 'block';
    }});

    function renderVideos() {{
        const container = document.getElementById('videosWrap');
        if(!container) return;
        if(!allVideos.length) {{
            container.innerHTML = '<div style="display:flex;align-items:center;justify-content:center;height:100vh;color:rgba(255,255,255,0.5);flex-direction:column;gap:12px"><i class="fas fa-video" style="font-size:48px;opacity:0.3;color:var(--neon)"></i><p>لا توجد فيديوهات بعد</p></div>';
            return;
        }}
        container.innerHTML = '';
        allVideos.forEach(video => {{
            const isLiked = video.likedBy && video.likedBy[currentUser?.uid];
            const commentsCount = video.comments ? Object.keys(video.comments).length : 0;
            const div = document.createElement('div');
            div.className = 'vid-card';
            div.innerHTML = `
                <div class="watermark-overlay">VØID_X SUPREME</div>
                <video loop playsinline muted data-src="${{video.url}}" poster="${{video.thumbnail || ''}}"></video>
                <div class="side-actions">
                    <div class="action-btn ${{isLiked ? 'liked' : ''}}" onclick="toggleLike('${{video.id}}', this)">
                        <i class="fas fa-bolt"></i>
                        <span class="btn-label">${{video.likes || 0}}</span>
                    </div>
                    <div class="action-btn" onclick="openCommentsPanel('${{video.id}}')">
                        <i class="fas fa-terminal"></i>
                        <span class="btn-label">${{commentsCount}}</span>
                    </div>
                    <div class="action-btn" onclick="openSharePanel('${{video.url}}')">
                        <i class="fas fa-share-nodes"></i>
                        <span class="btn-label">SEND</span>
                    </div>
                </div>`;
            const videoEl = div.querySelector('video');
            videoEl.addEventListener('dblclick', e => {{
                e.stopPropagation();
                const likeBtn = div.querySelector('.action-btn');
                if(likeBtn) toggleLike(video.id, likeBtn);
            }});
            container.appendChild(div);
        }});
        initObserver();
    }}

    function initObserver() {{
        const observer = new IntersectionObserver(entries => {{
            entries.forEach(entry => {{
                const video = entry.target.querySelector('video');
                if(entry.isIntersecting) {{
                    entry.target.classList.add('active');
                    if(!video.src) video.src = video.dataset.src;
                    video.muted = isMuted;
                    video.play().catch(() => {{}});
                }} else {{
                    entry.target.classList.remove('active');
                    video.pause();
                }}
            }});
        }}, {{threshold: 0.65}});
        document.querySelectorAll('.vid-card').forEach(seg => observer.observe(seg));
    }}

    async function toggleLike(videoId, btn) {{
        if(!currentUser) return;
        const ref = db.ref('videos/' + videoId);
        const snap = await ref.get();
        const video = snap.val();
        if(!video) return;
        let likes = video.likes || 0;
        let likedBy = video.likedBy || {{}};
        if(likedBy[currentUser.uid]) {{ likes--; delete likedBy[currentUser.uid]; }}
        else {{ likes++; likedBy[currentUser.uid] = true; }}
        await ref.update({{likes, likedBy}});
        btn.classList.toggle('liked');
        const lbl = btn.querySelector('.btn-label');
        if(lbl) lbl.innerText = likes;
    }}

    function showToast(msg) {{
        const toast = document.getElementById('toast');
        toast.innerText = msg;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2500);
    }}

    window.closePlayer = closePlayer;
    window.openSharePanel = openSharePanel;
    window.closeSharePanel = closeSharePanel;
    window.shareTo = shareTo;
    window.openCommentsPanel = openCommentsPanel;
    window.closeCommentsPanel = closeCommentsPanel;
    window.toggleLike = toggleLike;
    window.addComment = addComment;

    setInterval(() => {{ document.getElementById('clock').innerText = new Date().toLocaleTimeString('en-GB'); }}, 1000);

    console.log('💜 VØID_X v2 Ready');
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 4. profile.html - ADMIN DASHBOARD
# ═══════════════════════════════════════════════════════════

def build_profile():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💜 VØID_X | ملفي</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body {{ min-height: 100vh; overflow-y: auto; }}
        .cover-section {{ position: relative; width: 100%; height: 260px; overflow: hidden; background: linear-gradient(135deg, #1a000d, #2d0020); }}
        .cover-img {{ width: 100%; height: 130%; object-fit: cover; }}
        .cover-gradient {{ position: absolute; inset: 0; background: linear-gradient(to bottom, transparent 30%, rgba(5,0,2,0.5) 60%, rgba(5,0,2,0.97) 100%); }}
        .avatar-wrap {{ display: flex; justify-content: center; margin-top: -60px; z-index: 2; position: relative; }}
        .avatar-lg {{
            width: 120px; height: 120px; border-radius: 50%; overflow: hidden;
            background: linear-gradient(135deg, #ff007f, #ff00aa);
            padding: 3px; box-shadow: 0 0 35px rgba(255,0,127,0.5);
            animation: glowPulse 3s ease-in-out infinite;
        }}
        .avatar-lg img {{ width: 100%; height: 100%; object-fit: cover; border-radius: 50%; border: 3px solid var(--bg); }}
        .profile-info {{ padding: 20px; text-align: center; }}
        .username {{ font-size: 22px; font-weight: 800; color: #fff; }}
        .stats-row {{ display: flex; justify-content: center; gap: 30px; margin: 15px; padding: 18px; background: rgba(255,255,255,0.05); border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); }}
        .stat-item {{ text-align: center; }}
        .stat-val {{ font-size: 20px; font-weight: 700; color: var(--neon); }}
        .videos-grid {{ display: grid; grid-template-columns: repeat(3,1fr); gap: 2px; padding: 0 8px 100px; }}
        .video-grid-item {{ aspect-ratio: 9/16; background: #000; overflow: hidden; border-radius: 4px; cursor: pointer; }}
        .video-grid-item img {{ width: 100%; height: 100%; object-fit: cover; }}
        .btn {{
            background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);
            padding: 10px 20px; border-radius: 25px; color: #fff; cursor: pointer; font-size: 13px;
            transition: all 0.3s; margin: 5px;
        }}
        .btn-primary {{ background: linear-gradient(135deg, #ff007f, #ff00aa); border: none; font-weight: 700; box-shadow: 0 0 20px rgba(255,0,127,0.4); }}
        .btn-danger {{ background: rgba(255,0,0,0.2); border-color: #ff0000; color: #ff4444; }}
        .btn-success {{ background: rgba(0,255,0,0.2); border-color: #00ff00; color: #4ade80; }}
        .admin-panel {{
            padding: 20px 8px; margin: 0 8px 100px 8px;
        }}
        .stat-card {{
            background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);
            border-radius: 20px; padding: 20px; text-align: center;
        }}
        .admin-section {{
            background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px; padding: 16px; margin-bottom: 16px;
        }}
        .admin-user-item {{
            display: flex; align-items: center; justify-content: space-between;
            padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05);
            gap: 10px;
        }}
        .admin-actions {{ display: flex; gap: 8px; }}
        .admin-actions button {{
            padding: 6px 12px; border-radius: 15px; font-size: 11px; border: none; cursor: pointer;
            font-weight: bold;
        }}
        .verify-btn {{ background: #4ade80; color: #000; }}
        .ban-btn {{ background: #ff4444; color: #fff; }}
        .unban-btn {{ background: #fbbf24; color: #000; }}
        .delete-btn {{ background: #ff0000; color: #fff; }}
    </style>
</head>
<body>
<div id="loader" style="display:flex;align-items:center;justify-content:center;min-height:80vh;"><div class="spinner"></div></div>
<div id="content" style="display:none">
    <div class="cover-section" id="coverSection"><img class="cover-img" id="coverImg" src="" style="display:none"><div class="cover-gradient"></div></div>
    <button onclick="window.location.href='index.html'" style="position:fixed;top:20px;right:20px;z-index:50;background:rgba(0,0,0,0.5);width:40px;height:40px;border-radius:50%;border:1px solid rgba(255,255,255,0.2);color:#fff;font-size:16px;"><i class="fas fa-home"></i></button>
    <div class="avatar-wrap"><div class="avatar-lg"><img id="avatarImg" src=""></div></div>
    <div class="profile-info">
        <div class="username" id="nameDisplay"></div>
        <div class="bio-text" id="bioDisplay" style="opacity:0.7"></div>
    </div>
    <div class="stats-row">
        <div class="stat-item"><div class="stat-val" id="statFollowing">0</div><div class="stat-lbl">يتابع</div></div>
        <div class="stat-item"><div class="stat-val" id="statFollowers">0</div><div class="stat-lbl">متابع</div></div>
        <div class="stat-item"><div class="stat-val" id="statLikes">0</div><div class="stat-lbl">إعجابات</div></div>
    </div>
    <div style="text-align:center" id="actionsBar"></div>
    <div class="videos-grid" id="videosGrid"></div>
    <div id="adminDashboard" style="display:none"></div>
</div>
<div class="toast-msg" id="toastMsg">✅ تم</div>

<script src="firebase-config.js"></script>
<script>
    let profileUserId = null, currentUser = null, allVideos = [], allUsers = {{}}, isOwnProfile = false, isAdmin = false;

    auth.onAuthStateChanged(async u => {{
        if(!u) {{ window.location.href = 'auth.html'; return; }}
        currentUser = u;
        const params = new URLSearchParams(window.location.search);
        profileUserId = params.get('uid') || u.uid;
        isOwnProfile = (profileUserId === u.uid);
        isAdmin = ADMIN_EMAILS.includes(u.email);
        
        await loadAll(); await loadProfile();
        
        if(isOwnProfile && isAdmin) {{
            document.getElementById('adminDashboard').style.display = 'block';
            loadAdminPanel();
        }}
        
        document.getElementById('loader').style.display = 'none'; 
        document.getElementById('content').style.display = 'block';
    }});

    async function loadAll() {{
        const us = await db.ref('users').once('value'); allUsers = us.val() || {{}};
        const vs = await db.ref('videos').once('value'); 
        allVideos = Object.entries(vs.val() || {{}}).map(([k, v]) => ({{id: k, ...v}}));
    }}

    async function loadProfile() {{
        const u = allUsers[profileUserId];
        if(!u) return;
        document.getElementById('nameDisplay').innerHTML = '@' + (u.username || 'مستخدم') + (u.isVerified ? ' <i class="fas fa-check-circle" style="color:#ff007f"></i>' : '');
        document.getElementById('bioDisplay').innerText = u.bio || 'VØID_X Member';
        document.getElementById('statFollowing').innerText = Object.keys(u.following || {{}}).length;
        document.getElementById('statFollowers').innerText = Object.keys(u.followers || {{}}).length;
        const uvs = allVideos.filter(v => v.sender === profileUserId);
        document.getElementById('statLikes').innerText = uvs.reduce((s, v) => s + (v.likes || 0), 0);
        if(u.coverImageUrl) {{ document.getElementById('coverImg').src = u.coverImageUrl; document.getElementById('coverImg').style.display = 'block'; }}
        else {{ document.getElementById('coverSection').style.background = u.coverColor || COVER_COLORS[0]; }}
        document.getElementById('avatarImg').src = u.avatarUrl || (DICEBEAR_URL + '?seed=' + profileUserId);
        const grid = document.getElementById('videosGrid');
        grid.innerHTML = uvs.length ? uvs.map(v => `<div class="video-grid-item" onclick="window.open('${{v.url}}','_blank')">${{v.thumbnail ? `<img src="${{v.thumbnail}}">` : ''}}</div>`).join('') : '<div style="grid-column:1/-1;text-align:center;padding:40px;opacity:0.5">لا فيديوهات</div>';
        if(isOwnProfile) {{
            document.getElementById('actionsBar').innerHTML = `<button class="btn btn-primary" onclick="window.location.href='settings.html'"><i class="fas fa-cog"></i> إعدادات</button><button class="btn" onclick="auth.signOut();window.location.href='auth.html'"><i class="fas fa-sign-out-alt"></i> خروج</button>`;
        }}
    }}

    function loadAdminPanel() {{
        const adminDiv = document.getElementById('adminDashboard');
        const totalUsers = Object.keys(allUsers).length;
        const totalVideos = allVideos.length;
        const verifiedUsers = Object.values(allUsers).filter(u => u.isVerified).length;
        const bannedUsers = Object.values(allUsers).filter(u => u.banned).length;

        let usersHTML = Object.entries(allUsers).slice(0, 20).map(([uid, u]) => `
            <div class="admin-user-item">
                <div style="display:flex;align-items:center;gap:10px;flex:1">
                    <img src="${{u.avatarUrl || (DICEBEAR_URL + '?seed=' + uid)}}" style="width:35px;height:35px;border-radius:50%">
                    <div>
                        <div style="font-weight:600">@${{u.username || 'مستخدم'}} ${{u.isVerified ? '<span style="color:#4ade80"><i class="fas fa-check-circle"></i></span>' : ''}} ${{u.banned ? '<span style="color:#ff4444">(محظور)</span>' : ''}}</div>
                        <div style="font-size:11px;opacity:0.6">${{u.email || ''}}</div>
                    </div>
                </div>
                <div class="admin-actions">
                    ${{!u.isVerified ? `<button class="verify-btn" onclick="verifyUser('${{uid}}')"><i class="fas fa-check"></i> توثيق</button>` : ''}}
                    ${{u.banned ? `<button class="unban-btn" onclick="unbanUser('${{uid}}')"><i class="fas fa-unlock"></i> فك حظر</button>` : `<button class="ban-btn" onclick="banUser('${{uid}}')"><i class="fas fa-ban"></i> حظر</button>`}}
                </div>
            </div>
        `).join('');

        let videosHTML = allVideos.slice(0, 10).map(v => `
            <div class="admin-user-item">
                <video src="${{v.url}}" style="width:50px;height:70px;object-fit:cover;border-radius:8px"></video>
                <span style="flex:1;font-size:13px">${{(v.description||'بدون وصف').substring(0,40)}}</span>
                <button class="delete-btn" onclick="deleteVideo('${{v.id}}')"><i class="fas fa-trash"></i> حذف</button>
            </div>
        `).join('');

        adminDiv.innerHTML = `
            <div class="admin-panel">
                <h2 style="color:var(--neon);text-align:center;font-family:'Orbitron';text-shadow:0 0 15px var(--neon);">👑 ADMIN DASHBOARD</h2>
                <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-bottom:20px;">
                    <div class="stat-card"><div style="font-size:28px;color:var(--neon);font-family:'Orbitron'">${{totalUsers}}</div><div style="opacity:0.6">👥 مستخدمين</div></div>
                    <div class="stat-card"><div style="font-size:28px;color:var(--neon);font-family:'Orbitron'">${{totalVideos}}</div><div style="opacity:0.6">🎬 فيديوهات</div></div>
                    <div class="stat-card"><div style="font-size:28px;color:var(--neon);font-family:'Orbitron'">${{verifiedUsers}}</div><div style="opacity:0.6">✅ موثقين</div></div>
                    <div class="stat-card"><div style="font-size:28px;color:var(--neon);font-family:'Orbitron'">${{bannedUsers}}</div><div style="opacity:0.6">🚫 محظورين</div></div>
                </div>
                <div class="admin-section"><h3 style="color:var(--neon)"><i class="fas fa-users-cog"></i> إدارة المستخدمين</h3>${{usersHTML}}</div>
                <div class="admin-section"><h3 style="color:var(--neon)"><i class="fas fa-video"></i> آخر الفيديوهات</h3>${{videosHTML}}</div>
            </div>
        `;
    }}

    window.verifyUser = async (uid) => {{ if(confirm('توثيق هذا المستخدم؟')) {{ await db.ref('users/' + uid + '/isVerified').set(true); showToast('✅ تم التوثيق'); loadAll().then(loadProfile); }} }};
    window.banUser = async (uid) => {{ if(confirm('حظر هذا المستخدم؟')) {{ await db.ref('users/' + uid + '/banned').set(true); showToast('🚫 تم الحظر'); loadAll().then(loadProfile); }} }};
    window.unbanUser = async (uid) => {{ if(confirm('فك حظر هذا المستخدم؟')) {{ await db.ref('users/' + uid + '/banned').set(false); showToast('✅ تم فك الحظر'); loadAll().then(loadProfile); }} }};
    window.deleteVideo = async (id) => {{ if(confirm('حذف الفيديو نهائياً؟')) {{ await db.ref('videos/' + id).remove(); showToast('🗑️ تم الحذف'); loadAll().then(loadProfile); }} }};

    function showToast(msg) {{ const t=document.getElementById('toastMsg'); t.innerText=msg; t.classList.add('show'); setTimeout(()=>t.classList.remove('show'),2500); }}
</script>
</body>
</html>"""

def build_upload():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><title>💜 VØID_X | رفع</title><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"><style>{COMMON_CSS} body{{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;background:radial-gradient(ellipse at top, #1a000d, #050002);}} .card{{background:rgba(255,255,255,0.03);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.1);border-radius:24px;padding:30px;width:90%;max-width:400px;text-align:center;}} input[type="file"]{{display:none;}} .upload-btn{{padding:16px;background:var(--neon);border:none;border-radius:40px;color:#fff;font-weight:bold;font-size:16px;cursor:pointer;width:100%;margin-top:20px;box-shadow:0 0 25px var(--neon);}} video{{width:100%;max-height:200px;margin-top:15px;border-radius:12px;display:none;}} .progress-bar{{height:6px;background:rgba(255,255,255,0.1);border-radius:10px;margin:15px 0;overflow:hidden;}} .progress-fill{{height:100%;background:var(--neon);width:0%;}}</style></head>
<body>
<div class="card">
    <i class="fas fa-cloud-upload-alt" style="font-size:60px;color:var(--neon);filter:drop-shadow(0 0 20px var(--neon));"></i>
    <h2 style="font-family:'Orbitron';margin:15px 0;">UPLOAD</h2>
    <p style="opacity:0.7">اختر فيديو MP4 (حتى 100MB)</p>
    <input type="file" id="videoFile" accept="video/*" onchange="preview(this)">
    <video id="preview" controls playsinline></video>
    <div id="progressContainer" style="display:none;"><div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div><p id="progressText" style="font-size:12px;">0%</p></div>
    <button class="upload-btn" onclick="upload()"><i class="fas fa-arrow-up"></i> رفع الفيديو</button>
    <p id="status" style="margin-top:12px;"></p>
    <button onclick="window.location.href='index.html'" style="background:none;border:1px solid rgba(255,255,255,0.2);color:#fff;padding:10px 20px;border-radius:20px;margin-top:10px;cursor:pointer;"><i class="fas fa-arrow-right"></i> العودة</button>
</div>
<script src="firebase-config.js"></script>
<script>
    let selectedFile = null;
    auth.onAuthStateChanged(u => {{ if(!u) window.location.href='auth.html'; }});
    function preview(inp){{ const f=inp.files[0]; if(f && f.type.startsWith('video/') && f.size <= 100*1024*1024){{ selectedFile=f; const r=new FileReader(); r.onload=e=>{{ const v=document.getElementById('preview'); v.src=e.target.result; v.style.display='block'; }}; r.readAsDataURL(f); }} else {{ alert('ملف غير صالح'); inp.value=''; }} }}
    async function upload(){{
        if(!selectedFile){{ alert('اختر ملف'); return; }}
        document.getElementById('progressContainer').style.display='block';
        const fd = new FormData(); fd.append('file', selectedFile); fd.append('upload_preset', UPLOAD_PRESET);
        const xhr = new XMLHttpRequest(); xhr.open('POST', 'https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/video/upload');
        xhr.upload.onprogress = e => {{ const p=Math.round(e.loaded/e.total*100); document.getElementById('progressFill').style.width=p+'%'; document.getElementById('progressText').innerText=p+'%'; }};
        xhr.onload = async () => {{
            const r=JSON.parse(xhr.responseText);
            await db.ref('videos/').push({{ url: r.secure_url, thumbnail: r.secure_url.replace('.mp4','.jpg'), sender: auth.currentUser.uid, senderName: 'VØID', likes: 0, likedBy: {{}}, comments: {{}}, timestamp: Date.now() }});
            document.getElementById('status').innerHTML='✅ تم الرفع!'; setTimeout(()=>window.location.href='index.html',1500);
        }};
        xhr.onerror = () => document.getElementById('status').innerHTML='❌ فشل';
        xhr.send(fd);
    }}
</script>
</body></html>"""

def build_chat():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><title>💜 VØID_X | دردشة</title><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"><style>{COMMON_CSS} body{{height:100vh;display:flex;flex-direction:column;}} header{{padding:16px;border-bottom:1px solid rgba(255,255,255,0.1);display:flex;align-items:center;gap:12px;}} .msgs{{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:8px;}} .bubble{{max-width:80%;padding:10px 16px;border-radius:20px;word-break:break-word;font-size:14px;}} .bubble.sent{{background:linear-gradient(135deg, #ff007f, #ff00aa);align-self:flex-end;color:#fff;}} .bubble.received{{background:rgba(255,255,255,0.05);align-self:flex-start;border:1px solid rgba(255,255,255,0.1);}} .input-bar{{display:flex;gap:8px;padding:12px;background:rgba(5,0,2,0.9);border-top:1px solid rgba(255,255,255,0.1);}} input{{flex:1;padding:12px;border-radius:30px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#fff;}} button{{background:var(--neon);border:none;border-radius:50%;width:42px;height:42px;display:flex;align-items:center;justify-content:center;cursor:pointer;}}</style></head>
<body><header><button onclick="window.location.href='index.html'" style="background:none;border:none;color:#fff;font-size:18px;"><i class="fas fa-arrow-right"></i></button><h2 style="font-family:'Orbitron';">VØID_CHAT</h2></header><div class="msgs" id="chatBox"><div class="spinner"></div></div><div class="input-bar"><input type="text" id="msgInput" placeholder="اكتب رسالتك..." onkeydown="if(event.key==='Enter')sendMsg()"><button onclick="sendMsg()"><i class="fas fa-paper-plane"></i></button></div>
<script src="firebase-config.js"></script><script>let currentUser=null; auth.onAuthStateChanged(async u=>{{ if(!u)window.location.href='auth.html';currentUser=u;db.ref('global_chat').limitToLast(50).on('value',loadMsgs);}}); function loadMsgs(snap){{ const box=document.getElementById('chatBox');box.innerHTML='';const msgs=snap.val()||{{}}; Object.values(msgs).sort((a,b)=>a.timestamp-b.timestamp).forEach(m=>{{ const d=document.createElement('div');d.className='bubble '+(m.senderId===currentUser.uid?'sent':'received');d.innerHTML=`<strong style="font-size:11px;opacity:0.7">${{m.username||'مستخدم'}}</strong><br>${{m.text}}<div style="font-size:9px;opacity:0.4;margin-top:4px;">${{new Date(m.timestamp).toLocaleTimeString()}}</div>`;box.appendChild(d);}});box.scrollTop=box.scrollHeight;}} async function sendMsg(){{ const inp=document.getElementById('msgInput');if(!inp.value.trim())return; const userSnap=await db.ref('users/'+currentUser.uid).get();const username=userSnap.val()?.username||'مستخدم';await db.ref('global_chat').push({{senderId:currentUser.uid,username:username,text:inp.value.trim(),timestamp:Date.now()}});inp.value='';}} window.sendMsg=sendMsg;</script></body></html>"""

def build_explore():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><title>💜 VØID_X | استكشاف</title><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"><style>{COMMON_CSS} body{{min-height:100vh;overflow-y:auto;}} header{{padding:16px;border-bottom:1px solid rgba(255,255,255,0.1);position:sticky;top:0;background:rgba(5,0,2,0.8);backdrop-filter:blur(20px);z-index:10;display:flex;align-items:center;gap:12px;}} .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;padding:2px;}} .thumb{{aspect-ratio:9/16;background:rgba(255,0,127,0.05);cursor:pointer;overflow:hidden;position:relative;}} .thumb img{{width:100%;height:100%;object-fit:cover;}} .thumb i{{position:absolute;bottom:5px;left:5px;color:#fff;}}</style></head>
<body><header><button onclick="window.location.href='index.html'" style="background:none;border:none;color:#fff;font-size:18px;"><i class="fas fa-arrow-right"></i></button><h2>استكشاف</h2></header><div class="grid" id="exploreGrid"><div class="spinner" style="grid-column:1/-1"></div></div>
<script src="firebase-config.js"></script><script>auth.onAuthStateChanged(u=>{{ if(!u)window.location.href='auth.html';else loadExplore();}});async function loadExplore(){{ const snap=await db.ref('videos').once('value');const vids=Object.values(snap.val()||{{}}).sort((a,b)=>(b.likes||0)-(a.likes||0));const g=document.getElementById('exploreGrid');g.innerHTML=vids.length?vids.map(v=>`<div class="thumb" onclick="window.open('${{v.url}}','_blank')">${{v.thumbnail?`<img src="${{v.thumbnail}}">`:''}}<i class="fas fa-play"></i></div>`).join(''):'<div style="grid-column:1/-1;text-align:center;padding:40px;opacity:0.5">لا فيديوهات</div>';}}</script></body></html>"""

def build_notifications():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><title>💜 VØID_X | إشعارات</title><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"><style>{COMMON_CSS} body{{min-height:100vh;}} header{{padding:16px;border-bottom:1px solid rgba(255,255,255,0.1);display:flex;align-items:center;gap:12px;}} .notif-item{{display:flex;gap:12px;padding:14px;border-bottom:1px solid rgba(255,255,255,0.05);}}</style></head>
<body><header><button onclick="window.location.href='index.html'" style="background:none;border:none;color:#fff;font-size:18px;"><i class="fas fa-arrow-right"></i></button><h2>الإشعارات</h2></header><div id="list"><div class="spinner"></div></div>
<script src="firebase-config.js"></script><script>auth.onAuthStateChanged(async u=>{{ if(!u)window.location.href='auth.html';const snap=await db.ref('notifications/'+u.uid).once('value');const ns=snap.val()||{{}};const items=Object.values(ns).reverse();document.getElementById('list').innerHTML=items.length?items.map(n=>`<div class="notif-item"><i class="fas fa-bell" style="color:var(--neon)"></i><div><div>${{n.from}}</div><div style="font-size:12px;opacity:0.6">${{n.msg}}</div></div></div>`).join(''):'<div style="text-align:center;padding:40px;opacity:0.5">لا إشعارات</div>';await db.ref('notifications/'+u.uid).update(Object.fromEntries(Object.entries(ns).map(([k,v])=>[k,{{...v,read:true}}])));}});</script></body></html>"""

def build_settings():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><title>💜 VØID_X | إعدادات</title><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"><style>{COMMON_CSS} body{{min-height:100vh;}} header{{padding:16px;border-bottom:1px solid rgba(255,255,255,0.1);display:flex;align-items:center;gap:12px;}} .setting-item{{padding:16px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;cursor:pointer;}}</style></head>
<body><header><button onclick="window.location.href='index.html'" style="background:none;border:none;color:#fff;font-size:18px;"><i class="fas fa-arrow-right"></i></button><h2>الإعدادات</h2></header>
<div><div class="setting-item" onclick="window.location.href='profile.html'"><span><i class="fas fa-user"></i> الملف الشخصي</span><i class="fas fa-chevron-left"></i></div><div class="setting-item" onclick="window.location.href='notifications.html'"><span><i class="fas fa-bell"></i> الإشعارات</span><i class="fas fa-chevron-left"></i></div><button onclick="auth.signOut();window.location.href='auth.html'" style="display:block;margin:30px auto;background:rgba(255,0,0,0.2);border:1px solid red;color:#ff4444;padding:12px 30px;border-radius:30px;">تسجيل الخروج</button></div>
<script src="firebase-config.js"></script><script>auth.onAuthStateChanged(u=>{{ if(!u)window.location.href='auth.html';}});</script></body></html>"""

# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║  💜  VØID_X SUPREME v2 BUILDER                        ║
║  Bottom Nav: Profile | Chat | Upload | Explore | Alerts║
║  Cloudinary: dmqyd0haj / s3_gok                        ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    section("BUILDING SUPREME v2 FILES")
    
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    write("firebase-config.js", build_config())
    write("auth.html", build_auth())
    write("index.html", build_index())
    write("profile.html", build_profile())
    write("upload.html", build_upload())
    write("chat.html", build_chat())
    write("explore.html", build_explore())
    write("notifications.html", build_notifications())
    write("settings.html", build_settings())
    
    print(f"""
{'='*60}
  💜 BUILD COMPLETE! VØID_X SUPREME v2
{'='*60}
  📱 Bottom Nav: PROFILE | CHAT | [+] | EXPLORE | ALERTS
  ☁️  Cloudinary: dmqyd0haj (s3_gok)
  🔥 Firebase: europe-west1
  👑 Admin: jasim28v@gmail.com
  📁 {OUTPUT_DIR}/ folder ready
{'='*60}
    """)

if __name__ == "__main__":
    main()
