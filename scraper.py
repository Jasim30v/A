#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                            ║
║  ☁️  MNAENCA 2026 - SKY BLUE LUXURY EDITION  ☁️       ║
║     Ultimate Version - 9 Files - 3000+ Lines               ║
║                                                            ║
║  🔥  Firebase: muvg-42126                                 ║
║  ☁️   Cloudinary: dmqyd0haj / s3_gok                     ║
║  👑  Admin: jasim28v@gmail.com                            ║
║  👾  Avatars: DiceBear Big Smile (Random)                  ║
║  💎  Design: Modern Card UI + Glassmorphism               ║
║  ✨  Stories Shelf + Floating Bottom Bar                  ║
║                                                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import shutil

# ═══════════════════════════════════════════════════════════
# ☁️ CONFIGURATION - الإعدادات
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
ADMIN_EMAILS_JS = "['jasim28v@gmail.com']"
DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg"
APP_NAME = "MNAENCA"
WATERMARK_TEXT = "☁️ MNAENCA"
WATERMARK_URL = "https://res.cloudinary.com/dmqyd0haj/image/upload/v1/watermark_mnaenca"

# ☁️ Sky Blue Luxury Palette
SKY_COLORS_JS = """[
    "linear-gradient(135deg, #0c4a6e, #0369a1, #0284c7)",
    "linear-gradient(135deg, #082f49, #0c4a6e, #0369a1)",
    "linear-gradient(135deg, #164e63, #155e75, #0e7490)",
    "linear-gradient(135deg, #1e3a8a, #2563eb, #3b82f6)",
    "linear-gradient(135deg, #0284c7, #38bdf8, #7dd3fc)",
    "linear-gradient(135deg, #0a1628, #0f2847, #0369a1)"
]"""

OUTPUT_DIR = "output"

# ═══════════════════════════════════════════════════════════
# 💙 UTILITY - دوال مساعدة
# ═══════════════════════════════════════════════════════════

TOTAL_LINES = 0

