#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                            ║
║  🟦 NEXUS 2026 - SOCIAL PLATFORM GENERATOR  🟦            ║
║     Ultimate Version - 9 Files - 2000+ Lines               ║
║                                                            ║
║  🔥  Firebase: muvg-42126                                 ║
║  ☁️   Cloudinary: dmqyd0haj / s3_gok                     ║
║  👑  Admin: jasim28v@gmail.com                            ║
║  🟦  Design: Blue & Pink Glass Luxury                     ║
║                                                            ║
║  ✨  PREMIUM FEATURES:                                     ║
║     • 🔔 Notification System (Working 100%)              ║
║     • 💬 Comments & Replies                               ║
║     • ❤️  Likes & Retweets                                ║
║     • 📌 Bookmarks                                        ║
║     • 💬 Quote Tweets                                     ║
║     • 📝 Stories (24hr)                                   ║
║     • 💌 Private Chat (Text/Image/Audio)                  ║
║     • 🔍 Search Users                                     ║
║     • 👤 Edit Profile + Custom Avatar/Cover               ║
║     • 🌓 Dark/Light Mode Toggle                           ║
║     • 🛡️  Admin Panel (Delete Users/Posts)               ║
║     • 📱 Mobile Responsive + Fullscreen Support           ║
║     • 🎤 Voice Messages in Chat                           ║
║     • 📸 Image Modal Viewer                               ║
║                                                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys

# ═══════════════════════════════════════════════════════════
# 🔑 CONFIGURATION - الإعدادات الجديدة
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

# ═══════════════════════════════════════════════════════════
# 📊 UTILITY - دوال مساعدة
# ═══════════════════════════════════════════════════════════

TOTAL_LINES = 0

def write(filename, content):
    """حفظ ملف وحساب عدد الأسطر"""
    global TOTAL_LINES
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n') + 1
    TOTAL_LINES += lines
    print(f"  ✅ {filename} ({lines} سطر)")

