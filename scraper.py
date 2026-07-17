#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                            ║
║  🟦 SOTWE 2026 - SOCIAL PLATFORM GENERATOR  🟦            ║
║     Ultimate Version - 9 Files - 2500+ Lines               ║
║                                                            ║
║  🔥  Firebase: muvg-42126                                 ║
║  ☁️   Cloudinary: dmqyd0haj / s3_gok                     ║
║  👑  Admin: jasim28v@gmail.com                            ║
║  🟦  Design: Modern Blue & Pink Luxury                    ║
║                                                            ║
║  ✨  PREMIUM FEATURES:                                     ║
║     • 🔔 Notification System                              ║
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
║     • 🎨 Modern Polished UI                               ║
║                                                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys

# ═══════════════════════════════════════════════════════════
# 🔑 CONFIGURATION
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

TOTAL_LINES = 0

def write(filename, content):
    global TOTAL_LINES
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n') + 1
    TOTAL_LINES += lines
    print(f"  ✅ {filename} ({lines} سطر)")

def section(title):
    print(f"\n{'='*60}")
    print(f"  🟦  {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# 1. firebase-config.js
# ═══════════════════════════════════════════════════════════

def build_config():
    return f"""// 🟦 SOTWE 2026 - Firebase & Cloudinary Configuration
// Firebase: muvg-42126 | Cloudinary: dmqyd0haj

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

const ADMIN_EMAILS = {ADMIN_EMAILS_JS};
const APP_NAME = "Sotwe";
const APP_VERSION = "2026.1";

console.log('🟦 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨', 'color: #1d9bf0; font-size: 16px; font-weight: bold;');
"""

# ═══════════════════════════════════════════════════════════
# 2. auth.html
# ═══════════════════════════════════════════════════════════

def build_auth():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>🟦 Sotwe | دخول</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{min-height:100vh;min-height:-webkit-fill-available;background:#000;display:flex;align-items:center;justify-content:center;font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;overflow:hidden}
        .bg-orb{position:fixed;border-radius:50%;filter:blur(140px);opacity:0.2}
        .bg-orb:nth-child(1){width:450px;height:450px;background:#1d9bf0;top:-120px;left:-120px}
        .bg-orb:nth-child(2){width:380px;height:380px;background:#f91880;bottom:-120px;right:-120px;animation-delay:5s}
        @keyframes orbFloat{0%{transform:translate(0,0)scale(1)}100%{transform:translate(60px,-60px)scale(1.4)}}
        .bg-orb{animation:orbFloat 18s infinite alternate}
        .card{position:relative;z-index:1;width:90%;max-width:460px;background:rgba(0,0,0,0.85);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border-radius:32px;padding:48px 40px;border:1px solid rgba(29,155,240,0.2);box-shadow:0 30px 70px rgba(29,155,240,0.1);animation:fadeUp 0.8s ease;text-align:center}
        @keyframes fadeUp{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:translateY(0)}}
        h1{font-size:56px;font-weight:900;margin-bottom:32px;background:linear-gradient(135deg,#1d9bf0,#f91880);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
        h2{font-size:24px;font-weight:700;margin-bottom:8px;text-align:right}
        .sub{color:#71767b;font-size:14px;text-align:right;margin-bottom:24px}
        .tabs{display:flex;gap:4px;background:rgba(29,155,240,0.06);border-radius:40px;padding:4px;margin-bottom:24px}
        .tab{flex:1;padding:12px;background:none;border:none;color:rgba(255,255,255,0.5);cursor:pointer;border-radius:40px;font-size:14px;transition:all 0.3s;font-weight:600}
        .tab.active{background:linear-gradient(135deg,#1d9bf0,#f91880);color:#fff;box-shadow:0 8px 20px rgba(29,155,240,0.4)}
        .form{display:none;animation:fadeIn 0.4s ease;text-align:right}
        .form.active{display:block}
        @keyframes fadeIn{from{opacity:0}to{opacity:1}}
        input{width:100%;padding:16px 20px;margin:10px 0;border-radius:12px;background:#1a1a1a;border:1px solid #2f3336;color:#fff;font-size:16px;outline:none;transition:0.2s}
        input:focus{border-color:#1d9bf0;box-shadow:0 0 0 2px rgba(29,155,240,0.2)}
        input::placeholder{color:rgba(255,255,255,0.3)}
        button{width:100%;padding:14px;margin-top:16px;background:#1d9bf0;border:none;border-radius:40px;color:#fff;font-weight:700;font-size:16px;cursor:pointer;transition:0.2s}
        button:hover{background:#1a8cd8}
        button:disabled{opacity:0.5;pointer-events:none}
        .msg{text-align:center;color:#f91880;font-size:13px;margin-top:12px;min-height:20px}
        .msg.success{color:#4ade80}
        .link{margin-top:32px;color:#71767b;font-size:14px}
        .link a{color:#1d9bf0;text-decoration:none;font-weight:600}
        .forgot{display:block;text-align:right;color:#1d9bf0;font-size:13px;margin-top:8px;text-decoration:none}
        .forgot:hover{text-decoration:underline}
    </style>
</head>
<body>
    <div class="bg-orb"></div><div class="bg-orb"></div>
    <div class="card">
        <h1>Sotwe</h1>
        <div class="tabs">
            <button class="tab active" id="tabLogin" onclick="switchAuth('login')"><i class="fas fa-sign-in-alt"></i> دخول</button>
            <button class="tab" id="tabRegister" onclick="switchAuth('register')"><i class="fas fa-user-plus"></i> اشتراك</button>
        </div>
        <div id="formLogin" class="form active">
            <h2>تسجيل الدخول</h2>
            <p class="sub">قم بالوصول إلى حسابك في Sotwe</p>
            <input type="email" id="loginEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email">
            <input type="password" id="loginPass" placeholder="🔒 كلمة المرور" autocomplete="current-password">
            <a href="#" class="forgot" onclick="resetPassword()">نسيت كلمة المرور؟</a>
            <button id="btnLogin" onclick="doLogin()"><i class="fas fa-arrow-right-to-bracket"></i> تسجيل الدخول</button>
            <div class="msg" id="loginMsg"></div>
            <div class="link">ليس لديك حساب؟ <a href="#" onclick="switchAuth('register')">إنشاء حساب</a></div>
        </div>
        <div id="formRegister" class="form">
            <h2>إنشاء حساب</h2>
            <p class="sub">قم بإنشاء حسابك في Sotwe</p>
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
                await auth.signInWithEmailAndPassword(email, password);
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
                const userCredential = await auth.createUserWithEmailAndPassword(email, password);
                const uid = userCredential.user.uid;
                await db.ref('users/' + uid).set({
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
            auth.sendPasswordResetEmail(email).then(() => {
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
        auth.onAuthStateChanged(user => { if(user) window.location.replace('index.html'); });
        console.log('🟦 Sotwe Auth Ready');
    </script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 3. index.html - Sotwe الرئيسية
# ═══════════════════════════════════════════════════════════

def build_index():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>🟦 Sotwe | الرئيسية</title>
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
            --border: #2f3336;
            --text: #ffffff;
            --text-secondary: #71767b;
        }
        *{margin:0;padding:0;box-sizing:border-box}
        html,body{width:100%;height:100%;overflow:hidden;position:fixed;top:0;left:0;right:0;bottom:0}
        body{font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg);color:var(--text);overflow-y:auto;overflow-x:hidden;height:100%;width:100%;position:relative}
        body.light-mode{--bg:#ffffff;--surface:#f7f9f9;--border:#eef2f5;--text:#111111;--text-secondary:#536471}
        body.light-mode .tweet-card{background:#fff;border-bottom-color:#eef2f5}
        body.light-mode .tweet-card:hover{background:#f7f9f9}
        body.light-mode .top-bar{background:rgba(255,255,255,0.98);border-bottom-color:#eef2f5}
        body.light-mode .bottom-nav{background:rgba(255,255,255,0.98);border-top-color:#eef2f5}
        body.light-mode .panel{background:#fff}
        body.light-mode input{background:#f7f9f9;border-color:#eef2f5;color:#111}
        body.light-mode .message-bubble.received{background:#eef2f5}
        body.light-mode .admin-stat{background:#f0f2f5}
        ::-webkit-scrollbar{width:6px}
        ::-webkit-scrollbar-track{background:#2f3336;border-radius:10px}
        ::-webkit-scrollbar-thumb{background:var(--primary);border-radius:10px}
        .top-bar{position:sticky;top:0;background:rgba(0,0,0,0.95);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);padding:12px 20px;display:flex;justify-content:space-between;align-items:center;z-index:100}
        .logo{font-size:28px;font-weight:900;background:linear-gradient(135deg,var(--primary),var(--secondary));-webkit-background-clip:text;-webkit-text-fill-color:transparent;cursor:pointer}
        .top-icons{display:flex;gap:24px;align-items:center}
        .top-icon{font-size:22px;color:var(--text);cursor:pointer;position:relative;transition:0.2s}
        .top-icon:hover{color:var(--primary)}
        .notification-badge{position:absolute;top:-8px;right:-12px;background:var(--secondary);color:#fff;font-size:10px;font-weight:700;border-radius:50%;width:18px;height:18px;display:none;align-items:center;justify-content:center}
        .back-btn{background:none;border:none;color:var(--primary);font-size:14px;cursor:pointer;display:none;align-items:center;gap:6px}
        .feed-container{padding:0 0 80px}
        .tweet-card{background:var(--bg);border-bottom:1px solid var(--border);padding:16px 20px;transition:background 0.2s;cursor:pointer}
        .tweet-card:hover{background:#080808}
        .tweet-header{display:flex;gap:12px;margin-bottom:8px}
        .tweet-avatar{width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--secondary));overflow:hidden;cursor:pointer;flex-shrink:0}
        .tweet-avatar img{width:100%;height:100%;object-fit:cover}
        .tweet-name{font-weight:800;cursor:pointer;font-size:15px}
        .tweet-username{font-size:13px;color:var(--text-secondary)}
        .tweet-time{font-size:13px;color:var(--text-secondary)}
        .tweet-content{margin:8px 0 12px;font-size:15px;line-height:1.4;white-space:pre-wrap}
        .tweet-media{margin:12px 0;border-radius:20px;overflow:hidden;background:var(--surface);cursor:pointer}
        .tweet-media img{width:100%;max-height:500px;object-fit:cover;transition:transform 0.3s ease}
        .tweet-media img:hover{transform:scale(1.02)}
        .tweet-media video{width:100%;max-height:500px;border-radius:20px}
        .tweet-media audio{width:100%}
        .quote-embed{margin-top:12px;border:1px solid var(--border);border-radius:16px;padding:12px;cursor:pointer}
        .tweet-actions{display:flex;justify-content:space-between;max-width:425px;margin-top:12px}
        .tweet-action{display:flex;align-items:center;gap:8px;background:none;border:none;color:var(--text-secondary);cursor:pointer;font-size:13px;padding:8px;border-radius:40px;transition:0.2s}
        .tweet-action i{font-size:18px}
        .tweet-action:hover{color:var(--primary);background:rgba(29,155,240,0.1)}
        .tweet-action.active{color:var(--secondary)}
        @keyframes heartBeat{0%{transform:scale(1)}50%{transform:scale(1.3);color:#f91880}100%{transform:scale(1)}}
        .heart-animation{animation:heartBeat 0.3s ease}
        .bottom-nav{position:fixed;bottom:0;left:0;right:0;background:rgba(0,0,0,0.95);backdrop-filter:blur(12px);border-top:1px solid var(--border);display:flex;justify-content:space-around;padding:8px 0 16px;z-index:100}
        .nav-item{background:none;border:none;font-size:26px;color:var(--text-secondary);cursor:pointer;padding:8px;border-radius:40px;transition:0.2s}
        .nav-item.active{color:var(--primary)}
        .nav-item:hover{background:rgba(29,155,240,0.1);color:var(--primary)}
        .panel{position:fixed;inset:0;background:var(--bg);z-index:200;transform:translateX(100%);transition:0.3s cubic-bezier(0.2,0.9,0.4,1.1);overflow-y:auto;display:flex;flex-direction:column}
        .panel.open{transform:translateX(0)}
        .panel-header{padding:16px;border-bottom:1px solid var(--border);display:flex;justify-content:space-between;align-items:center}
        .panel-body{flex:1;overflow-y:auto;padding:16px}
        .compose-area{padding:20px;max-width:600px;margin:0 auto}
        .compose-input{width:100%;min-height:150px;background:transparent;border:none;padding:16px;color:var(--text);font-size:20px;resize:none;outline:none;font-family:inherit}
        .media-preview{margin:16px 0;display:none}
        .media-preview img,.media-preview video{max-height:300px;border-radius:20px;width:100%;object-fit:cover}
        .compose-tools{display:flex;gap:16px;padding:12px 0;border-top:1px solid var(--border);border-bottom:1px solid var(--border)}
        .compose-tool{background:none;border:none;color:var(--primary);font-size:20px;padding:10px;border-radius:50%;cursor:pointer;transition:0.2s}
        .compose-tool:hover{background:rgba(29,155,240,0.1)}
        .btn-post{width:100%;background:var(--primary);color:#fff;border:none;padding:14px;border-radius:40px;font-weight:700;font-size:18px;cursor:pointer;margin-top:20px}
        .btn-post:hover{background:#1a8cd8}
        .comment-item{margin-bottom:24px;padding-bottom:16px;border-bottom:1px solid var(--border)}
        .comment-header{display:flex;gap:12px;margin-bottom:8px}
        .comment-avatar{width:40px;height:40px;border-radius:50%;background:var(--primary);overflow:hidden;cursor:pointer;flex-shrink:0}
        .comment-avatar img{width:100%;height:100%;object-fit:cover}
        .comment-user{font-weight:700;font-size:14px;cursor:pointer}
        .comment-time{font-size:11px;color:var(--text-secondary)}
        .comment-text{font-size:14px;margin:8px 0;line-height:1.4}
        .reply-list{margin-top:12px;margin-right:48px;border-right:2px solid var(--primary);padding-right:12px}
        .reply-item{margin-bottom:12px;padding-bottom:8px;border-bottom:1px solid var(--border)}
        .reply-header{display:flex;gap:8px;align-items:center;margin-bottom:4px}
        .reply-avatar{width:28px;height:28px;border-radius:50%;background:var(--primary);overflow:hidden}
        .reply-avatar img{width:100%;height:100%;object-fit:cover}
        .reply-user{font-weight:600;font-size:12px;cursor:pointer}
        .reply-text{font-size:13px;margin:4px 0}
        .comment-input-area{padding:16px;border-top:1px solid var(--border);background:var(--bg)}
        .comment-input{display:flex;gap:12px;align-items:center}
        .comment-input input{flex:1;padding:12px 16px;background:var(--surface);border:1px solid var(--border);border-radius:40px;color:var(--text);outline:none;font-size:14px}
        .profile-cover{width:100%;height:200px;background:linear-gradient(135deg,var(--primary),var(--secondary));cursor:pointer;position:relative}
        .profile-cover img{width:100%;height:100%;object-fit:cover}
        .profile-info{padding:0 20px 20px;position:relative}
        .profile-avatar{width:112px;height:112px;border-radius:50%;background:#111;border:4px solid var(--bg);margin-top:-56px;display:flex;align-items:center;justify-content:center;overflow:hidden;cursor:pointer;position:relative}
        .profile-avatar img{width:100%;height:100%;object-fit:cover}
        .profile-name{font-size:20px;font-weight:800;margin-top:12px}
        .profile-bio{color:var(--text-secondary);font-size:14px;margin:8px 0;white-space:pre-wrap}
        .profile-stats{display:flex;gap:24px;margin:16px 0;padding:12px 0;border-top:1px solid var(--border);border-bottom:1px solid var(--border)}
        .profile-stats div{text-align:center;cursor:pointer}
        .stat-number{font-size:18px;font-weight:800}
        .stat-label{font-size:13px;color:var(--text-secondary)}
        .profile-buttons{display:flex;gap:12px;margin:16px 0;flex-wrap:wrap}
        .profile-btn{padding:8px 24px;border-radius:40px;font-weight:700;cursor:pointer;border:none;font-size:14px;transition:0.2s}
        .btn-primary{background:var(--primary);color:#fff}
        .btn-primary:hover{background:#1a8cd8}
        .btn-secondary{background:var(--surface);color:var(--text)}
        .btn-secondary:hover{background:#3a3f42}
        .profile-posts-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;margin-top:4px;padding-bottom:80px}
        .profile-post{aspect-ratio:1;background:var(--surface);overflow:hidden;cursor:pointer;display:flex;align-items:center;justify-content:center;position:relative}
        .profile-post img,.profile-post video{width:100%;height:100%;object-fit:cover}
        .chat-messages{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:12px}
        .chat-message{display:flex;gap:8px;max-width:85%}
        .chat-message.sent{align-self:flex-end;flex-direction:row-reverse}
        .message-bubble{background:var(--surface);padding:10px 14px;border-radius:20px}
        .message-bubble.sent{background:var(--primary);color:#fff}
        .message-image{max-width:200px;border-radius:16px;cursor:pointer}
        .message-audio audio{height:36px}
        .chat-input-area{display:flex;gap:12px;padding:12px;border-top:1px solid var(--border);background:var(--bg);align-items:center}
        .chat-input-area input{flex:1;padding:12px 16px;border:1px solid var(--border);border-radius:40px;background:var(--surface);color:var(--text);outline:none}
        .chat-input-area button{background:none;border:none;color:var(--primary);font-size:20px;cursor:pointer;padding:8px;border-radius:50%}
        .search-input{width:calc(100% - 32px);margin:16px;padding:12px 20px;background:var(--surface);border:1px solid var(--border);border-radius:40px;color:var(--text);font-size:16px;outline:none}
        .search-result{display:flex;align-items:center;gap:12px;padding:12px 16px;border-bottom:1px solid var(--border);cursor:pointer}
        .search-result:hover{background:#080808}
        .notification-item{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);cursor:pointer}
        .notification-item:hover{background:#080808}
        .follower-item{display:flex;align-items:center;gap:12px;padding:12px 16px;border-bottom:1px solid var(--border);cursor:pointer}
        .follower-item:hover{background:#080808}
        .conversation-item{display:flex;align-items:center;gap:12px;padding:14px 16px;border-bottom:1px solid var(--border);cursor:pointer}
        .conversation-item:hover{background:#080808}
        .avatar-sm{width:48px;height:48px;border-radius:50%;background:var(--primary);overflow:hidden;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:20px;color:#fff}
        .avatar-sm img{width:100%;height:100%;object-fit:cover}
        .avatar-xs{width:40px;height:40px;border-radius:50%;background:var(--primary);overflow:hidden;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:16px;color:#fff}
        .avatar-xs img{width:100%;height:100%;object-fit:cover}
        .edit-profile-modal{position:fixed;inset:0;background:rgba(0,0,0,0.9);z-index:600;display:flex;align-items:center;justify-content:center;opacity:0;visibility:hidden;transition:0.3s}
        .edit-profile-modal.open{opacity:1;visibility:visible}
        .edit-profile-content{background:var(--bg);border-radius:28px;padding:32px;width:90%;max-width:500px;border:1px solid var(--border)}
        .edit-profile-content input,.edit-profile-content textarea{width:100%;padding:14px 16px;margin:12px 0;background:var(--surface);border:1px solid var(--border);border-radius:16px;color:var(--text);font-size:16px;outline:none}
        .edit-profile-content textarea{resize:vertical;min-height:100px;font-family:inherit}
        .edit-profile-content input:focus,.edit-profile-content textarea:focus{border-color:var(--primary)}
        .image-modal{position:fixed;inset:0;background:rgba(0,0,0,0.98);z-index:2000;display:flex;align-items:center;justify-content:center;opacity:0;visibility:hidden;transition:0.3s;cursor:pointer}
        .image-modal.open{opacity:1;visibility:visible}
        .image-modal img{max-width:95%;max-height:95%;object-fit:contain;border-radius:8px}
        .close-modal{position:absolute;top:20px;right:20px;background:rgba(0,0,0,0.6);color:#fff;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:24px;cursor:pointer;z-index:2001}
        .admin-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;padding:20px}
        .admin-stat{background:linear-gradient(135deg,#1a1a2a,#0f0f1a);padding:24px;border-radius:24px;text-align:center;border:1px solid rgba(29,155,240,0.2);transition:transform 0.2s,border-color 0.2s}
        .admin-stat:hover{transform:translateY(-4px);border-color:var(--primary)}
        .admin-stat-icon{font-size:32px;margin-bottom:12px;color:var(--primary)}
        .admin-stat-number{font-size:32px;font-weight:800;margin-bottom:8px}
        .admin-stat-label{font-size:14px;color:var(--text-secondary)}
        .admin-section{padding:20px;border-top:1px solid var(--border)}
        .admin-section-title{font-size:20px;font-weight:700;margin-bottom:16px;display:flex;align-items:center;gap:8px}
        .admin-item{display:flex;justify-content:space-between;align-items:center;padding:16px;border-bottom:1px solid var(--border);transition:background 0.2s}
        .admin-item:hover{background:#080808}
        .admin-item-name{font-weight:600;margin-bottom:4px}
        .admin-item-email{font-size:12px;color:var(--text-secondary)}
        .admin-item-text{font-size:14px;color:var(--text-secondary)}
        .admin-delete-btn{background:var(--secondary);color:#fff;border:none;padding:8px 16px;border-radius:40px;cursor:pointer;font-size:12px;font-weight:600;transition:0.2s}
        .admin-delete-btn:hover{background:#e01070;transform:scale(1.02)}
        .upload-btn{flex:1;background:var(--surface);color:var(--text);padding:12px;border-radius:40px;font-weight:600;cursor:pointer;text-align:center;transition:0.2s}
        .upload-btn:hover{background:#3a3f42}
        .loading{text-align:center;padding:80px 20px;color:var(--text-secondary)}
        .spinner{width:40px;height:40px;border:3px solid rgba(29,155,240,0.2);border-top-color:var(--primary);border-radius:50%;animation:spin 0.8s linear infinite;margin:0 auto 16px}
        @keyframes spin{to{transform:rotate(360deg)}}
        #customToast{position:fixed;bottom:90px;left:50%;transform:translateX(-50%);background:var(--primary);color:#fff;padding:12px 24px;border-radius:40px;z-index:1100;font-size:14px;font-weight:500;opacity:0;transition:0.3s;pointer-events:none;white-space:nowrap}
    </style>
</head>
<body>

<div id="imageModal" class="image-modal" onclick="closeImageModal()">
    <div class="close-modal" onclick="closeImageModal()">&times;</div>
    <img id="modalImage" src="">
</div>

<div id="mainApp" style="display:none">
    <div class="top-bar">
        <div class="logo" onclick="goToHome()">Sotwe</div>
        <div class="top-icons">
            <button class="back-btn" id="backBtn" onclick="goBack()"><i class="fas fa-arrow-right"></i> رجوع</button>
            <i class="fas fa-search top-icon" onclick="openSearch()"></i>
            <div class="top-icon" onclick="openNotifications()" id="notifIcon" style="position:relative;">
                <i class="far fa-bell"></i><span class="notification-badge" id="notifBadge"></span>
            </div>
            <i class="far fa-envelope top-icon" onclick="openConversations()"></i>
            <i class="fas fa-sun top-icon" onclick="toggleTheme()"></i>
        </div>
    </div>

    <div id="feedContainer" class="feed-container">
        <div class="loading"><div class="spinner"></div><span>جاري التحميل...</span></div>
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
        <div class="panel-header"><h3 style="font-size:20px;font-weight:700;">إنشاء منشور</h3><button onclick="closeCompose()" style="font-size:28px;background:none;border:none;color:var(--text-secondary);cursor:pointer;">&times;</button></div>
        <div class="compose-area">
            <textarea id="postText" class="compose-input" placeholder="ماذا يحدث؟"></textarea>
            <div id="mediaPreview" class="media-preview"></div>
            <div class="compose-tools">
                <button class="compose-tool" onclick="document.getElementById('postImage').click()"><i class="fas fa-image"></i></button>
                <button class="compose-tool" onclick="document.getElementById('postVideo').click()"><i class="fas fa-video"></i></button>
                <button class="compose-tool" id="audioRecordBtn" onclick="startAudioRecording()"><i class="fas fa-microphone"></i></button>
            </div>
            <input type="file" id="postImage" accept="image/*" style="display:none" onchange="previewMedia(this,'image')">
            <input type="file" id="postVideo" accept="video/*" style="display:none" onchange="previewMedia(this,'video')">
            <div id="postStatus" style="text-align:center;margin-top:12px;font-size:14px;color:var(--primary);"></div>
            <button onclick="createPost()" class="btn-post">نشر</button>
        </div>
    </div>

    <!-- Comments Panel -->
    <div id="commentsPanel" class="panel">
        <div class="panel-header"><h3 style="font-weight:700;">التعليقات</h3><button onclick="closeComments()" style="font-size:28px;background:none;border:none;color:var(--text-secondary);cursor:pointer;">&times;</button></div>
        <div id="commentsList" class="panel-body"></div>
        <div class="comment-input-area">
            <div class="comment-input">
                <input type="text" id="commentInput" placeholder="أضف تعليقاً...">
                <button onclick="addComment()" style="background:var(--primary);color:#fff;padding:10px 20px;border:none;border-radius:40px;font-weight:700;cursor:pointer;">نشر</button>
            </div>
        </div>
    </div>

    <!-- Profile Panel -->
    <div id="profilePanel" class="panel">
        <div class="panel-header"><h3 style="font-weight:700;font-size:20px;">الملف الشخصي</h3><button onclick="closeProfile()" style="font-size:28px;background:none;border:none;color:var(--text-secondary);cursor:pointer;">&times;</button></div>
        <div id="profileCover" class="profile-cover" onclick="changeCover()">
            <div style="position:absolute;bottom:16px;right:16px;background:rgba(0,0,0,0.6);border-radius:50%;width:36px;height:36px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:10;"><i class="fas fa-camera"></i></div>
        </div>
        <div class="profile-info">
            <div class="profile-avatar" id="profileAvatar" onclick="changeAvatar()">
                <div style="position:absolute;bottom:4px;right:4px;background:rgba(0,0,0,0.6);border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:10;"><i class="fas fa-camera fa-xs"></i></div>
            </div>
            <div class="profile-name" id="profileName"></div>
            <div class="profile-bio" id="profileBio"></div>
            <div style="display:flex;gap:12px;margin:16px 0;">
                <div class="upload-btn" onclick="changeAvatar()"><i class="fas fa-user-circle"></i> تغيير الصورة الشخصية</div>
                <div class="upload-btn" onclick="changeCover()"><i class="fas fa-image"></i> تغيير صورة الغلاف</div>
            </div>
            <div class="profile-stats">
                <div onclick="openFollowersList('followers')"><div class="stat-number" id="profileFollowersCount">0</div><div class="stat-label">متابع</div></div>
                <div onclick="openFollowersList('following')"><div class="stat-number" id="profileFollowingCount">0</div><div class="stat-label">يتابع</div></div>
                <div><div class="stat-number" id="profilePostsCount">0</div><div class="stat-label">منشورات</div></div>
            </div>
            <div id="profileButtons" class="profile-buttons"></div>
        </div>
        <div id="profilePostsGrid" class="profile-posts-grid"></div>
    </div>

    <!-- Edit Profile Modal -->
    <div id="editProfileModal" class="edit-profile-modal">
        <div class="edit-profile-content">
            <h3 style="font-size:24px;font-weight:800;margin-bottom:24px;text-align:center;">تعديل الملف الشخصي</h3>
            <input type="text" id="editName" placeholder="الاسم">
            <textarea id="editBio" placeholder="السيرة الذاتية..."></textarea>
            <div style="display:flex;gap:12px;margin-top:24px;">
                <button class="btn-secondary" onclick="closeEditProfileModal()" style="flex:1;padding:12px;border-radius:40px;font-weight:600;cursor:pointer;">إلغاء</button>
                <button class="btn-primary" onclick="saveProfileEdit()" style="flex:1;padding:12px;border-radius:40px;font-weight:600;cursor:pointer;">حفظ التغييرات</button>
            </div>
        </div>
    </div>

    <!-- Chat Panel -->
    <div id="chatPanel" class="panel">
        <div class="panel-header">
            <div style="display:flex;align-items:center;gap:12px;">
                <div class="avatar-sm" id="chatAvatar">👤</div>
                <h3 id="chatUserName">محادثة</h3>
            </div>
            <button onclick="closeChat()" style="font-size:28px;background:none;border:none;color:var(--text-secondary);cursor:pointer;">&times;</button>
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
        <div class="panel-header"><h3 style="font-weight:700;">الرسائل</h3><button onclick="closeConversations()" style="font-size:28px;background:none;border:none;color:var(--text-secondary);cursor:pointer;">&times;</button></div>
        <div id="conversationsList" class="panel-body"></div>
    </div>

    <!-- Followers Panel -->
    <div id="followersPanel" class="panel">
        <div class="panel-header"><h3 id="followersTitle" style="font-weight:700;">المتابعون</h3><button onclick="closeFollowers()" style="font-size:28px;background:none;border:none;color:var(--text-secondary);cursor:pointer;">&times;</button></div>
        <div id="followersList" class="panel-body"></div>
    </div>

    <!-- Notifications Panel -->
    <div id="notificationsPanel" class="panel">
        <div class="panel-header"><h3 style="font-weight:700;">الإشعارات</h3><button onclick="closeNotifications()" style="font-size:28px;background:none;border:none;color:var(--text-secondary);cursor:pointer;">&times;</button></div>
        <div id="notificationsList" class="panel-body"></div>
    </div>

    <!-- Search Panel -->
    <div id="searchPanel" class="panel">
        <div class="panel-header"><h3 style="font-weight:700;">بحث</h3><button onclick="closeSearch()" style="font-size:28px;background:none;border:none;color:var(--text-secondary);cursor:pointer;">&times;</button></div>
        <input type="text" id="searchInput" class="search-input" placeholder="بحث عن مستخدمين..." onkeyup="searchAll()">
        <div id="searchResults" class="panel-body"></div>
    </div>

    <!-- Admin Panel -->
    <div id="adminPanel" class="panel">
        <div class="panel-header"><h3 style="font-weight:700;font-size:20px;">🔧 لوحة التحكم</h3><button onclick="closeAdmin()" style="font-size:28px;background:none;border:none;color:var(--text-secondary);cursor:pointer;">&times;</button></div>
        <div id="adminStats" class="admin-stats"></div>
        <div class="admin-section">
            <div class="admin-section-title"><i class="fas fa-users" style="color:var(--primary);"></i> إدارة المستخدمين</div>
            <div id="adminUsersList"></div>
        </div>
        <div class="admin-section">
            <div class="admin-section-title"><i class="fas fa-file-alt" style="color:var(--primary);"></i> إدارة المنشورات</div>
            <div id="adminPostsList"></div>
        </div>
    </div>
</div>

<script src="firebase-config.js"></script>
<script src="script.js"></script>
<script>
    window.openImageModal=function(u){document.getElementById('modalImage').src=u;document.getElementById('imageModal').classList.add('open')};
    window.closeImageModal=function(){document.getElementById('imageModal').classList.remove('open')};
    window.toggleTheme=function(){document.body.classList.toggle('light-mode');localStorage.setItem('theme',document.body.classList.contains('light-mode')?'light':'dark')};
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 4. script.js - Sotwe Full Logic
# ═══════════════════════════════════════════════════════════

def build_script():
    return r"""// 🟦 SOTWE 2026 - Main Script (Compat Version)
let currentUser=null,currentUserData=null,allUsers={},allPosts=[],selectedMediaFile=null,currentChatUserId=null,viewingProfileUserId=null,currentPostForComments=null,mediaRecorder=null,audioChunks=[],bookmarks={},isAdmin=false;

async function loadUserData(){const snap=await db.ref('users/'+currentUser.uid).once('value');if(snap.exists())currentUserData={uid:currentUser.uid,...snap.val()};if(currentUserData?.bookmarks)bookmarks=currentUserData.bookmarks}
db.ref('users').on('value',s=>{allUsers=s.val()||{}});
db.ref('posts').on('value',s=>{const data=s.val();if(!data){allPosts=[];renderFeed();return}allPosts=[];Object.keys(data).forEach(k=>allPosts.push({id:k,...data[k]}));allPosts.sort((a,b)=>(b.timestamp||0)-(a.timestamp||0));renderFeed()});

async function uploadMedia(file){const fd=new FormData();fd.append('file',file);fd.append('upload_preset',UPLOAD_PRESET);let rt='image';if(file.type.startsWith('video/'))rt='video';else if(file.type.startsWith('audio/'))rt='raw';const res=await fetch('https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/'+rt+'/upload',{method:'POST',body:fd});const data=await res.json();return{url:data.secure_url,type:rt==='raw'?'audio':rt}}

function escapeHtml(text){if(!text)return '';const div=document.createElement('div');div.textContent=text;return div.innerHTML}

function renderFeed(){const c=document.getElementById('feedContainer');if(!c)return;c.innerHTML='';if(!allPosts.length){c.innerHTML='<div class="loading"><div class="spinner"></div><span>لا توجد منشورات بعد</span></div>';return}
allPosts.forEach(post=>{const user=allUsers[post.sender]||{name:post.senderName||'مستخدم',avatarUrl:''};const isLiked=post.likedBy&&post.likedBy[currentUser?.uid];const isRetweeted=post.retweetedBy&&post.retweetedBy[currentUser?.uid];const isBookmarked=bookmarks[post.id];const cc=post.comments?Object.keys(post.comments).length:0;const rc=post.retweets?Object.keys(post.retweets).length:0;
let mh='';if(post.mediaUrl){if(post.mediaType==='image')mh='<div class="tweet-media" onclick="event.stopPropagation();openImageModal(\''+post.mediaUrl+'\')"><img src="'+post.mediaUrl+'" loading="lazy"></div>';else if(post.mediaType==='video')mh='<div class="tweet-media" onclick="event.stopPropagation()"><video controls src="'+post.mediaUrl+'"></video></div>';else mh='<div class="tweet-media" onclick="event.stopPropagation()"><audio controls src="'+post.mediaUrl+'"></audio></div>'}
let qh='';if(post.quotePostId&&post.quotePostData){const qu=allUsers[post.quotePostData.sender]||{name:'مستخدم',avatarUrl:''};qh='<div class="quote-embed" onclick="event.stopPropagation();openCommentsModal(\''+post.quotePostId+'\')"><div style="display:flex;gap:8px;align-items:center;margin-bottom:6px;"><div class="comment-avatar">'+(qu.avatarUrl?'<img src="'+qu.avatarUrl+'">':(qu.name?.charAt(0)||'U'))+'</div><span style="font-weight:600;font-size:13px;">'+escapeHtml(qu.name)+'</span></div><div style="font-size:13px;">'+escapeHtml(post.quotePostData.text?.substring(0,100)||'')+'</div></div>'}
const div=document.createElement('div');div.className='tweet-card';div.onclick=()=>openCommentsModal(post.id);div.innerHTML='<div class="tweet-header"><div class="tweet-avatar" onclick="event.stopPropagation();viewProfile(\''+post.sender+'\')">'+(user.avatarUrl?'<img src="'+user.avatarUrl+'">':(user.name?.charAt(0)||'👤'))+'</div><div style="flex:1"><div><span class="tweet-name" onclick="event.stopPropagation();viewProfile(\''+post.sender+'\')">'+escapeHtml(user.name)+'</span><span class="tweet-username mx-1">@'+user.name?.toLowerCase().replace(/\s/g,'')+'</span><span class="tweet-time">· '+new Date(post.timestamp).toLocaleString()+'</span></div><div class="tweet-content">'+escapeHtml(post.text||'')+'</div>'+mh+qh+'</div></div><div class="tweet-actions" onclick="event.stopPropagation()"><button class="tweet-action" onclick="openCommentsModal(\''+post.id+'\')"><i class="far fa-comment"></i> <span>'+cc+'</span></button><button class="tweet-action '+(isRetweeted?'active':'')+'" onclick="toggleRetweet(\''+post.id+'\',this)"><i class="fas fa-retweet"></i> <span>'+rc+'</span></button><button class="tweet-action '+(isLiked?'active':'')+'" onclick="toggleLike(\''+post.id+'\',this)"><i class="fas fa-heart"></i> <span>'+(post.likes||0)+'</span></button><button class="tweet-action '+(isBookmarked?'active':'')+'" onclick="toggleBookmark(\''+post.id+'\',this)"><i class="fas fa-bookmark"></i></button><button class="tweet-action" onclick="openQuoteModal(\''+post.id+'\')"><i class="fas fa-quote-right"></i></button></div>';c.appendChild(div)})}

window.openCompose=function(){document.getElementById('composePanel').classList.add('open');document.getElementById('backBtn').style.display='flex';resetCompose()}
window.closeCompose=function(){document.getElementById('composePanel').classList.remove('open');if(!document.querySelector('.panel.open'))document.getElementById('backBtn').style.display='none'}
function resetCompose(){document.getElementById('postText').value='';document.getElementById('mediaPreview').innerHTML='';document.getElementById('mediaPreview').style.display='none';selectedMediaFile=null;document.getElementById('postImage').value='';document.getElementById('postVideo').value='';document.getElementById('postStatus').innerHTML=''}
window.previewMedia=function(input,type){const file=input.files[0];if(!file)return;selectedMediaFile=file;const reader=new FileReader();reader.onload=function(e){const mp=document.getElementById('mediaPreview');if(type==='image')mp.innerHTML='<img src="'+e.target.result+'">';else mp.innerHTML='<video controls><source src="'+e.target.result+'"></video>';mp.style.display='block'};reader.readAsDataURL(file)}
window.startAudioRecording=async function(){const btn=document.getElementById('audioRecordBtn');if(mediaRecorder&&mediaRecorder.state==='recording'){mediaRecorder.stop();btn.innerHTML='<i class="fas fa-microphone"></i>';return}try{const stream=await navigator.mediaDevices.getUserMedia({audio:true});mediaRecorder=new MediaRecorder(stream);audioChunks=[];mediaRecorder.ondataavailable=e=>audioChunks.push(e.data);mediaRecorder.onstop=async()=>{const blob=new Blob(audioChunks,{type:'audio/mp3'});selectedMediaFile=new File([blob],'recording.mp3',{type:'audio/mp3'});const url=URL.createObjectURL(blob);document.getElementById('mediaPreview').innerHTML='<audio controls src="'+url+'"></audio>';document.getElementById('mediaPreview').style.display='block';stream.getTracks().forEach(t=>t.stop())};mediaRecorder.start();btn.innerHTML='<i class="fas fa-stop-circle" style="color:#f91880"></i>'}catch(err){showToast('لا يمكن الوصول إلى الميكروفون')}}
window.createPost=async function(){const text=document.getElementById('postText')?.value||'';if(!text.trim()&&!selectedMediaFile){showToast('اكتب شيئاً أو اختر وسائط');return}document.getElementById('postStatus').innerHTML='📤 جاري النشر...';let mediaUrl='',mediaType='none';if(selectedMediaFile){try{const result=await uploadMedia(selectedMediaFile);mediaUrl=result.url;mediaType=result.type}catch(e){document.getElementById('postStatus').innerHTML='❌ فشل رفع الوسائط';return}}try{await db.ref('posts').push({text,mediaUrl,mediaType,sender:currentUser.uid,senderName:currentUserData?.name,likes:0,likedBy:{},retweets:{},retweetedBy:{},comments:{},timestamp:Date.now()});document.getElementById('postStatus').innerHTML='✅ تم النشر!';setTimeout(()=>closeCompose(),1500)}catch(e){document.getElementById('postStatus').innerHTML='❌ فشل النشر'}}

window.toggleLike=async function(postId,btn){if(!currentUser)return;const ref=db.ref('posts/'+postId);const snap=await ref.once('value');const post=snap.val();if(!post)return;let likes=post.likes||0;let likedBy=post.likedBy||{};if(likedBy[currentUser.uid]){likes--;delete likedBy[currentUser.uid];showToast('تم إلغاء الإعجاب')}else{likes++;likedBy[currentUser.uid]=true;addNotification(post.sender,'like',postId);showToast('❤️ أعجبتك');if(btn){const icon=btn.querySelector('i');if(icon)icon.classList.add('heart-animation');setTimeout(()=>icon?.classList.remove('heart-animation'),300)}}await ref.update({likes,likedBy});if(btn){btn.classList.toggle('active');const span=btn.querySelector('span');if(span)span.innerText=likes}}
window.toggleRetweet=async function(postId,btn){if(!currentUser)return;const ref=db.ref('posts/'+postId);const snap=await ref.once('value');const post=snap.val();if(!post)return;let retweets=post.retweets||{};let retweetedBy=post.retweetedBy||{};let rc=Object.keys(retweets).length;if(retweetedBy[currentUser.uid]){const k=Object.keys(retweets).find(k=>retweets[k].userId===currentUser.uid);if(k)delete retweets[k];delete retweetedBy[currentUser.uid];rc--;showToast('تم إلغاء إعادة التغريد')}else{retweets[Date.now().toString()]={userId:currentUser.uid,timestamp:Date.now()};retweetedBy[currentUser.uid]=true;rc++;addNotification(post.sender,'retweet',postId);showToast('🔁 تم إعادة التغريد')}await ref.update({retweets,retweetedBy});if(btn){btn.classList.toggle('active');const span=btn.querySelector('span');if(span)span.innerText=rc}}
window.toggleBookmark=async function(postId,btn){if(!currentUser)return;const ref=db.ref('users/'+currentUser.uid+'/bookmarks/'+postId);const snap=await ref.once('value');if(snap.exists()){await ref.set(null);delete bookmarks[postId];showToast('تمت إزالة من الإشارات المرجعية')}else{await ref.set(true);bookmarks[postId]=true;showToast('📌 تمت إضافة إلى الإشارات المرجعية')}if(btn)btn.classList.toggle('active')}
window.openQuoteModal=function(postId){const text=prompt('أضف تعليقك على هذا المنشور:');if(text)createQuotePost(postId,text)}
async function createQuotePost(opid,text){const op=allPosts.find(p=>p.id===opid);if(!op)return;await db.ref('posts').push({text,mediaUrl:'',mediaType:'none',sender:currentUser.uid,senderName:currentUserData?.name,quotePostId:opid,quotePostData:{text:op.text,sender:op.sender,senderName:op.senderName,mediaUrl:op.mediaUrl,mediaType:op.mediaType},likes:0,likedBy:{},retweets:{},retweetedBy:{},comments:{},timestamp:Date.now()});addNotification(op.sender,'quote',opid);showToast('✅ تم نشر الاقتباس')}

window.openCommentsModal=async function(postId){currentPostForComments=postId;const post=allPosts.find(p=>p.id===postId);if(!post)return;const c=document.getElementById('commentsList');const comments=post.comments||{};c.innerHTML='';const sorted=Object.entries(comments).sort((a,b)=>b[1].timestamp-a[1].timestamp);for(const[ck,comment]of sorted){const user=allUsers[comment.userId]||{name:comment.username||'مستخدم',avatarUrl:''};const replies=comment.replies||{};const cd=document.createElement('div');cd.className='comment-item';cd.innerHTML='<div class="comment-header"><div class="comment-avatar" onclick="viewProfile(\''+comment.userId+'\')">'+(user.avatarUrl?'<img src="'+user.avatarUrl+'">':(user.name?.charAt(0)||'U'))+'</div><div style="flex:1"><div><span class="comment-user" onclick="viewProfile(\''+comment.userId+'\')">'+escapeHtml(user.name)+'</span><span class="comment-time mx-2">· '+new Date(comment.timestamp).toLocaleString()+'</span></div><div class="comment-text">'+escapeHtml(comment.text)+'</div></div></div><div class="reply-list" id="replies-'+ck+'"></div><div><button style="color:#1d9bf0;font-size:14px;margin-top:8px;" onclick="showReplyInput(\''+ck+'\')"><i class="fas fa-reply"></i> رد</button></div><div id="reply-input-'+ck+'" style="margin-top:8px;"></div>';const rc=cd.querySelector('#replies-'+ck);if(rc&&replies){const sr=Object.entries(replies).sort((a,b)=>a[1].timestamp-b[1].timestamp);for(const[rk,reply]of sr){const ru=allUsers[reply.userId]||{name:reply.username||'مستخدم',avatarUrl:''};rc.innerHTML+='<div class="reply-item"><div class="reply-header"><div class="reply-avatar" onclick="viewProfile(\''+reply.userId+'\')">'+(ru.avatarUrl?'<img src="'+ru.avatarUrl+'">':(ru.name?.charAt(0)||'U'))+'</div><div class="reply-user" onclick="viewProfile(\''+reply.userId+'\')">'+escapeHtml(ru.name)+'</div><div class="comment-time">'+new Date(reply.timestamp).toLocaleTimeString()+'</div></div><div class="reply-text">'+escapeHtml(reply.text)+'</div></div>'}}c.appendChild(cd)}if(c.innerHTML==='')c.innerHTML='<div style="text-align:center;color:#71767b;padding:40px;">لا توجد تعليقات بعد</div>';document.getElementById('commentsPanel').classList.add('open');document.getElementById('backBtn').style.display='flex'}
window.closeComments=function(){document.getElementById('commentsPanel').classList.remove('open');if(!document.querySelector('.panel.open'))document.getElementById('backBtn').style.display='none'}
window.showReplyInput=function(commentId){const d=document.getElementById('reply-input-'+commentId);if(!d)return;if(d.innerHTML){d.innerHTML='';return}d.innerHTML='<div style="display:flex;gap:8px;"><input type="text" id="reply-text-'+commentId+'" style="flex:1;background:#1a1a2a;border:1px solid #2f3336;border-radius:40px;padding:8px 12px;color:#fff;font-size:13px;outline:none;" placeholder="اكتب رداً..." onkeypress="if(event.key===\'Enter\')addReply(\''+commentId+'\')"><button onclick="addReply(\''+commentId+'\')" style="background:#1d9bf0;color:#fff;border:none;padding:8px 16px;border-radius:40px;font-size:13px;cursor:pointer;">نشر</button></div>'}
window.addReply=async function(commentId){const input=document.getElementById('reply-text-'+commentId);const text=input?.value;if(!text?.trim())return;await db.ref('posts/'+currentPostForComments+'/comments/'+commentId+'/replies').push({userId:currentUser.uid,username:currentUserData?.name,text,timestamp:Date.now()});if(input)input.value='';openCommentsModal(currentPostForComments)}
window.addComment=async function(){const input=document.getElementById('commentInput');const text=input?.value;if(!text?.trim()||!currentPostForComments)return;await db.ref('posts/'+currentPostForComments+'/comments').push({userId:currentUser.uid,username:currentUserData?.name,text,replies:{},timestamp:Date.now()});if(input)input.value='';openCommentsModal(currentPostForComments);const post=allPosts.find(p=>p.id===currentPostForComments);if(post)addNotification(post.sender,'comment',currentPostForComments)}

async function addNotification(targetUserId,type,postId=null){if(targetUserId===currentUser.uid)return;const messages={like:'❤️ أعجب بمنشورك',comment:'💬 علق على منشورك',retweet:'🔁 أعاد تغريد منشورك',quote:'📝 اقتبس منشورك',follow:'👥 بدأ بمتابعتك'};await db.ref('notifications/'+targetUserId).push({type,fromUserId:currentUser.uid,fromUsername:currentUserData?.name,message:messages[type],postId:postId,timestamp:Date.now(),read:false});updateNotificationBadge()}
function updateNotificationBadge(){if(!currentUser?.uid)return;db.ref('notifications/'+currentUser.uid).on('value',snap=>{const notifs=snap.val()||{};const unread=Object.values(notifs).filter(n=>!n.read).length;const badge=document.getElementById('notifBadge');if(badge){if(unread>0){badge.style.display='flex';badge.innerText=unread>9?'9+':unread}else badge.style.display='none'}})}
window.openNotifications=async function(){const panel=document.getElementById('notificationsPanel');const snap=await db.ref('notifications/'+currentUser.uid).once('value');const notifs=snap.val()||{};const c=document.getElementById('notificationsList');c.innerHTML='';const sorted=Object.entries(notifs).sort((a,b)=>b[1].timestamp-a[1].timestamp);for(const[key,n]of sorted){const icons={like:'❤️',comment:'💬',retweet:'🔁',quote:'📝',follow:'👥'};const bg=n.read?'':'background:rgba(29,155,240,0.1);border-right:4px solid #1d9bf0;';c.innerHTML+='<div class="notification-item" style="'+bg+'" onclick="handleNotificationClick(\''+n.type+'\',\''+n.fromUserId+'\',\''+(n.postId||'')+'\')"><div style="font-size:24px;">'+(icons[n.type]||'🔔')+'</div><div style="flex:1"><div style="font-weight:700;">'+escapeHtml(n.fromUsername)+'</div><div style="font-size:14px;color:#71767b;">'+n.message+'</div><div style="font-size:12px;color:#71767b;margin-top:4px;">'+new Date(n.timestamp).toLocaleString()+'</div></div></div>';if(!n.read)await db.ref('notifications/'+currentUser.uid+'/'+key).update({read:true})}if(c.innerHTML==='')c.innerHTML='<div style="text-align:center;color:#71767b;padding:40px;">لا توجد إشعارات</div>';panel.classList.add('open');document.getElementById('backBtn').style.display='flex'}
window.handleNotificationClick=function(type,userId,postId){closeNotifications();if(type==='follow')viewProfile(userId);else if(postId)openCommentsModal(postId)}
window.closeNotifications=function(){document.getElementById('notificationsPanel').classList.remove('open');if(!document.querySelector('.panel.open'))document.getElementById('backBtn').style.display='none'}

function showToast(msg){let t=document.getElementById('customToast');if(!t){t=document.createElement('div');t.id='customToast';document.body.appendChild(t)}t.innerText=msg;t.style.opacity='1';setTimeout(()=>{t.style.opacity='0'},3000)}

window.openMyProfile=function(){viewProfile(currentUser.uid)}
window.viewProfile=async function(userId){if(!userId)return;viewingProfileUserId=userId;await loadProfileData(userId);document.getElementById('profilePanel').classList.add('open');document.getElementById('backBtn').style.display='flex'}
window.closeProfile=function(){document.getElementById('profilePanel').classList.remove('open');if(!document.querySelector('.panel.open'))document.getElementById('backBtn').style.display='none'}
async function loadProfileData(userId){const snap=await db.ref('users/'+userId).once('value');const user=snap.val();if(!user)return;const cover=document.getElementById('profileCover');if(user.coverUrl)cover.style.background='url('+user.coverUrl+') center/cover';else cover.style.background='linear-gradient(135deg,#1d9bf0,#f91880)';document.getElementById('profileAvatar').innerHTML=user.avatarUrl?'<img src="'+user.avatarUrl+'">':(user.name?.charAt(0)||'👤');document.getElementById('profileName').innerText=user.name;document.getElementById('profileBio').innerText=user.bio||'✏️ أضف سيرة ذاتية';const ups=allPosts.filter(p=>p.sender===userId);document.getElementById('profilePostsCount').innerText=ups.length;document.getElementById('profileFollowersCount').innerText=Object.keys(user.followers||{}).length;document.getElementById('profileFollowingCount').innerText=Object.keys(user.following||{}).length;const grid=document.getElementById('profilePostsGrid');grid.innerHTML=ups.map(p=>'<div class="profile-post" onclick="openCommentsModal(\''+p.id+'\')">'+(p.mediaUrl?(p.mediaType==='image'?'<img src="'+p.mediaUrl+'" loading="lazy">':p.mediaType==='video'?'<video src="'+p.mediaUrl+'"></video>':'<i class="fas fa-music" style="font-size:24px;"></i>'):'<i class="fas fa-file-alt" style="font-size:24px;"></i>')+'</div>').join('');if(!ups.length)grid.innerHTML='<div style="grid-column:1/-1;text-align:center;color:#71767b;padding:40px;">لا توجد منشورات</div>';const bd=document.getElementById('profileButtons');bd.innerHTML='';if(userId===currentUser.uid){bd.innerHTML='<button class="profile-btn btn-primary" onclick="openEditProfileModal()">✏️ تعديل الملف</button><button class="profile-btn btn-secondary" onclick="logout()">🚪 تسجيل خروج</button>'+(isAdmin?'<button class="profile-btn btn-secondary" onclick="openAdmin()">🔧 لوحة التحكم</button>':'')}else{const isF=currentUserData?.following&&currentUserData.following[userId];bd.innerHTML='<button class="profile-btn btn-primary" onclick="toggleFollow(\''+userId+'\',this)">'+(isF?'✅ متابع':'➕ متابعة')+'</button><button class="profile-btn btn-secondary" onclick="openPrivateChat(\''+userId+'\')"><i class="fas fa-envelope"></i> مراسلة</button>'}}

window.openEditProfileModal=function(){document.getElementById('editName').value=currentUserData?.name||'';document.getElementById('editBio').value=currentUserData?.bio||'';document.getElementById('editProfileModal').classList.add('open')}
window.closeEditProfileModal=function(){document.getElementById('editProfileModal').classList.remove('open')}
window.saveProfileEdit=async function(){const name=document.getElementById('editName').value;const bio=document.getElementById('editBio').value;if(!name.trim()){showToast('الاسم مطلوب');return}await db.ref('users/'+currentUser.uid).update({name:name.trim(),bio});showToast('✅ تم تحديث الملف الشخصي');closeEditProfileModal();setTimeout(()=>location.reload(),1000)}

window.changeAvatar=function(){document.getElementById('avatarInput')?.click()}
window.changeCover=function(){document.getElementById('coverInput')?.click()}
(function(){if(!document.getElementById('avatarInput')){const inp=document.createElement('input');inp.type='file';inp.accept='image/*';inp.id='avatarInput';inp.style.display='none';document.body.appendChild(inp);inp.addEventListener('change',async e=>{const file=e.target.files[0];if(!file)return;showToast('📤 جاري رفع الصورة...');const result=await uploadMedia(file);await db.ref('users/'+currentUser.uid).update({avatarUrl:result.url});showToast('✅ تم تحديث الصورة الشخصية');location.reload()})}if(!document.getElementById('coverInput')){const inp=document.createElement('input');inp.type='file';inp.accept='image/*';inp.id='coverInput';inp.style.display='none';document.body.appendChild(inp);inp.addEventListener('change',async e=>{const file=e.target.files[0];if(!file)return;showToast('📤 جاري رفع الصورة...');const result=await uploadMedia(file);await db.ref('users/'+currentUser.uid).update({coverUrl:result.url});showToast('✅ تم تحديث صورة الغلاف');location.reload()})}})()

window.toggleFollow=async function(userId,btn){if(!currentUser||currentUser.uid===userId)return;const ref=db.ref('users/'+currentUser.uid+'/following/'+userId);const tref=db.ref('users/'+userId+'/followers/'+currentUser.uid);const snap=await ref.once('value');if(snap.exists()){await ref.set(null);await tref.set(null);if(btn)btn.innerText='➕ متابعة';showToast('👋 توقفت عن متابعة '+(allUsers[userId]?.name||''))}else{await ref.set(true);await tref.set(true);if(btn)btn.innerText='✅ متابع';addNotification(userId,'follow');showToast('👥 بدأت بمتابعة '+(allUsers[userId]?.name||''))}if(viewingProfileUserId===userId)await loadProfileData(userId)}
window.openFollowersList=async function(type){document.getElementById('followersTitle').innerText=type==='followers'?'المتابعون':'المتابَعون';const c=document.getElementById('followersList');const user=viewingProfileUserId?allUsers[viewingProfileUserId]:currentUserData;const list=type==='followers'?user?.followers:user?.following;c.innerHTML='';if(list){for(const[uid]of Object.entries(list)){const u=allUsers[uid];if(u)c.innerHTML+='<div class="follower-item" onclick="viewProfile(\''+uid+'\')"><div class="avatar-xs">'+(u.avatarUrl?'<img src="'+u.avatarUrl+'">':(u.name?.charAt(0)||'U'))+'</div><div><div style="font-weight:700;">'+escapeHtml(u.name)+'</div><div style="font-size:13px;color:#71767b;">@'+u.name?.toLowerCase().replace(/\s/g,'')+'</div></div></div>'}}if(c.innerHTML==='')c.innerHTML='<div style="text-align:center;color:#71767b;padding:40px;">لا يوجد مستخدمين</div>';document.getElementById('followersPanel').classList.add('open');document.getElementById('backBtn').style.display='flex'}
window.closeFollowers=function(){document.getElementById('followersPanel').classList.remove('open');if(!document.querySelector('.panel.open'))document.getElementById('backBtn').style.display='none'}

function getChatId(u1,u2){return u1<u2?u1+'_'+u2:u2+'_'+u1}
window.openConversations=async function(){const panel=document.getElementById('conversationsPanel');const c=document.getElementById('conversationsList');const snap=await db.ref('private_chats/'+currentUser.uid).once('value');const convs=snap.val()||{};c.innerHTML='';for(const[oid,cd]of Object.entries(convs)){const u=allUsers[oid];if(u)c.innerHTML+='<div class="conversation-item" onclick="openPrivateChat(\''+oid+'\')"><div class="avatar-sm">'+(u.avatarUrl?'<img src="'+u.avatarUrl+'">':(u.name?.charAt(0)||'U'))+'</div><div><div style="font-weight:700;">'+escapeHtml(u.name)+'</div><div style="font-size:13px;color:#71767b;">'+(cd.lastMessage?.substring(0,40)||'رسالة')+'</div></div></div>'}if(c.innerHTML==='')c.innerHTML='<div style="text-align:center;color:#71767b;padding:40px;">لا توجد محادثات بعد</div>';panel.classList.add('open');document.getElementById('backBtn').style.display='flex'}
window.closeConversations=function(){document.getElementById('conversationsPanel').classList.remove('open');if(!document.querySelector('.panel.open'))document.getElementById('backBtn').style.display='none'}
window.openPrivateChat=async function(oid){currentChatUserId=oid;const u=allUsers[oid];document.getElementById('chatUserName').innerText=u?.name||'مستخدم';document.getElementById('chatAvatar').innerHTML=u?.avatarUrl?'<img src="'+u.avatarUrl+'">':(u?.name?.charAt(0)||'U');await loadPrivateMessages(oid);document.getElementById('chatPanel').classList.add('open');document.getElementById('backBtn').style.display='flex';closeConversations()}
window.closeChat=function(){document.getElementById('chatPanel').classList.remove('open');if(!document.querySelector('.panel.open'))document.getElementById('backBtn').style.display='none';currentChatUserId=null}
async function loadPrivateMessages(oid){const c=document.getElementById('chatMessages');c.innerHTML='<div style="text-align:center;color:#71767b;padding:40px;">جاري التحميل...</div>';const chatId=getChatId(currentUser.uid,oid);const snap=await db.ref('private_messages/'+chatId).once('value');const msgs=snap.val()||{};c.innerHTML='';const sorted=Object.entries(msgs).sort((a,b)=>a[1].timestamp-b[1].timestamp);for(const[id,msg]of sorted){const sent=msg.senderId===currentUser.uid;const time=new Date(msg.timestamp).toLocaleTimeString();let content='';if(msg.type==='text')content='<div class="message-bubble '+(sent?'sent':'received')+'">'+escapeHtml(msg.text)+'</div>';else if(msg.type==='image')content='<img src="'+msg.imageUrl+'" class="message-image" onclick="openImageModal(\''+msg.imageUrl+'\')">';else if(msg.type==='audio')content='<div class="message-audio"><audio controls src="'+msg.audioUrl+'"></audio></div>';c.innerHTML+='<div class="chat-message '+(sent?'sent':'received')+'"><div>'+content+'<div style="font-size:10px;opacity:0.5;margin-top:4px;">'+time+'</div></div></div>'}if(c.innerHTML==='')c.innerHTML='<div style="text-align:center;color:#71767b;padding:40px;">لا توجد رسائل بعد</div>';c.scrollTop=c.scrollHeight}
window.sendChatMessage=async function(){const input=document.getElementById('chatMessageInput');const text=input?.value.trim();if(!text||!currentChatUserId)return;const chatId=getChatId(currentUser.uid,currentChatUserId);await db.ref('private_messages/'+chatId).push({senderId:currentUser.uid,senderName:currentUserData?.name,text,type:'text',timestamp:Date.now()});await db.ref('private_chats/'+currentUser.uid+'/'+currentChatUserId).set({lastMessage:text,lastTimestamp:Date.now(),withUser:currentChatUserId});await db.ref('private_chats/'+currentChatUserId+'/'+currentUser.uid).set({lastMessage:text,lastTimestamp:Date.now(),withUser:currentUser.uid});input.value='';await loadPrivateMessages(currentChatUserId)}
window.sendChatImage=async function(input){const file=input.files[0];if(!file||!currentChatUserId)return;const result=await uploadMedia(file);const chatId=getChatId(currentUser.uid,currentChatUserId);await db.ref('private_messages/'+chatId).push({senderId:currentUser.uid,senderName:currentUserData?.name,imageUrl:result.url,type:'image',timestamp:Date.now()});await db.ref('private_chats/'+currentUser.uid+'/'+currentChatUserId).set({lastMessage:'📷 صورة',lastTimestamp:Date.now(),withUser:currentChatUserId});await db.ref('private_chats/'+currentChatUserId+'/'+currentUser.uid).set({lastMessage:'📷 صورة',lastTimestamp:Date.now(),withUser:currentUser.uid});input.value='';await loadPrivateMessages(currentChatUserId)}
window.startRecordingChat=async function(){const btn=document.getElementById('chatRecordBtn');if(mediaRecorder&&mediaRecorder.state==='recording'){mediaRecorder.stop();btn.innerHTML='<i class="fas fa-microphone"></i>';return}try{const stream=await navigator.mediaDevices.getUserMedia({audio:true});mediaRecorder=new MediaRecorder(stream);audioChunks=[];mediaRecorder.ondataavailable=e=>audioChunks.push(e.data);mediaRecorder.onstop=async()=>{const blob=new Blob(audioChunks,{type:'audio/mp3'});const file=new File([blob],'recording.mp3',{type:'audio/mp3'});const result=await uploadMedia(file);if(currentChatUserId){const chatId=getChatId(currentUser.uid,currentChatUserId);await db.ref('private_messages/'+chatId).push({senderId:currentUser.uid,senderName:currentUserData?.name,audioUrl:result.url,type:'audio',timestamp:Date.now()});await db.ref('private_chats/'+currentUser.uid+'/'+currentChatUserId).set({lastMessage:'🎤 رسالة صوتية',lastTimestamp:Date.now(),withUser:currentChatUserId});await db.ref('private_chats/'+currentChatUserId+'/'+currentUser.uid).set({lastMessage:'🎤 رسالة صوتية',lastTimestamp:Date.now(),withUser:currentUser.uid});await loadPrivateMessages(currentChatUserId)}stream.getTracks().forEach(t=>t.stop())};mediaRecorder.start();btn.innerHTML='<i class="fas fa-stop-circle" style="color:#f91880"></i>'}catch(err){showToast('لا يمكن الوصول إلى الميكروفون')}}

window.openSearch=function(){document.getElementById('searchPanel').classList.add('open');document.getElementById('backBtn').style.display='flex'}
window.closeSearch=function(){document.getElementById('searchPanel').classList.remove('open');if(!document.querySelector('.panel.open'))document.getElementById('backBtn').style.display='none'}
window.searchAll=function(){const q=document.getElementById('searchInput').value.toLowerCase();const r=document.getElementById('searchResults');if(!q){r.innerHTML='';return}const users=Object.values(allUsers).filter(u=>u.name?.toLowerCase().includes(q));r.innerHTML=users.map(u=>'<div class="search-result" onclick="viewProfile(\''+u.uid+'\')"><div class="avatar-xs">'+(u.avatarUrl?'<img src="'+u.avatarUrl+'">':(u.name?.charAt(0)||'U'))+'</div><div><div style="font-weight:700;">'+escapeHtml(u.name)+'</div><div style="font-size:13px;color:#71767b;">@'+u.name?.toLowerCase().replace(/\s/g,'')+'</div></div></div>').join('');if(!users.length)r.innerHTML='<div style="text-align:center;color:#71767b;padding:40px;">لا توجد نتائج</div>'}

window.openAdmin=async function(){if(!isAdmin)return;const tu=Object.keys(allUsers).length;const tp=allPosts.length;const tl=allPosts.reduce((s,p)=>s+(p.likes||0),0);const tc=allPosts.reduce((s,p)=>s+(p.comments?Object.keys(p.comments).length:0),0);document.getElementById('adminStats').innerHTML='<div class="admin-stat"><div class="admin-stat-icon"><i class="fas fa-users"></i></div><div class="admin-stat-number">'+tu+'</div><div class="admin-stat-label">مستخدمين</div></div><div class="admin-stat"><div class="admin-stat-icon"><i class="fas fa-file-alt"></i></div><div class="admin-stat-number">'+tp+'</div><div class="admin-stat-label">منشورات</div></div><div class="admin-stat"><div class="admin-stat-icon" style="color:#f91880;"><i class="fas fa-heart"></i></div><div class="admin-stat-number">'+tl+'</div><div class="admin-stat-label">إعجابات</div></div><div class="admin-stat"><div class="admin-stat-icon" style="color:#1d9bf0;"><i class="fas fa-comment"></i></div><div class="admin-stat-number">'+tc+'</div><div class="admin-stat-label">تعليقات</div></div>';const ul=document.getElementById('adminUsersList');ul.innerHTML='';Object.entries(allUsers).forEach(([uid,u])=>{if(uid!==currentUser.uid)ul.innerHTML+='<div class="admin-item"><div><div class="admin-item-name">'+escapeHtml(u.name)+'</div><div class="admin-item-email">'+u.email+'</div></div><button class="admin-delete-btn" onclick="adminDeleteUser(\''+uid+'\')"><i class="fas fa-trash"></i> حذف</button></div>'});if(ul.innerHTML==='')ul.innerHTML='<div style="text-align:center;color:#71767b;padding:40px;">لا يوجد مستخدمين آخرين</div>';const pl=document.getElementById('adminPostsList');pl.innerHTML='';allPosts.slice(0,30).forEach(p=>{pl.innerHTML+='<div class="admin-item"><div><div class="admin-item-name">'+escapeHtml(p.senderName||'مستخدم')+'</div><div class="admin-item-text">'+(p.text?.substring(0,60)||'منشور بدون نص')+'</div><div class="admin-item-email">'+new Date(p.timestamp).toLocaleString()+'</div></div><button class="admin-delete-btn" onclick="adminDeletePost(\''+p.id+'\')"><i class="fas fa-trash"></i> حذف</button></div>'});document.getElementById('adminPanel').classList.add('open');document.getElementById('backBtn').style.display='flex'}
window.closeAdmin=function(){document.getElementById('adminPanel').classList.remove('open');if(!document.querySelector('.panel.open'))document.getElementById('backBtn').style.display='none'}
window.adminDeleteUser=async function(uid){if(!isAdmin||!confirm('⚠️ حذف هذا المستخدم وجميع منشوراته؟'))return;const posts=allPosts.filter(p=>p.sender===uid);for(const p of posts)await db.ref('posts/'+p.id).set(null);await db.ref('users/'+uid).set(null);showToast('✅ تم حذف المستخدم');location.reload()}
window.adminDeletePost=async function(pid){if(!isAdmin||!confirm('⚠️ حذف هذا المنشور؟'))return;await db.ref('posts/'+pid).set(null);showToast('✅ تم حذف المنشور');renderFeed()}

window.switchTab=function(tab){document.querySelectorAll('.nav-item').forEach(t=>t.classList.remove('active'));if(event&&event.target){const clicked=event.target.closest('.nav-item');if(clicked)clicked.classList.add('active')}if(tab==='home'){closeCompose();closeProfile();closeChat();closeConversations();closeNotifications();closeSearch();closeComments();closeFollowers();closeAdmin();closeEditProfileModal()}}
window.goToHome=function(){const hb=document.querySelector('.nav-item i.fa-home')?.closest('.nav-item');if(hb){document.querySelectorAll('.nav-item').forEach(t=>t.classList.remove('active'));hb.classList.add('active')}closeCompose();closeProfile();closeChat();closeConversations();closeNotifications();closeSearch();closeComments();closeFollowers();closeAdmin();closeEditProfileModal();document.getElementById('backBtn').style.display='none'}
window.goBack=function(){if(document.getElementById('commentsPanel')?.classList.contains('open'))closeComments();else if(document.getElementById('profilePanel')?.classList.contains('open'))closeProfile();else if(document.getElementById('chatPanel')?.classList.contains('open'))closeChat();else if(document.getElementById('conversationsPanel')?.classList.contains('open'))closeConversations();else if(document.getElementById('notificationsPanel')?.classList.contains('open'))closeNotifications();else if(document.getElementById('searchPanel')?.classList.contains('open'))closeSearch();else if(document.getElementById('followersPanel')?.classList.contains('open'))closeFollowers();else if(document.getElementById('adminPanel')?.classList.contains('open'))closeAdmin();else if(document.getElementById('composePanel')?.classList.contains('open'))closeCompose();else if(document.getElementById('editProfileModal')?.classList.contains('open'))closeEditProfileModal();else goToHome()}
window.logout=function(){auth.signOut();location.reload()}

auth.onAuthStateChanged(async user=>{if(user){currentUser=user;await loadUserData();isAdmin=ADMIN_EMAILS.includes(currentUser.email);document.getElementById('mainApp').style.display='block';updateNotificationBadge();if(localStorage.getItem('theme')==='light')document.body.classList.add('light-mode');showToast('👋 مرحباً '+(currentUserData?.name||'مستخدم'))}else{window.location.replace('auth.html')}})
console.log('🟦 Sotwe Platform Ready ✨')
"""

# ═══════════════════════════════════════════════════════════
# 5-9. الملفات المتبقية
# ═══════════════════════════════════════════════════════════

def build_upload():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟦 Sotwe | رفع منشور</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>:root{--primary:#1d9bf0;--bg:#000;--surface:#1a1a1a;--border:#2f3336;--text:#fff}*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;overflow-y:auto}.header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(0,0,0,0.95);backdrop-filter:blur(12px);z-index:10}.btn-back{background:rgba(29,155,240,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:var(--text);cursor:pointer;font-size:16px}.container{max-width:500px;margin:0 auto;padding:20px}textarea{width:100%;min-height:150px;background:transparent;border:none;color:var(--text);font-size:20px;resize:none;outline:none;font-family:inherit;padding:16px}.tools{display:flex;gap:16px;padding:12px 0;border-top:1px solid var(--border);border-bottom:1px solid var(--border)}.tool{background:none;border:none;color:var(--primary);font-size:20px;padding:10px;border-radius:50%;cursor:pointer}.preview{margin:16px 0;display:none}.preview img,.preview video{max-height:300px;border-radius:20px;width:100%;object-fit:cover}.btn-post{width:100%;background:var(--primary);color:#fff;border:none;padding:14px;border-radius:40px;font-weight:700;font-size:18px;cursor:pointer;margin-top:20px}</style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>🟦 رفع منشور</h2></div>
<div class="container"><textarea id="postText" placeholder="ماذا يحدث؟"></textarea><div id="mediaPreview" class="preview"></div><div class="tools"><button class="tool" onclick="document.getElementById('postImage').click()"><i class="fas fa-image"></i></button><button class="tool" onclick="document.getElementById('postVideo').click()"><i class="fas fa-video"></i></button></div><input type="file" id="postImage" accept="image/*" style="display:none" onchange="previewMedia(this,'image')"><input type="file" id="postVideo" accept="video/*" style="display:none" onchange="previewMedia(this,'video')"><button class="btn-post" onclick="createPost()">نشر</button><div id="status" style="text-align:center;margin-top:12px;font-size:14px;color:var(--primary)"></div></div>
<script src="firebase-config.js"></script>
<script>let currentUser=null,currentUserData=null,selectedMediaFile=null;auth.onAuthStateChanged(async u=>{if(!u)window.location.href='auth.html';currentUser=u;const snap=await db.ref('users/'+u.uid).once('value');if(snap.exists())currentUserData={uid:u.uid,...snap.val()}});window.previewMedia=function(input,type){const file=input.files[0];if(!file)return;selectedMediaFile=file;const reader=new FileReader();reader.onload=function(e){const preview=document.getElementById('mediaPreview');if(type==='image')preview.innerHTML='<img src="'+e.target.result+'">';else preview.innerHTML='<video controls><source src="'+e.target.result+'"></video>';preview.style.display='block'};reader.readAsDataURL(file)};async function uploadMedia(file){const fd=new FormData();fd.append('file',file);fd.append('upload_preset',UPLOAD_PRESET);let rt='image';if(file.type.startsWith('video/'))rt='video';const res=await fetch('https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/'+rt+'/upload',{method:'POST',body:fd});const data=await res.json();return{url:data.secure_url,type:rt}}window.createPost=async function(){const text=document.getElementById('postText').value;if(!text.trim()&&!selectedMediaFile){document.getElementById('status').innerText='اكتب شيئاً أو اختر وسائط';return}document.getElementById('status').innerText='جاري النشر...';let mediaUrl='',mediaType='none';if(selectedMediaFile){try{const result=await uploadMedia(selectedMediaFile);mediaUrl=result.url;mediaType=result.type}catch(e){document.getElementById('status').innerText='فشل رفع الوسائط';return}}try{await db.ref('posts').push({text,mediaUrl,mediaType,sender:currentUser.uid,senderName:currentUserData?.name,likes:0,likedBy:{},retweets:{},retweetedBy:{},comments:{},timestamp:Date.now()});document.getElementById('status').innerText='تم النشر!';setTimeout(()=>window.location.href='index.html',1500)}catch(e){document.getElementById('status').innerText='فشل النشر'}}</script>
</body>
</html>"""

def build_chat():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🟦 Sotwe | رسائل</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>:root{--primary:#1d9bf0;--bg:#000;--surface:#1a1a1a;--border:#2f3336;--text:#fff}*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);height:100vh;display:flex;flex-direction:column}.header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);background:rgba(0,0,0,0.95);backdrop-filter:blur(12px)}.btn-back{background:rgba(29,155,240,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:var(--text);cursor:pointer;font-size:16px}.conv-item{display:flex;align-items:center;gap:12px;padding:14px 16px;border-bottom:1px solid var(--border);cursor:pointer}.conv-item:hover{background:#080808}.avatar-sm{width:48px;height:48px;border-radius:50%;background:var(--primary);overflow:hidden;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:20px}.avatar-sm img{width:100%;height:100%;object-fit:cover}.msgs{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:12px}.bubble{max-width:85%;padding:10px 14px;border-radius:20px}.bubble.sent{background:var(--primary);color:#fff;align-self:flex-end}.bubble.received{background:var(--surface);align-self:flex-start}.input-bar{display:flex;gap:12px;padding:12px;border-top:1px solid var(--border);background:var(--bg);align-items:center}.input-bar input{flex:1;padding:12px 16px;border:1px solid var(--border);border-radius:40px;background:var(--surface);color:var(--text);outline:none}.input-bar button{background:none;border:none;color:var(--primary);font-size:20px;cursor:pointer;padding:8px}</style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>🟦 الرسائل</h2></div>
<div id="convList" style="flex:1;overflow-y:auto"></div>
<div id="msgsList" class="msgs" style="display:none"></div>
<div class="input-bar" id="chatInput" style="display:none"><input type="text" id="msgInput" placeholder="اكتب رسالة..."><button onclick="sendMsg()"><i class="fas fa-paper-plane"></i></button></div>
<script src="firebase-config.js"></script>
<script>let currentUser=null,allUsers={},chatUserId=null;function getChatId(u1,u2){return u1<u2?u1+'_'+u2:u2+'_'+u1}auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;db.ref('users').on('value',s=>{allUsers=s.val()||{}});loadConvs()});async function loadConvs(){const cl=document.getElementById('convList');cl.style.display='block';document.getElementById('msgsList').style.display='none';document.getElementById('chatInput').style.display='none';const snap=await db.ref('private_chats/'+currentUser.uid).once('value');const convs=snap.val()||{};cl.innerHTML='';for(const[oid,c]of Object.entries(convs)){const u=allUsers[oid];if(u)cl.innerHTML+='<div class="conv-item" onclick="openChat(\''+oid+'\')"><div class="avatar-sm">'+(u.avatarUrl?'<img src="'+u.avatarUrl+'">':(u.name?.charAt(0)||'U'))+'</div><div><div style="font-weight:700;">'+u.name+'</div><div style="font-size:13px;color:#71767b;">'+(c.lastMessage?.substring(0,40)||'رسالة')+'</div></div></div>'}if(cl.innerHTML==='')cl.innerHTML='<div style="text-align:center;color:#71767b;padding:40px;">لا توجد محادثات</div>'}async function openChat(uid){chatUserId=uid;const u=allUsers[uid];document.getElementById('convList').style.display='none';document.getElementById('msgsList').style.display='flex';document.getElementById('chatInput').style.display='flex';await loadMsgs()}async function loadMsgs(){const ml=document.getElementById('msgsList');ml.innerHTML='';const chatId=getChatId(currentUser.uid,chatUserId);const snap=await db.ref('private_messages/'+chatId).once('value');const ms=snap.val()||{};Object.values(ms).sort((a,b)=>a.timestamp-b.timestamp).forEach(m=>{const sent=m.senderId===currentUser.uid;ml.innerHTML+='<div class="bubble '+(sent?'sent':'received')+'">'+(m.type==='image'?'<img src="'+m.imageUrl+'" style="max-width:200px;border-radius:16px;">':m.text)+'<div style="font-size:10px;opacity:0.5;margin-top:4px;">'+new Date(m.timestamp).toLocaleTimeString()+'</div></div>'});ml.scrollTop=ml.scrollHeight}async function sendMsg(){const inp=document.getElementById('msgInput');const txt=inp.value.trim();if(!txt||!chatUserId)return;const chatId=getChatId(currentUser.uid,chatUserId);await db.ref('private_messages/'+chatId).push({senderId:currentUser.uid,text:txt,type:'text',timestamp:Date.now()});await db.ref('private_chats/'+currentUser.uid+'/'+chatUserId).set({lastMessage:txt,lastTimestamp:Date.now(),withUser:chatUserId});await db.ref('private_chats/'+chatUserId+'/'+currentUser.uid).set({lastMessage:txt,lastTimestamp:Date.now(),withUser:currentUser.uid});inp.value='';await loadMsgs()}window.openChat=openChat;window.sendMsg=sendMsg;window.loadConvs=loadConvs</script>
</body>
</html>"""

def build_explore():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><title>🟦 Sotwe | استكشاف</title><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"><style>:root{--primary:#1d9bf0;--bg:#000;--border:#2f3336}*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Inter',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}.header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(0,0,0,0.95);backdrop-filter:blur(12px);z-index:10}.btn-back{background:rgba(29,155,240,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;padding:2px}.thumb{aspect-ratio:1;background:#1a1a2a;display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;overflow:hidden}.thumb img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.thumb i{position:absolute;font-size:24px;color:#fff;z-index:1;opacity:0;transition:0.3s}.thumb:hover i{opacity:1}.thumb .likes{position:absolute;bottom:4px;left:4px;font-size:10px;background:rgba(0,0,0,0.6);padding:2px 6px;border-radius:10px}</style></head>
<body><div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>🟦 استكشاف</h2></div><div class="grid" id="exploreGrid"></div><script src="firebase-config.js"></script><script>db.ref('posts').on('value',s=>{const data=s.val()||{};const vids=Object.entries(data).map(([k,v])=>({id:k,...v})).filter(p=>p.mediaUrl&&(p.mediaType==='image'||p.mediaType==='video')).sort((a,b)=>(b.likes||0)-(a.likes||0));const g=document.getElementById('exploreGrid');g.innerHTML=vids.length?vids.map(p=>'<div class="thumb" onclick="window.open(\''+p.mediaUrl+'\',\'_blank\')">'+(p.mediaType==='image'?'<img src="'+p.mediaUrl+'">':'<video src="'+p.mediaUrl+'"></video>')+'<i class="fas fa-play"></i><span class="likes"><i class="fas fa-heart"></i> '+(p.likes||0)+'</span></div>').join(''):'<div style="text-align:center;padding:40px;grid-column:1/-1;color:#71767b">لا توجد وسائط</div>'})</script></body></html>"""

def build_notifications():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><title>🟦 Sotwe | إشعارات</title><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"><style>:root{--primary:#1d9bf0;--bg:#000;--border:#2f3336}*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Inter',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}.header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(0,0,0,0.95);backdrop-filter:blur(12px);z-index:10}.btn-back{background:rgba(29,155,240,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}.notif-item{display:flex;gap:12px;padding:16px;border-bottom:1px solid var(--border);align-items:center}.notif-item:hover{background:#080808}.notif-icon{width:40px;height:40px;border-radius:50%;background:rgba(29,155,240,0.1);display:flex;align-items:center;justify-content:center;font-size:18px}</style></head>
<body><div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>🟦 الإشعارات</h2></div><div id="notifsList"></div><script src="firebase-config.js"></script><script>auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}const snap=await db.ref('notifications/'+u.uid).once('value');const ns=snap.val()||{};const c=document.getElementById('notifsList');const items=Object.values(ns).reverse();const icons={like:'❤️',comment:'💬',retweet:'🔁',quote:'📝',follow:'👥'};c.innerHTML=items.length?items.map(n=>'<div class="notif-item"><div class="notif-icon">'+(icons[n.type]||'🔔')+'</div><div><div style="font-weight:700;">'+(n.fromUsername||'مستخدم')+'</div><div style="font-size:14px;color:#71767b;margin-top:4px;">'+(n.message||'')+'</div><div style="font-size:12px;color:#71767b;margin-top:4px;">'+new Date(n.timestamp).toLocaleString()+'</div></div></div>').join(''):'<div style="text-align:center;padding:40px;color:#71767b">لا توجد إشعارات</div>'})</script></body></html>"""

def build_settings():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><title>🟦 Sotwe | إعدادات</title><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"><style>:root{--primary:#1d9bf0;--bg:#000;--border:#2f3336;--surface:#1a1a1a}*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Inter',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}.header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(0,0,0,0.95);backdrop-filter:blur(12px);z-index:10}.btn-back{background:rgba(29,155,240,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}.item{display:flex;justify-content:space-between;align-items:center;padding:16px;border-bottom:1px solid var(--border);cursor:pointer}.item:hover{background:#080808}.btn-danger{background:rgba(249,24,128,0.2);border:1px solid rgba(249,24,128,0.3);color:#f91880;padding:12px 24px;border-radius:30px;cursor:pointer;font-size:14px;margin:20px auto;display:block}</style></head>
<body><div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>🟦 الإعدادات</h2></div><div><div class="item" onclick="window.location.href='index.html'"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-user" style="color:var(--primary)"></i><span>الملف الشخصي</span></div><i class="fas fa-chevron-left" style="opacity:0.5"></i></div><div class="item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-moon" style="color:var(--primary)"></i><span>المظهر</span></div><span style="opacity:0.5;font-size:13px">داكن / فاتح</span></div><div class="item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-info-circle" style="color:var(--primary)"></i><span>حول التطبيق</span></div><span style="opacity:0.5;font-size:13px">Sotwe v2026.1</span></div><button class="btn-danger" onclick="logout()"><i class="fas fa-sign-out-alt"></i> تسجيل الخروج</button></div><script src="firebase-config.js"></script><script>auth.onAuthStateChanged(u=>{if(!u)window.location.href='auth.html'});function logout(){auth.signOut();window.location.href='auth.html'}</script></body></html>"""

# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  🟦  SOTWE 2026 - SOCIAL PLATFORM GENERATOR  ✨      ║
║     Ultimate Generator - 9 Files - 2500+ Lines           ║
║                                                          ║
║  ✨  Posts + Comments + Replies + Quotes              ║
║  ❤️   Likes + Retweets + Bookmarks                   ║
║  💬  Private Chat (Text/Image/Audio)                  ║
║  📝  Stories + Search + Admin Panel                   ║
║  🛡️   Delete Users/Posts + Dark/Light Mode           ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)

    section("BUILDING FILES - Sotwe")

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
  🟦 SOTWE BUILD COMPLETE! ✨
{'='*60}

  📊 إحصائيات:
     • {TOTAL_LINES} إجمالي عدد الأسطر
     • 9 ملفات تم إنشاؤها

  📁 الملفات:
     1. firebase-config.js
     2. auth.html
     3. index.html (تصميم Sotwe المحسّن)
     4. script.js (كل المنطق - Compat Version)
     5. upload.html
     6. chat.html
     7. explore.html
     8. notifications.html
     9. settings.html

  🟦 SOTWE المميزات:
     • ❤️  منشورات + إعجابات + ريتويت + إشارات
     • 💬 تعليقات + ردود متداخلة
     • 📝 اقتباسات (Quote Tweets)
     • 💌 دردشة (نص + صورة + صوت)
     • 📸 رفع وسائط + تسجيل صوتي
     • 👤 ملف شخصي + تعديل + صورة + غلاف
     • 🔍 بحث + 🔔 إشعارات + 🌓 ليلي/نهاري
     • 🛡️  لوحة أدمن كاملة
     • 🎨 تصميم عصري محسّن

  🔑 البيانات:
     • Firebase: muvg-42126
     • Cloudinary: dmqyd0haj / s3_gok
     • Admin: jasim28v@gmail.com

  🚀 للتشغيل:
     python scraper.py
  🟦 SOTWE READY! ✨
{'='*60}
    """)

if __name__ == "__main__":
    main()