def write(filename, content):
    """حفظ ملف وحساب عدد الأسطر"""
    global TOTAL_LINES
    filepath = os.path.join(OUTPUT_DIR, filename)
    os.makedirs(os.path.dirname(filepath) if os.path.dirname(filepath) else OUTPUT_DIR, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n') + 1
    TOTAL_LINES += lines
    print(f"  ✅ {filename} ({lines} سطر)")

def section(title):
    """طباعة عنوان القسم"""
    print(f"\n{'='*60}")
    print(f"  ☁️  {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# ☁️ COMMON CSS - ستايل مشترك (نمط البطاقات والزجاج)
# ═══════════════════════════════════════════════════════════

COMMON_CSS = """
    :root{
        --glass:rgba(255, 255, 255, 0.05);
        --border:rgba(255, 255, 255, 0.1);
        --accent:#0ea5e9;
        --accent2:#38bdf8;
        --bg:#020617;
        --card:rgba(255, 255, 255, 0.03);
        --danger:#ef4444;
        --success:#22c55e;
        --warning:#f59e0b;
        --radius:24px;
    }
    *{margin:0;padding:0;box-sizing:border-box}
    body{
        font-family:'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
        background:var(--bg);
        color:#fff;
        -webkit-tap-highlight-color:transparent;
        user-select:none;
        -webkit-user-select:none;
        height:100vh;overflow:hidden;
    }
    @keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
    @keyframes fadeUp{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:translateY(0)}}
    @keyframes spin{to{transform:rotate(360deg)}}
    @keyframes pulse{0%,100%{opacity:1}50%{opacity:0.5}}
    @keyframes slideUp{from{transform:translateY(100%)}to{transform:translateY(0)}}
    @keyframes slideDown{from{transform:translateY(0)}to{transform:translateY(100%)}}
    @keyframes scaleIn{from{transform:scale(0.8);opacity:0}to{transform:scale(1);opacity:1}}
    @keyframes glowPulse{0%,100%{box-shadow:0 0 20px rgba(14,165,233,0.3)}50%{box-shadow:0 0 40px rgba(6,182,212,0.7)}}
    .spinner{
        width:36px;height:36px;
        border:3px solid rgba(255,255,255,0.1);
        border-top-color:var(--accent);
        border-radius:50%;
        animation:spin 0.7s linear infinite;
        margin:30px auto;
    }
    .toast-msg{
        position:fixed;bottom:120px;left:50%;transform:translateX(-50%);
        background:rgba(2,6,23,0.95);padding:12px 24px;border-radius:30px;
        z-index:10000;border:1px solid rgba(255,255,255,0.1);font-size:13px;
        opacity:0;transition:opacity 0.3s;pointer-events:none;white-space:nowrap;
        box-shadow:0 8px 32px rgba(0,0,0,0.4);
    }
    .toast-msg.show{opacity:1}
    .overlay{
        position:fixed;inset:0;background:rgba(2,6,23,0.97);
        backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);
        z-index:400;overflow-y:auto;
        animation:fadeIn 0.3s ease;
    }
    .overlay-header{
        display:flex;justify-content:space-between;align-items:center;
        padding:16px 20px;border-bottom:1px solid var(--border);
        position:sticky;top:0;background:rgba(2,6,23,0.9);
        backdrop-filter:blur(20px);z-index:5;
    }
    .overlay-header h3{font-weight:700;font-size:17px;display:flex;align-items:center;gap:8px}
    .btn-close-overlay{
        background:rgba(255,255,255,0.05);border:1px solid var(--border);
        color:#fff;width:36px;height:36px;border-radius:50%;
        display:flex;align-items:center;justify-content:center;
        cursor:pointer;font-size:16px;transition:all 0.3s;
    }
    .btn-close-overlay:hover{background:rgba(14,165,233,0.2);}
"""

# ═══════════════════════════════════════════════════════════
# ☁️ 1. firebase-config.js
# ═══════════════════════════════════════════════════════════

def build_config():
    return f"""// ☁️ MNAENCA 2026 - Sky Blue Luxury Configuration
// Firebase: muvg-42126 | Cloudinary: dmqyd0haj
// ✨ PREMIUM: TikTok Comments + Share System + Watermark + Enhanced Profile

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

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

// Cloudinary Configuration
const CLOUD_NAME = "{CLOUD_NAME}";
const UPLOAD_PRESET = "{UPLOAD_PRESET}";
const CLOUDINARY_UPLOAD_URL = `https://api.cloudinary.com/v1_1/${{CLOUD_NAME}}/auto/upload`;

// ☁️ MNAENCA Settings
const ADMIN_EMAILS = {ADMIN_EMAILS_JS};
const DICEBEAR_URL = "{DICEBEAR_URL}";
const COVER_COLORS = {SKY_COLORS_JS};

// ☁️ App Info
const APP_NAME = "{APP_NAME}";
const APP_VERSION = "2026.3";
const PRIMARY_COLOR = "#0ea5e9";
const SECONDARY_COLOR = "#38bdf8";
const WATERMARK_TEXT = "{WATERMARK_TEXT}";
const WATERMARK_URL = "{WATERMARK_URL}";

console.log('☁️ %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨', 'color: #0ea5e9; font-size: 16px; font-weight: bold;');
"""

# ═══════════════════════════════════════════════════════════
# ☁️ 2. auth.html - تسجيل الدخول والاشتراك
# ═══════════════════════════════════════════════════════════

def build_auth():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>☁️ MNAENCA | دخول</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{
            min-height:100vh;
            background:radial-gradient(ellipse at top, #0a1628, #060d1a, #020617);
            display:flex;align-items:center;justify-content:center;
            overflow:hidden;position:relative;
        }}
        .bg-orb{{
            position:fixed;border-radius:50%;filter:blur(130px);opacity:0.25;
            animation:orbFloat 20s infinite alternate;pointer-events:none;
        }}
        .bg-orb:nth-child(1){{width:400px;height:400px;background:#0ea5e9;top:-100px;left:-100px}}
        .bg-orb:nth-child(2){{width:350px;height:350px;background:#06b6d4;bottom:-100px;right:-100px;animation-delay:5s}}
        .bg-orb:nth-child(3){{width:300px;height:300px;background:#38bdf8;top:50%;left:50%;animation-delay:10s}}
        @keyframes orbFloat{{0%{{transform:translate(0,0) scale(1)}}100%{{transform:translate(50px,-50px) scale(1.3)}}}}

        .card{{
            position:relative;z-index:1;width:90%;max-width:420px;
            background:rgba(255,255,255,0.03);
            backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);
            border-radius:32px;padding:36px 24px;
            border:1px solid rgba(255,255,255,0.1);
            box-shadow:0 30px 70px rgba(14,165,233,0.1),inset 0 0 30px rgba(14,165,233,0.02);
            animation:fadeUp 0.8s ease;
        }}
        .logo{{
            width:70px;height:70px;margin:0 auto 20px;
            background:linear-gradient(135deg, rgba(14,165,233,0.3), rgba(6,182,212,0.3));
            border-radius:20px;display:flex;align-items:center;justify-content:center;
            font-size:36px;border:1px solid rgba(14,165,233,0.2);
            animation:glowPulse 3s ease-in-out infinite;
        }}
        h1{{text-align:center;font-size:36px;font-weight:900;background:linear-gradient(to bottom, #fff, #7dd3fc);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:4px}}
        .sub{{text-align:center;color:rgba(255,255,255,0.4);font-size:13px;margin-bottom:20px}}

        .tabs{{display:flex;gap:4px;background:rgba(255,255,255,0.03);border-radius:40px;padding:4px;margin-bottom:24px}}
        .tab{{flex:1;padding:12px;background:none;border:none;color:rgba(255,255,255,0.5);cursor:pointer;border-radius:40px;font-size:14px;transition:all 0.3s;font-weight:500}}
        .tab.active{{background:linear-gradient(135deg, #0ea5e9, #06b6d4);color:#fff;box-shadow:0 8px 20px rgba(14,165,233,0.4)}}

        .form{{display:none;animation:fadeIn 0.4s ease}}
        .form.active{{display:block}}

        input{{
            width:100%;padding:15px 18px;margin:8px 0;
            border-radius:50px;background:rgba(255,255,255,0.03);
            border:1px solid rgba(255,255,255,0.1);color:#fff;
            font-size:14px;outline:none;transition:all 0.4s;
        }}
        input:focus{{border-color:rgba(14,165,233,0.6);box-shadow:0 0 20px rgba(14,165,233,0.1);background:rgba(14,165,233,0.08)}}
        input::placeholder{{color:rgba(255,255,255,0.3)}}

        button{{
            width:100%;padding:15px;margin-top:18px;
            background:linear-gradient(135deg, #0ea5e9, #06b6d4);
            border:none;border-radius:50px;color:#fff;
            font-weight:bold;font-size:15px;cursor:pointer;
            transition:all 0.3s;box-shadow:0 10px 30px rgba(14,165,233,0.4);
        }}
        button:hover{{transform:translateY(-2px);box-shadow:0 20px 40px rgba(14,165,233,0.6)}}
        button:active{{transform:scale(0.97)}}
        button:disabled{{opacity:0.5;pointer-events:none}}

        .msg{{text-align:center;color:#fca5a5;font-size:13px;margin-top:12px;min-height:20px}}
        .msg.success{{color:#4ade80}}
    </style>
</head>
<body>
    <div class="bg-orb"></div><div class="bg-orb"></div><div class="bg-orb"></div>

    <div class="card">
        <div class="logo">☁️</div>
        <h1>MNAENCA</h1>
        <p class="sub">Sky Blue Luxury 2026 ✨</p>

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
            <input type="text" id="regName" placeholder="👤 اسم المستخدم" autocomplete="username">
            <input type="email" id="regEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email" dir="ltr">
            <input type="password" id="regPass" placeholder="🔒 كلمة المرور (6 أحرف على الأقل)" autocomplete="new-password">
            <button id="btnRegister" onclick="doRegister()"><i class="fas fa-heart"></i> إنشاء حساب</button>
            <div class="msg" id="regMsg"></div>
        </div>
    </div>

    <script src="firebase-config.js"></script>
    <script>
        function switchTab(type){{
            document.getElementById('tabLogin').classList.remove('active');
            document.getElementById('tabRegister').classList.remove('active');
            document.getElementById('formLogin').classList.remove('active');
            document.getElementById('formRegister').classList.remove('active');
            document.getElementById('loginMsg').innerText = '';
            document.getElementById('regMsg').innerText = '';
            if(type === 'login'){{
                document.getElementById('tabLogin').classList.add('active');
                document.getElementById('formLogin').classList.add('active');
            }} else {{
                document.getElementById('tabRegister').classList.add('active');
                document.getElementById('formRegister').classList.add('active');
            }}
        }}

        async function doLogin(){{
            const email = document.getElementById('loginEmail').value.trim();
            const password = document.getElementById('loginPass').value;
            const msg = document.getElementById('loginMsg');
            const btn = document.getElementById('btnLogin');
            if(!email || !password){{ msg.innerText = '❌ الرجاء ملء جميع الحقول'; return; }}
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

        async function doRegister(){{
            const username = document.getElementById('regName').value.trim();
            const email = document.getElementById('regEmail').value.trim();
            const password = document.getElementById('regPass').value;
            const msg = document.getElementById('regMsg');
            const btn = document.getElementById('btnRegister');
            if(!username || !email || !password){{ msg.innerText = '❌ الرجاء ملء جميع الحقول'; return; }}
            if(username.length < 3){{ msg.innerText = '❌ اسم المستخدم 3 أحرف على الأقل'; return; }}
            if(password.length < 6){{ msg.innerText = '❌ كلمة المرور 6 أحرف على الأقل'; return; }}
            if(!email.includes('@') || !email.includes('.')){{ msg.innerText = '❌ بريد إلكتروني غير صالح'; return; }}
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
                    case 'auth/operation-not-allowed': msg.innerText = '❌ التسجيل غير مفعل، راجع إعدادات Firebase'; break;
                    default: msg.innerText = '❌ خطأ: ' + (error.message || 'غير معروف');
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

        console.log('☁️ MNAENCA Auth Ready');
    </script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# ☁️ 3. index.html - الرئيسية (التصميم الجديد)
# ═══════════════════════════════════════════════════════════

def build_index():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>☁️ MNAENCA | الرئيسية</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        
        #loaderScreen{{
            position:fixed;inset:0;z-index:9999;
            background:radial-gradient(ellipse at top, #0a1628, #060d1a, #020617);
            display:flex;align-items:center;justify-content:center;
            flex-direction:column;gap:16px;
        }}
        .spinner-big{{
            width:50px;height:50px;
            border:4px solid rgba(255,255,255,0.1);
            border-top-color:var(--accent);
            border-radius:50%;
            animation:spin 0.8s linear infinite;
        }}

        #mainApp{{display:none;height:100vh;position:relative;flex-direction:column;}}

        /* 🌟 شريط العنوان العلوي */
        .top-header{{
            display:flex;justify-content:space-between;align-items:center;
            padding:16px 20px 8px;
            position:sticky;top:0;z-index:20;
            background:var(--bg);
        }}
        .top-header .menu-icon{{
            width:44px;height:44px;border-radius:50%;
            background:rgba(255,255,255,0.03);border:1px solid var(--border);
            display:flex;align-items:center;justify-content:center;cursor:pointer;
        }}
        .top-header .header-actions{{display:flex;gap:12px;align-items:center}}
        .top-header .action-icon{{
            width:44px;height:44px;border-radius:50%;
            background:rgba(255,255,255,0.03);border:1px solid var(--border);
            display:flex;align-items:center;justify-content:center;
            font-size:18px;cursor:pointer;position:relative;color:rgba(255,255,255,0.6);
        }}
        .top-header .action-icon .notif-badge{{
            position:absolute;top:-4px;right:-4px;width:8px;height:8px;
            background:#ef4444;border-radius:50%;display:none;
        }}

        /* 🌟 شريط التبويبات العلوي */
        .tabs-row{{
            display:flex;gap:20px;padding:0 20px;margin-bottom:16px;
            border-bottom:1px solid rgba(255,255,255,0.05);position:sticky;top:65px;
            background:var(--bg);z-index:10;padding-bottom:12px;
        }}
        .tabs-row .tab-btn{{
            background:none;border:none;color:rgba(255,255,255,0.5);font-size:16px;font-weight:600;cursor:pointer;padding-bottom:12px;border-bottom:2px solid transparent;transition:all 0.3s;
        }}
        .tabs-row .tab-btn.active{{color:#fff;border-bottom-color:var(--accent);}}

        /* 🌟 شريط القصص الأفقي (Stories Shelf) */
        .stories-scroll{{
            display:flex;gap:12px;padding:0 20px;overflow-x:auto;margin-bottom:16px;
            scrollbar-width:none;-ms-overflow-style:none;
        }}
        .stories-scroll::-webkit-scrollbar{{display:none}}
        .story-item{{
            flex-shrink:0;width:70px;display:flex;flex-direction:column;align-items:center;gap:6px;
        }}
        .story-ring{{
            width:70px;height:70px;border-radius:50%;padding:3px;
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            cursor:pointer;
        }}
        .story-ring img{{width:100%;height:100%;border-radius:50%;object-fit:cover;border:2px solid var(--bg)}}
        .story-ring.add-story{{background:rgba(255,255,255,0.1);display:flex;align-items:center;justify-content:center;font-size:24px;color:#fff;}}
        .story-name{{font-size:11px;color:rgba(255,255,255,0.7);text-align:center;width:100%;overflow:hidden;white-space:nowrap;text-overflow:ellipsis}}

        /* 📹 تخطيط الفيديوهات (Cards) */
        .videos-wrap{{
            flex:1;overflow-y:auto;padding:0 16px 140px;
            scroll-behavior:smooth;
        }}
        .videos-wrap::-webkit-scrollbar{{display:none}}
        
        .vid-card{{
            position:relative;margin-bottom:20px;border-radius:var(--radius);
            overflow:hidden;background:#0f111a;aspect-ratio:9/16;box-shadow:0 10px 40px rgba(0,0,0,0.5);
            animation:fadeUp 0.5s ease;
        }}
        .vid-card video{{
            width:100%;height:100%;object-fit:cover;display:block;
        }}

        .vid-info{{
            position:absolute;bottom:16px;left:16px;right:70px;z-index:10;
        }}
        .author-row{{display:flex;align-items:center;gap:8px;margin-bottom:4px}}
        .author-avatar{{
            width:32px;height:32px;border-radius:50%;overflow:hidden;
            cursor:pointer;flex-shrink:0;border:1px solid rgba(255,255,255,0.2);
        }}
        .author-avatar img{{width:100%;height:100%;object-fit:cover}}
        .author-name{{font-size:13px;font-weight:600;display:flex;align-items:center;gap:4px}}
        .btn-follow{{
            background:rgba(255,255,255,0.1);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.2);
            padding:2px 12px;border-radius:12px;font-size:10px;font-weight:600;color:#fff;cursor:pointer;
        }}
        .caption{{font-size:12px;opacity:0.8;margin:4px 0;line-height:1.3;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}}
        .music{{font-size:11px;opacity:0.5;display:flex;align-items:center;gap:4px}}

        /* 🎛️ أزرار التفاعل (Glassmorphism) */
        .side-btns{{
            position:absolute;right:10px;bottom:20px;
            display:flex;flex-direction:column;gap:14px;z-index:20;
        }}
        .sbtn{{
            display:flex;flex-direction:column;align-items:center;gap:2px;
            background:rgba(255,255,255,0.05);backdrop-filter:blur(10px);
            border:1px solid rgba(255,255,255,0.1);
            width:44px;height:44px;border-radius:50%;
            color:#fff;cursor:pointer;font-size:10px;transition:all 0.2s;
            justify-content:center;box-shadow:0 4px 15px rgba(0,0,0,0.3);
        }}
        .sbtn:active{{transform:scale(0.85)}}
        .sbtn i{{font-size:18px}}
        .sbtn.liked{{background:rgba(239,68,68,0.2);border-color:rgba(239,68,68,0.5);color:#f87171;}}
        .sbtn.liked i{{animation:likePop 0.4s ease}}
        @keyframes likePop{{0%{{transform:scale(1)}}50%{{transform:scale(1.4)}}100%{{transform:scale(1)}}}}
        .sbtn .cnt{{font-weight:600;font-size:10px;}}

        /* 📤 Share Panel */
        .share-panel{{
            position:fixed;bottom:0;left:0;right:0;
            background:rgba(2,6,23,0.98);backdrop-filter:blur(40px);
            border-top:2px solid var(--accent);border-radius:var(--radius) var(--radius) 0 0;
            padding:24px 20px 40px;z-index:500;transform:translateY(100%);transition:transform 0.4s cubic-bezier(0.4,0,0.2,1);
        }}
        .share-panel.show{{transform:translateY(0)}}
        .share-panel h3{{font-size:17px;font-weight:700;margin-bottom:20px;text-align:center;}}
        .share-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:20px}}
        .share-item{{display:flex;flex-direction:column;align-items:center;gap:8px;cursor:pointer;transition:transform 0.2s}}
        .share-item:hover{{transform:scale(1.1)}}
        .share-item .share-icon{{width:50px;height:50px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:22px;background:rgba(255,255,255,0.05);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.1)}}
        .share-item span{{font-size:11px;opacity:0.7}}
        .share-copy-row{{display:flex;gap:8px;align-items:center;background:rgba(255,255,255,0.03);border-radius:16px;padding:8px;border:1px solid var(--border);}}
        .share-copy-row input{{flex:1;padding:12px;border-radius:12px;background:rgba(255,255,255,0.03);border:1px solid var(--border);color:#fff;font-size:13px;outline:none;direction:ltr;}}
        .share-copy-row button{{background:var(--accent);border:none;color:#fff;padding:12px 20px;border-radius:12px;font-weight:700;cursor:pointer;}}

        /* 💬 Comments Panel */
        .comments-panel{{
            position:fixed;bottom:0;left:0;right:0;background:rgba(2,6,23,0.98);backdrop-filter:blur(40px);
            border-top:2px solid var(--accent);border-radius:var(--radius) var(--radius) 0 0;padding:0;z-index:500;max-height:70vh;display:flex;flex-direction:column;
            transform:translateY(100%);transition:transform 0.4s cubic-bezier(0.4,0,0.2,1);
        }}
        .comments-panel.show{{transform:translateY(0)}}
        .comments-header{{display:flex;justify-content:space-between;align-items:center;padding:16px 20px;border-bottom:1px solid var(--border);flex-shrink:0;}}
        .comments-list{{flex:1;overflow-y:auto;padding:12px 16px;}}
        .comment-item{{display:flex;gap:10px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,0.03);}}
        .comment-avatar{{width:32px;height:32px;border-radius:50%;overflow:hidden;flex-shrink:0;border:1px solid rgba(255,255,255,0.1);}}
        .comment-body{{flex:1;min-width:0}}
        .comment-user{{font-weight:600;font-size:13px;display:flex;align-items:center;gap:5px}}
        .comment-text{{font-size:13px;line-height:1.4;word-break:break-word}}
        .comment-actions{{display:flex;gap:16px;margin-top:6px;font-size:11px;opacity:0.6}}
        .reply-item{{margin-right:40px;padding:8px 0;border-bottom:1px solid rgba(255,255,255,0.02);display:flex;gap:8px;}}
        .comment-input-row{{display:flex;gap:8px;padding:12px 16px;border-top:1px solid var(--border);background:rgba(2,6,23,0.95);flex-shrink:0;}}
        .comment-input-row input{{flex:1;padding:10px 16px;border-radius:40px;background:rgba(255,255,255,0.03);border:1px solid var(--border);color:#fff;font-size:13px;outline:none;}}
        .comment-input-row button{{background:var(--accent);border:none;color:#fff;padding:8px 18px;border-radius:40px;font-weight:700;cursor:pointer;font-size:13px;}}

        /* 📱 FLOATING BOTTOM NAV (شريط سفلي ذكي) */
        .nav-bottom{{
            position:fixed;bottom:16px;left:16px;right:16px;
            display:flex;justify-content:space-between;align-items:center;
            padding:12px 20px;background:rgba(2,6,23,0.85);backdrop-filter:blur(20px);
            border:1px solid rgba(255,255,255,0.05);border-radius:50px;z-index:100;
            box-shadow:0 8px 32px rgba(0,0,0,0.6);
        }}
        .nav-item{{display:flex;align-items:center;justify-content:center;background:none;border:none;color:rgba(255,255,255,0.5);font-size:22px;cursor:pointer;transition:all 0.3s;width:44px;height:44px;border-radius:50%;}}
        .nav-item.active{{color:var(--accent);background:rgba(14,165,233,0.1);}}
        .nav-item:hover{{color:#fff;}}
        .nav-add-btn{{
            width:52px;height:52px;background:linear-gradient(135deg,var(--accent),var(--accent2));
            border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none;color:#fff;font-size:20px;box-shadow:0 4px 20px rgba(14,165,233,0.6);transition:transform 0.2s;
        }}
        .nav-add-btn:active{{transform:scale(0.9);}}
        
        /* ☁️ Fullscreen Video Player */
        .fullscreen-player {{
            position:fixed;top:0;left:0;width:100vw;height:100vh;background:#000;z-index:9999;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity 0.3s ease;flex-direction:column;
        }}
        .fullscreen-player.active {{opacity:1;pointer-events:auto}}
        .fullscreen-player video {{max-width:100%;max-height:85vh;object-fit:contain;cursor:pointer}}
        .player-controls{{position:absolute;bottom:40px;left:20px;right:20px;display:flex;align-items:center;justify-content:space-between;background:rgba(0,0,0,0.6);backdrop-filter:blur(20px);border-radius:50px;padding:10px 20px;border:1px solid rgba(255,255,255,0.1);z-index:10000;color:#fff;gap:12px;flex-wrap:wrap;}}
        .close-player{{position:absolute;top:20px;left:20px;background:rgba(0,0,0,0.5);border:1px solid rgba(255,255,255,0.2);color:#fff;width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:20px;z-index:10001;}}
    </style>
</head>
<body>

<div id="loaderScreen">
    <div class="spinner-big"></div>
    <p style="color:rgba(255,255,255,0.5);font-size:15px">☁️ MNAENCA جاري التحميل...</p>
</div>

<div id="mainApp">
    <!-- ✨ رأس الصفحة العلوي -->
    <div class="top-header">
        <div class="menu-icon" onclick="window.location.href='settings.html'"><i class="fas fa-bars" style="font-size:18px;color:rgba(255,255,255,0.6)"></i></div>
        <div class="header-actions">
            <div class="action-icon" onclick="openNotifs()"><i class="fas fa-bell"></i><span class="notif-badge" id="notifBadge"></span></div>
            <div class="action-icon" onclick="openSearch()"><i class="fas fa-search"></i></div>
        </div>
    </div>

    <!-- ✨ شريط التبويبات -->
    <div class="tabs-row">
        <button class="tab-btn active" onclick="switchFeed('forYou', this)">لك</button>
        <button class="tab-btn" onclick="switchFeed('following', this)">متابَعين</button>
    </div>

    <!-- ✨ شريط القصص (ثابت حالياً، يمكن ربطه لاحقاً) -->
    <div class="stories-scroll">
        <div class="story-item"><div class="story-ring add-story"><i class="fas fa-plus"></i></div><div class="story-name">قصتي</div></div>
        <div class="story-item"><div class="story-ring"><img src="https://api.dicebear.com/7.x/big-smile/svg?seed=user1" alt=""></div><div class="story-name">سارة</div></div>
        <div class="story-item"><div class="story-ring"><img src="https://api.dicebear.com/7.x/big-smile/svg?seed=user2" alt=""></div><div class="story-name">أحمد</div></div>
        <div class="story-item"><div class="story-ring"><img src="https://api.dicebear.com/7.x/big-smile/svg?seed=user3" alt=""></div><div class="story-name">ليلى</div></div>
        <div class="story-item"><div class="story-ring"><img src="https://api.dicebear.com/7.x/big-smile/svg?seed=user4" alt=""></div><div class="story-name">خالد</div></div>
    </div>

    <div class="videos-wrap" id="videosWrap">
        <div style="display:flex;align-items:center;justify-content:center;height:50vh;color:rgba(255,255,255,0.5);flex-direction:column;gap:12px">
            <i class="fas fa-video" style="font-size:48px;opacity:0.3;color:#0ea5e9"></i>
            <p>لا توجد فيديوهات بعد</p>
        </div>
    </div>

    <!-- 📱 شريط سفلي عائم -->
    <div class="nav-bottom">
        <button class="nav-item active"><i class="fas fa-home"></i></button>
        <button class="nav-item" onclick="openSearch()"><i class="fas fa-search"></i></button>
        <button class="nav-add-btn" onclick="window.location.href='upload.html'"><i class="fas fa-plus"></i></button>
        <button class="nav-item" onclick="window.location.href='profile.html'"><i class="fas fa-user"></i></button>
        <button class="nav-item" onclick="window.location.href='chat.html'"><i class="fas fa-envelope"></i></button>
    </div>

    <div class="toast-msg" id="toast">✅ تم النسخ</div>
</div>

<script src="firebase-config.js"></script>
<script>
    let currentUser = null;
    let currentUserData = null;
    let allUsers = {{}};
    let allVideos = [];
    let allSounds = {{}};
    let isMuted = true;
    let currentFeed = 'forYou';
    let currentShareUrl = null;
    let playerVideo = null;
    let currentCommentVideoId = null;
    let replyingTo = null;

    // ☁️ Player Functions
    function openPlayer(url, title) {{
        const player = document.getElementById('fullscreenPlayer');
        const video = document.getElementById('fullscreenVideo');
        player.classList.add('active');
        video.src = url;
        video.load();
        video.play();
        document.getElementById('downloadLink').href = url;
        document.getElementById('downloadLink').download = title || 'video.mp4';
        playerVideo = video;
        video.onloadedmetadata = () => {{
            document.getElementById('duration').innerText = formatTime(video.duration);
            document.getElementById('muteIcon').className = video.muted ? 'fas fa-volume-mute' : 'fas fa-volume-up';
        }};
        video.ontimeupdate = () => {{
            const pct = (video.currentTime / video.duration) * 100;
            document.getElementById('progressFill').style.width = pct + '%';
            document.getElementById('currentTime').innerText = formatTime(video.currentTime);
        }};
    }}
    window.openPlayer = openPlayer;

    function closePlayer() {{
        const player = document.getElementById('fullscreenPlayer');
        const video = document.getElementById('fullscreenVideo');
        video.pause();video.src='';player.classList.remove('active');
    }}
    function togglePlayPause() {{
        const video = document.getElementById('fullscreenVideo');
        if(video.paused){{video.play();document.getElementById('btnPlayPause').innerHTML='<i class="fas fa-pause"></i>';}}
        else{{video.pause();document.getElementById('btnPlayPause').innerHTML='<i class="fas fa-play"></i>';}}
    }}
    function skipTime(sec) {{if(playerVideo)playerVideo.currentTime+=sec;}}
    function seekVideo(e) {{
        if(!playerVideo)return;
        const bar=document.getElementById('progressBar');
        const rect=bar.getBoundingClientRect();
        const pct=(e.clientX-rect.left)/rect.width;
        playerVideo.currentTime=pct*playerVideo.duration;
    }}
    function toggleMutePlayer() {{
        if(playerVideo){{playerVideo.muted=!playerVideo.muted;document.getElementById('muteIcon').className=playerVideo.muted?'fas fa-volume-mute':'fas fa-volume-up';}}
    }}

    // 📤 Share Functions
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
        const text = encodeURIComponent('شاهد هذا الفيديو على MNAENCA ☁️');
        let shareUrl = '';
        switch(platform) {{
            case 'whatsapp': shareUrl = 'https://wa.me/?text=' + text + '%20' + url; break;
            case 'telegram': shareUrl = 'https://t.me/share/url?url=' + url + '&text=' + text; break;
            case 'facebook': shareUrl = 'https://www.facebook.com/sharer/sharer.php?u=' + url; break;
            case 'twitter': shareUrl = 'https://twitter.com/intent/tweet?url=' + url + '&text=' + text; break;
            case 'messenger': shareUrl = 'https://www.facebook.com/dialog/send?link=' + url + '&app_id=0'; break;
            case 'email': shareUrl = 'mailto:?subject=' + text + '&body=' + url; break;
            case 'copy':
                navigator.clipboard.writeText(currentShareUrl).then(() => {{
                    showToast('✅ تم نسخ الرابط');
                    closeSharePanel();
                }});
                return;
            case 'embed':
                const embedCode = '<iframe src="' + currentShareUrl + '" width="100%" height="600" frameborder="0"></iframe>';
                navigator.clipboard.writeText(embedCode).then(() => {{
                    showToast('✅ تم نسخ كود التضمين');
                    closeSharePanel();
                }});
                return;
        }}
        if(shareUrl) window.open(shareUrl, '_blank');
        closeSharePanel();
    }}

    // 💬 Comments Functions
    async function openCommentsPanel(videoId) {{
        currentCommentVideoId = videoId;
        replyingTo = null;
        document.getElementById('commentsPanel').classList.add('show');
        document.getElementById('commentsOverlay').style.display = 'block';
        document.getElementById('commentInput').placeholder = 'أضف تعليقاً...';
        await loadComments();
    }}
    function closeCommentsPanel() {{
        document.getElementById('commentsPanel').classList.remove('show');
        document.getElementById('commentsOverlay').style.display = 'none';
        currentCommentVideoId = null;
        replyingTo = null;
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
            list.innerHTML = '<div style="text-align:center;opacity:0.5;padding:30px"><i class="fas fa-comment-slash" style="font-size:32px;color:var(--accent);margin-bottom:8px;display:block"></i>لا توجد تعليقات</div>';
            return;
        }}
        list.innerHTML = commentsArr.map(c => {{
            const user = allUsers[c.userId] || {{username: c.username || 'مستخدم'}};
            const avatar = user.avatarUrl || (DICEBEAR_URL + '?seed=' + c.userId);
            const replies = c.replies ? Object.entries(c.replies).map(([rid, r]) => ({{id: rid, ...r}})) : [];
            replies.sort((a, b) => (a.timestamp || 0) - (b.timestamp || 0));
            let repliesHTML = '';
            if(replies.length) {{
                repliesHTML = replies.map(r => {{
                    const rUser = allUsers[r.userId] || {{username: r.username || 'مستخدم'}};
                    const rAvatar = rUser.avatarUrl || (DICEBEAR_URL + '?seed=' + r.userId);
                    return `<div class="reply-item">
                        <div class="comment-avatar"><img src="${{rAvatar}}" alt=""></div>
                        <div style="flex:1;min-width:0">
                            <div class="comment-user" style="font-size:12px">@${{rUser.username}} <span class="comment-time">${{formatTimeAgo(r.timestamp)}}</span></div>
                            <div class="comment-text" style="font-size:12px">${{r.text}}</div>
                        </div>
                    </div>`;
                }}).join('');
            }}
            return `<div class="comment-item">
                <div class="comment-avatar"><img src="${{avatar}}" alt=""></div>
                <div class="comment-body">
                    <div class="comment-user">@${{user.username}} ${{user.isVerified ? '<span class="verified-badge-main"><i class="fas fa-check"></i></span>' : ''}} <span class="comment-time">${{formatTimeAgo(c.timestamp)}}</span></div>
                    <div class="comment-text">${{c.text}}</div>
                    <div class="comment-actions">
                        <span onclick="replyToComment('${{c.id}}', '@${{user.username}}')"><i class="fas fa-reply"></i> رد</span>
                        <span>${{c.likes || 0}} <i class="fas fa-heart"></i></span>
                    </div>
                    ${{repliesHTML}}
                </div>
            </div>`;
        }}).join('');
    }}
    function replyToComment(commentId, username) {{
        replyingTo = commentId;
        const input = document.getElementById('commentInput');
        input.placeholder = 'رد على ' + username + '...';
        input.focus();
    }}
    async function addComment() {{
        const input = document.getElementById('commentInput');
        const text = input.value.trim();
        if(!text || !currentCommentVideoId || !currentUser) return;
        const commentData = {{
            userId: currentUser.uid,
            username: currentUserData?.username || 'مستخدم',
            text: text,
            timestamp: Date.now(),
            likes: 0
        }};
        if(replyingTo) {{
            await db.ref('videos/' + currentCommentVideoId + '/comments/' + replyingTo + '/replies').push(commentData);
            replyingTo = null;
            input.placeholder = 'أضف تعليقاً...';
        }} else {{
            await db.ref('videos/' + currentCommentVideoId + '/comments').push(commentData);
            const videoSnap = await db.ref('videos/' + currentCommentVideoId).get();
            const video = videoSnap.val();
            if(video && video.sender !== currentUser.uid) {{
                sendNotification(video.sender, currentUserData?.username, 'علق على فيديو الخاص بك 💬');
            }}
        }}
        input.value = '';
        await loadComments();
    }}
    window.addComment = addComment;
    window.replyToComment = replyToComment;

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
            if(!data) {{ allVideos = []; allSounds = {{}}; }}
            else {{
                allVideos = []; allSounds = {{}};
                Object.entries(data).forEach(([key, value]) => {{
                    allVideos.push({{id: key, ...value}});
                    if(value.music) allSounds[value.music] = (allSounds[value.music] || 0) + 1;
                }});
                allVideos.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
            }}
            renderVideos();
        }});

        db.ref('notifications/' + user.uid).on('value', s => {{
            const ns = s.val() || {{}};
            const badge = document.getElementById('notifBadge');
            if(badge) {{
                const count = Object.keys(ns).length;
                badge.style.display = count > 0 ? 'block' : 'none';
            }}
        }});

        db.ref('presence/' + user.uid).set(true);
        db.ref('presence/' + user.uid).onDisconnect().remove();
        db.ref('users/' + user.uid + '/lastSeen').set(Date.now());
        setInterval(() => {{ db.ref('users/' + user.uid + '/lastSeen').set(Date.now()); }}, 60000);

        document.getElementById('loaderScreen').style.display = 'none';
        document.getElementById('mainApp').style.display = 'flex';
    }});

    async function sendNotification(toUserId, fromUsername, msg) {{
        if(!currentUser) return;
        await db.ref('notifications/' + toUserId).push({{
            from: fromUsername || currentUserData?.username || 'مستخدم',
            msg: msg,
            timestamp: Date.now(),
            read: false
        }});
    }}

    // دالة التبديل الجديدة للتبويبات
    function switchFeed(feed, btn) {{
        currentFeed = feed;
        document.querySelectorAll('.tab-btn').forEach(t => t.classList.remove('active'));
        btn.classList.add('active');
        renderVideos();
    }}
    window.switchFeed = switchFeed;

    function renderVideos() {{
        const container = document.getElementById('videosWrap');
        if(!container) return;
        let filtered = currentFeed === 'forYou' ? allVideos : allVideos.filter(v => currentUserData?.following?.[v.sender]);
        if(!filtered.length) {{
            container.innerHTML = `<div style="display:flex;align-items:center;justify-content:center;height:50vh;color:rgba(255,255,255,0.5);flex-direction:column;gap:12px"><i class="fas fa-video" style="font-size:48px;opacity:0.3;color:#0ea5e9"></i><p>${{currentFeed === 'forYou' ? 'لا توجد فيديوهات بعد' : 'تابع مستخدمين لرؤية فيديوهاتهم'}}</p></div>`;
            return;
        }}
        container.innerHTML = '';
        filtered.forEach(video => {{
            const isLiked = video.likedBy && video.likedBy[currentUser?.uid];
            const user = allUsers[video.sender] || {{username: video.senderName || 'مستخدم'}};
            const isFollowing = currentUserData?.following && currentUserData.following[video.sender];
            const commentsCount = video.comments ? Object.keys(video.comments).length : 0;
            const caption = (video.description || '').replace(/#(\\w+)/g, '<span class="tag" style="color:var(--accent2)">#$1</span>');
            const avatarUrl = user.avatarUrl || (DICEBEAR_URL + '?seed=' + video.sender);
            
            const div = document.createElement('div'); div.className = 'vid-card';
            div.innerHTML = `
                <video loop playsinline muted data-src="${{video.url}}" poster="${{video.thumbnail || ''}}"></video>
                <div class="vid-info">
                    <div class="author-row">
                        <div class="author-avatar" onclick="openUserProfile('${{video.sender}}')"><img src="${{avatarUrl}}" alt="avatar"></div>
                        <div class="author-name">
                            <span onclick="openUserProfile('${{video.sender}}')">@${{user.username}}</span>
                            ${{currentUser?.uid !== video.sender ? `<button class="btn-follow" onclick="event.stopPropagation();toggleFollow('${{video.sender}}', this)">${{isFollowing ? 'متابَع' : '+ متابعة'}}</button>` : ''}}
                        </div>
                    </div>
                    <div class="caption">${{caption}}</div>
                    <div class="music"><i class="fas fa-music" style="font-size:11px"></i> ${{video.music || 'Original Sound'}}</div>
                </div>
                <div class="side-btns">
                    <button class="sbtn" onclick="toggleMute()"><i class="fas ${{isMuted ? 'fa-volume-mute' : 'fa-volume-up'}}" style="font-size:14px"></i></button>
                    <button class="sbtn like-btn ${{isLiked ? 'liked' : ''}}" onclick="toggleLike('${{video.id}}', this)"><i class="fas fa-heart"></i><span class="cnt">${{video.likes || 0}}</span></button>
                    <button class="sbtn" onclick="openCommentsPanel('${{video.id}}')"><i class="fas fa-comment"></i><span class="cnt">${{commentsCount}}</span></button>
                    <button class="sbtn" onclick="openSharePanel('${{video.url}}')"><i class="fas fa-share"></i></button>
                </div>`;
            const videoEl = div.querySelector('video');
            videoEl.addEventListener('dblclick', e => {{
                e.stopPropagation(); const likeBtn = div.querySelector('.like-btn'); if(likeBtn) toggleLike(video.id, likeBtn);
            }});
            container.appendChild(div);
        }});
        initVideoObserver();
    }}

    function openUserProfile(userId) {{
        if(userId === currentUser?.uid) window.location.href = 'profile.html';
        else window.location.href = 'profile.html?uid=' + userId;
    }}

    function initVideoObserver() {{
        const observer = new IntersectionObserver(entries => {{
            entries.forEach(entry => {{
                const video = entry.target.querySelector('video');
                if(entry.isIntersecting) {{ if(!video.src) video.src = video.dataset.src; video.muted = isMuted; video.play().catch(() => {{}}); }} else {{ video.pause(); }}
            }});
        }}, {{threshold: 0.6}});
        document.querySelectorAll('.vid-card').forEach(seg => observer.observe(seg));
    }}

    function toggleMute() {{ isMuted = !isMuted; document.querySelectorAll('video').forEach(v => v.muted = isMuted); }}

    async function toggleLike(videoId, btn) {{
        if(!currentUser) return;
        const ref = db.ref('videos/' + videoId);
        const snap = await ref.get();
        const video = snap.val();
        if(!video) return;
        let likes = video.likes || 0;
        let likedBy = video.likedBy || {{}};
        if(likedBy[currentUser.uid]) {{ likes--; delete likedBy[currentUser.uid]; }}
        else {{
            likes++; likedBy[currentUser.uid] = true;
            if(video.sender && video.sender !== currentUser.uid) {{
                sendNotification(video.sender, currentUserData?.username, 'أعجب بفيديو الخاص بك ❤️');
            }}
        }}
        await ref.update({{likes, likedBy}});
        btn.classList.toggle('liked');
        const countSpan = btn.querySelector('.cnt');
        if(countSpan) countSpan.innerText = likes;
    }}

    async function toggleFollow(userId, btn) {{
        if(!currentUser || currentUser.uid === userId) return;
        const userRef = db.ref('users/' + currentUser.uid + '/following/' + userId);
        const targetRef = db.ref('users/' + userId + '/followers/' + currentUser.uid);
        const snap = await userRef.get();
        if(snap.exists()) {{ await userRef.remove(); await targetRef.remove(); btn.innerText = '+ متابعة'; }}
        else {{
            await userRef.set(true); await targetRef.set(true); btn.innerText = 'متابَع'; 
            sendNotification(userId, currentUserData?.username, 'بدأ بمتابعتك 👤');
        }}
    }}

    async function openNotifs() {{
        const snap = await db.ref('notifications/' + currentUser.uid).once('value');
        const ns = snap.val() || {{}};
        const items = Object.values(ns).reverse();
        let notifHTML = '';
        if(!items.length) {{
            notifHTML = '<div style="text-align:center;opacity:0.5;padding:40px"><i class="fas fa-bell" style="font-size:48px;color:#0ea5e9;margin-bottom:12px;display:block"></i><p>لا توجد إشعارات</p></div>';
        }} else {{
            items.forEach(n => {{
                notifHTML += `<div style="display:flex;gap:12px;padding:14px;border-bottom:1px solid rgba(255,255,255,0.05);align-items:center;animation:fadeIn 0.3s ease">
                    <div style="width:40px;height:40px;border-radius:50%;background:rgba(14,165,233,0.15);display:flex;align-items:center;justify-content:center;font-size:18px;color:#0ea5e9"><i class="fas fa-bell"></i></div>
                    <div><div style="font-weight:600">${{n.from || 'مستخدم'}}</div><div style="font-size:12px;opacity:0.6;margin-top:2px">${{n.msg || ''}}</div><div style="font-size:10px;opacity:0.3;margin-top:4px">${{new Date(n.timestamp).toLocaleString('ar-SA')}}</div></div></div>`;
            }});
        }}
        await db.ref('notifications/' + currentUser.uid).remove();
        const badge = document.getElementById('notifBadge');
        if(badge) badge.style.display = 'none';
        showOverlay('🔔 الإشعارات', notifHTML);
    }}

    function openSearch() {{
        showOverlay('🔍 بحث', `<input type="text" id="searchQ" onkeyup="doSearch()" placeholder="ابحث عن مستخدمين، فيديوهات..." style="width:100%;padding:14px;border-radius:30px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.1);color:#fff;font-size:14px;outline:none;margin-bottom:16px"><div id="searchR"></div>`);
        window.doSearch = function() {{
            const query = document.getElementById('searchQ').value.toLowerCase();
            const resultsDiv = document.getElementById('searchR');
            if(!query) {{ resultsDiv.innerHTML = ''; return; }}
            const users = Object.values(allUsers).filter(u => u.username?.toLowerCase().includes(query));
            const vids = allVideos.filter(v => (v.description || '').toLowerCase().includes(query));
            resultsDiv.innerHTML = `${{users.length ? `<div style="margin-bottom:16px"><h4 style="font-size:12px;opacity:0.5;margin-bottom:8px"><i class="fas fa-users"></i> مستخدمين</h4>${{users.map(u => `<div onclick="openUserProfile('${{u.uid || Object.keys(allUsers).find(k=>allUsers[k]===u)}}')" style="display:flex;align-items:center;gap:10px;padding:10px;cursor:pointer;border-bottom:1px solid rgba(255,255,255,0.05)"><img src="${{u.avatarUrl || (DICEBEAR_URL + '?seed=' + (u.uid || u.username))}}" style="width:40px;height:40px;border-radius:50%"><div>@${{u.username}} ${{u.isVerified ? '<span class="verified-badge-main"><i class="fas fa-check"></i></span>' : ''}}</div></div>`).join('')}}</div>` : ''}}${{vids.length ? `<div><h4 style="font-size:12px;opacity:0.5;margin-bottom:8px"><i class="fas fa-video"></i> فيديوهات</h4>${{vids.map(v => `<div onclick="openPlayer('${{v.url}}', 'video.mp4')" style="display:flex;align-items:center;gap:10px;padding:10px;cursor:pointer;border-bottom:1px solid rgba(255,255,255,0.05)"><i class="fas fa-play-circle" style="color:#0ea5e9;font-size:20px"></i><span style="font-size:13px">${{(v.description || 'فيديو').substring(0, 40)}}</span></div>`).join('')}}</div>` : ''}}${{!users.length && !vids.length ? '<div style="text-align:center;opacity:0.5;padding:30px">لا توجد نتائج</div>' : ''}}`;
        }};
        setTimeout(() => {{ const input = document.getElementById('searchQ'); if(input) input.focus(); }}, 300);
    }}

    function showOverlay(title, content) {{
        const id = 'overlay_' + Date.now();
        const html = `<div id="${{id}}" class="overlay"><div class="overlay-header"><h3>${{title}}</h3><button class="btn-close-overlay" onclick="document.getElementById('${{id}}').remove()"><i class="fas fa-times"></i></button></div><div style="padding:16px">${{content}}</div></div>`;
        document.body.insertAdjacentHTML('beforeend', html);
    }}

    function showToast(msg) {{
        const toast = document.getElementById('toast');
        toast.innerText = msg;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2500);
    }}

    function formatTime(seconds) {{
        if(isNaN(seconds)) return '0:00';
        const m = Math.floor(seconds / 60);
        const s = Math.floor(seconds % 60);
        return m + ':' + (s < 10 ? '0' : '') + s;
    }}

    function formatTimeAgo(ts) {{
        if(!ts) return '';
        const diff = Date.now() - ts;
        const mins = Math.floor(diff / 60000);
        const hours = Math.floor(diff / 3600000);
        const days = Math.floor(diff / 86400000);
        if(mins < 1) return 'الآن';
        if(mins < 60) return 'منذ ' + mins + ' د';
        if(hours < 24) return 'منذ ' + hours + ' س';
        if(days < 7) return 'منذ ' + days + ' يوم';
        return new Date(ts).toLocaleDateString('ar-SA');
    }}

    window.closePlayer = closePlayer;
    window.togglePlayPause = togglePlayPause;
    window.skipTime = skipTime;
    window.seekVideo = seekVideo;
    window.toggleMutePlayer = toggleMutePlayer;
    window.openSharePanel = openSharePanel;
    window.closeSharePanel = closeSharePanel;
    window.shareTo = shareTo;
    window.openCommentsPanel = openCommentsPanel;
    window.closeCommentsPanel = closeCommentsPanel;
    window.openUserProfile = openUserProfile;
    window.toggleFollow = toggleFollow;
    window.toggleLike = toggleLike;
    window.formatTime = formatTime;

    console.log('☁️ MNAENCA Index Ready ✨');
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# ☁️ 4. profile.html
# ═══════════════════════════════════════════════════════════

def build_profile():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>☁️ MNAENCA | ملف شخصي</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{min-height:100vh;overflow-y:auto;overflow-x:hidden;}}
        .cover-section{{position:relative;width:100%;height:260px;overflow:hidden;cursor:pointer}}
        .cover-img{{width:100%;height:130%;object-fit:cover;transition:transform 0.1s linear;transform:translateY(0)}}
        .cover-gradient{{position:absolute;inset:0;background:linear-gradient(to bottom,transparent 30%,rgba(2,6,23,0.4) 60%,rgba(2,6,23,0.95) 100%);pointer-events:none;z-index:1}}
        .cover-glow{{position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(14,165,233,0.15) 0%,transparent 70%);pointer-events:none;z-index:2}}
        .cover-edit-btn{{position:absolute;top:12px;left:12px;background:rgba(0,0,0,0.5);backdrop-filter:blur(15px);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:5;border:1px solid rgba(255,255,255,0.2);color:#fff;font-size:14px;transition:all 0.3s;box-shadow:0 4px 15px rgba(0,0,0,0.3)}}
        .cover-edit-btn:hover{{background:rgba(14,165,233,0.4);}}
        .btn-back{{position:fixed;top:20px;right:20px;background:rgba(0,0,0,0.5);backdrop-filter:blur(15px);width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:50;border:1px solid rgba(255,255,255,0.2);color:#fff;font-size:16px;transition:all 0.3s}}
        .btn-back:hover{{background:rgba(14,165,233,0.3);}}
        .avatar-wrap{{position:relative;z-index:2;margin-top:-60px;display:flex;justify-content:center}}
        .avatar-lg{{width:120px;height:120px;border-radius:50%;overflow:hidden;cursor:pointer;background:linear-gradient(135deg,#0ea5e9,#06b6d4,#7dd3fc);padding:3px;box-shadow:0 0 30px rgba(14,165,233,0.4),0 0 60px rgba(14,165,233,0.1);animation:avatarGlow 3s ease-in-out infinite}}
        @keyframes avatarGlow{{0%,100%{{box-shadow:0 0 30px rgba(14,165,233,0.4),0 0 60px rgba(14,165,233,0.1)}}50%{{box-shadow:0 0 40px rgba(6,182,212,0.7),0 0 80px rgba(14,165,233,0.3)}}}}
        .avatar-lg img{{width:100%;height:100%;object-fit:cover;border-radius:50%;border:3px solid var(--bg)}}
        .avatar-edit-btn{{position:absolute;bottom:5px;right:5px;width:30px;height:30px;background:var(--accent);border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;border:2px solid var(--bg);color:#fff;font-size:12px;box-shadow:0 0 15px rgba(14,165,233,0.5)}}
        .online-dot{{position:absolute;top:10px;right:10px;width:18px;height:18px;background:#22c55e;border-radius:50%;border:3px solid var(--bg);z-index:3;box-shadow:0 0 10px rgba(34,197,94,0.6)}}
        .profile-info{{padding:20px 20px 10px;text-align:center}}
        .username{{font-size:22px;font-weight:800;margin-bottom:4px;display:flex;align-items:center;justify-content:center;gap:8px}}
        .bio-text{{font-size:13px;opacity:0.7;margin-bottom:8px;max-width:320px;margin-left:auto;margin-right:auto;line-height:1.5}}
        .contact-info{{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-bottom:8px;font-size:12px}}
        .contact-info a{{color:var(--accent2);text-decoration:none;display:flex;align-items:center;gap:5px;background:rgba(255,255,255,0.03);padding:6px 14px;border-radius:20px;border:1px solid var(--border);transition:all 0.3s}}
        .contact-info a:hover{{background:rgba(14,165,233,0.1);}}
        .last-seen{{font-size:11px;opacity:0.5;display:flex;align-items:center;justify-content:center;gap:5px;margin-top:6px}}
        .stats-row{{display:flex;justify-content:center;gap:30px;margin:15px 20px;padding:18px;background:rgba(255,255,255,0.03);backdrop-filter:blur(20px);border-radius:20px;border:1px solid var(--border);box-shadow:0 8px 32px rgba(0,0,0,0.2)}}
        .stat-item{{text-align:center;cursor:pointer;transition:transform 0.2s}}
        .stat-item:hover{{transform:scale(1.05)}}
        .stat-val{{font-size:20px;font-weight:700;color:var(--accent2)}}
        .stat-lbl{{font-size:10px;opacity:0.6;margin-top:2px}}
        .action-btns{{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:0 20px 20px}}
        .btn{{background:rgba(255,255,255,0.05);border:1px solid var(--border);padding:10px 20px;border-radius:25px;color:#fff;cursor:pointer;font-size:13px;transition:all 0.3s;display:flex;align-items:center;gap:6px;backdrop-filter:blur(10px)}}
        .btn:hover{{background:rgba(14,165,233,0.1);border-color:var(--accent);}}
        .btn-primary{{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;font-weight:700;color:#fff;box-shadow:0 8px 25px rgba(14,165,233,0.4)}}
        .btn-primary:hover{{transform:translateY(-2px);}}
        .section-title{{font-size:16px;font-weight:700;padding:0 20px;margin-bottom:12px;display:flex;align-items:center;gap:8px}}
        .videos-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;padding:0 8px 100px}}
        .video-grid-item{{aspect-ratio:9/16;position:relative;overflow:hidden;cursor:pointer;background:#000;border-radius:4px}}
        .video-grid-item video{{width:100%;height:100%;object-fit:cover}}
        .video-grid-item .grid-play-icon{{position:absolute;bottom:4px;left:4px;font-size:14px;color:#fff;z-index:1;opacity:0.8}}
        .video-grid-item .grid-views{{position:absolute;bottom:4px;right:4px;font-size:10px;color:#fff;z-index:1;display:flex;align-items:center;gap:3px;opacity:0.8}}
        .empty-state{{text-align:center;opacity:0.5;padding:40px 20px}}
        .empty-state i{{font-size:48px;color:var(--accent);margin-bottom:12px;display:block}}
        .badge-verified{{background:linear-gradient(135deg,#0ea5e9,#06b6d4);color:#fff;font-size:12px;padding:3px 6px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;font-weight:bold;box-shadow:0 0 15px rgba(56,189,248,0.6);animation:verifyGlow 2s ease-in-out infinite}}
        @keyframes verifyGlow{{0%,100%{{box-shadow:0 0 15px rgba(56,189,248,0.6)}}50%{{box-shadow:0 0 25px rgba(56,189,248,0.9)}}}}
        .edit-panel{{position:fixed;bottom:0;left:0;right:0;background:rgba(2,6,23,0.98);backdrop-filter:blur(40px);border-top:2px solid var(--accent);border-radius:var(--radius) var(--radius) 0 0;padding:24px 20px 40px;z-index:200;transform:translateY(100%);transition:transform 0.4s cubic-bezier(0.4,0,0.2,1);max-height:80vh;overflow-y:auto;}}
        .edit-panel.show{{transform:translateY(0)}}
        .edit-panel h3{{font-size:18px;font-weight:700;margin-bottom:20px;color:var(--accent2);text-align:center}}
        .edit-panel label{{display:block;font-size:12px;opacity:0.7;margin-bottom:6px;margin-top:14px}}
        .edit-panel input,.edit-panel textarea{{width:100%;padding:12px 16px;border-radius:14px;background:rgba(255,255,255,0.03);border:1px solid var(--border);color:#fff;font-size:14px;outline:none;resize:none;font-family:'Segoe UI',sans-serif;transition:border 0.3s}}
        .edit-panel input:focus,.edit-panel textarea:focus{{border-color:var(--accent);}}
        .edit-actions{{display:flex;gap:10px;margin-top:20px}}
        .edit-actions button{{flex:1;padding:12px;border-radius:25px;font-weight:700;cursor:pointer;font-size:14px;transition:all 0.3s}}
        .btn-save{{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;color:#fff}}
        .btn-cancel{{background:rgba(255,255,255,0.05);border:1px solid var(--border);color:#fff}}
        .overlay-panel{{position:fixed;inset:0;background:rgba(0,0,0,0.7);z-index:150;display:none}}
        .overlay-panel.show{{display:block}}

        /* Admin Panel (بقية الكود كما هو) */
        .admin-panel{{padding:0 8px;margin:0 8px 100px 8px}}
        .admin-panel h3{{color:#38bdf8;font-size:20px;margin-bottom:20px;display:flex;align-items:center;gap:10px;font-weight:700}}
        .admin-stats-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-bottom:24px}}
        .stat-card{{background:rgba(14,165,233,0.06);border:1px solid rgba(14,165,233,0.15);border-radius:16px;padding:16px;display:flex;align-items:center;gap:14px;backdrop-filter:blur(10px)}}
        .stat-icon{{width:44px;height:44px;border-radius:12px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-size:20px;box-shadow:0 4px 15px rgba(14,165,233,0.3)}}
        .stat-info h4{{font-size:12px;color:rgba(255,255,255,0.5);margin-bottom:4px;font-weight:500}}
        .stat-info span{{font-size:22px;font-weight:800}}
        .admin-user-item{{display:flex;align-items:center;justify-content:space-between;padding:10px 8px;border-bottom:1px solid rgba(255,255,255,0.03);transition:background 0.2s;border-radius:8px}}
        .admin-user-item:hover{{background:rgba(14,165,233,0.04)}}
        .admin-user-info{{display:flex;align-items:center;gap:12px;flex:1;min-width:0}}
        .admin-avatar{{width:40px;height:40px;border-radius:50%;overflow:hidden;border:2px solid rgba(14,165,233,0.3);flex-shrink:0}}
        .admin-avatar img{{width:100%;height:100%;object-fit:cover}}
        .admin-user-details h4{{font-weight:600;font-size:15px}}
        .admin-user-details p{{font-size:11px;color:rgba(255,255,255,0.4);margin-top:2px}}
        .admin-user-actions{{display:flex;gap:8px;align-items:center;flex-shrink:0}}
        .admin-btn{{border:none;border-radius:20px;padding:8px 16px;font-size:12px;font-weight:700;cursor:pointer;transition:all 0.2s;display:flex;align-items:center;gap:5px}}
        .btn-ban{{background:rgba(255,255,255,0.1);color:#fff;border:1px solid rgba(255,255,255,0.1)}}
        .btn-unban{{background:rgba(34,197,94,0.1);color:#4ade80;border:1px solid rgba(34,197,94,0.2)}}
        .btn-verify{{background:linear-gradient(135deg,#0ea5e9,#06b6d4);color:#fff;box-shadow:0 4px 12px rgba(14,165,233,0.3)}}
        .btn-delete-video{{background:rgba(239,68,68,0.1);color:#f87171;border:1px solid rgba(239,68,68,0.2)}}
        .btn-delete-video:hover{{background:rgba(239,68,68,0.3)}}
    </style>
</head>
<body>

<div class="load-center" id="loader" style="display:flex;align-items:center;justify-content:center;min-height:80vh;flex-direction:column;gap:12px;color:rgba(255,255,255,0.5)">
    <div class="spinner"></div><span>☁️ تحميل الملف...</span>
</div>

<div id="content" style="display:none">
    <div class="cover-section" id="coverSection" onmousemove="parallaxCover(event)">
        <img class="cover-img" id="coverImg" src="" alt="cover" style="display:none">
        <div class="cover-gradient"></div>
        <div class="cover-glow"></div>
        <div class="cover-edit-btn" id="coverEditBtn" onclick="event.stopPropagation();document.getElementById('coverInput').click()" style="display:none">
            <i class="fas fa-camera"></i>
        </div>
    </div>
    <input type="file" id="coverInput" accept="image/*" style="display:none" onchange="uploadCover(this)">
    
    <button class="btn-back" onclick="history.back()"><i class="fas fa-arrow-right"></i></button>
    
    <div class="avatar-wrap">
        <div class="avatar-lg" id="avatarDisplay">
            <img src="" alt="avatar" id="avatarImg">
            <div class="avatar-edit-btn" id="avatarEditBtn" onclick="event.stopPropagation();document.getElementById('avatarInput').click()" style="display:none">
                <i class="fas fa-camera"></i>
            </div>
            <div class="online-dot" id="onlineDot" style="display:none"></div>
        </div>
    </div>
    <input type="file" id="avatarInput" accept="image/*" style="display:none" onchange="uploadAvatar(this)">

    <div class="profile-info">
        <div class="username"><span id="nameDisplay"></span></div>
        <div class="bio-text" id="bioDisplay"></div>
        <div class="contact-info" id="contactInfo"></div>
        <div class="last-seen" id="lastSeenDisplay"></div>
    </div>

    <div class="stats-row">
        <div class="stat-item" onclick="showList('following')"><div class="stat-val" id="statFollowing">0</div><div class="stat-lbl">يتابع</div></div>
        <div class="stat-item" onclick="showList('followers')"><div class="stat-val" id="statFollowers">0</div><div class="stat-lbl">متابع</div></div>
        <div class="stat-item"><div class="stat-val" id="statLikes">0</div><div class="stat-lbl">إعجابات</div></div>
    </div>

    <div class="action-btns" id="actionsBar"></div>

    <div class="section-title"><i class="fas fa-video" style="color:var(--accent)"></i> الفيديوهات</div>
    <div class="videos-grid" id="videosGrid"></div>
</div>

<div class="overlay-panel" id="overlayPanel" onclick="closeEditPanel()"></div>
<div class="edit-panel" id="editPanel">
    <h3>☁️ لوحة تعديل الملف الشخصي</h3>
    <label>👤 اسم المستخدم</label>
    <input type="text" id="editUsername" placeholder="اسم المستخدم">
    <label>📝 السيرة الذاتية</label>
    <textarea id="editBio" placeholder="اكتب شيئاً عن نفسك..."></textarea>
    <label>🌐 الموقع الإلكتروني</label>
    <input type="text" id="editWebsite" placeholder="https://example.com" dir="ltr">
    <label>📧 البريد الإلكتروني</label>
    <input type="text" id="editContactEmail" placeholder="example@email.com" dir="ltr">
    <label>🎨 لون الغلاف</label>
    <div id="coverColors" style="display:flex;gap:8px;flex-wrap:wrap;margin-top:8px"></div>
    <div class="edit-actions">
        <button class="btn-cancel" onclick="closeEditPanel()">إلغاء</button>
        <button class="btn-save" onclick="saveProfile()"><i class="fas fa-save"></i> حفظ التغييرات</button>
    </div>
</div>

<div class="toast-msg" id="toastMsg">✅ تم</div>

<script src="firebase-config.js"></script>
<script>
    let profileUserId = null, currentUser = null, currentUserData = null, allVideos = [], allUsers = {{}}, isOwnProfile = false, _selectedCover = null;

    window.parallaxCover = function(event) {{
        const img = document.getElementById('coverImg');
        if(!img || !img.src || img.style.display === 'none') return;
        const cover = document.getElementById('coverSection');
        const rect = cover.getBoundingClientRect();
        const y = event.clientY - rect.top;
        const percent = (y / rect.height - 0.5) * 0.15;
        img.style.transform = `translateY(${{percent * 100}}px)`;
    }};

    auth.onAuthStateChanged(async u => {{
        if(!u) {{ window.location.href = 'auth.html'; return; }}
        currentUser = u;
        const params = new URLSearchParams(window.location.search);
        profileUserId = params.get('uid') || u.uid;
        isOwnProfile = (profileUserId === u.uid);
        const snap = await db.ref('users/' + u.uid).get();
        if(snap.exists()) currentUserData = {{uid: u.uid, ...snap.val()}};
        await loadAll();
        await loadProfile();
        if(!isOwnProfile) {{
            db.ref('presence/' + profileUserId).on('value', s => {{
                const isOnline = s.val();
                const dot = document.getElementById('onlineDot');
                const lastSeen = document.getElementById('lastSeenDisplay');
                if(dot) dot.style.display = isOnline ? 'block' : 'none';
                if(lastSeen) {{
                    const userData = allUsers[profileUserId];
                    if(userData) lastSeen.innerHTML = isOnline ? '<i class="fas fa-circle" style="color:#22c55e;font-size:8px"></i> نشط الآن' : '<i class="fas fa-clock"></i> آخر ظهور: ' + formatTime(userData.lastSeen);
                }}
            }});
        }}
        document.getElementById('loader').style.display = 'none';
        document.getElementById('content').style.display = 'block';
    }});

    async function loadAll() {{
        const us = await db.ref('users').once('value'); allUsers = us.val() || {{}};
        const vs = await db.ref('videos').once('value'); allVideos = Object.entries(vs.val() || {{}}).map(([k, v]) => ({{id: k, ...v}}));
    }}

    async function loadProfile() {{
        const u = allUsers[profileUserId];
        if(!u) {{ document.getElementById('content').innerHTML = '<div class="empty-state" style="padding-top:100px"><i class="fas fa-user-slash"></i><p>المستخدم غير موجود</p></div>'; return; }}
        const skyVerifiedBadge = u.isVerified ? '<span class="badge-verified"><i class="fas fa-check"></i></span>' : '';
        document.getElementById('nameDisplay').innerHTML = '@' + (u.username || 'مستخدم') + ' ' + skyVerifiedBadge;
        document.getElementById('bioDisplay').innerText = u.bio || 'لم تتم إضافة سيرة ذاتية بعد';
        const contactInfo = document.getElementById('contactInfo');
        let contactHTML = '';
        if(u.website) contactHTML += `<a href="${{u.website}}" target="_blank"><i class="fas fa-globe"></i> ${{u.website.replace('https://','').replace('http://','')}}</a>`;
        if(u.contactEmail) contactHTML += `<a href="mailto:${{u.contactEmail}}"><i class="fas fa-envelope"></i> ${{u.contactEmail}}</a>`;
        contactInfo.innerHTML = contactHTML;
        document.getElementById('statFollowing').innerText = Object.keys(u.following || {{}}).length;
        document.getElementById('statFollowers').innerText = Object.keys(u.followers || {{}}).length;
        const uvs = allVideos.filter(v => v.sender === profileUserId);
        document.getElementById('statLikes').innerText = uvs.reduce((s, v) => s + (v.likes || 0), 0);
        const coverImg = document.getElementById('coverImg');
        if(u.coverImageUrl) {{ coverImg.src = u.coverImageUrl; coverImg.style.display = 'block'; }}
        else {{ document.getElementById('coverSection').style.background = u.coverColor || COVER_COLORS[0]; coverImg.style.display = 'none'; }}
        document.getElementById('avatarImg').src = u.avatarUrl || (DICEBEAR_URL + '?seed=' + profileUserId);
        if(isOwnProfile) {{ document.getElementById('avatarEditBtn').style.display = 'flex'; document.getElementById('coverEditBtn').style.display = 'flex'; }}
        const lastSeen = document.getElementById('lastSeenDisplay');
        if(!isOwnProfile) {{
            const presenceSnap = await db.ref('presence/' + profileUserId).get();
            const isOnline = presenceSnap.val();
            document.getElementById('onlineDot').style.display = isOnline ? 'block' : 'none';
            lastSeen.innerHTML = isOnline ? '<i class="fas fa-circle" style="color:#22c55e;font-size:8px"></i> نشط الآن' : '<i class="fas fa-clock"></i> آخر ظهور: ' + formatTime(u.lastSeen || u.createdAt);
        }}

        const grid = document.getElementById('videosGrid');
        grid.innerHTML = '';
        if(!uvs.length) {{ grid.innerHTML = '<div class="empty-state" style="grid-column:1/-1"><i class="fas fa-video-slash"></i><p>لا توجد فيديوهات</p></div>'; }}
        else {{
            uvs.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0)).forEach(v => {{
                const d = document.createElement('div'); d.className = 'video-grid-item';
                d.onclick = () => window.open(v.url, '_blank');
                d.innerHTML = `${{v.thumbnail ? `<img src="${{v.thumbnail}}" style="width:100%;height:100%;object-fit:cover">` : '<div style="width:100%;height:100%;background:#111;display:flex;align-items:center;justify-content:center"><i class="fas fa-play" style="color:#555;font-size:24px"></i></div>'}}<div class="grid-play-icon"><i class="fas fa-play"></i></div><div class="grid-views"><i class="fas fa-heart" style="color:var(--accent)"></i> ${{v.likes || 0}}</div>`;
                grid.appendChild(d);
            }});
        }}

        const actionsBar = document.getElementById('actionsBar');
        if(isOwnProfile) {{
            actionsBar.innerHTML = `<button class="btn btn-primary" onclick="openEditPanel()"><i class="fas fa-edit"></i> تعديل الملف</button><button class="btn" onclick="window.location.href='chat.html'"><i class="fas fa-envelope"></i> الرسائل</button><button class="btn" onclick="auth.signOut();window.location.href='auth.html'"><i class="fas fa-sign-out-alt"></i> خروج</button>`;
        }} else {{
            const isFollowing = currentUserData?.following?.[profileUserId];
            actionsBar.innerHTML = `<button class="btn btn-follow ${{isFollowing ? 'following' : ''}}" id="followBtn" onclick="toggleFollowUser()">${{isFollowing ? '<i class="fas fa-user-check"></i> متابع' : '<i class="fas fa-user-plus"></i> متابعة'}}</button><button class="btn btn-primary" onclick="window.location.href='chat.html?uid=${{profileUserId}}'"><i class="fas fa-comment"></i> مراسلة</button><button class="btn" onclick="copyProfile()"><i class="fas fa-copy"></i> نسخ المعلومات</button>`;
        }}
        if(isOwnProfile && ADMIN_EMAILS.includes(currentUser?.email)) {{ loadAdminPanel(); }}
    }}

    function openEditPanel() {{
        const u = allUsers[profileUserId] || currentUserData;
        document.getElementById('editUsername').value = u.username || '';
        document.getElementById('editBio').value = u.bio || '';
        document.getElementById('editWebsite').value = u.website || '';
        document.getElementById('editContactEmail').value = u.contactEmail || '';
        _selectedCover = u.coverColor || COVER_COLORS[0];
        const colorsDiv = document.getElementById('coverColors');
        colorsDiv.innerHTML = COVER_COLORS.map((c, i) => `<div onclick="selectCover('${{c.replace(/'/g, "\\\\'")}}', this)" style="width:40px;height:40px;border-radius:50%;background:${{c}};cursor:pointer;border:3px solid ${{_selectedCover === c ? '#fff' : 'transparent'}};transition:all 0.2s;box-shadow:0 4px 15px rgba(0,0,0,0.3)" title="غلاف ${{i+1}}"></div>`).join('');
        document.getElementById('editPanel').classList.add('show'); document.getElementById('overlayPanel').classList.add('show');
    }}
    function closeEditPanel() {{ document.getElementById('editPanel').classList.remove('show'); document.getElementById('overlayPanel').classList.remove('show'); }}
    function selectCover(color, el) {{ _selectedCover = color; document.getElementById('coverSection').style.background = color; document.getElementById('coverImg').style.display = 'none'; document.querySelectorAll('#coverColors div').forEach(d => d.style.borderColor = 'transparent'); el.style.borderColor = '#fff'; }}
    async function saveProfile() {{
        const username = document.getElementById('editUsername').value.trim();
        const bio = document.getElementById('editBio').value.trim();
        const website = document.getElementById('editWebsite').value.trim();
        const contactEmail = document.getElementById('editContactEmail').value.trim();
        if(!username || username.length < 3) {{ showToast('❌ اسم المستخدم 3 أحرف على الأقل'); return; }}
        const updates = {{username, bio, website, contactEmail}};
        if(_selectedCover) updates.coverColor = _selectedCover;
        try {{ await db.ref('users/' + profileUserId).update(updates); closeEditPanel(); await loadAll(); await loadProfile(); showToast('✅ تم حفظ التغييرات بنجاح'); }} catch(e) {{ showToast('❌ حدث خطأ'); }}
    }}
    async function uploadAvatar(inp) {{
        const file = inp.files[0]; if(!file) return; showToast('⏳ جاري رفع الصورة...');
        const fd = new FormData(); fd.append('file', file); fd.append('upload_preset', UPLOAD_PRESET);
        try {{
            const res = await fetch('https://api.cloudinary.com/v1_1/' + CLOUD_NAME + '/image/upload', {{method: 'POST', body: fd}});
            const data = await res.json();
            if(data.secure_url) {{ await db.ref('users/' + profileUserId).update({{avatarUrl: data.secure_url, hasCustomAvatar: true}}); document.getElementById('avatarImg').src = data.secure_url; showToast('✅ تم تحديث الصورة الشخصية'); }}
        }} catch(e) {{ showToast('❌ خطأ في الرفع'); }} inp.value = '';
    }}
    async function uploadCover(inp) {{
        const file = inp.files[0]; if(!file) return; showToast('⏳ جاري رفع الغلاف...');
        const fd = new FormData(); fd.append('file', file); fd.append('upload_preset', UPLOAD_PRESET);
        try {{
            const res = await fetch('https://api.cloudinary.com/v1_1/' + CLOUD_NAME + '/image/upload', {{method: 'POST', body: fd}});
            const data = await res.json();
            if(data.secure_url) {{ await db.ref('users/' + profileUserId).update({{coverImageUrl: data.secure_url, hasCustomCover: true}}); const coverImg = document.getElementById('coverImg'); coverImg.src = data.secure_url; coverImg.style.display = 'block'; document.getElementById('coverSection').style.background = 'none'; showToast('✅ تم تحديث الغلاف'); }}
        }} catch(e) {{ showToast('❌ خطأ في الرفع'); }} inp.value = '';
    }}
    async function toggleFollowUser() {{
        if(!currentUser || isOwnProfile) return;
        const btn = document.getElementById('followBtn');
        const userRef = db.ref('users/' + currentUser.uid + '/following/' + profileUserId);
        const targetRef = db.ref('users/' + profileUserId + '/followers/' + currentUser.uid);
        const snap = await userRef.get();
        if(snap.exists()) {{ await userRef.remove(); await targetRef.remove(); btn.innerHTML = '<i class="fas fa-user-plus"></i> متابعة'; btn.classList.remove('following'); }}
        else {{ await userRef.set(true); await targetRef.set(true); btn.innerHTML = '<i class="fas fa-user-check"></i> متابع'; btn.classList.add('following'); }}
        await loadAll(); await loadProfile();
    }}
    async function copyProfile() {{
        const u = allUsers[profileUserId];
        const text = `👤 @${{u.username || 'مستخدم'}}\\n📝 ${{u.bio || ''}}\\n☁️ MNAENCA 2026`;
        try {{ await navigator.clipboard.writeText(text); }} catch(e) {{ const ta = document.createElement('textarea'); ta.value = text; document.body.appendChild(ta); ta.select(); document.execCommand('copy'); document.body.removeChild(ta); }}
        showToast('✅ تم نسخ معلومات الملف الشخصي');
    }}
    function showList(type) {{
        const u = allUsers[profileUserId];
        const list = type === 'followers' ? (u?.followers || {{}}) : (u?.following || {{}});
        const ids = Object.keys(list);
        if(!ids.length) {{ alert('لا يوجد'); return; }}
        const names = ids.map(id => {{ const user = allUsers[id]; return user ? '@' + user.username : 'مستخدم'; }}).join('\\n');
        alert((type === 'followers' ? 'المتابِعون' : 'المتابَعون') + ':\\n' + names);
    }}
    function showToast(msg) {{ const toast = document.getElementById('toastMsg'); toast.innerText = msg; toast.classList.add('show'); setTimeout(() => toast.classList.remove('show'), 2500); }}
    function formatTime(ts) {{
        if(!ts) return 'غير معروف';
        const diff = Date.now() - ts;
        const mins = Math.floor(diff / 60000);
        const hours = Math.floor(diff / 3600000);
        const days = Math.floor(diff / 86400000);
        if(mins < 1) return 'الآن';
        if(mins < 60) return 'منذ ' + mins + ' دقيقة';
        if(hours < 24) return 'منذ ' + hours + ' ساعة';
        if(days < 7) return 'منذ ' + days + ' يوم';
        return new Date(ts).toLocaleDateString('ar-SA');
    }}

    async function loadAdminPanel() {{
        const grid = document.getElementById('videosGrid'); if(!grid) return;
        const oldPanel = document.getElementById('adminPanelContainer'); if(oldPanel) oldPanel.remove();
        const adminDiv = document.createElement('div'); adminDiv.id = 'adminPanelContainer'; adminDiv.className = 'admin-panel';
        const totalUsers = Object.keys(allUsers).length;
        const totalVideos = allVideos.length;
        const totalVerified = Object.values(allUsers).filter(u => u.isVerified).length;
        const totalBanned = Object.values(allUsers).filter(u => u.banned).length;
        adminDiv.innerHTML = `<h3><i class="fas fa-crown"></i> لوحة تحكم الأدمن</h3>
            <div class="admin-stats-grid">
                <div class="stat-card"><div class="stat-icon"><i class="fas fa-users"></i></div><div class="stat-info"><h4>المستخدمين</h4><span>${{totalUsers}}</span></div></div>
                <div class="stat-card"><div class="stat-icon" style="background:linear-gradient(135deg,#f59e0b,#0ea5e9)"><i class="fas fa-video"></i></div><div class="stat-info"><h4>فيديوهات</h4><span>${{totalVideos}}</span></div></div>
                <div class="stat-card"><div class="stat-icon"><i class="fas fa-check-circle"></i></div><div class="stat-info"><h4>موثقين</h4><span>${{totalVerified}}</span></div></div>
                <div class="stat-card"><div class="stat-icon" style="background:linear-gradient(135deg,#ef4444,#dc2626)"><i class="fas fa-ban"></i></div><div class="stat-info"><h4>محظورين</h4><span>${{totalBanned}}</span></div></div>
            </div>
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;color:rgba(255,255,255,0.6);font-size:13px;font-weight:600;border-bottom:1px solid rgba(14,165,233,0.1);padding-bottom:8px">
                <span>📋 قائمة المستخدمين</span><span style="font-size:11px">${{totalUsers}} إجمالي</span>
            </div>
            <div id="adminDynamicList"></div>
            <div style="display:flex;justify-content:space-between;align-items:center;margin-top:24px;margin-bottom:14px;color:rgba(255,255,255,0.6);font-size:13px;font-weight:600;border-bottom:1px solid rgba(14,165,233,0.1);padding-bottom:8px">
                <span>🎬 جميع الفيديوهات</span><span style="font-size:11px">${{totalVideos}} إجمالي</span>
            </div>
            <div id="adminVideosList"></div>`;
        grid.after(adminDiv);
        loadAdminUsersList(); loadAdminVideosList();
    }}

    function loadAdminUsersList() {{
        const listContainer = document.getElementById('adminDynamicList'); if(!listContainer) return;
        const usersArray = Object.entries(allUsers).sort(([, a], [, b]) => (b.createdAt || 0) - (a.createdAt || 0)).slice(0, 15);
        if(!usersArray.length) {{ listContainer.innerHTML = '<div style="text-align:center;opacity:0.5;padding:20px">لا يوجد مستخدمون</div>'; return; }}
        listContainer.innerHTML = usersArray.map(([id, u]) => {{
            const avatar = u.avatarUrl || (DICEBEAR_URL + '?seed=' + id);
            const isVerified = u.isVerified;
            const isBanned = u.banned;
            const verifiedBadgeHtml = isVerified ? '<span class="badge-verified"><i class="fas fa-check"></i></span>' : '';
            let actionBtns = '';
            if(isBanned) {{ actionBtns = `<button class="admin-btn btn-unban" onclick="toggleBanUser('${{id}}')"><i class="fas fa-undo"></i> إلغاء الحظر</button>`; }}
            else {{ actionBtns = `<button class="admin-btn btn-verify ${{isVerified ? 'unverify' : ''}}" onclick="toggleVerifyUser('${{id}}')">${{isVerified ? '<i class="fas fa-times-circle"></i> إلغاء' : '<i class="fas fa-check-circle"></i> توثيق'}}</button><button class="admin-btn btn-ban" onclick="toggleBanUser('${{id}}')"><i class="fas fa-ban"></i> حظر</button>`; }}
            return `<div class="admin-user-item"><div class="admin-user-info" onclick="openUserProfile('${{id}}')" style="cursor:pointer"><div class="admin-avatar"><img src="${{avatar}}"></div><div class="admin-user-details"><h4>@${{u.username || 'مستخدم'}} ${{verifiedBadgeHtml}}</h4><p>${{u.email || ''}}</p></div></div><div class="admin-user-actions">${{actionBtns}}</div></div>`;
        }}).join('');
    }}

    function loadAdminVideosList() {{
        const listContainer = document.getElementById('adminVideosList'); if(!listContainer) return;
        const videosArray = allVideos.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0)).slice(0, 20);
        if(!videosArray.length) {{ listContainer.innerHTML = '<div style="text-align:center;opacity:0.5;padding:20px">لا توجد فيديوهات</div>'; return; }}
        listContainer.innerHTML = videosArray.map(v => {{
            const user = allUsers[v.sender] || {{username: v.senderName || 'مستخدم'}};
            const desc = (v.description || 'بدون وصف').substring(0, 40);
            return `<div class="admin-user-item"><div class="admin-user-info"><div class="admin-avatar" style="border-radius:8px;width:50px;height:70px">${{v.thumbnail ? `<img src="${{v.thumbnail}}" style="object-fit:cover">` : ''}}</div><div class="admin-user-details"><p style="font-size:12px">${{desc}}</p><span style="font-size:10px;opacity:0.4">@${{user.username}} · ❤️ ${{v.likes || 0}}</span></div></div><div class="admin-user-actions"><button class="admin-btn btn-delete-video" onclick="deleteVideo('${{v.id}}')"><i class="fas fa-trash"></i> حذف</button></div></div>`;
        }}).join('');
    }}

    window.deleteVideo = async function(videoId) {{ if(!confirm('هل أنت متأكد من حذف هذا الفيديو؟')) return; try {{ await db.ref('videos/' + videoId).remove(); showToast('🗑️ تم حذف الفيديو بنجاح'); await loadAll(); await loadProfile(); loadAdminVideosList(); }} catch(e) {{ showToast('❌ فشل حذف الفيديو'); }} }};
    window.toggleVerifyUser = async function(id) {{ const snap = await db.ref('users/' + id).once('value'); const data = snap.val(); if(!data) return; const newState = !data.isVerified; if(!confirm(`تأكيد ${{newState ? 'توثيق' : 'إلغاء توثيق'}} @${{data.username || 'المستخدم'}}؟`)) return; await db.ref('users/' + id).update({{isVerified: newState, verifiedAt: newState ? Date.now() : null, verifiedBy: newState ? currentUser.uid : null}}); await loadAll(); await loadProfile(); showToast(`✅ تم ${{newState ? 'توثيق' : 'إلغاء توثيق'}} المستخدم`); loadAdminUsersList(); }};
    window.toggleBanUser = async function(id) {{ const snap = await db.ref('users/' + id).once('value'); const data = snap.val(); if(!data) return; const newState = !data.banned; if(!confirm(`تأكيد ${{newState ? 'حظر' : 'إلغاء حظر'}} @${{data.username || 'المستخدم'}}؟`)) return; await db.ref('users/' + id).update({{banned: newState, bannedAt: newState ? Date.now() : null, bannedBy: newState ? currentUser.uid : null}}); await loadAll(); await loadProfile(); showToast(`✅ تم ${{newState ? 'حظر' : 'إلغاء حظر'}} المستخدم`); loadAdminUsersList(); }};
    window.openUserProfile = function(id) {{ if(id === currentUser?.uid) window.location.href = 'profile.html'; else window.location.href = 'profile.html?uid=' + id; }};

    console.log('☁️ MNAENCA Profile Ready ✨');
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# ☁️ 5-9. الملفات المتبقية (upload, chat, explore, notifications, settings)
# ═══════════════════════════════════════════════════════════

def build_upload():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>☁️ MNAENCA | رفع فيديو</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{min-height:100vh;overflow-y:auto}}
        .header{{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);background:rgba(2,6,23,0.8);backdrop-filter:blur(20px);position:sticky;top:0;z-index:10}}
        .btn-back{{background:rgba(14,165,233,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}}
        .container{{max-width:500px;margin:0 auto;padding:20px}}
        .dropzone{{border:2px dashed rgba(14,165,233,0.3);border-radius:20px;padding:50px 20px;text-align:center;cursor:pointer;background:var(--glass);margin-bottom:20px}}
        .dropzone i{{font-size:48px;color:var(--accent)}}
        .dropzone video{{width:100%;max-height:250px;object-fit:contain;margin-top:12px;border-radius:12px;display:none}}
        .form-card{{background:rgba(14,165,233,0.03);border:1px solid var(--border);border-radius:20px;padding:20px}}
        .form-card label{{display:block;font-size:13px;opacity:0.7;margin-bottom:6px;margin-top:12px}}
        .form-card textarea,.form-card input{{width:100%;padding:14px 16px;border-radius:16px;background:rgba(14,165,233,0.04);border:1px solid var(--border);color:#fff;font-size:14px;outline:none;resize:none;font-family:'Segoe UI',sans-serif}}
        .progress-wrap{{display:none;margin:16px 0}}
        .progress-bar{{background:rgba(255,255,255,0.1);border-radius:30px;height:6px;overflow:hidden}}
        .progress-fill{{background:linear-gradient(90deg,var(--accent),var(--accent2));height:100%;border-radius:30px;width:0%}}
        .progress-text{{text-align:center;font-size:12px;margin-top:6px;color:var(--accent2)}}
        .btn-upload{{width:100%;padding:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;border-radius:30px;color:#fff;font-weight:700;font-size:15px;cursor:pointer;margin-top:16px;box-shadow:0 10px 25px rgba(14,165,233,0.4)}}
        .btn-upload:disabled{{opacity:0.5}}
        .status{{text-align:center;margin-top:12px;font-size:13px}}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2><i class="fas fa-cloud-upload-alt"></i> رفع فيديو جديد</h2></div>
<div class="container">
    <div class="dropzone" onclick="document.getElementById('videoFile').click()"><i class="fas fa-cloud-upload-alt"></i><p>اضغط لاختيار فيديو</p><span style="font-size:11px;opacity:0.5">MP4 - حتى 100MB</span><video id="preview" controls></video></div>
    <input type="file" id="videoFile" accept="video/*" style="display:none" onchange="onFilePick(this)">
    <div class="form-card">
        <label><i class="fas fa-pen"></i> وصف الفيديو</label><textarea id="vidDesc" placeholder="اكتب وصفاً... #هاشتاقات"></textarea>
        <label><i class="fas fa-music"></i> الموسيقى</label><input type="text" id="vidMusic" placeholder="Original Sound">
        <div class="progress-wrap" id="progressWrap"><div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div><div class="progress-text" id="progressText">0%</div></div>
        <button class="btn-upload" id="uploadBtn" onclick="upload()"><i class="fas fa-heart"></i> رفع الفيديو</button>
        <div class="status" id="status"></div>
    </div>
</div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null,currentUserData=null,selectedFile=null;
    auth.onAuthStateChanged(async u=>{{if(!u)window.location.href='auth.html';currentUser=u;const snap=await db.ref('users/'+u.uid).get();if(snap.exists())currentUserData={{uid:u.uid,...snap.val()}}}});
    function onFilePick(inp){{const f=inp.files[0];if(!f||!f.type.startsWith('video/')){{alert('اختر فيديو صحيح');return}}if(f.size>100*1024*1024){{alert('أقل من 100MB');return}}selectedFile=f;const r=new FileReader();r.onload=e=>{{const v=document.getElementById('preview');v.src=e.target.result;v.style.display='block'}};r.readAsDataURL(f)}}
    async function upload(){{
        if(!selectedFile){{alert('اختر فيديو');return}}if(!currentUser){{alert('سجل دخول');return}}
        const desc=document.getElementById('vidDesc').value;const music=document.getElementById('vidMusic').value||'Original Sound';
        const pw=document.getElementById('progressWrap');pw.style.display='block';const pf=document.getElementById('progressFill');pf.style.width='0%';const pt=document.getElementById('progressText');pt.innerText='0%';
        const st=document.getElementById('status');st.innerHTML='';const btn=document.getElementById('uploadBtn');btn.disabled=true;
        const fd=new FormData();fd.append('file',selectedFile);fd.append('upload_preset',UPLOAD_PRESET);
        const xhr=new XMLHttpRequest();xhr.open('POST','https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/video/upload');
        xhr.upload.onprogress=e=>{{if(e.lengthComputable){{const p=Math.round(e.loaded/e.total*100);pf.style.width=p+'%';pt.innerText=p+'%'}}}};
        xhr.onload=async()=>{{const r=JSON.parse(xhr.response.text);await db.ref('videos/').push({{url:r.secure_url,thumbnail:r.secure_url.replace('.mp4','.jpg'),description:desc,music:music,sender:currentUser.uid,senderName:currentUserData?.username,likes:0,likedBy:{{}},comments:{{}},timestamp:Date.now()}});st.innerHTML='✅ تم الرفع بنجاح!';st.style.color='#4ade80';setTimeout(()=>window.location.href='index.html',1500)}};
        xhr.onerror=()=>{{st.innerHTML='❌ فشل الرفع';btn.disabled=false}};xhr.send(fd);
    }}
</script>
</body>
</html>"""

def build_chat():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>☁️ MNAENCA | دردشة</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{height:100vh;display:flex;flex-direction:column}}
        .header{{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);background:rgba(2,6,23,0.8);backdrop-filter:blur(20px)}}
        .btn-back{{background:rgba(14,165,233,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}}
        .msgs{{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:8px}}
        .bubble{{max-width:80%;padding:10px 16px;border-radius:20px;word-break:break-word;font-size:14px;position:relative;animation:msgIn 0.3s ease}}
        @keyframes msgIn{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:translateY(0)}}}}
        .bubble.sent{{background:linear-gradient(135deg,var(--accent),var(--accent2));align-self:flex-end;color:#fff}}
        .bubble.received{{background:rgba(255,255,255,0.03);align-self:flex-start;border:1px solid rgba(255,255,255,0.1)}}
        .bubble img{{max-width:200px;border-radius:12px;cursor:pointer;margin-top:4px}}
        .bubble .time{{font-size:9px;opacity:0.6;margin-top:4px}}
        .input-bar{{display:flex;gap:10px;padding:12px;background:rgba(2,6,23,0.95);backdrop-filter:blur(20px);border-top:1px solid var(--border);align-items:center}}
        .input-bar input{{flex:1;padding:12px 16px;border-radius:30px;background:rgba(255,255,255,0.03);border:1px solid var(--border);color:#fff;font-size:14px;outline:none}}
        .btn-icon{{width:42px;height:42px;background:rgba(255,255,255,0.05);border:1px solid var(--border);border-radius:50%;color:#fff;cursor:pointer;font-size:18px;display:flex;align-items:center;justify-content:center}}
        .btn-send{{width:42px;height:42px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;border-radius:50%;color:#fff;cursor:pointer;font-size:18px;display:flex;align-items:center;justify-content:center}}
        .conv-item{{display:flex;align-items:center;gap:12px;padding:14px;border-bottom:1px solid var(--border);cursor:pointer}}
        .conv-item:hover{{background:rgba(255,255,255,0.03)}}
        .chat-avatar{{width:40px;height:40px;border-radius:50%;overflow:hidden;border:2px solid rgba(255,255,255,0.2)}}
        .chat-avatar img{{width:100%;height:100%;object-fit:cover}}
        .online-indicator{{width:10px;height:10px;background:#22c55e;border-radius:50%;display:inline-block;margin-left:6px}}
    </style>
</head>
<body>
<div id="loader" style="flex:1;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px"><div class="spinner"></div><span>☁️ تحميل...</span></div>
<div id="convView" style="display:none;flex:1;flex-direction:column;overflow:hidden"><div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2><i class="fas fa-comments"></i> المحادثات</h2></div><div id="convList" style="flex:1;overflow-y:auto"></div></div>
<div id="chatView" style="display:none;flex:1;flex-direction:column;overflow:hidden"><div class="header"><button class="btn-back" onclick="showConvs()"><i class="fas fa-arrow-right"></i></button><div class="chat-avatar" id="chatAvatar"></div><h3 id="chatName">محادثة</h3><span id="chatOnline" style="font-size:11px;opacity:0.5;margin-right:8px"></span></div><div class="msgs" id="msgsList"></div><div class="input-bar"><button class="btn-icon" onclick="sendImage()" title="إرسال صورة"><i class="fas fa-image"></i></button><input type="text" id="msgInput" placeholder="اكتب رسالة..." onkeydown="if(event.key==='Enter')sendMsg()"><button class="btn-send" onclick="sendMsg()"><i class="fas fa-paper-plane"></i></button><button class="btn-icon" onclick="copyChat()" title="نسخ المحادثة"><i class="fas fa-copy"></i></button></div></div>
<div class="toast-msg" id="toastMsg">✅ تم</div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null,allUsers={{}},chatUserId=null;
    auth.onAuthStateChanged(async u=>{{if(!u){{window.location.href='auth.html';return}}currentUser=u;const us=await db.ref('users').once('value');allUsers=us.val()||{{}};document.getElementById('loader').style.display='none';const params=new URLSearchParams(window.location.search);const targetUid=params.get('uid');if(targetUid){{openChat(targetUid)}}else{{showConvs()}}setInterval(()=>{{if(currentUser)db.ref('users/'+currentUser.uid+'/lastSeen').set(Date.now())}},60000)}});
    function showConvs(){{document.getElementById('chatView').style.display='none';document.getElementById('convView').style.display='flex';chatUserId=null;loadConvs()}}
    async function loadConvs(){{const cl=document.getElementById('convList');cl.innerHTML='';const snap=await db.ref('private_messages').once('value');const all=snap.val()||{{}};const found=new Set();Object.keys(all).forEach(cid=>{{const[u1,u2]=cid.split('_');const other=u1===currentUser.uid?u2:u2===currentUser.uid?u1:null;if(other&&!found.has(other)&&allUsers[other])found.add(other)}});if(!found.size){{cl.innerHTML='<div style="text-align:center;opacity:0.5;padding:40px">لا محادثات</div>';return}}found.forEach(uid=>{{const u=allUsers[uid];const d=document.createElement('div');d.className='conv-item';d.innerHTML=`<div class="chat-avatar"><img src="${{u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid)}}"></div><div><div style="font-weight:600">@${{u?.username||'?'}} ${{u?.isVerified?'<span style="color:#38bdf8;font-size:12px"><i class="fas fa-check-circle"></i></span>':''}}</div></div>`;d.onclick=()=>openChat(uid);cl.appendChild(d)}})}}
    async function openChat(uid){{chatUserId=uid;const u=allUsers[uid];document.getElementById('chatName').innerText='@'+(u?.username||'مستخدم');document.getElementById('chatAvatar').innerHTML=`<img src="${{u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid)}}">`;document.getElementById('convView').style.display='none';document.getElementById('chatView').style.display='flex';db.ref('presence/'+uid).on('value',s=>{{const online=s.val();document.getElementById('chatOnline').innerHTML=online?'<span class="online-indicator"></span> نشط الآن':'آخر ظهور: '+formatTime(u?.lastSeen)}});await loadMsgs()}}
    function getChatId(){{return[currentUser.uid,chatUserId].sort().join('_')}}
    async function loadMsgs(){{const ml=document.getElementById('msgsList');ml.innerHTML='';if(!chatUserId)return;const snap=await db.ref('private_messages/'+getChatId()).once('value');const ms=snap.val()||{{}};Object.values(ms).sort((a,b)=>a.timestamp-b.timestamp).forEach(m=>{{const sent=m.senderId===currentUser.uid;const d=document.createElement('div');d.className='bubble '+(sent?'sent':'received');d.innerHTML=`${{m.type==='image'?`<img src="${{m.imageUrl}}" onclick="window.open('${{m.imageUrl}}','_blank')">`:m.text}}<div class="time">${{new Date(m.timestamp).toLocaleTimeString('ar-SA')}}</div>`;ml.appendChild(d)}});ml.scrollTop=ml.scrollHeight}}
    async function sendMsg(){{const inp=document.getElementById('msgInput');const txt=inp.value.trim();if(!txt||!chatUserId)return;await db.ref('private_messages/'+getChatId()).push({{senderId:currentUser.uid,text:txt,type:'text',timestamp:Date.now()}});inp.value='';await loadMsgs()}}
    async function sendImage(){{if(!chatUserId)return;const inp=document.createElement('input');inp.type='file';inp.accept='image/*';inp.onchange=async(e)=>{{const file=e.target.files[0];if(!file)return;showToast('⏳ جاري رفع الصورة...');const fd=new FormData();fd.append('file',file);fd.append('upload_preset',UPLOAD_PRESET);const res=await fetch('https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/image/upload',{{method:'POST',body:fd}});const data=await res.json();if(data.secure_url){{await db.ref('private_messages/'+getChatId()).push({{senderId:currentUser.uid,type:'image',imageUrl:data.secure_url,timestamp:Date.now()}});await loadMsgs()}}}};inp.click()}}
    async function copyChat(){{if(!chatUserId)return;const snap=await db.ref('private_messages/'+getChatId()).once('value');const msgs=snap.val()||{{}};let text='💬 محادثة MNAENCA\\n'+'─'.repeat(30)+'\\n';Object.values(msgs).sort((a,b)=>a.timestamp-b.timestamp).forEach(m=>{{const sender=m.senderId===currentUser.uid?'أنت':(allUsers[m.senderId]?.username||'مستخدم');const content=m.type==='image'?'[صورة]':m.text;const time=new Date(m.timestamp).toLocaleTimeString('ar-SA');text+=`\\n${{sender}} (${{time}}):\\n${{content}}\\n`}});try{{await navigator.clipboard.writeText(text)}}catch(e){{const ta=document.createElement('textarea');ta.value=text;document.body.appendChild(ta);ta.select();document.execCommand('copy');document.body.removeChild(ta)}}showToast('✅ تم نسخ المحادثة')}}
    function showToast(msg){{const toast=document.getElementById('toastMsg');toast.innerText=msg;toast.classList.add('show');setTimeout(()=>toast.classList.remove('show'),2500)}}
    function formatTime(ts){{if(!ts)return'غير معروف';const diff=Date.now()-ts;const mins=Math.floor(diff/60000);const hours=Math.floor(diff/3600000);const days=Math.floor(diff/86400000);if(mins<1)return'الآن';if(mins<60)return'منذ '+mins+' دقيقة';if(hours<24)return'منذ '+hours+' ساعة';if(days<7)return'منذ '+days+' يوم';return new Date(ts).toLocaleDateString('ar-SA')}}
</script>
</body>
</html>"""

def build_explore():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>☁️ MNAENCA | استكشاف</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{min-height:100vh;overflow-y:auto}}
        .header{{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(2,6,23,0.8);backdrop-filter:blur(20px);z-index:10}}
        .btn-back{{background:rgba(14,165,233,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}}
        .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;padding:2px}}
        .thumb{{aspect-ratio:9/16;background:rgba(14,165,233,0.05);display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;overflow:hidden}}
        .thumb img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
        .thumb i{{position:absolute;font-size:24px;color:#fff;z-index:1;opacity:0;transition:opacity 0.3s}}
        .thumb:hover i{{opacity:1}}
        .thumb .views{{position:absolute;bottom:4px;left:4px;font-size:10px;background:rgba(0,0,0,0.6);padding:2px 6px;border-radius:10px}}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2><i class="fas fa-globe"></i> استكشاف</h2></div>
<div class="grid" id="exploreGrid"><div class="spinner" style="grid-column:1/-1"></div></div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null;
    auth.onAuthStateChanged(async u=>{{if(!u){{window.location.href='auth.html';return}}currentUser=u;loadExplore()}});
    async function loadExplore(){{
        const snap=await db.ref('videos').once('value');
        const videos=snap.val()||{{}};
        const allVids=Object.entries(videos).map(([k,v])=>({{id:k,...v}})).sort((a,b)=>(b.likes||0)-(a.likes||0));
        const g=document.getElementById('exploreGrid');
        if(!allVids.length){{g.innerHTML='<div style="text-align:center;padding:40px;grid-column:1/-1;opacity:0.5">لا توجد فيديوهات</div>';return}}
        g.innerHTML=allVids.map(v=>`<div class="thumb" onclick="window.open('${{v.url}}','_blank')">${{v.thumbnail?`<img src="${{v.thumbnail}}">`:''}}<i class="fas fa-play"></i><span class="views"><i class="fas fa-heart"></i> ${{v.likes||0}}</span></div>`).join('');
    }}
</script>
</body>
</html>"""

def build_notifications():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>☁️ MNAENCA | إشعارات</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{min-height:100vh;overflow-y:auto}}
        .header{{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(2,6,23,0.8);backdrop-filter:blur(20px);z-index:10}}
        .btn-back{{background:rgba(14,165,233,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}}
        .notif-item{{display:flex;gap:12px;padding:14px 16px;border-bottom:1px solid var(--border);align-items:center}}
        .notif-icon{{width:40px;height:40px;border-radius:50%;background:rgba(255,255,255,0.03);display:flex;align-items:center;justify-content:center;font-size:18px;color:var(--accent)}}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2><i class="fas fa-bell"></i> الإشعارات</h2></div>
<div id="notifsList"><div class="spinner"></div></div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null;
    auth.onAuthStateChanged(async u=>{{if(!u){{window.location.href='auth.html';return}}currentUser=u;loadNotifs()}});
    async function loadNotifs(){{
        const snap=await db.ref('notifications/'+currentUser.uid).once('value');
        const ns=snap.val()||{{}};
        const c=document.getElementById('notifsList');
        const items=Object.values(ns).reverse();
        if(!items.length){{c.innerHTML='<div style="text-align:center;opacity:0.5;padding:40px"><i class="fas fa-bell" style="font-size:48px;color:#0ea5e9;margin-bottom:12px;display:block"></i><p>لا توجد إشعارات</p></div>';return}}
        c.innerHTML=items.map(n=>`<div class="notif-item"><div class="notif-icon"><i class="fas fa-bell"></i></div><div><div style="font-weight:600">${{n.from||'مستخدم'}}</div><div style="font-size:12px;opacity:0.6;margin-top:2px">${{n.msg||''}}</div></div></div>`).join('');
    }}
</script>
</body>
</html>"""

def build_settings():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>☁️ MNAENCA | إعدادات</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{min-height:100vh;overflow-y:auto}}
        .header{{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(2,6,23,0.8);backdrop-filter:blur(20px);z-index:10}}
        .btn-back{{background:rgba(14,165,233,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}}
        .setting-item{{display:flex;justify-content:space-between;align-items:center;padding:16px;border-bottom:1px solid var(--border);cursor:pointer;transition:background 0.2s}}
        .setting-item:hover{{background:rgba(255,255,255,0.03)}}
        .setting-item i{{color:var(--accent);font-size:18px;width:30px}}
        .btn-danger{{background:rgba(239,68,68,0.2);border:1px solid rgba(239,68,68,0.3);color:#f87171;padding:12px 24px;border-radius:30px;cursor:pointer;font-size:14px;margin:20px auto;display:block}}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2><i class="fas fa-cog"></i> الإعدادات</h2></div>
<div style="padding:8px 0">
    <div class="setting-item" onclick="window.location.href='profile.html'"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-user"></i><span>تعديل الملف الشخصي</span></div><i class="fas fa-chevron-left" style="opacity:0.5"></i></div>
    <div class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-lock"></i><span>الخصوصية</span></div><i class="fas fa-chevron-left" style="opacity:0.5"></i></div>
    <div class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-globe"></i><span>اللغة</span></div><span style="opacity:0.5;font-size:13px">العربية</span></div>
    <div class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-info-circle"></i><span>حول التطبيق</span></div><span style="opacity:0.5;font-size:13px">v2026.3 ☁️</span></div>
    <button class="btn-danger" onclick="if(confirm('تسجيل الخروج؟')){{auth.signOut();window.location.href='auth.html'}}"><i class="fas fa-sign-out-alt"></i> تسجيل الخروج</button>
</div>
<script src="firebase-config.js"></script>
<script>auth.onAuthStateChanged(u=>{{if(!u)window.location.href='auth.html'}});</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# ☁️ MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  ☁️  MNAENCA 2026 - SKY BLUE LUXURY EDITION  ✨      ║
║     Ultimate Generator - 9 Files - 3000+ Lines           ║
║     ✅ NEW MODERN UI (Cards + Stories + Glass)        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    section("BUILDING FILES - إنشاء الملفات")
    
    # Clean output directory
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
    
    # Copy to root for GitHub Pages
    for f in os.listdir(OUTPUT_DIR):
        src = os.path.join(OUTPUT_DIR, f)
        dst = os.path.join('.', f)
        if os.path.isfile(src):
            shutil.copy2(src, dst)
    
    print(f"""
{'='*60}
  ☁️ BUILD COMPLETE - تم الإنشاء بنجاح! ✨
{'='*60}

  📊 إحصائيات:
     • {TOTAL_LINES} إجمالي عدد الأسطر
     • 9 ملفات تم إنشاؤها

  ✨ الميزات الجديدة (تحديث التصميم):
     • شريط القصص (Stories) في الأعلى.
     • فيديوهات داخل بطاقات (Cards) بتصميم ناعم.
     • أزرار تفاعل بتأثير الزجاج (Glassmorphism).
     • شريط سفلي عائم بتصميم حديث.
     • شريط علوي نظيف مع تبويبات نصية.

  ☁️ MNAENCA READY! ✨
{'='*60}
    """)

if __name__ == "__main__":
    main()