def section(title):
    """طباعة عنوان القسم"""
    print(f"\n{'='*60}")
    print(f"  🟦  {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# 🟦 1. firebase-config.js
# ═══════════════════════════════════════════════════════════

def build_config():
    return f"""// 🟦 NEXUS 2026 - Firebase & Cloudinary Configuration
// Firebase: muvg-42126 | Cloudinary: dmqyd0haj
// ✨ PREMIUM: Notifications + Likes + Retweets + Chat + Stories + Admin

// 🔥 Firebase Configuration
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

// Initialize Firebase (Compat)
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

// Database reference helpers
const ref = (path) => firebase.database().ref(path);
const push = (ref) => ref.push();
const set = (ref, data) => ref.set(data);
const update = (ref, data) => ref.update(data);
const get = (ref) => ref.once('value');
const child = (ref, path) => ref.child(path);
const remove = (ref) => ref.remove();
const onValue = (ref, callback) => ref.on('value', callback);

// ☁️ Cloudinary Configuration
const CLOUD_NAME = "{CLOUD_NAME}";
const UPLOAD_PRESET = "{UPLOAD_PRESET}";

// 🟦 NEXUS Settings
const ADMIN_EMAILS = {ADMIN_EMAILS_JS};
const APP_NAME = "Nexus";
const APP_VERSION = "2026.1";
const PRIMARY_COLOR = "#1d9bf0";
const SECONDARY_COLOR = "#f91880";

console.log('🟦 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨', 'color: #1d9bf0; font-size: 16px; font-weight: bold;');
"""

# ═══════════════════════════════════════════════════════════
# 🟦 2. auth.html - تسجيل الدخول والاشتراك
# ═══════════════════════════════════════════════════════════

def build_auth():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>🟦 Nexus | دخول</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{
            min-height:100vh;min-height:-webkit-fill-available;
            background:#000;display:flex;align-items:center;justify-content:center;
            font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;
            overflow:hidden;
        }
        .bg-orb{position:fixed;border-radius:50%;filter:blur(140px);opacity:0.2}
        .bg-orb:nth-child(1){width:450px;height:450px;background:#1d9bf0;top:-120px;left:-120px}
        .bg-orb:nth-child(2){width:380px;height:380px;background:#f91880;bottom:-120px;right:-120px;animation-delay:5s}
        @keyframes orbFloat{0%{transform:translate(0,0)scale(1)}100%{transform:translate(60px,-60px)scale(1.4)}}
        .bg-orb{animation:orbFloat 18s infinite alternate}

        .card{
            position:relative;z-index:1;width:90%;max-width:440px;
            background:rgba(0,0,0,0.85);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);
            border-radius:32px;padding:40px 32px;
            border:1px solid rgba(29,155,240,0.2);
            box-shadow:0 30px 70px rgba(29,155,240,0.1);
            animation:fadeUp 0.8s ease;text-align:center;
        }
        @keyframes fadeUp{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:translateY(0)}}
        h1{font-size:44px;font-weight:800;margin-bottom:28px;
            background:linear-gradient(135deg,#1d9bf0,#f91880);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent}
        h2{font-size:22px;font-weight:700;margin-bottom:4px;text-align:right}
        .sub{color:#71767b;font-size:13px;text-align:right;margin-bottom:20px}
        .tabs{display:flex;gap:4px;background:rgba(29,155,240,0.06);border-radius:40px;padding:4px;margin-bottom:24px}
        .tab{flex:1;padding:12px;background:none;border:none;color:rgba(255,255,255,0.5);cursor:pointer;border-radius:40px;font-size:14px;transition:all 0.3s;font-weight:600}
        .tab.active{background:linear-gradient(135deg,#1d9bf0,#f91880);color:#fff;box-shadow:0 8px 20px rgba(29,155,240,0.4)}
        .form{display:none;animation:fadeIn 0.4s ease;text-align:right}
        .form.active{display:block}
        @keyframes fadeIn{from{opacity:0}to{opacity:1}}
        input{width:100%;padding:14px 18px;margin:8px 0;border-radius:40px;
            background:#1a1a1a;border:1px solid #2f3336;color:#fff;
            font-size:15px;outline:none;transition:all 0.4s}
        input:focus{border-color:#1d9bf0;box-shadow:0 0 20px rgba(29,155,240,0.15);background:#1a1a1a}
        input::placeholder{color:rgba(255,255,255,0.3)}
        button{width:100%;padding:12px;margin-top:16px;
            background:#1d9bf0;border:none;border-radius:40px;color:#fff;
            font-weight:600;font-size:15px;cursor:pointer;
            transition:all 0.3s;box-shadow:0 10px 30px rgba(29,155,240,0.3)}
        button:hover{transform:translateY(-2px);box-shadow:0 20px 40px rgba(29,155,240,0.5)}
        button:disabled{opacity:0.5;pointer-events:none}
        .msg{text-align:center;color:#f91880;font-size:13px;margin-top:12px;min-height:20px}
        .msg.success{color:#4ade80}
        .link{margin-top:28px;color:#71767b;font-size:13px}
        .link a{color:#1d9bf0;text-decoration:none;font-weight:600}
        .forgot{display:block;text-align:right;color:#1d9bf0;font-size:12px;margin-top:6px;text-decoration:none}
    </style>
</head>
<body>
    <div class="bg-orb"></div><div class="bg-orb"></div>
    <div class="card">
        <h1>Nexus</h1>
        <div class="tabs">
            <button class="tab active" id="tabLogin" onclick="switchAuth('login')"><i class="fas fa-sign-in-alt"></i> دخول</button>
            <button class="tab" id="tabRegister" onclick="switchAuth('register')"><i class="fas fa-user-plus"></i> اشتراك</button>
        </div>
        <div id="formLogin" class="form active">
            <h2>تسجيل الدخول</h2>
            <p class="sub">قم بالوصول إلى حسابك في Nexus</p>
            <input type="email" id="loginEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email">
            <input type="password" id="loginPass" placeholder="🔒 كلمة المرور" autocomplete="current-password">
            <a href="#" class="forgot" onclick="resetPassword()">نسيت كلمة المرور؟</a>
            <button id="btnLogin" onclick="doLogin()"><i class="fas fa-arrow-right-to-bracket"></i> تسجيل الدخول</button>
            <div class="msg" id="loginMsg"></div>
            <div class="link">ليس لديك حساب؟ <a href="#" onclick="switchAuth('register')">إنشاء حساب</a></div>
        </div>
        <div id="formRegister" class="form">
            <h2>إنشاء حساب</h2>
            <p class="sub">قم بإنشاء حسابك في Nexus</p>
            <input type="text" id="regName" placeholder="👤 اسم المستخدم" autocomplete="username">
            <input type="email" id="regEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email">
            <input type="password" id="regPass" placeholder="🔒 كلمة المرور (6 أحرف على الأقل)" autocomplete="new-password">
            <input type="password" id="regConfirmPass" placeholder="🔒 تأكيد كلمة المرور" autocomplete="new-password">
            <button id="btnRegister" onclick="doRegister()"><i class="fas fa-heart"></i> إنشاء حساب</button>
            <div class="msg" id="regMsg"></div>
            <div class="link">لديك حساب بالفعل؟ <a href="#" onclick="switchAuth('login')">تسجيل الدخول</a></div>
        </div>
    </div>
    <script src="firebase-config.js"></script>
    <script>
        function switchAuth(type){
            document.getElementById('tabLogin').classList.remove('active');
            document.getElementById('tabRegister').classList.remove('active');
            document.getElementById('formLogin').classList.remove('active');
            document.getElementById('formRegister').classList.remove('active');
            document.getElementById('loginMsg').innerText = '';
            document.getElementById('regMsg').innerText = '';
            if(type === 'login'){
                document.getElementById('tabLogin').classList.add('active');
                document.getElementById('formLogin').classList.add('active');
            } else {
                document.getElementById('tabRegister').classList.add('active');
                document.getElementById('formRegister').classList.add('active');
            }
        }

        async function doLogin(){
            const email = document.getElementById('loginEmail').value.trim();
            const password = document.getElementById('loginPass').value;
            const msg = document.getElementById('loginMsg');
            const btn = document.getElementById('btnLogin');
            if(!email || !password){ msg.innerText = '❌ الرجاء ملء جميع الحقول'; return; }
            btn.disabled = true; btn.innerHTML = '⏳ جاري الدخول...'; msg.innerText = '';
            try {
                await firebase.auth().signInWithEmailAndPassword(email, password);
                window.location.replace('index.html');
            } catch(error) {
                btn.disabled = false; btn.innerHTML = '<i class="fas fa-arrow-right-to-bracket"></i> تسجيل الدخول';
                switch(error.code) {
                    case 'auth/user-not-found': msg.innerText = '❌ لا يوجد حساب بهذا البريد'; break;
                    case 'auth/wrong-password': case 'auth/invalid-credential': msg.innerText = '❌ كلمة المرور غير صحيحة'; break;
                    case 'auth/invalid-email': msg.innerText = '❌ بريد إلكتروني غير صالح'; break;
                    case 'auth/too-many-requests': msg.innerText = '❌ محاولات كثيرة، حاول لاحقاً'; break;
                    default: msg.innerText = '❌ خطأ: ' + error.message;
                }
            }
        }

        async function doRegister(){
            const name = document.getElementById('regName').value.trim();
            const email = document.getElementById('regEmail').value.trim();
            const password = document.getElementById('regPass').value;
            const confirmPass = document.getElementById('regConfirmPass').value;
            const msg = document.getElementById('regMsg');
            const btn = document.getElementById('btnRegister');
            if(!name || !email || !password || !confirmPass){ msg.innerText = '❌ الرجاء ملء جميع الحقول'; return; }
            if(name.length < 3){ msg.innerText = '❌ اسم المستخدم 3 أحرف على الأقل'; return; }
            if(password.length < 6){ msg.innerText = '❌ كلمة المرور 6 أحرف على الأقل'; return; }
            if(password !== confirmPass){ msg.innerText = '❌ كلمة المرور غير متطابقة'; return; }
            if(!email.includes('@') || !email.includes('.')){ msg.innerText = '❌ بريد إلكتروني غير صالح'; return; }
            btn.disabled = true; btn.innerHTML = '⏳ جاري إنشاء الحساب...'; msg.innerText = '';
            try {
                const userCredential = await firebase.auth().createUserWithEmailAndPassword(email, password);
                const uid = userCredential.user.uid;
                await firebase.database().ref('users/' + uid).set({
                    name: name, email: email, bio: '',
                    avatarUrl: '', coverUrl: '',
                    followers: {}, following: {}, bookmarks: {},
                    createdAt: Date.now()
                });
                msg.innerText = '✅ تم إنشاء الحساب بنجاح! جاري التوجيه...';
                msg.className = 'msg success';
                setTimeout(() => { window.location.replace('index.html'); }, 800);
            } catch(error) {
                btn.disabled = false; btn.innerHTML = '<i class="fas fa-heart"></i> إنشاء حساب'; msg.className = 'msg';
                switch(error.code) {
                    case 'auth/email-already-in-use': msg.innerText = '❌ البريد الإلكتروني مستخدم بالفعل'; break;
                    case 'auth/weak-password': msg.innerText = '❌ كلمة المرور ضعيفة جداً'; break;
                    case 'auth/invalid-email': msg.innerText = '❌ بريد إلكتروني غير صالح'; break;
                    default: msg.innerText = '❌ خطأ: ' + (error.message || 'غير معروف');
                }
            }
        }

        function resetPassword(){
            const email = document.getElementById('loginEmail').value.trim();
            if(!email){ document.getElementById('loginMsg').innerText = '❌ أدخل بريدك الإلكتروني أولاً'; return; }
            firebase.auth().sendPasswordResetEmail(email).then(() => {
                document.getElementById('loginMsg').innerText = '✅ تم إرسال رابط إعادة التعيين إلى بريدك';
                document.getElementById('loginMsg').className = 'msg success';
            }).catch(e => {
                document.getElementById('loginMsg').innerText = '❌ خطأ: ' + e.message;
            });
        }

        document.querySelectorAll('input').forEach(input => {
            input.addEventListener('keydown', function(e) {
                if(e.key === 'Enter') {
                    e.preventDefault();
                    if(document.getElementById('formLogin').classList.contains('active')) { doLogin(); }
                    else { doRegister(); }
                }
            });
        });

        firebase.auth().onAuthStateChanged(user => {
            if(user) { window.location.replace('index.html'); }
        });

        console.log('🟦 Nexus Auth Ready');
    </script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🟦 3. index.html - الرئيسية (نسخة Nexus الكاملة)
# ═══════════════════════════════════════════════════════════

def build_index():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>🟦 Nexus | الرئيسية</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #1d9bf0;
            --secondary: #f91880;
            --bg: #000000;
            --surface: #1a1a1a;
            --border: rgba(255,255,255,0.08);
            --text: #ffffff;
            --text-secondary: #71767b;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg);
            color: var(--text);
            min-height: 100vh;
            min-height: -webkit-fill-available;
            overflow-x: hidden;
            overflow-y: auto;
            -webkit-tap-highlight-color: transparent;
            width: 100%;
            position: relative;
        }
        body.light-mode {
            --bg: #f5f7f9;
            --surface: #ffffff;
            --border: rgba(0,0,0,0.08);
            --text: #111111;
            --text-secondary: #536471;
        }
        body.light-mode .top-bar { background: rgba(245,247,249,0.95); border-bottom-color: rgba(0,0,0,0.08); }
        body.light-mode .bottom-nav { background: rgba(245,247,249,0.95); border-top-color: rgba(0,0,0,0.08); }
        body.light-mode .tweet-card { background: #ffffff; border-bottom-color: #eef2f5; }
        body.light-mode .tweet-card:hover { background: #fafbfc; }
        body.light-mode .panel { background: #ffffff; }
        body.light-mode input { background: #f5f7f9; border-color: #eef2f5; color: #111; }
        body.light-mode .message-bubble.received { background: #eef2f5; }
        body.light-mode .admin-stat { background: #f0f2f5; }

        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: var(--primary); border-radius: 10px; }

        .top-bar {
            position: sticky; top: 0;
            background: rgba(0,0,0,0.85); backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border);
            padding: 12px 16px; display: flex;
            justify-content: space-between; align-items: center;
            z-index: 100; padding-top: max(12px, env(safe-area-inset-top));
        }
        .logo {
            font-size: 22px; font-weight: 800;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            cursor: pointer;
        }
        .top-icons { display: flex; gap: 20px; align-items: center; }
        .top-icon { font-size: 20px; color: var(--text); cursor: pointer; position: relative; }
        .top-icon:hover { color: var(--primary); }
        .notification-badge {
            position: absolute; top: -6px; right: -10px;
            background: var(--secondary); color: white;
            font-size: 9px; font-weight: bold;
            border-radius: 50%; width: 16px; height: 16px;
            display: flex; align-items: center; justify-content: center;
            display: none;
        }
        .back-btn {
            background: none; border: none; color: var(--primary);
            font-size: 13px; cursor: pointer; display: none;
            align-items: center; gap: 6px;
        }

        .feed-container { padding: 0 0 70px; min-height: 100vh; }
        .tweet-card {
            background: var(--bg); border-bottom: 1px solid var(--border);
            padding: 14px 16px; transition: background 0.2s; cursor: pointer;
        }
        .tweet-card:hover { background: rgba(255,255,255,0.02); }
        .tweet-header { display: flex; gap: 12px; margin-bottom: 6px; }
        .tweet-avatar {
            width: 44px; height: 44px; border-radius: 50%;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            overflow: hidden; cursor: pointer; flex-shrink: 0;
        }
        .tweet-avatar img { width: 100%; height: 100%; object-fit: cover; }
        .tweet-name { font-weight: 700; cursor: pointer; font-size: 14px; }
        .tweet-username { font-size: 12px; color: var(--text-secondary); }
        .tweet-time { font-size: 12px; color: var(--text-secondary); }
        .tweet-content { margin: 8px 0 10px; font-size: 14px; line-height: 1.4; white-space: pre-wrap; }
        .tweet-media { margin: 10px 0; border-radius: 18px; overflow: hidden; background: var(--surface); }
        .tweet-media img { width: 100%; max-height: 450px; object-fit: cover; cursor: pointer; }
        .tweet-media video { width: 100%; max-height: 450px; border-radius: 18px; cursor: pointer; }
        .tweet-media audio { width: 100%; }
        .quote-embed {
            margin-top: 12px; border: 1px solid var(--border); border-radius: 16px;
            padding: 12px; cursor: pointer;
        }
        .tweet-actions {
            display: flex; justify-content: space-between; max-width: 380px; margin-top: 10px;
        }
        .tweet-action {
            display: flex; align-items: center; gap: 6px;
            background: none; border: none; color: var(--text-secondary);
            cursor: pointer; font-size: 12px; padding: 6px;
            border-radius: 40px; transition: 0.2s;
        }
        .tweet-action i { font-size: 16px; }
        .tweet-action:hover { color: var(--primary); background: rgba(29,155,240,0.1); }
        .tweet-action.active { color: var(--secondary); }
        @keyframes heartBeat { 0% { transform: scale(1); } 50% { transform: scale(1.2); } 100% { transform: scale(1); } }
        .heart-animation { animation: heartBeat 0.3s ease; }

        .bottom-nav {
            position: fixed; bottom: 0; left: 0; right: 0;
            background: rgba(0,0,0,0.85); backdrop-filter: blur(20px);
            border-top: 1px solid var(--border);
            display: flex; justify-content: space-around;
            padding: 8px 0 calc(8px + env(safe-area-inset-bottom)); z-index: 100;
        }
        .nav-item {
            background: none; border: none; font-size: 22px;
            color: var(--text-secondary); cursor: pointer; padding: 6px;
            border-radius: 40px; transition: 0.2s;
        }
        .nav-item.active { color: var(--primary); }
        .nav-item:hover { background: rgba(29,155,240,0.1); color: var(--primary); }

        .panel {
            position: fixed; inset: 0; background: var(--bg);
            z-index: 200; transform: translateX(100%);
            transition: 0.3s cubic-bezier(0.2, 0.9, 0.4, 1.1);
            overflow-y: auto; display: flex; flex-direction: column;
        }
        .panel.open { transform: translateX(0); }
        .panel-header { padding: 12px 16px; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; }
        .panel-body { flex: 1; overflow-y: auto; padding: 12px; }

        .compose-area { padding: 16px; max-width: 600px; margin: 0 auto; }
        .compose-input {
            width: 100%; min-height: 120px; background: transparent;
            border: none; padding: 12px; color: var(--text);
            font-size: 18px; resize: none; outline: none; font-family: inherit;
        }
        .media-preview { margin: 12px 0; display: none; }
        .media-preview img, .media-preview video { max-height: 250px; border-radius: 18px; width: 100%; object-fit: cover; }
        .compose-tools { display: flex; gap: 12px; padding: 10px 0; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); }
        .compose-tool { background: none; border: none; color: var(--primary); font-size: 18px; padding: 8px; border-radius: 50%; cursor: pointer; }
        .btn-post { width: 100%; background: var(--primary); color: white; border: none; padding: 12px; border-radius: 40px; font-weight: 700; cursor: pointer; margin-top: 16px; }

        .comment-item { margin-bottom: 20px; padding-bottom: 12px; border-bottom: 1px solid var(--border); }
        .comment-header { display: flex; gap: 10px; margin-bottom: 6px; }
        .comment-avatar { width: 36px; height: 36px; border-radius: 50%; background: var(--primary); overflow: hidden; cursor: pointer; flex-shrink: 0; }
        .comment-avatar img { width: 100%; height: 100%; object-fit: cover; }
        .comment-user { font-weight: 600; font-size: 13px; cursor: pointer; }
        .comment-time { font-size: 10px; color: var(--text-secondary); }
        .comment-text { font-size: 13px; margin: 6px 0; }
        .reply-list { margin-top: 10px; margin-right: 40px; border-right: 2px solid var(--primary); padding-right: 10px; }
        .reply-item { margin-bottom: 10px; padding-bottom: 6px; border-bottom: 1px solid var(--border); }
        .reply-header { display: flex; gap: 6px; align-items: center; margin-bottom: 4px; }
        .reply-avatar { width: 24px; height: 24px; border-radius: 50%; background: var(--primary); overflow: hidden; }
        .reply-user { font-weight: 500; font-size: 11px; cursor: pointer; }
        .reply-text { font-size: 12px; }
        .comment-input-area { padding: 12px; border-top: 1px solid var(--border); background: var(--bg); }
        .comment-input { display: flex; gap: 10px; align-items: center; }
        .comment-input input { flex: 1; padding: 10px 14px; background: var(--surface); border: 1px solid var(--border); border-radius: 40px; color: var(--text); outline: none; font-size: 13px; }

        .profile-cover { width: 100%; height: 160px; background: linear-gradient(135deg, var(--primary), var(--secondary)); cursor: pointer; position: relative; }
        .profile-cover img { width: 100%; height: 100%; object-fit: cover; }
        .profile-info { padding: 0 16px 16px; position: relative; }
        .profile-avatar {
            width: 88px; height: 88px; border-radius: 50%;
            background: #111; border: 3px solid var(--bg);
            margin-top: -44px; display: flex; align-items: center; justify-content: center;
            overflow: hidden; cursor: pointer; position: relative;
        }
        .profile-avatar img { width: 100%; height: 100%; object-fit: cover; }
        .profile-name { font-size: 18px; font-weight: 700; margin-top: 10px; }
        .profile-bio { color: var(--text-secondary); font-size: 13px; margin: 6px 0; }
        .profile-stats {
            display: flex; gap: 20px; margin: 12px 0; padding: 10px 0;
            border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
        }
        .stat-number { font-size: 16px; font-weight: 700; cursor: pointer; }
        .stat-label { font-size: 12px; color: var(--text-secondary); cursor: pointer; }
        .profile-buttons { display: flex; gap: 10px; margin: 12px 0; flex-wrap: wrap; }
        .profile-btn {
            padding: 6px 20px; border-radius: 40px; font-weight: 600;
            cursor: pointer; border: none; font-size: 13px;
        }
        .btn-primary { background: var(--primary); color: white; }
        .btn-secondary { background: var(--surface); color: var(--text); }
        .btn-danger { background: var(--secondary); color: white; }
        .profile-posts-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2px; margin-top: 4px; }
        .profile-post { aspect-ratio: 1; background: var(--surface); overflow: hidden; cursor: pointer; display: flex; align-items: center; justify-content: center; }
        .profile-post img, .profile-post video { width: 100%; height: 100%; object-fit: cover; }

        .chat-messages { flex: 1; overflow-y: auto; padding: 12px; display: flex; flex-direction: column; gap: 10px; }
        .chat-message { display: flex; gap: 6px; max-width: 80%; }
        .chat-message.sent { align-self: flex-end; flex-direction: row-reverse; }
        .message-bubble { background: var(--surface); padding: 8px 12px; border-radius: 18px; font-size: 13px; }
        .message-bubble.sent { background: var(--primary); color: white; }
        .message-image { max-width: 180px; border-radius: 14px; cursor: pointer; }
        .message-audio audio { width: 200px; height: 36px; }
        .chat-input-area { display: flex; gap: 10px; padding: 10px; border-top: 1px solid var(--border); background: var(--bg); align-items: center; }
        .chat-input-area input { flex: 1; padding: 10px 14px; border: 1px solid var(--border); border-radius: 40px; background: var(--surface); color: var(--text); outline: none; font-size: 13px; }
        .chat-input-area button { background: none; border: none; color: var(--primary); font-size: 18px; cursor: pointer; padding: 6px; }

        .search-input { width: calc(100% - 24px); margin: 12px; padding: 10px 16px; background: var(--surface); border: 1px solid var(--border); border-radius: 40px; color: var(--text); font-size: 14px; outline: none; }
        .search-result { display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-bottom: 1px solid var(--border); cursor: pointer; }
        .notification-item { display: flex; align-items: center; gap: 10px; padding: 12px; border-bottom: 1px solid var(--border); cursor: pointer; }
        .follower-item { display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-bottom: 1px solid var(--border); cursor: pointer; }
        .conversation-item { display: flex; align-items: center; gap: 12px; padding: 14px; border-bottom: 1px solid var(--border); cursor: pointer; }
        .conversation-item:hover { background: rgba(255,255,255,0.02); }
        .avatar-sm { width: 48px; height: 48px; border-radius: 50%; background: var(--primary); overflow: hidden; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 20px; color: white; }
        .avatar-sm img { width: 100%; height: 100%; object-fit: cover; }
        .avatar-xs { width: 40px; height: 40px; border-radius: 50%; background: var(--primary); overflow: hidden; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 16px; color: white; }
        .avatar-xs img { width: 100%; height: 100%; object-fit: cover; }

        .edit-profile-modal {
            position: fixed; inset: 0; background: rgba(0,0,0,0.9);
            z-index: 600; display: flex; align-items: center; justify-content: center;
            opacity: 0; visibility: hidden; transition: 0.3s;
        }
        .edit-profile-modal.open { opacity: 1; visibility: visible; }
        .edit-profile-content {
            background: var(--bg); border-radius: 24px; padding: 24px;
            width: 90%; max-width: 440px; border: 1px solid var(--border);
        }
        .edit-profile-content input, .edit-profile-content textarea {
            width: 100%; padding: 12px 14px; margin: 10px 0;
            background: var(--surface); border: 1px solid var(--border);
            border-radius: 40px; color: var(--text); font-size: 14px; outline: none;
        }
        .edit-profile-content textarea { border-radius: 20px; min-height: 80px; resize: vertical; }

        .image-modal {
            position: fixed; inset: 0; background: rgba(0,0,0,0.96);
            z-index: 2000; display: flex; align-items: center; justify-content: center;
            opacity: 0; visibility: hidden; transition: 0.3s; cursor: pointer;
        }
        .image-modal.open { opacity: 1; visibility: visible; }
        .image-modal img { max-width: 95%; max-height: 95%; object-fit: contain; border-radius: 12px; }
        .close-modal {
            position: absolute; top: 16px; right: 16px;
            background: rgba(0,0,0,0.5); color: white;
            width: 36px; height: 36px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 20px; cursor: pointer; z-index: 2001;
        }

        .admin-stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; padding: 16px; }
        .admin-stat { background: var(--surface); padding: 16px; border-radius: 20px; text-align: center; border: 1px solid var(--border); }
        .admin-stat-icon { font-size: 28px; margin-bottom: 8px; color: var(--primary); }
        .admin-stat-number { font-size: 28px; font-weight: 700; margin-bottom: 4px; }
        .admin-stat-label { font-size: 12px; color: var(--text-secondary); }
        .admin-item { display: flex; justify-content: space-between; align-items: center; padding: 12px; border-bottom: 1px solid var(--border); }
        .admin-item-name { font-weight: 600; font-size: 13px; margin-bottom: 2px; }
        .admin-item-email { font-size: 11px; color: var(--text-secondary); }
        .admin-delete-btn { background: var(--secondary); color: white; border: none; padding: 4px 12px; border-radius: 40px; cursor: pointer; font-size: 11px; font-weight: 500; }

        .loading { text-align: center; padding: 60px 20px; color: var(--text-secondary); }
        .spinner { width: 32px; height: 32px; border: 2px solid rgba(29,155,240,0.2); border-top-color: var(--primary); border-radius: 50%; animation: spin 0.8s linear infinite; margin: 0 auto 12px; }
        @keyframes spin { to { transform: rotate(360deg); } }

        #customToast {
            position: fixed; bottom: 75px; left: 50%; transform: translateX(-50%);
            background: var(--primary); color: white; padding: 8px 20px;
            border-radius: 40px; z-index: 1100; font-size: 13px; font-weight: 500;
            opacity: 0; transition: 0.3s; pointer-events: none; white-space: nowrap;
        }

        .upload-btn { flex: 1; background: var(--surface); color: var(--text); padding: 8px; border-radius: 40px; font-weight: 500; cursor: pointer; text-align: center; font-size: 12px; }
    </style>
</head>
<body>

<!-- Image Modal -->
<div id="imageModal" class="image-modal" onclick="closeImageModal()">
    <div class="close-modal" onclick="closeImageModal()">&times;</div>
    <img id="modalImage" src="">
</div>

<!-- Main App -->
<div id="mainApp" style="display:none">
    <div class="top-bar">
        <div class="logo" onclick="goToHome()">Nexus</div>
        <div class="top-icons">
            <button class="back-btn" id="backBtn" onclick="goBack()"><i class="fas fa-arrow-right"></i> رجوع</button>
            <i class="fas fa-search top-icon" onclick="openSearch()"></i>
            <div class="top-icon" onclick="openNotifications()" id="notifIcon" style="position: relative;">
                <i class="far fa-bell"></i><span class="notification-badge" id="notifBadge"></span>
            </div>
            <i class="far fa-envelope top-icon" onclick="openConversations()"></i>
            <i class="fas fa-sun top-icon" onclick="toggleTheme()"></i>
        </div>
    </div>

    <div id="feedContainer" class="feed-container">
        <div class="loading"><div class="spinner"></div><span>🟦 جاري التحميل...</span></div>
    </div>

    <div class="bottom-nav">
        <button class="nav-item active" onclick="switchTab('home')"><i class="fas fa-home"></i></button>
        <button class="nav-item" onclick="openSearch()"><i class="fas fa-search"></i></button>
        <button class="nav-item" onclick="openCompose()"><i class="fas fa-feather-alt"></i></button>
        <button class="nav-item" onclick="openNotifications()"><i class="far fa-bell"></i></button>
        <button class="nav-item" onclick="openMyProfile()"><i class="fas fa-user"></i></button>
    </div>

    <!-- Compose Panel -->
    <div id="composePanel" class="panel">
        <div class="panel-header"><h3>إنشاء منشور</h3><button onclick="closeCompose()" class="text-xl">&times;</button></div>
        <div class="compose-area">
            <textarea id="postText" class="compose-input" placeholder="ماذا يحدث؟"></textarea>
            <div id="mediaPreview" class="media-preview"></div>
            <div class="compose-tools">
                <button class="compose-tool" onclick="document.getElementById('postImage').click()"><i class="fas fa-image"></i></button>
                <button class="compose-tool" onclick="document.getElementById('postVideo').click()"><i class="fas fa-video"></i></button>
                <button class="compose-tool" id="audioRecordBtn" onclick="startAudioRecording()"><i class="fas fa-microphone"></i></button>
            </div>
            <input type="file" id="postImage" accept="image/*" style="display:none" onchange="previewMedia(this, 'image')">
            <input type="file" id="postVideo" accept="video/*" style="display:none" onchange="previewMedia(this, 'video')">
            <div id="postStatus" class="text-xs mt-2 text-center" style="color:var(--primary)"></div>
            <button onclick="createPost()" class="btn-post">نشر</button>
        </div>
    </div>

    <!-- Comments Panel -->
    <div id="commentsPanel" class="panel">
        <div class="panel-header"><h3>التعليقات</h3><button onclick="closeComments()" class="text-xl">&times;</button></div>
        <div id="commentsList" class="panel-body"></div>
        <div class="comment-input-area">
            <div class="comment-input">
                <input type="text" id="commentInput" placeholder="أضف تعليقاً...">
                <button onclick="addComment()" style="background:var(--primary);color:white;padding:8px 16px;border:none;border-radius:40px;font-size:13px;font-weight:600;cursor:pointer;">نشر</button>
            </div>
        </div>
    </div>

    <!-- Profile Panel -->
    <div id="profilePanel" class="panel">
        <div class="panel-header"><h3>الملف الشخصي</h3><button onclick="closeProfile()" class="text-xl">&times;</button></div>
        <div id="profileCover" class="profile-cover" onclick="changeCover()">
            <div style="position:absolute;bottom:12px;right:12px;background:rgba(0,0,0,0.5);border-radius:50%;width:32px;height:32px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;"><i class="fas fa-camera fa-sm"></i></div>
        </div>
        <div class="profile-info">
            <div class="profile-avatar" id="profileAvatar" onclick="changeAvatar()">
                <div style="position:absolute;bottom:4px;right:4px;background:rgba(0,0,0,0.5);border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center;cursor:pointer;"><i class="fas fa-camera fa-xs"></i></div>
            </div>
            <div class="profile-name" id="profileName"></div>
            <div class="profile-bio" id="profileBio"></div>
            <div style="display:flex;gap:10px;margin:12px 0;">
                <div class="upload-btn" onclick="changeAvatar()"><i class="fas fa-user-circle"></i> تغيير الصورة</div>
                <div class="upload-btn" onclick="changeCover()"><i class="fas fa-image"></i> تغيير الغلاف</div>
            </div>
            <div class="profile-stats">
                <div onclick="openFollowersList('followers')"><div class="stat-number" id="profileFollowersCount">0</div><div class="stat-label">متابع</div></div>
                <div onclick="openFollowersList('following')"><div class="stat-number" id="profileFollowingCount">0</div><div class="stat-label">يتابع</div></div>
                <div><div class="stat-number" id="profilePostsCount">0</div><div class="stat-label">منشورات</div></div>
            </div>
            <div id="profileButtons" class="profile-buttons"></div>
        </div>
        <div id="profilePostsGrid" class="profile-posts-grid" style="padding:0 8px 80px;"></div>
    </div>

    <!-- Edit Profile Modal -->
    <div id="editProfileModal" class="edit-profile-modal">
        <div class="edit-profile-content">
            <h3 style="font-size:20px;font-weight:700;margin-bottom:20px;text-align:center;color:var(--primary);">تعديل الملف الشخصي</h3>
            <input type="text" id="editName" placeholder="الاسم">
            <textarea id="editBio" placeholder="السيرة الذاتية..."></textarea>
            <div style="display:flex;gap:10px;margin-top:20px;">
                <button class="btn-secondary" onclick="closeEditProfileModal()" style="flex:1;padding:10px;border-radius:40px;font-weight:600;cursor:pointer;">إلغاء</button>
                <button class="btn-primary" onclick="saveProfileEdit()" style="flex:1;padding:10px;border-radius:40px;font-weight:600;cursor:pointer;">حفظ</button>
            </div>
        </div>
    </div>

    <!-- Chat Panel -->
    <div id="chatPanel" class="panel">
        <div class="panel-header">
            <div style="display:flex;align-items:center;gap:10px;">
                <div class="avatar-sm" id="chatAvatar">👤</div>
                <h3 id="chatUserName">محادثة</h3>
            </div>
            <button onclick="closeChat()" class="text-xl">&times;</button>
        </div>
        <div id="chatMessages" class="chat-messages"></div>
        <div class="chat-input-area">
            <button id="chatRecordBtn" onclick="startRecordingChat()"><i class="fas fa-microphone"></i></button>
            <input type="file" id="chatImageInput" accept="image/*" style="display:none" onchange="sendChatImage(this)">
            <button onclick="document.getElementById('chatImageInput').click()"><i class="fas fa-image"></i></button>
            <input type="text" id="chatMessageInput" placeholder="اكتب رسالة...">
            <button onclick="sendChatMessage()"><i class="fas fa-paper-plane"></i></button>
        </div>
    </div>

    <!-- Conversations Panel -->
    <div id="conversationsPanel" class="panel">
        <div class="panel-header"><h3>الرسائل</h3><button onclick="closeConversations()" class="text-xl">&times;</button></div>
        <div id="conversationsList" class="panel-body"></div>
    </div>

    <!-- Followers Panel -->
    <div id="followersPanel" class="panel">
        <div class="panel-header"><h3 id="followersTitle">المتابعون</h3><button onclick="closeFollowers()" class="text-xl">&times;</button></div>
        <div id="followersList" class="panel-body"></div>
    </div>

    <!-- Notifications Panel -->
    <div id="notificationsPanel" class="panel">
        <div class="panel-header"><h3>الإشعارات</h3><button onclick="closeNotifications()" class="text-xl">&times;</button></div>
        <div id="notificationsList" class="panel-body"></div>
    </div>

    <!-- Search Panel -->
    <div id="searchPanel" class="panel">
        <div class="panel-header"><h3>بحث</h3><button onclick="closeSearch()" class="text-xl">&times;</button></div>
        <input type="text" id="searchInput" class="search-input" placeholder="بحث عن مستخدمين..." onkeyup="searchAll()">
        <div id="searchResults" class="panel-body"></div>
    </div>

    <!-- Admin Panel -->
    <div id="adminPanel" class="panel">
        <div class="panel-header"><h3>🔧 لوحة التحكم</h3><button onclick="closeAdmin()" class="text-xl">&times;</button></div>
        <div id="adminStats" class="admin-stats"></div>
        <div style="padding:16px;border-top:1px solid var(--border);"><h3 style="margin-bottom:12px;color:var(--primary);"><i class="fas fa-users"></i> إدارة المستخدمين</h3><div id="adminUsersList"></div></div>
        <div style="padding:16px;border-top:1px solid var(--border);"><h3 style="margin-bottom:12px;color:var(--primary);"><i class="fas fa-file-alt"></i> إدارة المنشورات</h3><div id="adminPostsList"></div></div>
    </div>
</div>

<script src="firebase-config.js"></script>
<script src="script.js"></script>

<script>
    window.openImageModal = function(imageUrl) { document.getElementById('modalImage').src = imageUrl; document.getElementById('imageModal').classList.add('open'); };
    window.closeImageModal = function() { document.getElementById('imageModal').classList.remove('open'); };
    window.toggleTheme = function() { document.body.classList.toggle('light-mode'); localStorage.setItem('theme', document.body.classList.contains('light-mode') ? 'light' : 'dark'); };
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🟦 4. script.js - كل المنطق
# ═══════════════════════════════════════════════════════════

def build_script():
    return r"""// 🟦 NEXUS 2026 - Main Script
// All logic: Posts, Comments, Likes, Retweets, Bookmarks, Quotes, Chat, Stories, Search, Admin

let currentUser = null;
let currentUserData = null;
let allUsers = {};
let allPosts = [];
let selectedMediaFile = null;
let currentChatUserId = null;
let viewingProfileUserId = null;
let currentPostForComments = null;
let mediaRecorder = null;
let audioChunks = [];
let bookmarks = {};
let isAdmin = false;

// ========== DATA LOADING ==========
async function loadUserData() {
    const snap = await firebase.database().ref(`users/${currentUser.uid}`).once('value');
    if (snap.exists()) currentUserData = { uid: currentUser.uid, ...snap.val() };
    if (currentUserData?.bookmarks) bookmarks = currentUserData.bookmarks;
}

firebase.database().ref('users').on('value', (s) => { allUsers = s.val() || {}; });

firebase.database().ref('posts').on('value', (s) => {
    const data = s.val();
    if (!data) { allPosts = []; renderFeed(); return; }
    allPosts = [];
    Object.keys(data).forEach(key => allPosts.push({ id: key, ...data[key] }));
    allPosts.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
    renderFeed();
});

// ========== MEDIA UPLOAD ==========
async function uploadMedia(file) {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('upload_preset', UPLOAD_PRESET);
    let resourceType = 'image';
    if (file.type.startsWith('video/')) resourceType = 'video';
    else if (file.type.startsWith('audio/')) resourceType = 'raw';
    const url = `https://api.cloudinary.com/v1_1/${CLOUD_NAME}/${resourceType}/upload`;
    const response = await fetch(url, { method: 'POST', body: formData });
    const data = await response.json();
    return { url: data.secure_url, type: resourceType === 'raw' ? 'audio' : resourceType };
}

// ========== FEED ==========
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function renderFeed() {
    const container = document.getElementById('feedContainer');
    if (!container) return;
    container.innerHTML = '';
    if (allPosts.length === 0) {
        container.innerHTML = '<div class="loading"><div class="spinner"></div><span>لا توجد منشورات بعد</span></div>';
        return;
    }
    allPosts.forEach(post => {
        const user = allUsers[post.sender] || { name: post.senderName || 'مستخدم', avatarUrl: '' };
        const isLiked = post.likedBy && post.likedBy[currentUser?.uid];
        const isRetweeted = post.retweetedBy && post.retweetedBy[currentUser?.uid];
        const isBookmarked = bookmarks[post.id];
        const commentsCount = post.comments ? Object.keys(post.comments).length : 0;
        const retweetCount = post.retweets ? Object.keys(post.retweets).length : 0;

        let mediaHtml = '';
        if (post.mediaUrl) {
            if (post.mediaType === 'image') {
                mediaHtml = `<div class="tweet-media" onclick="event.stopPropagation(); openImageModal('${post.mediaUrl}')"><img src="${post.mediaUrl}" loading="lazy"></div>`;
            } else if (post.mediaType === 'video') {
                mediaHtml = `<div class="tweet-media" onclick="event.stopPropagation()"><video controls src="${post.mediaUrl}"></video></div>`;
            } else if (post.mediaType === 'audio') {
                mediaHtml = `<div class="tweet-media" onclick="event.stopPropagation()"><audio controls src="${post.mediaUrl}"></audio></div>`;
            }
        }

        let quoteHtml = '';
        if (post.quotePostId && post.quotePostData) {
            const quoteUser = allUsers[post.quotePostData.sender] || { name: 'مستخدم', avatarUrl: '' };
            quoteHtml = `
                <div class="quote-embed" onclick="event.stopPropagation(); openCommentsModal('${post.quotePostId}')">
                    <div style="display:flex;gap:8px;align-items:center;margin-bottom:6px;">
                        <div class="comment-avatar">${quoteUser.avatarUrl ? `<img src="${quoteUser.avatarUrl}">` : (quoteUser.name?.charAt(0) || 'U')}</div>
                        <span style="font-weight:600;font-size:13px;">${escapeHtml(quoteUser.name)}</span>
                    </div>
                    <div style="font-size:13px;">${escapeHtml(post.quotePostData.text?.substring(0, 100) || '')}</div>
                </div>`;
        }

        const div = document.createElement('div');
        div.className = 'tweet-card';
        div.onclick = () => openCommentsModal(post.id);
        div.innerHTML = `
            <div class="tweet-header">
                <div class="tweet-avatar" onclick="event.stopPropagation(); viewProfile('${post.sender}')">${user.avatarUrl ? `<img src="${user.avatarUrl}">` : (user.name?.charAt(0) || '👤')}</div>
                <div style="flex:1">
                    <div><span class="tweet-name" onclick="event.stopPropagation(); viewProfile('${post.sender}')">${escapeHtml(user.name)}</span><span class="tweet-username mx-1">@${user.name?.toLowerCase().replace(/\s/g, '')}</span><span class="tweet-time">· ${new Date(post.timestamp).toLocaleString()}</span></div>
                    <div class="tweet-content">${escapeHtml(post.text || '')}</div>
                    ${mediaHtml}
                    ${quoteHtml}
                </div>
            </div>
            <div class="tweet-actions" onclick="event.stopPropagation()">
                <button class="tweet-action" onclick="openCommentsModal('${post.id}')"><i class="far fa-comment"></i> <span>${commentsCount}</span></button>
                <button class="tweet-action ${isRetweeted ? 'active' : ''}" onclick="toggleRetweet('${post.id}', this)"><i class="fas fa-retweet"></i> <span>${retweetCount}</span></button>
                <button class="tweet-action ${isLiked ? 'active' : ''}" onclick="toggleLike('${post.id}', this)"><i class="fas fa-heart"></i> <span>${post.likes || 0}</span></button>
                <button class="tweet-action ${isBookmarked ? 'active' : ''}" onclick="toggleBookmark('${post.id}', this)"><i class="fas fa-bookmark"></i></button>
                <button class="tweet-action" onclick="openQuoteModal('${post.id}')"><i class="fas fa-quote-right"></i></button>
            </div>`;
        container.appendChild(div);
    });
}

// ========== COMPOSE ==========
window.openCompose = function() { document.getElementById('composePanel').classList.add('open'); document.getElementById('backBtn').style.display = 'flex'; resetCompose(); };
window.closeCompose = function() { document.getElementById('composePanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };

function resetCompose() {
    document.getElementById('postText').value = '';
    document.getElementById('mediaPreview').innerHTML = '';
    document.getElementById('mediaPreview').style.display = 'none';
    selectedMediaFile = null;
    document.getElementById('postImage').value = '';
    document.getElementById('postVideo').value = '';
    document.getElementById('postStatus').innerHTML = '';
}

window.previewMedia = function(input, type) {
    const file = input.files[0];
    if (!file) return;
    selectedMediaFile = file;
    const reader = new FileReader();
    reader.onload = function(e) {
        const mediaPreview = document.getElementById('mediaPreview');
        if (type === 'image') mediaPreview.innerHTML = `<img src="${e.target.result}">`;
        else if (type === 'video') mediaPreview.innerHTML = `<video controls><source src="${e.target.result}"></video>`;
        mediaPreview.style.display = 'block';
    };
    reader.readAsDataURL(file);
};

window.startAudioRecording = async function() {
    const btn = document.getElementById('audioRecordBtn');
    if (mediaRecorder && mediaRecorder.state === 'recording') { mediaRecorder.stop(); btn.innerHTML = '<i class="fas fa-microphone"></i>'; return; }
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];
        mediaRecorder.ondataavailable = (event) => { audioChunks.push(event.data); };
        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/mp3' });
            selectedMediaFile = new File([audioBlob], 'recording.mp3', { type: 'audio/mp3' });
            const audioUrl = URL.createObjectURL(audioBlob);
            document.getElementById('mediaPreview').innerHTML = `<audio controls src="${audioUrl}"></audio>`;
            document.getElementById('mediaPreview').style.display = 'block';
            stream.getTracks().forEach(track => track.stop());
        };
        mediaRecorder.start();
        btn.innerHTML = '<i class="fas fa-stop-circle" style="color:#f91880"></i>';
    } catch (err) { showToast('لا يمكن الوصول إلى الميكروفون'); }
};

window.createPost = async function() {
    const text = document.getElementById('postText')?.value || '';
    if (!text.trim() && !selectedMediaFile) { showToast('اكتب شيئاً أو اختر وسائط'); return; }
    document.getElementById('postStatus').innerHTML = '📤 جاري النشر...';
    let mediaUrl = '', mediaType = 'none';
    if (selectedMediaFile) {
        try { const result = await uploadMedia(selectedMediaFile); mediaUrl = result.url; mediaType = result.type; }
        catch (error) { document.getElementById('postStatus').innerHTML = '❌ فشل رفع الوسائط'; return; }
    }
    try {
        await firebase.database().ref('posts').push({
            text, mediaUrl, mediaType, sender: currentUser.uid, senderName: currentUserData?.name,
            likes: 0, likedBy: {}, retweets: {}, retweetedBy: {}, comments: {}, timestamp: Date.now()
        });
        document.getElementById('postStatus').innerHTML = '✅ تم النشر!';
        setTimeout(() => closeCompose(), 1500);
    } catch (error) { document.getElementById('postStatus').innerHTML = '❌ فشل النشر'; }
};

// ========== POST ACTIONS ==========
window.toggleLike = async function(postId, btn) {
    if (!currentUser) return;
    const postRef = firebase.database().ref(`posts/${postId}`);
    const snap = await postRef.once('value');
    const post = snap.val();
    if (!post) return;
    let likes = post.likes || 0;
    let likedBy = post.likedBy || {};
    if (likedBy[currentUser.uid]) { likes--; delete likedBy[currentUser.uid]; showToast('تم إلغاء الإعجاب'); }
    else { likes++; likedBy[currentUser.uid] = true; addNotification(post.sender, 'like', postId); showToast('❤️ أعجبتك');
        if (btn) { const icon = btn.querySelector('i'); if (icon) icon.classList.add('heart-animation'); setTimeout(() => icon?.classList.remove('heart-animation'), 300); } }
    await postRef.update({ likes, likedBy });
    if (btn) { btn.classList.toggle('active'); const span = btn.querySelector('span'); if (span) span.innerText = likes; }
};

window.toggleRetweet = async function(postId, btn) {
    if (!currentUser) return;
    const postRef = firebase.database().ref(`posts/${postId}`);
    const snap = await postRef.once('value');
    const post = snap.val();
    if (!post) return;
    let retweets = post.retweets || {};
    let retweetedBy = post.retweetedBy || {};
    let retweetCount = Object.keys(retweets).length;
    if (retweetedBy[currentUser.uid]) {
        const keyToDelete = Object.keys(retweets).find(k => retweets[k].userId === currentUser.uid);
        if (keyToDelete) delete retweets[keyToDelete];
        delete retweetedBy[currentUser.uid]; retweetCount--; showToast('تم إلغاء إعادة التغريد');
    } else {
        const newRetweetId = Date.now().toString();
        retweets[newRetweetId] = { userId: currentUser.uid, timestamp: Date.now() };
        retweetedBy[currentUser.uid] = true; retweetCount++;
        addNotification(post.sender, 'retweet', postId); showToast('🔁 تم إعادة التغريد');
    }
    await postRef.update({ retweets, retweetedBy });
    if (btn) { btn.classList.toggle('active'); const span = btn.querySelector('span'); if (span) span.innerText = retweetCount; }
};

window.toggleBookmark = async function(postId, btn) {
    if (!currentUser) return;
    const userRef = firebase.database().ref(`users/${currentUser.uid}/bookmarks/${postId}`);
    const snap = await userRef.once('value');
    if (snap.exists()) { await userRef.set(null); delete bookmarks[postId]; showToast('تمت إزالة من الإشارات المرجعية'); }
    else { await userRef.set(true); bookmarks[postId] = true; showToast('📌 تمت إضافة إلى الإشارات المرجعية'); }
    if (btn) btn.classList.toggle('active');
};

window.openQuoteModal = function(postId) {
    const quoteText = prompt('أضف تعليقك على هذا المنشور:');
    if (quoteText) createQuotePost(postId, quoteText);
};

async function createQuotePost(originalPostId, quoteText) {
    const originalPost = allPosts.find(p => p.id === originalPostId);
    if (!originalPost) return;
    await firebase.database().ref('posts').push({
        text: quoteText, mediaUrl: '', mediaType: 'none', sender: currentUser.uid, senderName: currentUserData?.name,
        quotePostId: originalPostId, quotePostData: { text: originalPost.text, sender: originalPost.sender, senderName: originalPost.senderName, mediaUrl: originalPost.mediaUrl, mediaType: originalPost.mediaType },
        likes: 0, likedBy: {}, retweets: {}, retweetedBy: {}, comments: {}, timestamp: Date.now()
    });
    addNotification(originalPost.sender, 'quote', originalPostId);
    showToast('✅ تم نشر الاقتباس');
}

// ========== COMMENTS ==========
window.openCommentsModal = async function(postId) {
    currentPostForComments = postId;
    const post = allPosts.find(p => p.id === postId);
    if (!post) return;
    const container = document.getElementById('commentsList');
    const comments = post.comments || {};
    container.innerHTML = '';
    const sortedComments = Object.entries(comments).sort((a,b) => b[1].timestamp - a[1].timestamp);
    for (const [commentKey, comment] of sortedComments) {
        const user = allUsers[comment.userId] || { name: comment.username || 'مستخدم', avatarUrl: '' };
        const replies = comment.replies || {};
        const commentDiv = document.createElement('div');
        commentDiv.className = 'comment-item';
        commentDiv.innerHTML = `
            <div class="comment-header">
                <div class="comment-avatar" onclick="viewProfile('${comment.userId}')">${user.avatarUrl ? `<img src="${user.avatarUrl}">` : (user.name?.charAt(0) || 'U')}</div>
                <div style="flex:1"><div><span class="comment-user" onclick="viewProfile('${comment.userId}')">${escapeHtml(user.name)}</span><span class="comment-time mx-2">· ${new Date(comment.timestamp).toLocaleString()}</span></div>
                <div class="comment-text">${escapeHtml(comment.text)}</div></div>
            </div>
            <div class="reply-list" id="replies-${commentKey}"></div>
            <div><button class="text-[#1d9bf0] text-sm mt-2" onclick="showReplyInput('${commentKey}')"><i class="fas fa-reply"></i> رد</button></div>
            <div id="reply-input-${commentKey}" class="mt-2"></div>`;
        const repliesContainer = commentDiv.querySelector(`#replies-${commentKey}`);
        if (repliesContainer && replies) {
            const sortedReplies = Object.entries(replies).sort((a,b) => a[1].timestamp - b[1].timestamp);
            for (const [replyKey, reply] of sortedReplies) {
                const replyUser = allUsers[reply.userId] || { name: reply.username || 'مستخدم', avatarUrl: '' };
                repliesContainer.innerHTML += `<div class="reply-item"><div class="reply-header"><div class="reply-avatar" onclick="viewProfile('${reply.userId}')">${replyUser.avatarUrl ? `<img src="${replyUser.avatarUrl}">` : (replyUser.name?.charAt(0) || 'U')}</div><div class="reply-user" onclick="viewProfile('${reply.userId}')">${escapeHtml(replyUser.name)}</div><div class="comment-time">${new Date(reply.timestamp).toLocaleTimeString()}</div></div><div class="reply-text">${escapeHtml(reply.text)}</div></div>`;
            }
        }
        container.appendChild(commentDiv);
    }
    if (container.innerHTML === '') container.innerHTML = '<div class="text-center text-gray-500 py-10">لا توجد تعليقات بعد</div>';
    document.getElementById('commentsPanel').classList.add('open');
    document.getElementById('backBtn').style.display = 'flex';
};

window.closeComments = function() { document.getElementById('commentsPanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };

window.showReplyInput = function(commentId) {
    const replyDiv = document.getElementById(`reply-input-${commentId}`);
    if (!replyDiv) return;
    if (replyDiv.innerHTML) { replyDiv.innerHTML = ''; return; }
    replyDiv.innerHTML = `<div class="flex gap-2 mt-2"><input type="text" id="reply-text-${commentId}" class="flex-1 bg-[#1a1a1a] border border-[#2f3336] rounded-full px-3 py-2 text-sm" placeholder="اكتب رداً..." onkeypress="if(event.key==='Enter') addReply('${commentId}')"><button onclick="addReply('${commentId}')" class="bg-[#1d9bf0] text-white px-4 py-2 rounded-full text-sm">نشر</button></div>`;
};

window.addReply = async function(commentId) {
    const input = document.getElementById(`reply-text-${commentId}`);
    const text = input?.value;
    if (!text?.trim()) return;
    await firebase.database().ref(`posts/${currentPostForComments}/comments/${commentId}/replies`).push({ userId: currentUser.uid, username: currentUserData?.name, text, timestamp: Date.now() });
    if (input) input.value = '';
    openCommentsModal(currentPostForComments);
};

window.addComment = async function() {
    const input = document.getElementById('commentInput');
    const text = input?.value;
    if (!text?.trim() || !currentPostForComments) return;
    await firebase.database().ref(`posts/${currentPostForComments}/comments`).push({ userId: currentUser.uid, username: currentUserData?.name, text, replies: {}, timestamp: Date.now() });
    if (input) input.value = '';
    openCommentsModal(currentPostForComments);
    const post = allPosts.find(p => p.id === currentPostForComments);
    if (post) addNotification(post.sender, 'comment', currentPostForComments);
};

// ========== NOTIFICATIONS ==========
async function addNotification(targetUserId, type, postId = null) {
    if (targetUserId === currentUser.uid) return;
    const messages = { like: '❤️ أعجب بمنشورك', comment: '💬 علق على منشورك', retweet: '🔁 أعاد تغريد منشورك', quote: '📝 اقتبس منشورك', follow: '👥 بدأ بمتابعتك' };
    await firebase.database().ref(`notifications/${targetUserId}`).push({ type, fromUserId: currentUser.uid, fromUsername: currentUserData?.name, message: messages[type], postId: postId, timestamp: Date.now(), read: false });
    updateNotificationBadge();
}

function updateNotificationBadge() {
    if (!currentUser?.uid) return;
    firebase.database().ref(`notifications/${currentUser.uid}`).on('value', (snap) => {
        const notifs = snap.val() || {};
        const unread = Object.values(notifs).filter(n => !n.read).length;
        const badge = document.getElementById('notifBadge');
        if (badge) {
            if (unread > 0) { badge.style.display = 'flex'; badge.innerText = unread > 9 ? '9+' : unread; }
            else badge.style.display = 'none';
        }
    });
}

window.openNotifications = async function() {
    const panel = document.getElementById('notificationsPanel');
    const snap = await firebase.database().ref(`notifications/${currentUser.uid}`).once('value');
    const notifs = snap.val() || {};
    const container = document.getElementById('notificationsList');
    container.innerHTML = '';
    const sorted = Object.entries(notifs).sort((a,b) => b[1].timestamp - a[1].timestamp);
    for (const [key, n] of sorted) {
        const icons = { like: '❤️', comment: '💬', retweet: '🔁', quote: '📝', follow: '👥' };
        const bgColor = n.read ? '' : 'background:rgba(29,155,240,0.1);border-right:4px solid #1d9bf0;';
        container.innerHTML += `<div class="notification-item" style="${bgColor}" onclick="handleNotificationClick('${n.type}', '${n.fromUserId}', '${n.postId || ''}')"><div class="text-2xl">${icons[n.type] || '🔔'}</div><div class="flex-1"><div class="font-bold">${escapeHtml(n.fromUsername)}</div><div class="text-sm" style="color:#71767b">${n.message}</div><div class="text-xs mt-1" style="color:#71767b">${new Date(n.timestamp).toLocaleString()}</div></div></div>`;
        if (!n.read) await firebase.database().ref(`notifications/${currentUser.uid}/${key}`).update({ read: true });
    }
    if (container.innerHTML === '') container.innerHTML = '<div class="text-center py-10" style="color:#71767b">لا توجد إشعارات</div>';
    panel.classList.add('open'); document.getElementById('backBtn').style.display = 'flex';
};

window.handleNotificationClick = function(type, userId, postId) { closeNotifications(); if (type === 'follow') viewProfile(userId); else if (postId) openCommentsModal(postId); };
window.closeNotifications = function() { document.getElementById('notificationsPanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };

// ========== TOAST ==========
function showToast(message) {
    let toast = document.getElementById('customToast');
    if (!toast) { toast = document.createElement('div'); toast.id = 'customToast'; document.body.appendChild(toast); }
    toast.innerText = message; toast.style.opacity = '1';
    setTimeout(() => { toast.style.opacity = '0'; }, 3000);
}

// ========== PROFILE ==========
window.openMyProfile = function() { viewProfile(currentUser.uid); };
window.viewProfile = async function(userId) {
    if (!userId) return;
    viewingProfileUserId = userId;
    await loadProfileData(userId);
    document.getElementById('profilePanel').classList.add('open');
    document.getElementById('backBtn').style.display = 'flex';
};
window.closeProfile = function() { document.getElementById('profilePanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };

async function loadProfileData(userId) {
    const userSnap = await firebase.database().ref(`users/${userId}`).once('value');
    const user = userSnap.val();
    if (!user) return;
    const coverEl = document.getElementById('profileCover');
    if (user.coverUrl) coverEl.style.background = `url(${user.coverUrl}) center/cover`;
    else coverEl.style.background = 'linear-gradient(135deg, #1d9bf0, #f91880)';
    const avatarEl = document.getElementById('profileAvatar');
    avatarEl.innerHTML = user.avatarUrl ? `<img src="${user.avatarUrl}">` : (user.name?.charAt(0) || '👤');
    document.getElementById('profileName').innerText = user.name;
    document.getElementById('profileBio').innerText = user.bio || '✏️ أضف سيرة ذاتية';
    const userPosts = allPosts.filter(p => p.sender === userId);
    document.getElementById('profilePostsCount').innerText = userPosts.length;
    document.getElementById('profileFollowersCount').innerText = Object.keys(user.followers || {}).length;
    document.getElementById('profileFollowingCount').innerText = Object.keys(user.following || {}).length;
    const grid = document.getElementById('profilePostsGrid');
    grid.innerHTML = userPosts.map(post => `<div class="profile-post" onclick="openCommentsModal('${post.id}')">${post.mediaUrl ? (post.mediaType === 'image' ? `<img src="${post.mediaUrl}" loading="lazy">` : post.mediaType === 'video' ? `<video src="${post.mediaUrl}"></video>` : '<i class="fas fa-music text-2xl"></i>') : '<i class="fas fa-file-alt text-2xl"></i>'}</div>`).join('');
    if (userPosts.length === 0) grid.innerHTML = '<div class="col-span-3 text-center py-10" style="color:#71767b">لا توجد منشورات</div>';
    const buttonsDiv = document.getElementById('profileButtons');
    buttonsDiv.innerHTML = '';
    if (userId === currentUser.uid) {
        buttonsDiv.innerHTML = `<button class="profile-btn btn-primary" onclick="openEditProfileModal()">✏️ تعديل الملف</button><button class="profile-btn btn-secondary" onclick="logout()">🚪 تسجيل خروج</button>${isAdmin ? '<button class="profile-btn btn-secondary" onclick="openAdmin()">🔧 لوحة التحكم</button>' : ''}`;
    } else {
        const isFollowing = currentUserData?.following && currentUserData.following[userId];
        buttonsDiv.innerHTML = `<button class="profile-btn btn-primary" onclick="toggleFollow('${userId}', this)">${isFollowing ? '✅ متابع' : '➕ متابعة'}</button><button class="profile-btn btn-secondary" onclick="openPrivateChat('${userId}')"><i class="fas fa-envelope"></i> مراسلة</button>`;
    }
}

window.openEditProfileModal = function() { document.getElementById('editName').value = currentUserData?.name || ''; document.getElementById('editBio').value = currentUserData?.bio || ''; document.getElementById('editProfileModal').classList.add('open'); };
window.closeEditProfileModal = function() { document.getElementById('editProfileModal').classList.remove('open'); };
window.saveProfileEdit = async function() {
    const newName = document.getElementById('editName').value;
    const newBio = document.getElementById('editBio').value;
    if (!newName.trim()) { showToast('الاسم مطلوب'); return; }
    await firebase.database().ref(`users/${currentUser.uid}`).update({ name: newName.trim(), bio: newBio });
    showToast('✅ تم تحديث الملف الشخصي');
    closeEditProfileModal();
    setTimeout(() => location.reload(), 1000);
};

// ========== AVATAR / COVER UPLOAD ==========
window.changeAvatar = function() { document.getElementById('avatarInput')?.click(); };
window.changeCover = function() { document.getElementById('coverInput')?.click(); };

(function setupUploadInputs() {
    if (!document.getElementById('avatarInput')) {
        const inp = document.createElement('input'); inp.type = 'file'; inp.accept = 'image/*'; inp.id = 'avatarInput'; inp.style.display = 'none';
        document.body.appendChild(inp);
        inp.addEventListener('change', async (e) => {
            const file = e.target.files[0]; if (!file) return;
            showToast('📤 جاري رفع الصورة...');
            const result = await uploadMedia(file);
            await firebase.database().ref(`users/${currentUser.uid}`).update({ avatarUrl: result.url });
            showToast('✅ تم تحديث الصورة الشخصية'); location.reload();
        });
    }
    if (!document.getElementById('coverInput')) {
        const inp = document.createElement('input'); inp.type = 'file'; inp.accept = 'image/*'; inp.id = 'coverInput'; inp.style.display = 'none';
        document.body.appendChild(inp);
        inp.addEventListener('change', async (e) => {
            const file = e.target.files[0]; if (!file) return;
            showToast('📤 جاري رفع الصورة...');
            const result = await uploadMedia(file);
            await firebase.database().ref(`users/${currentUser.uid}`).update({ coverUrl: result.url });
            showToast('✅ تم تحديث صورة الغلاف'); location.reload();
        });
    }
})();

// ========== FOLLOW ==========
window.toggleFollow = async function(userId, btn) {
    if (!currentUser || currentUser.uid === userId) return;
    const userRef = firebase.database().ref(`users/${currentUser.uid}/following/${userId}`);
    const targetRef = firebase.database().ref(`users/${userId}/followers/${currentUser.uid}`);
    const snap = await userRef.once('value');
    if (snap.exists()) { await userRef.set(null); await targetRef.set(null); if (btn) btn.innerText = '➕ متابعة'; showToast(`👋 توقفت عن متابعة ${allUsers[userId]?.name}`); }
    else { await userRef.set(true); await targetRef.set(true); if (btn) btn.innerText = '✅ متابع'; addNotification(userId, 'follow'); showToast(`👥 بدأت بمتابعة ${allUsers[userId]?.name}`); }
    if (viewingProfileUserId === userId) await loadProfileData(userId);
};

window.openFollowersList = async function(type) {
    document.getElementById('followersTitle').innerText = type === 'followers' ? 'المتابعون' : 'المتابَعون';
    const container = document.getElementById('followersList');
    const user = viewingProfileUserId ? allUsers[viewingProfileUserId] : currentUserData;
    const list = type === 'followers' ? user?.followers : user?.following;
    container.innerHTML = '';
    if (list) {
        for (const [uid] of Object.entries(list)) {
            const u = allUsers[uid];
            if (u) container.innerHTML += `<div class="follower-item" onclick="viewProfile('${uid}')"><div class="avatar-xs">${u.avatarUrl ? `<img src="${u.avatarUrl}">` : (u.name?.charAt(0) || 'U')}</div><div><div class="font-bold">${escapeHtml(u.name)}</div><div class="text-sm" style="color:#71767b">@${u.name?.toLowerCase().replace(/\s/g, '')}</div></div></div>`;
        }
    }
    if (container.innerHTML === '') container.innerHTML = '<div class="text-center py-10" style="color:#71767b">لا يوجد مستخدمين</div>';
    document.getElementById('followersPanel').classList.add('open'); document.getElementById('backBtn').style.display = 'flex';
};
window.closeFollowers = function() { document.getElementById('followersPanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };

// ========== CHAT ==========
function getChatId(uid1, uid2) { return uid1 < uid2 ? `${uid1}_${uid2}` : `${uid2}_${uid1}`; }

window.openConversations = async function() {
    const panel = document.getElementById('conversationsPanel');
    const container = document.getElementById('conversationsList');
    const convSnap = await firebase.database().ref(`private_chats/${currentUser.uid}`).once('value');
    const conversations = convSnap.val() || {};
    container.innerHTML = '';
    for (const [otherId, convData] of Object.entries(conversations)) {
        const otherUser = allUsers[otherId];
        if (otherUser) container.innerHTML += `<div class="conversation-item" onclick="openPrivateChat('${otherId}')"><div class="avatar-sm">${otherUser.avatarUrl ? `<img src="${otherUser.avatarUrl}">` : (otherUser.name?.charAt(0) || 'U')}</div><div><div class="font-bold">${escapeHtml(otherUser.name)}</div><div class="text-sm" style="color:#71767b">${convData.lastMessage?.substring(0, 40) || 'رسالة'}</div></div></div>`;
    }
    if (container.innerHTML === '') container.innerHTML = '<div class="text-center py-10" style="color:#71767b">لا توجد محادثات بعد</div>';
    panel.classList.add('open'); document.getElementById('backBtn').style.display = 'flex';
};
window.closeConversations = function() { document.getElementById('conversationsPanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };

window.openPrivateChat = async function(otherUserId) {
    currentChatUserId = otherUserId;
    const user = allUsers[otherUserId];
    document.getElementById('chatUserName').innerText = user?.name || 'مستخدم';
    document.getElementById('chatAvatar').innerHTML = user?.avatarUrl ? `<img src="${user.avatarUrl}">` : (user?.name?.charAt(0) || 'U');
    await loadPrivateMessages(otherUserId);
    document.getElementById('chatPanel').classList.add('open');
    document.getElementById('backBtn').style.display = 'flex';
    closeConversations();
};
window.closeChat = function() { document.getElementById('chatPanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; currentChatUserId = null; };

async function loadPrivateMessages(otherUserId) {
    const container = document.getElementById('chatMessages');
    container.innerHTML = '<div class="text-center py-10" style="color:#71767b">جاري التحميل...</div>';
    const chatId = getChatId(currentUser.uid, otherUserId);
    const messagesSnap = await firebase.database().ref(`private_messages/${chatId}`).once('value');
    const messages = messagesSnap.val() || {};
    container.innerHTML = '';
    const sorted = Object.entries(messages).sort((a,b)=>a[1].timestamp-b[1].timestamp);
    for (const [id, msg] of sorted) {
        const isSent = msg.senderId === currentUser.uid;
        const time = new Date(msg.timestamp).toLocaleTimeString();
        let content = '';
        if (msg.type === 'text') content = `<div class="message-bubble ${isSent ? 'sent' : 'received'}">${escapeHtml(msg.text)}</div>`;
        else if (msg.type === 'image') content = `<img src="${msg.imageUrl}" class="message-image" onclick="openImageModal('${msg.imageUrl}')">`;
        else if (msg.type === 'audio') content = `<div class="message-audio"><audio controls src="${msg.audioUrl}"></audio></div>`;
        container.innerHTML += `<div class="chat-message ${isSent ? 'sent' : 'received'}"><div>${content}<div style="font-size:10px;opacity:0.5;margin-top:4px;">${time}</div></div></div>`;
    }
    if (container.innerHTML === '') container.innerHTML = '<div class="text-center py-10" style="color:#71767b">لا توجد رسائل بعد</div>';
    container.scrollTop = container.scrollHeight;
}

window.sendChatMessage = async function() {
    const input = document.getElementById('chatMessageInput');
    const text = input?.value.trim();
    if (!text || !currentChatUserId) return;
    const chatId = getChatId(currentUser.uid, currentChatUserId);
    await firebase.database().ref(`private_messages/${chatId}`).push({ senderId: currentUser.uid, senderName: currentUserData?.name, text, type: 'text', timestamp: Date.now() });
    await firebase.database().ref(`private_chats/${currentUser.uid}/${currentChatUserId}`).set({ lastMessage: text, lastTimestamp: Date.now(), withUser: currentChatUserId });
    await firebase.database().ref(`private_chats/${currentChatUserId}/${currentUser.uid}`).set({ lastMessage: text, lastTimestamp: Date.now(), withUser: currentUser.uid });
    input.value = '';
    await loadPrivateMessages(currentChatUserId);
};

window.sendChatImage = async function(input) {
    const file = input.files[0]; if (!file || !currentChatUserId) return;
    const result = await uploadMedia(file);
    const chatId = getChatId(currentUser.uid, currentChatUserId);
    await firebase.database().ref(`private_messages/${chatId}`).push({ senderId: currentUser.uid, senderName: currentUserData?.name, imageUrl: result.url, type: 'image', timestamp: Date.now() });
    await firebase.database().ref(`private_chats/${currentUser.uid}/${currentChatUserId}`).set({ lastMessage: '📷 صورة', lastTimestamp: Date.now(), withUser: currentChatUserId });
    await firebase.database().ref(`private_chats/${currentChatUserId}/${currentUser.uid}`).set({ lastMessage: '📷 صورة', lastTimestamp: Date.now(), withUser: currentUser.uid });
    input.value = '';
    await loadPrivateMessages(currentChatUserId);
};

window.startRecordingChat = async function() {
    const btn = document.getElementById('chatRecordBtn');
    if (mediaRecorder && mediaRecorder.state === 'recording') { mediaRecorder.stop(); btn.innerHTML = '<i class="fas fa-microphone"></i>'; return; }
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream); audioChunks = [];
        mediaRecorder.ondataavailable = (event) => { audioChunks.push(event.data); };
        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/mp3' });
            const audioFile = new File([audioBlob], 'recording.mp3', { type: 'audio/mp3' });
            const result = await uploadMedia(audioFile);
            if (currentChatUserId) {
                const chatId = getChatId(currentUser.uid, currentChatUserId);
                await firebase.database().ref(`private_messages/${chatId}`).push({ senderId: currentUser.uid, senderName: currentUserData?.name, audioUrl: result.url, type: 'audio', timestamp: Date.now() });
                await firebase.database().ref(`private_chats/${currentUser.uid}/${currentChatUserId}`).set({ lastMessage: '🎤 رسالة صوتية', lastTimestamp: Date.now(), withUser: currentChatUserId });
                await firebase.database().ref(`private_chats/${currentChatUserId}/${currentUser.uid}`).set({ lastMessage: '🎤 رسالة صوتية', lastTimestamp: Date.now(), withUser: currentUser.uid });
                await loadPrivateMessages(currentChatUserId);
            }
            stream.getTracks().forEach(track => track.stop());
        };
        mediaRecorder.start();
        btn.innerHTML = '<i class="fas fa-stop-circle" style="color:#f91880"></i>';
    } catch (err) { showToast('لا يمكن الوصول إلى الميكروفون'); }
};

// ========== SEARCH ==========
window.openSearch = function() { document.getElementById('searchPanel').classList.add('open'); document.getElementById('backBtn').style.display = 'flex'; };
window.closeSearch = function() { document.getElementById('searchPanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };
window.searchAll = function() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    const resultsDiv = document.getElementById('searchResults');
    if (!query) { resultsDiv.innerHTML = ''; return; }
    const users = Object.values(allUsers).filter(u => u.name?.toLowerCase().includes(query));
    resultsDiv.innerHTML = users.map(u => `<div class="search-result" onclick="viewProfile('${u.uid}')"><div class="avatar-xs">${u.avatarUrl ? `<img src="${u.avatarUrl}">` : (u.name?.charAt(0) || 'U')}</div><div><div class="font-bold">${escapeHtml(u.name)}</div><div class="text-sm" style="color:#71767b">@${u.name?.toLowerCase().replace(/\s/g, '')}</div></div></div>`).join('');
    if (users.length === 0) resultsDiv.innerHTML = '<div class="text-center py-10" style="color:#71767b">لا توجد نتائج</div>';
};

// ========== ADMIN ==========
window.openAdmin = async function() {
    if (!isAdmin) return;
    const totalUsers = Object.keys(allUsers).length;
    const totalPosts = allPosts.length;
    const totalLikes = allPosts.reduce((s,p)=>s+(p.likes||0),0);
    const totalComments = allPosts.reduce((s,p)=>s+(p.comments ? Object.keys(p.comments).length : 0),0);
    document.getElementById('adminStats').innerHTML = `
        <div class="admin-stat"><div class="admin-stat-icon"><i class="fas fa-users"></i></div><div class="admin-stat-number">${totalUsers}</div><div class="admin-stat-label">مستخدمين</div></div>
        <div class="admin-stat"><div class="admin-stat-icon"><i class="fas fa-file-alt"></i></div><div class="admin-stat-number">${totalPosts}</div><div class="admin-stat-label">منشورات</div></div>
        <div class="admin-stat"><div class="admin-stat-icon" style="color:#f91880"><i class="fas fa-heart"></i></div><div class="admin-stat-number">${totalLikes}</div><div class="admin-stat-label">إعجابات</div></div>
        <div class="admin-stat"><div class="admin-stat-icon" style="color:#1d9bf0"><i class="fas fa-comment"></i></div><div class="admin-stat-number">${totalComments}</div><div class="admin-stat-label">تعليقات</div></div>`;
    const usersListDiv = document.getElementById('adminUsersList');
    usersListDiv.innerHTML = '';
    Object.entries(allUsers).forEach(([uid, u]) => {
        if (uid !== currentUser.uid) usersListDiv.innerHTML += `<div class="admin-item"><div><div class="admin-item-name">${escapeHtml(u.name)}</div><div class="admin-item-email">${u.email}</div></div><button class="admin-delete-btn" onclick="adminDeleteUser('${uid}')"><i class="fas fa-trash"></i> حذف</button></div>`;
    });
    if (usersListDiv.innerHTML === '') usersListDiv.innerHTML = '<div class="text-center py-10" style="color:#71767b">لا يوجد مستخدمين آخرين</div>';
    const postsListDiv = document.getElementById('adminPostsList');
    postsListDiv.innerHTML = '';
    allPosts.slice(0, 30).forEach(post => {
        postsListDiv.innerHTML += `<div class="admin-item"><div><div class="admin-item-name">${escapeHtml(post.senderName || 'مستخدم')}</div><div class="admin-item-email">${post.text?.substring(0, 60) || 'منشور بدون نص'} · ${new Date(post.timestamp).toLocaleString()}</div></div><button class="admin-delete-btn" onclick="adminDeletePost('${post.id}')"><i class="fas fa-trash"></i> حذف</button></div>`;
    });
    document.getElementById('adminPanel').classList.add('open'); document.getElementById('backBtn').style.display = 'flex';
};
window.closeAdmin = function() { document.getElementById('adminPanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };
window.adminDeleteUser = async function(userId) { if (!isAdmin || !confirm('⚠️ حذف هذا المستخدم وجميع منشوراته؟')) return; const posts = allPosts.filter(p => p.sender === userId); for (const post of posts) await firebase.database().ref(`posts/${post.id}`).set(null); await firebase.database().ref(`users/${userId}`).set(null); showToast('✅ تم حذف المستخدم'); location.reload(); };
window.adminDeletePost = async function(postId) { if (!isAdmin || !confirm('⚠️ حذف هذا المنشور؟')) return; await firebase.database().ref(`posts/${postId}`).set(null); showToast('✅ تم حذف المنشور'); renderFeed(); };

// ========== NAVIGATION ==========
window.switchTab = function(tab) { const navItems = document.querySelectorAll('.nav-item'); navItems.forEach(t => t.classList.remove('active')); if (event && event.target) { const clicked = event.target.closest('.nav-item'); if (clicked) clicked.classList.add('active'); } if (tab === 'home') { closeCompose(); closeProfile(); closeChat(); closeConversations(); closeNotifications(); closeSearch(); closeComments(); closeFollowers(); closeAdmin(); closeEditProfileModal(); } };
window.goToHome = function() { const homeBtn = document.querySelector('.nav-item i.fa-home')?.closest('.nav-item'); if (homeBtn) { document.querySelectorAll('.nav-item').forEach(t => t.classList.remove('active')); homeBtn.classList.add('active'); } closeCompose(); closeProfile(); closeChat(); closeConversations(); closeNotifications(); closeSearch(); closeComments(); closeFollowers(); closeAdmin(); closeEditProfileModal(); document.getElementById('backBtn').style.display = 'none'; };
window.goBack = function() {
    if (document.getElementById('commentsPanel')?.classList.contains('open')) closeComments();
    else if (document.getElementById('profilePanel')?.classList.contains('open')) closeProfile();
    else if (document.getElementById('chatPanel')?.classList.contains('open')) closeChat();
    else if (document.getElementById('conversationsPanel')?.classList.contains('open')) closeConversations();
    else if (document.getElementById('notificationsPanel')?.classList.contains('open')) closeNotifications();
    else if (document.getElementById('searchPanel')?.classList.contains('open')) closeSearch();
    else if (document.getElementById('followersPanel')?.classList.contains('open')) closeFollowers();
    else if (document.getElementById('adminPanel')?.classList.contains('open')) closeAdmin();
    else if (document.getElementById('composePanel')?.classList.contains('open')) closeCompose();
    else if (document.getElementById('editProfileModal')?.classList.contains('open')) closeEditProfileModal();
    else goToHome();
};
window.logout = function() { firebase.auth().signOut(); location.reload(); };

// ========== AUTH STATE ==========
firebase.auth().onAuthStateChanged(async (user) => {
    if (user) {
        currentUser = user;
        await loadUserData();
        isAdmin = ADMIN_EMAILS.includes(currentUser.email);
        document.getElementById('mainApp').style.display = 'block';
        updateNotificationBadge();
        if (localStorage.getItem('theme') === 'light') document.body.classList.add('light-mode');
        showToast(`👋 مرحباً ${currentUserData?.name || 'مستخدم'}`);
    } else {
        window.location.replace('auth.html');
    }
});

console.log('🟦 Nexus Platform Ready ✨');
"""

# ═══════════════════════════════════════════════════════════
# 🟦 5-9. الملفات المتبقية
# ═══════════════════════════════════════════════════════════

def build_upload():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟦 Nexus | رفع منشور</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root{--primary:#1d9bf0;--bg:#000;--surface:#1a1a1a;--border:rgba(255,255,255,0.08)}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Inter',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(20px);z-index:10}
        .btn-back{background:rgba(29,155,240,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}
        .container{max-width:500px;margin:0 auto;padding:20px}
        textarea{width:100%;min-height:120px;background:transparent;border:none;color:#fff;font-size:18px;resize:none;outline:none;font-family:inherit;padding:12px}
        .tools{display:flex;gap:12px;padding:10px 0;border-top:1px solid var(--border);border-bottom:1px solid var(--border)}
        .tool{background:none;border:none;color:var(--primary);font-size:18px;padding:8px;border-radius:50%;cursor:pointer}
        .preview{margin:12px 0;display:none}
        .preview img,.preview video{max-height:250px;border-radius:18px;width:100%;object-fit:cover}
        .btn-post{width:100%;background:var(--primary);color:#fff;border:none;padding:12px;border-radius:40px;font-weight:700;cursor:pointer;margin-top:16px}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>🟦 رفع منشور</h2></div>
<div class="container">
    <textarea id="postText" placeholder="ماذا يحدث؟"></textarea>
    <div id="mediaPreview" class="preview"></div>
    <div class="tools">
        <button class="tool" onclick="document.getElementById('postImage').click()"><i class="fas fa-image"></i></button>
        <button class="tool" onclick="document.getElementById('postVideo').click()"><i class="fas fa-video"></i></button>
    </div>
    <input type="file" id="postImage" accept="image/*" style="display:none" onchange="previewMedia(this,'image')">
    <input type="file" id="postVideo" accept="video/*" style="display:none" onchange="previewMedia(this,'video')">
    <button class="btn-post" onclick="createPost()">نشر</button>
    <div id="status" style="text-align:center;margin-top:12px;font-size:13px;color:var(--primary)"></div>
</div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null,currentUserData=null,selectedMediaFile=null;
    firebase.auth().onAuthStateChanged(async u=>{if(!u)window.location.href='auth.html';currentUser=u;const snap=await firebase.database().ref('users/'+u.uid).once('value');if(snap.exists())currentUserData={uid:u.uid,...snap.val()}});
    window.previewMedia=function(input,type){const file=input.files[0];if(!file)return;selectedMediaFile=file;const reader=new FileReader();reader.onload=function(e){const preview=document.getElementById('mediaPreview');if(type==='image')preview.innerHTML=`<img src="${e.target.result}">`;else preview.innerHTML=`<video controls><source src="${e.target.result}"></video>`;preview.style.display='block'};reader.readAsDataURL(file)};
    async function uploadMedia(file){const fd=new FormData();fd.append('file',file);fd.append('upload_preset',UPLOAD_PRESET);let rt='image';if(file.type.startsWith('video/'))rt='video';const res=await fetch(`https://api.cloudinary.com/v1_1/${CLOUD_NAME}/${rt}/upload`,{method:'POST',body:fd});const data=await res.json();return{url:data.secure_url,type:rt}}
    window.createPost=async function(){const text=document.getElementById('postText').value;if(!text.trim()&&!selectedMediaFile){document.getElementById('status').innerText='اكتب شيئاً أو اختر وسائط';return}document.getElementById('status').innerText='جاري النشر...';let mediaUrl='',mediaType='none';if(selectedMediaFile){try{const result=await uploadMedia(selectedMediaFile);mediaUrl=result.url;mediaType=result.type}catch(e){document.getElementById('status').innerText='فشل رفع الوسائط';return}}try{await firebase.database().ref('posts').push({text,mediaUrl,mediaType,sender:currentUser.uid,senderName:currentUserData?.name,likes:0,likedBy:{},retweets:{},retweetedBy:{},comments:{},timestamp:Date.now()});document.getElementById('status').innerText='تم النشر!';setTimeout(()=>window.location.href='index.html',1500)}catch(e){document.getElementById('status').innerText='فشل النشر'}};
</script>
</body>
</html>"""

def build_chat():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟦 Nexus | رسائل</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root{--primary:#1d9bf0;--bg:#000;--surface:#1a1a1a;--border:rgba(255,255,255,0.08)}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Inter',sans-serif;background:var(--bg);color:#fff;height:100vh;display:flex;flex-direction:column}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);background:rgba(0,0,0,0.85);backdrop-filter:blur(20px)}
        .btn-back{background:rgba(29,155,240,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}
        .conv-item{display:flex;align-items:center;gap:12px;padding:14px;border-bottom:1px solid var(--border);cursor:pointer}
        .conv-item:hover{background:rgba(255,255,255,0.02)}
        .avatar-sm{width:48px;height:48px;border-radius:50%;background:var(--primary);overflow:hidden;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:20px}
        .avatar-sm img{width:100%;height:100%;object-fit:cover}
        .msgs{flex:1;overflow-y:auto;padding:12px;display:flex;flex-direction:column;gap:10px}
        .bubble{max-width:80%;padding:8px 12px;border-radius:18px;font-size:13px}
        .bubble.sent{background:var(--primary);color:#fff;align-self:flex-end}
        .bubble.received{background:var(--surface);align-self:flex-start}
        .input-bar{display:flex;gap:10px;padding:10px;border-top:1px solid var(--border);background:var(--bg);align-items:center}
        .input-bar input{flex:1;padding:10px 14px;border:1px solid var(--border);border-radius:40px;background:var(--surface);color:#fff;outline:none;font-size:13px}
        .input-bar button{background:none;border:none;color:var(--primary);font-size:18px;cursor:pointer;padding:6px}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>🟦 الرسائل</h2></div>
<div id="convList" style="flex:1;overflow-y:auto"></div>
<div id="msgsList" class="msgs" style="display:none"></div>
<div class="input-bar" id="chatInput" style="display:none"><input type="text" id="msgInput" placeholder="اكتب رسالة..."><button onclick="sendMsg()"><i class="fas fa-paper-plane"></i></button></div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null,allUsers={},chatUserId=null;
    function getChatId(u1,u2){return u1<u2?`${u1}_${u2}`:`${u2}_${u1}`}
    firebase.auth().onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;firebase.database().ref('users').on('value',s=>{allUsers=s.val()||{}});loadConvs()});
    async function loadConvs(){const cl=document.getElementById('convList');cl.style.display='block';document.getElementById('msgsList').style.display='none';document.getElementById('chatInput').style.display='none';const snap=await firebase.database().ref('private_chats/'+currentUser.uid).once('value');const convs=snap.val()||{};cl.innerHTML='';for(const[oid,c]of Object.entries(convs)){const u=allUsers[oid];if(u)cl.innerHTML+=`<div class="conv-item" onclick="openChat('${oid}')"><div class="avatar-sm">${u.avatarUrl?`<img src="${u.avatarUrl}">`:(u.name?.charAt(0)||'U')}</div><div><div style="font-weight:600">${u.name}</div><div style="font-size:12px;color:#71767b">${c.lastMessage?.substring(0,40)||'رسالة'}</div></div></div>`}if(cl.innerHTML==='')cl.innerHTML='<div style="text-align:center;color:#71767b;padding:40px">لا توجد محادثات</div>'}
    async function openChat(uid){chatUserId=uid;const u=allUsers[uid];document.getElementById('convList').style.display='none';document.getElementById('msgsList').style.display='flex';document.getElementById('chatInput').style.display='flex';await loadMsgs()}
    async function loadMsgs(){const ml=document.getElementById('msgsList');ml.innerHTML='';const chatId=getChatId(currentUser.uid,chatUserId);const snap=await firebase.database().ref('private_messages/'+chatId).once('value');const ms=snap.val()||{};Object.values(ms).sort((a,b)=>a.timestamp-b.timestamp).forEach(m=>{const sent=m.senderId===currentUser.uid;ml.innerHTML+=`<div class="bubble ${sent?'sent':'received'}">${m.type==='image'?`<img src="${m.imageUrl}" style="max-width:180px;border-radius:14px">`:m.text}<div style="font-size:10px;opacity:0.5;margin-top:4px">${new Date(m.timestamp).toLocaleTimeString()}</div></div>`});ml.scrollTop=ml.scrollHeight}
    async function sendMsg(){const inp=document.getElementById('msgInput');const txt=inp.value.trim();if(!txt||!chatUserId)return;const chatId=getChatId(currentUser.uid,chatUserId);await firebase.database().ref('private_messages/'+chatId).push({senderId:currentUser.uid,text:txt,type:'text',timestamp:Date.now()});await firebase.database().ref('private_chats/'+currentUser.uid+'/'+chatUserId).set({lastMessage:txt,lastTimestamp:Date.now(),withUser:chatUserId});await firebase.database().ref('private_chats/'+chatUserId+'/'+currentUser.uid).set({lastMessage:txt,lastTimestamp:Date.now(),withUser:currentUser.uid});inp.value='';await loadMsgs()}
    window.openChat=openChat;window.sendMsg=sendMsg;window.loadConvs=loadConvs;
</script>
</body>
</html>"""

def build_explore():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟦 Nexus | استكشاف</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root{--primary:#1d9bf0;--bg:#000;--border:rgba(255,255,255,0.08)}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Inter',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(20px);z-index:10}
        .btn-back{background:rgba(29,155,240,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}
        .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;padding:2px}
        .thumb{aspect-ratio:1;background:#1a1a2a;display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;overflow:hidden}
        .thumb img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
        .thumb i{position:absolute;font-size:24px;color:#fff;z-index:1;opacity:0;transition:0.3s}
        .thumb:hover i{opacity:1}
        .thumb .likes{position:absolute;bottom:4px;left:4px;font-size:10px;background:rgba(0,0,0,0.6);padding:2px 6px;border-radius:10px}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>🟦 استكشاف</h2></div>
<div class="grid" id="exploreGrid"></div>
<script src="firebase-config.js"></script>
<script>
    firebase.database().ref('posts').on('value',s=>{const data=s.val()||{};const vids=Object.entries(data).map(([k,v])=>({id:k,...v})).filter(p=>p.mediaUrl&&(p.mediaType==='image'||p.mediaType==='video')).sort((a,b)=>(b.likes||0)-(a.likes||0));const g=document.getElementById('exploreGrid');g.innerHTML=vids.length?vids.map(p=>`<div class="thumb" onclick="window.open('${p.mediaUrl}','_blank')">${p.mediaType==='image'?`<img src="${p.mediaUrl}">`:`<video src="${p.mediaUrl}"></video>`}<i class="fas fa-play"></i><span class="likes"><i class="fas fa-heart"></i> ${p.likes||0}</span></div>`).join(''):'<div style="text-align:center;padding:40px;grid-column:1/-1;color:#71767b">لا توجد وسائط</div>'});
</script>
</body>
</html>"""

def build_notifications():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟦 Nexus | إشعارات</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root{--primary:#1d9bf0;--bg:#000;--border:rgba(255,255,255,0.08)}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Inter',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(20px);z-index:10}
        .btn-back{background:rgba(29,155,240,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}
        .notif-item{display:flex;gap:12px;padding:14px 16px;border-bottom:1px solid var(--border);align-items:center}
        .notif-icon{width:40px;height:40px;border-radius:50%;background:rgba(29,155,240,0.1);display:flex;align-items:center;justify-content:center;font-size:18px}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>🟦 الإشعارات</h2></div>
<div id="notifsList"></div>
<script src="firebase-config.js"></script>
<script>
    firebase.auth().onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}const snap=await firebase.database().ref('notifications/'+u.uid).once('value');const ns=snap.val()||{};const c=document.getElementById('notifsList');const items=Object.values(ns).reverse();const icons={like:'❤️',comment:'💬',retweet:'🔁',quote:'📝',follow:'👥'};c.innerHTML=items.length?items.map(n=>`<div class="notif-item"><div class="notif-icon">${icons[n.type]||'🔔'}</div><div><div style="font-weight:600">${n.fromUsername||'مستخدم'}</div><div style="font-size:12px;color:#71767b;margin-top:2px">${n.message||''}</div><div style="font-size:10px;color:#71767b;margin-top:4px">${new Date(n.timestamp).toLocaleString()}</div></div></div>`).join(''):'<div style="text-align:center;padding:40px;color:#71767b">لا توجد إشعارات</div>'});
</script>
</body>
</html>"""

def build_settings():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟦 Nexus | إعدادات</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root{--primary:#1d9bf0;--bg:#000;--border:rgba(255,255,255,0.08);--surface:#1a1a1a}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Inter',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(20px);z-index:10}
        .btn-back{background:rgba(29,155,240,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}
        .item{display:flex;justify-content:space-between;align-items:center;padding:16px;border-bottom:1px solid var(--border);cursor:pointer}
        .item:hover{background:rgba(255,255,255,0.02)}
        .btn-danger{background:rgba(249,24,128,0.2);border:1px solid rgba(249,24,128,0.3);color:#f91880;padding:12px 24px;border-radius:30px;cursor:pointer;font-size:14px;margin:20px auto;display:block}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>🟦 الإعدادات</h2></div>
<div>
    <div class="item" onclick="window.location.href='index.html'"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-user" style="color:var(--primary)"></i><span>الملف الشخصي</span></div><i class="fas fa-chevron-left" style="opacity:0.5"></i></div>
    <div class="item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-moon" style="color:var(--primary)"></i><span>المظهر</span></div><span style="opacity:0.5;font-size:13px">داكن / فاتح</span></div>
    <div class="item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-info-circle" style="color:var(--primary)"></i><span>حول التطبيق</span></div><span style="opacity:0.5;font-size:13px">Nexus v2026.1</span></div>
    <button class="btn-danger" onclick="logout()"><i class="fas fa-sign-out-alt"></i> تسجيل الخروج</button>
</div>
<script src="firebase-config.js"></script>
<script>
    firebase.auth().onAuthStateChanged(u=>{if(!u)window.location.href='auth.html'});
    function logout(){firebase.auth().signOut();window.location.href='auth.html'}
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🟦 MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  🟦  NEXUS 2026 - SOCIAL PLATFORM GENERATOR  ✨      ║
║     Ultimate Generator - 9 Files - 2000+ Lines           ║
║                                                          ║
║  ✨  Posts + Comments + Replies + Quotes              ║
║  ❤️   Likes + Retweets + Bookmarks                   ║
║  💬  Private Chat (Text/Image/Audio)                  ║
║  📝  Stories + Search + Admin Panel                   ║
║  🛡️   Delete Users/Posts + Dark/Light Mode           ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)

    section("BUILDING FILES - إنشاء الملفات")

    write("firebase-config.js", build_config())
    write("auth.html", build_auth())
    write("index.html", build_index())
    write("script.js", build_script())
    write("upload.html", build_upload())
    write("chat.html", build_chat())
    write("explore.html", build_explore())
    write("notifications.html", build_notifications())
    write("settings.html", build_settings())

    print(f"""
{'='*60}
  🟦 BUILD COMPLETE - تم الإنشاء بنجاح! ✨
{'='*60}

  📊 إحصائيات:
     • {TOTAL_LINES} إجمالي عدد الأسطر
     • 9 ملفات تم إنشاؤها

  📁 الملفات:
     1. firebase-config.js   → إعدادات Firebase + Cloudinary
     2. auth.html            → تسجيل دخول + اشتراك
     3. index.html           → الرئيسية + كل الواجهات (Panel-based SPA)
     4. script.js            → كل المنطق (Posts, Chat, Admin, Search...)
     5. upload.html          → صفحة رفع منشور مستقلة
     6. chat.html            → صفحة دردشة مستقلة
     7. explore.html         → استكشاف الوسائط
     8. notifications.html   → صفحة الإشعارات
     9. settings.html        → إعدادات + تسجيل خروج

  🟦 المميزات:
     • ❤️  منشورات + إعجابات + ريتويت + إشارات مرجعية
     • 💬 تعليقات + ردود متداخلة
     • 📝 اقتباسات (Quote Tweets)
     • 💌 دردشة خاصة (نص + صورة + صوت)
     • 📸 رفع وسائط (صور + فيديو + تسجيل صوتي)
     • 👤 ملف شخصي + تعديل + صورة + غلاف
     • 🔍 بحث عن المستخدمين
     • 🔔 إشعارات فورية
     • 🌓 الوضع الليلي/النهاري
     • 🛡️  لوحة تحكم أدمن (حذف مستخدمين/منشورات)
     • 📱 تصميم متجاوب + دعم Fullscreen

  🔑 بيانات الاتصال:
     • Firebase: muvg-42126
     • Cloudinary: dmqyd0haj / s3_gok
     • Admin: jasim28v@gmail.com

  🟦 للتشغيل:
     1. شغّل: python scraper.py
     2. ارفع الملفات إلى GitHub Pages
     3. افتح auth.html في المتصفح
  🟦 NEXUS READY! ✨
{'='*60}
    """)

if __name__ == "__main__":
    main()
