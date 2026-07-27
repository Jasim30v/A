#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                            ║
║  💎  MNAENCA 2026 - EMERALD GREEN GLASS LUXURY EDITION  💎 ║
║     Ultimate Version - 10 Files - 4000+ Lines              ║
║     ✨ PROFILE 2.0 - Advanced Professional Profile         ║
║                                                            ║
║  🔥  Firebase: muvg-42126                                 ║
║  ☁️   Cloudinary: trz3ktjf / s44_kk                     ║
║  👑  Admin: jasim28v@gmail.com                            ║
║  👾  Avatars: DiceBear Big Smile (Random)                  ║
║  💎  Design: Light Green Glass Luxury                      ║
║  ✨  RESPONSIVE (Mobile + Desktop/Landscape)            ║
║  🎬  NATURAL VIDEO DISPLAY (No Zoom/Crop)               ║
║  📝  TEXT BELOW VIDEO                                    ║
║                                                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import shutil

# ═══════════════════════════════════════════════════════════
# 💎 CONFIGURATION - الإعدادات
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

CLOUD_NAME = "trz3ktjf"
UPLOAD_PRESET = "s44_kk"
ADMIN_EMAILS_JS = "['jasim28v@gmail.com']"
DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg"
APP_NAME = "MNAENCA"
WATERMARK_TEXT = "💎 MNAENCA"
WATERMARK_URL = "https://res.cloudinary.com/trz3ktjf/image/upload/v1/watermark_mnaenca"

# 💎 Light Green Luxury Palette
EMERALD_COLORS_JS = """[
    "linear-gradient(135deg, #064e3b, #059669, #10b981)",
    "linear-gradient(135deg, #022c22, #047857, #34d399)",
    "linear-gradient(135deg, #065f46, #10b981, #6ee7b7)",
    "linear-gradient(135deg, #064e3b, #14b8a6, #5eead4)",
    "linear-gradient(135deg, #047857, #34d399, #a7f3d0)",
    "linear-gradient(135deg, #0f172a, #064e3b, #10b981)"
]"""

OUTPUT_DIR = "output"

# ═══════════════════════════════════════════════════════════
# 💎 UTILITY - دوال مساعدة
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
    print(f"  💎  {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# 💎 COMMON CSS - ستايل مشترك
# ═══════════════════════════════════════════════════════════

COMMON_CSS = """
    :root{
        --glass:rgba(16,185,129,0.03);
        --border:rgba(16,185,129,0.12);
        --accent:#10b981;
        --accent2:#34d399;
        --bg:#05140b;
        --card:rgba(16,185,129,0.06);
        --danger:#ef4444;
        --success:#22c55e;
        --warning:#f59e0b;
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
    @keyframes shimmer{0%{background-position:-200% 0}100%{background-position:200% 0}}
    @keyframes glowPulse{0%,100%{box-shadow:0 0 20px rgba(16,185,129,0.3)}50%{box-shadow:0 0 40px rgba(52,211,153,0.7)}}
    .spinner{
        width:36px;height:36px;
        border:3px solid rgba(16,185,129,0.2);
        border-top-color:var(--accent);
        border-radius:50%;
        animation:spin 0.7s linear infinite;
        margin:30px auto;
    }
    .toast-msg{
        position:fixed;bottom:120px;left:50%;transform:translateX(-50%);
        background:rgba(5,20,11,0.95);padding:12px 24px;border-radius:30px;
        z-index:10000;border:1px solid rgba(16,185,129,0.3);font-size:13px;
        opacity:0;transition:opacity 0.3s;pointer-events:none;white-space:nowrap;
        box-shadow:0 8px 32px rgba(0,0,0,0.4);
    }
    .toast-msg.show{opacity:1}
    .overlay{
        position:fixed;inset:0;background:rgba(5,20,11,0.97);
        backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);
        z-index:400;overflow-y:auto;
        animation:fadeIn 0.3s ease;
    }
    .overlay-header{
        display:flex;justify-content:space-between;align-items:center;
        padding:16px 20px;border-bottom:1px solid var(--border);
        position:sticky;top:0;background:rgba(5,20,11,0.9);
        backdrop-filter:blur(20px);z-index:5;
    }
    .overlay-header h3{font-weight:700;font-size:17px;display:flex;align-items:center;gap:8px}
    .btn-close-overlay{
        background:rgba(16,185,129,0.1);border:1px solid var(--border);
        color:#fff;width:36px;height:36px;border-radius:50%;
        display:flex;align-items:center;justify-content:center;
        cursor:pointer;font-size:16px;transition:all 0.3s;
    }
    .btn-close-overlay:hover{background:rgba(16,185,129,0.25);box-shadow:0 0 15px rgba(16,185,129,0.3)}

    /* ✨ RESPONSIVE LAYOUT ✨ */
    #mainApp {
        display: flex;
        flex-direction: column;
        height: 100vh;
        width: 100vw;
        position: relative;
    }

    .desktop-sidebar { display: none; }
    .desktop-header { display: none; }

    @media screen and (min-width: 800px) {
        body { overflow: hidden; }
        
        #mainApp {
            flex-direction: row;
            height: 100vh;
            width: 100vw;
        }

        .desktop-sidebar {
            display: flex;
            flex-direction: column;
            width: 280px;
            height: 100vh;
            padding: 24px 16px;
            border-right: 1px solid var(--border);
            background: rgba(5,20,11,0.6);
            flex-shrink: 0;
            overflow-y: auto;
        }

        .sidebar-logo {
            font-size: 24px;
            font-weight: 800;
            margin-bottom: 30px;
            background: linear-gradient(to bottom,#fff,#a7f3d0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: flex; align-items: center; gap: 10px;
        }
        .sidebar-nav-item {
            display: flex; align-items: center; gap: 14px;
            padding: 12px 16px; margin-bottom: 6px;
            border-radius: 16px; cursor: pointer;
            font-size: 15px; font-weight: 500;
            color: rgba(255,255,255,0.7);
            transition: all 0.3s;
        }
        .sidebar-nav-item:hover, .sidebar-nav-item.active {
            background: rgba(16,185,129,0.1);
            color: #fff;
        }
        .sidebar-nav-item i { font-size: 20px; width: 24px; text-align: center; }
        
        .topbar { display: none !important; }
        .nav-bottom { display: none !important; }

        .videos-wrap {
            flex: 1;
            height: 100vh;
            width: auto;
        }
        .vid-card video { opacity: 1 !important; transform: translateY(0) !important; }
        
        .side-btns { bottom: 40px; right: 30px; }
        .vid-info { bottom: 40px; left: 30px; right: 90px; }
    }
"""

# ═══════════════════════════════════════════════════════════
# 💎 1. firebase-config.js
# ═══════════════════════════════════════════════════════════

def build_config():
    return f"""// 💎 MNAENCA 2026 - Emerald Green Luxury Configuration
// Firebase: muvg-42126 | Cloudinary: {CLOUD_NAME}
// ✨ PREMIUM: TikTok Comments + Share System + Watermark + Enhanced Profile + Posts

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

// 💎 MNAENCA Settings
const ADMIN_EMAILS = {ADMIN_EMAILS_JS};
const DICEBEAR_URL = "{DICEBEAR_URL}";
const COVER_COLORS = {EMERALD_COLORS_JS};

// 💎 App Info
const APP_NAME = "{APP_NAME}";
const APP_VERSION = "2026.4";
const PRIMARY_COLOR = "#10b981";
const SECONDARY_COLOR = "#a7f3d0";
const WATERMARK_TEXT = "{WATERMARK_TEXT}";
const WATERMARK_URL = "{WATERMARK_URL}";

console.log('💎 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨', 'color: #10b981; font-size: 16px; font-weight: bold;');
"""

# ═══════════════════════════════════════════════════════════
# 💎 2. auth.html - تسجيل الدخول والاشتراك (مطور بالكامل)
# ═══════════════════════════════════════════════════════════

def build_auth():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💎 MNAENCA | دخول</title>
    <!-- Firebase SDK v10.12.0 (أحدث إصدار) -->
    <script src="https://www.gstatic.com/firebasejs/10.12.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.12.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.12.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        :root {{
            --emerald-400: #34d399;
            --emerald-500: #10b981;
            --emerald-600: #059669;
            --surface-glass: rgba(16, 185, 129, 0.04);
            --border-glass: rgba(16, 185, 129, 0.15);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            min-height: 100vh;
            background: radial-gradient(ellipse at top, #0f172a 0%, #05140b 50%, #020617 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            position: relative;
            font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, sans-serif;
        }}

        /* Background orbs with enhanced animation */
        .bg-orb {{
            position: fixed;
            border-radius: 50%;
            filter: blur(140px);
            opacity: 0.2;
            animation: orbFloat 25s infinite alternate;
            pointer-events: none;
        }}
        .bg-orb:nth-child(1) {{
            width: 500px;
            height: 500px;
            background: #10b981;
            top: -150px;
            left: -150px;
            animation-delay: 0s;
        }}
        .bg-orb:nth-child(2) {{
            width: 400px;
            height: 400px;
            background: #34d399;
            bottom: -150px;
            right: -150px;
            animation-delay: -7s;
        }}
        .bg-orb:nth-child(3) {{
            width: 350px;
            height: 350px;
            background: #6ee7b7;
            top: 50%;
            left: 50%;
            animation-delay: -14s;
        }}
        .bg-orb:nth-child(4) {{
            width: 250px;
            height: 250px;
            background: #a7f3d0;
            top: 20%;
            right: 20%;
            animation-delay: -21s;
        }}

        @keyframes orbFloat {{
            0% {{
                transform: translate(0, 0) scale(1) rotate(0deg);
            }}
            33% {{
                transform: translate(60px, -40px) scale(1.2) rotate(120deg);
            }}
            66% {{
                transform: translate(-30px, 50px) scale(0.9) rotate(240deg);
            }}
            100% {{
                transform: translate(40px, -30px) scale(1.15) rotate(360deg);
            }}
        }}

        /* Particle effect */
        .particles {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
        }}
        .particle {{
            position: absolute;
            background: rgba(16, 185, 129, 0.3);
            border-radius: 50%;
            animation: floatUp linear infinite;
        }}
        @keyframes floatUp {{
            0% {{
                transform: translateY(100vh) scale(0);
                opacity: 0;
            }}
            10% {{
                opacity: 1;
            }}
            90% {{
                opacity: 1;
            }}
            100% {{
                transform: translateY(-10vh) scale(1);
                opacity: 0;
            }}
        }}

        /* Main card with enhanced glass morphism */
        .card {{
            position: relative;
            z-index: 1;
            width: 90%;
            max-width: 440px;
            background: rgba(16, 185, 129, 0.03);
            backdrop-filter: blur(60px);
            -webkit-backdrop-filter: blur(60px);
            border-radius: 36px;
            padding: 40px 28px;
            border: 1px solid rgba(16, 185, 129, 0.2);
            box-shadow: 
                0 30px 80px rgba(16, 185, 129, 0.1),
                0 0 0 1px rgba(16, 185, 129, 0.05),
                inset 0 0 40px rgba(16, 185, 129, 0.02);
            animation: cardFadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .card:hover {{
            transform: translateY(-2px);
            box-shadow: 
                0 35px 90px rgba(16, 185, 129, 0.15),
                0 0 0 1px rgba(16, 185, 129, 0.08),
                inset 0 0 40px rgba(16, 185, 129, 0.03);
        }}

        @keyframes cardFadeUp {{
            from {{
                opacity: 0;
                transform: translateY(40px) scale(0.95);
            }}
            to {{
                opacity: 1;
                transform: translateY(0) scale(1);
            }}
        }}

        /* Logo with pulse glow */
        .logo-container {{
            position: relative;
            width: 80px;
            height: 80px;
            margin: 0 auto 24px;
        }}
        .logo {{
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.25), rgba(52, 211, 153, 0.25));
            border-radius: 22px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 42px;
            border: 1px solid rgba(16, 185, 129, 0.3);
            position: relative;
            z-index: 2;
        }}
        .logo-glow {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100%;
            height: 100%;
            background: radial-gradient(circle, rgba(16, 185, 129, 0.4) 0%, transparent 70%);
            border-radius: 22px;
            animation: glowPulse 2.5s ease-in-out infinite;
            z-index: 1;
        }}
        @keyframes glowPulse {{
            0%, 100% {{
                transform: translate(-50%, -50%) scale(1);
                opacity: 0.6;
            }}
            50% {{
                transform: translate(-50%, -50%) scale(1.3);
                opacity: 0.2;
            }}
        }}

        h1 {{
            text-align: center;
            font-size: 38px;
            font-weight: 900;
            background: linear-gradient(180deg, #ffffff 0%, #6ee7b7 50%, #34d399 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 4px;
            letter-spacing: -0.5px;
        }}
        .sub {{
            text-align: center;
            color: rgba(255, 255, 255, 0.35);
            font-size: 13px;
            margin-bottom: 28px;
            font-weight: 300;
            letter-spacing: 1px;
        }}

        /* Enhanced tabs */
        .tabs {{
            display: flex;
            gap: 6px;
            background: rgba(16, 185, 129, 0.05);
            border-radius: 50px;
            padding: 5px;
            margin-bottom: 28px;
            position: relative;
        }}
        .tab {{
            flex: 1;
            padding: 13px;
            background: transparent;
            border: none;
            color: rgba(255, 255, 255, 0.5);
            cursor: pointer;
            border-radius: 50px;
            font-size: 14px;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            font-weight: 600;
            position: relative;
            z-index: 1;
            font-family: inherit;
        }}
        .tab.active {{
            background: linear-gradient(135deg, #10b981, #059669);
            color: #fff;
            box-shadow: 
                0 8px 25px rgba(16, 185, 129, 0.4),
                0 0 0 1px rgba(255, 255, 255, 0.1) inset;
            transform: scale(1.02);
        }}
        .tab:hover:not(.active) {{
            color: rgba(255, 255, 255, 0.8);
            background: rgba(16, 185, 129, 0.08);
        }}

        /* Forms */
        .form {{
            display: none;
            animation: fadeSlideIn 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .form.active {{
            display: block;
        }}
        @keyframes fadeSlideIn {{
            from {{
                opacity: 0;
                transform: translateX(-10px);
            }}
            to {{
                opacity: 1;
                transform: translateX(0);
            }}
        }}

        /* Input fields with icons */
        .input-group {{
            position: relative;
            margin-bottom: 12px;
        }}
        .input-group i {{
            position: absolute;
            right: 18px;
            top: 50%;
            transform: translateY(-50%);
            color: rgba(16, 185, 129, 0.4);
            font-size: 15px;
            transition: color 0.3s;
            pointer-events: none;
            z-index: 2;
        }}
        input {{
            width: 100%;
            padding: 16px 45px 16px 20px;
            border-radius: 50px;
            background: rgba(16, 185, 129, 0.04);
            border: 1.5px solid rgba(16, 185, 129, 0.12);
            color: #fff;
            font-size: 14px;
            outline: none;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            font-family: inherit;
        }}
        input:focus {{
            border-color: rgba(16, 185, 129, 0.6);
            box-shadow: 
                0 0 25px rgba(16, 185, 129, 0.1),
                0 0 0 3px rgba(16, 185, 129, 0.05);
            background: rgba(16, 185, 129, 0.08);
        }}
        input:focus + i,
        .input-group:focus-within i {{
            color: rgba(16, 185, 129, 0.8);
        }}
        input::placeholder {{
            color: rgba(255, 255, 255, 0.25);
            font-size: 13px;
        }}

        /* Primary button */
        .btn-primary {{
            width: 100%;
            padding: 16px;
            margin-top: 20px;
            background: linear-gradient(135deg, #10b981, #059669);
            border: none;
            border-radius: 50px;
            color: #fff;
            font-weight: 700;
            font-size: 15px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 
                0 10px 30px rgba(16, 185, 129, 0.35),
                0 0 0 1px rgba(255, 255, 255, 0.1) inset;
            position: relative;
            overflow: hidden;
            font-family: inherit;
        }}
        .btn-primary::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent);
            transition: left 0.5s;
        }}
        .btn-primary:hover {{
            transform: translateY(-3px);
            box-shadow: 
                0 20px 45px rgba(16, 185, 129, 0.5),
                0 0 0 1px rgba(255, 255, 255, 0.15) inset;
        }}
        .btn-primary:hover::before {{
            left: 100%;
        }}
        .btn-primary:active {{
            transform: scale(0.96);
            transition: transform 0.1s;
        }}
        .btn-primary:disabled {{
            opacity: 0.6;
            pointer-events: none;
            filter: grayscale(30%);
        }}

        /* Divider */
        .divider {{
            display: flex;
            align-items: center;
            margin: 22px 0;
            gap: 12px;
        }}
        .divider::before,
        .divider::after {{
            content: '';
            flex: 1;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(16, 185, 129, 0.2), transparent);
        }}
        .divider span {{
            color: rgba(255, 255, 255, 0.3);
            font-size: 12px;
            font-weight: 500;
            white-space: nowrap;
        }}

        /* Google button - Modern design */
        .btn-google {{
            width: 100%;
            padding: 14px;
            background: rgba(255, 255, 255, 0.04);
            border: 1.5px solid rgba(255, 255, 255, 0.12);
            border-radius: 50px;
            color: #fff;
            font-weight: 600;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            backdrop-filter: blur(10px);
            font-family: inherit;
        }}
        .btn-google:hover {{
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(255, 255, 255, 0.25);
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }}
        .btn-google:active {{
            transform: scale(0.97);
        }}
        .btn-google img {{
            width: 20px;
            height: 20px;
        }}

        /* Messages */
        .msg {{
            text-align: center;
            color: #fca5a5;
            font-size: 13px;
            margin-top: 14px;
            min-height: 20px;
            font-weight: 500;
            transition: all 0.3s;
        }}
        .msg.success {{
            color: #4ade80;
        }}

        /* Loading spinner */
        .spinner {{
            display: inline-block;
            width: 18px;
            height: 18px;
            border: 2px solid rgba(255,255,255,0.3);
            border-top-color: #fff;
            border-radius: 50%;
            animation: spin 0.6s linear infinite;
            vertical-align: middle;
        }}
        @keyframes spin {{
            to {{ transform: rotate(360deg); }}
        }}

        /* Ripple effect */
        .ripple {{
            position: relative;
            overflow: hidden;
        }}
        .ripple::after {{
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255,255,255,0.2);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }}
        .ripple:active::after {{
            width: 300px;
            height: 300px;
        }}

        /* Responsive */
        @media (max-width: 480px) {{
            .card {{
                padding: 30px 20px;
                border-radius: 28px;
            }}
            h1 {{
                font-size: 30px;
            }}
            .logo-container {{
                width: 65px;
                height: 65px;
            }}
            .logo {{
                font-size: 34px;
                border-radius: 18px;
            }}
            .logo-glow {{
                border-radius: 18px;
            }}
        }}
    </style>
</head>
<body>
    <!-- Floating orbs -->
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>

    <!-- Particles -->
    <div class="particles" id="particles"></div>

    <!-- Main Card -->
    <div class="card">
        <div class="logo-container">
            <div class="logo-glow"></div>
            <div class="logo">💎</div>
        </div>
        <h1>MNAENCA</h1>
        <p class="sub">✦ Emerald Luxury 2026 ✦</p>

        <!-- Tabs -->
        <div class="tabs">
            <button class="tab active" id="tabLogin" onclick="switchTab('login')">
                <i class="fas fa-sign-in-alt"></i> دخول
            </button>
            <button class="tab" id="tabRegister" onclick="switchTab('register')">
                <i class="fas fa-user-plus"></i> اشتراك
            </button>
        </div>

        <!-- Login Form -->
        <div id="formLogin" class="form active">
            <div class="input-group">
                <input type="email" id="loginEmail" placeholder="البريد الإلكتروني" autocomplete="email" dir="ltr">
                <i class="fas fa-envelope"></i>
            </div>
            <div class="input-group">
                <input type="password" id="loginPass" placeholder="كلمة المرور" autocomplete="current-password">
                <i class="fas fa-lock"></i>
            </div>
            <button class="btn-primary ripple" id="btnLogin" onclick="doLogin()">
                <i class="fas fa-arrow-right-to-bracket"></i> تسجيل الدخول
            </button>
            <div class="divider">
                <span>أو سجل دخولك بـ</span>
            </div>
            <button class="btn-google" id="btnGoogleLogin" onclick="doGoogleLogin()">
                <img src="https://www.google.com/favicon.ico" alt="Google" width="20" height="20" style="border-radius:50%;">
                متابعة باستخدام Google
            </button>
            <div class="divider">
                <span>أو سجل دخولك بـ</span>
            </div>
            <button class="btn-google" id="btnGoogleRegister" onclick="doGoogleRegister()">
                <img src="https://www.google.com/favicon.ico" alt="Google" width="20" height="20" style="border-radius:50%;">
                متابعة باستخدام Google
            </button>
            <div class="msg" id="loginMsg"></div>
        </div>

        <!-- Register Form -->
        <div id="formRegister" class="form">
            <div class="input-group">
                <input type="text" id="regName" placeholder="اسم المستخدم" autocomplete="username">
                <i class="fas fa-user"></i>
            </div>
            <div class="input-group">
                <input type="email" id="regEmail" placeholder="البريد الإلكتروني" autocomplete="email" dir="ltr">
                <i class="fas fa-envelope"></i>
            </div>
            <div class="input-group">
                <input type="password" id="regPass" placeholder="كلمة المرور (6 أحرف على الأقل)" autocomplete="new-password">
                <i class="fas fa-key"></i>
            </div>
            <button class="btn-primary ripple" id="btnRegister" onclick="doRegister()">
                <i class="fas fa-heart"></i> إنشاء حساب
            </button>
            <div class="msg" id="regMsg"></div>
        </div>
    </div>

    <script src="firebase-config.js"></script>
    <script>
        // Initialize Firebase (يجب أن يكون موجوداً في firebase-config.js)
        // firebase.initializeApp(firebaseConfig);
        // const auth = firebase.auth();
        // const db = firebase.database();

        // Create particles
        (function createParticles() {{
            const container = document.getElementById('particles');
            if (!container) return;
            const count = 25;
            for (let i = 0; i < count; i++) {{
                const particle = document.createElement('div');
                particle.className = 'particle';
                const size = Math.random() * 4 + 2;
                particle.style.width = size + 'px';
                particle.style.height = size + 'px';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.animationDuration = Math.random() * 8 + 6 + 's';
                particle.style.animationDelay = Math.random() * 8 + 's';
                container.appendChild(particle);
            }}
        }})();

        // Tab switching
        function switchTab(type) {{
            const tabLogin = document.getElementById('tabLogin');
            const tabRegister = document.getElementById('tabRegister');
            const formLogin = document.getElementById('formLogin');
            const formRegister = document.getElementById('formRegister');
            const btnGoogleLogin = document.getElementById('btnGoogleLogin');
            const btnGoogleRegister = document.getElementById('btnGoogleRegister');
            
            document.getElementById('loginMsg').innerText = '';
            document.getElementById('regMsg').innerText = '';
            document.getElementById('loginMsg').className = 'msg';
            document.getElementById('regMsg').className = 'msg';
            
            if (type === 'login') {{
                tabLogin.classList.add('active');
                tabRegister.classList.remove('active');
                formLogin.classList.add('active');
                formRegister.classList.remove('active');
                if (btnGoogleLogin) btnGoogleLogin.style.display = 'flex';
                if (btnGoogleRegister) btnGoogleRegister.style.display = 'flex';
            }} else {{
                tabRegister.classList.add('active');
                tabLogin.classList.remove('active');
                formRegister.classList.add('active');
                formLogin.classList.remove('active');
                if (btnGoogleLogin) btnGoogleLogin.style.display = 'none';
                if (btnGoogleRegister) btnGoogleRegister.style.display = 'none';
            }}
        }}

        // Login with Email/Password
        async function doLogin() {{
            const email = document.getElementById('loginEmail').value.trim();
            const password = document.getElementById('loginPass').value;
            const msg = document.getElementById('loginMsg');
            const btn = document.getElementById('btnLogin');
            
            if (!email || !password) {{
                msg.innerText = '❌ الرجاء ملء جميع الحقول';
                msg.className = 'msg';
                shakeElement(document.getElementById('loginEmail').parentElement);
                return;
            }}
            
            btn.disabled = true;
            btn.innerHTML = '<span class="spinner"></span> جاري الدخول...';
            msg.innerText = '';
            msg.className = 'msg';
            
            try {{
                await auth.signInWithEmailAndPassword(email, password);
                window.location.replace('index.html');
            }} catch (error) {{
                btn.disabled = false;
                btn.innerHTML = '<i class="fas fa-arrow-right-to-bracket"></i> تسجيل الدخول';
                
                let errorMsg = '❌ حدث خطأ غير متوقع';
                switch (error.code) {{
                    case 'auth/user-not-found':
                        errorMsg = '❌ لا يوجد حساب بهذا البريد الإلكتروني';
                        break;
                    case 'auth/wrong-password':
                    case 'auth/invalid-credential':
                        errorMsg = '❌ كلمة المرور غير صحيحة';
                        break;
                    case 'auth/invalid-email':
                        errorMsg = '❌ صيغة البريد الإلكتروني غير صالحة';
                        break;
                    case 'auth/too-many-requests':
                        errorMsg = '❌ محاولات كثيرة، الرجاء المحاولة لاحقاً';
                        break;
                    case 'auth/user-disabled':
                        errorMsg = '❌ تم تعطيل هذا الحساب';
                        break;
                    default:
                        errorMsg = '❌ خطأ: ' + (error.message || 'غير معروف');
                }}
                msg.innerText = errorMsg;
                msg.className = 'msg';
            }}
        }}

        // Register with Email/Password
        async function doRegister() {{
            const username = document.getElementById('regName').value.trim();
            const email = document.getElementById('regEmail').value.trim();
            const password = document.getElementById('regPass').value;
            const msg = document.getElementById('regMsg');
            const btn = document.getElementById('btnRegister');
            
            // Validation
            if (!username || !email || !password) {{
                msg.innerText = '❌ الرجاء ملء جميع الحقول';
                msg.className = 'msg';
                return;
            }}
            if (username.length < 3) {{
                msg.innerText = '❌ اسم المستخدم يجب أن يكون 3 أحرف على الأقل';
                msg.className = 'msg';
                return;
            }}
            if (password.length < 6) {{
                msg.innerText = '❌ كلمة المرور يجب أن تكون 6 أحرف على الأقل';
                msg.className = 'msg';
                return;
            }}
            if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {{
                msg.innerText = '❌ صيغة البريد الإلكتروني غير صالحة';
                msg.className = 'msg';
                return;
            }}
            
            btn.disabled = true;
            btn.innerHTML = '<span class="spinner"></span> جاري إنشاء الحساب...';
            msg.innerText = '';
            msg.className = 'msg';
            
            try {{
                const userCredential = await auth.createUserWithEmailAndPassword(email, password);
                const uid = userCredential.user.uid;
                
                // إنشاء بيانات المستخدم
                const avatarUrl = DICEBEAR_URL + '?seed=' + uid;
                const coverColor = COVER_COLORS[Math.floor(Math.random() * COVER_COLORS.length)];
                
                const userData = {{
                    username: username,
                    email: email,
                    bio: '',
                    website: '',
                    location: '',
                    contactEmail: '',
                    avatarUrl: avatarUrl,
                    hasCustomAvatar: false,
                    coverImageUrl: '',
                    hasCustomCover: false,
                    coverColor: coverColor,
                    followers: {{}},
                    following: {{}},
                    totalLikes: 0,
                    totalPosts: 0,
                    isVerified: false,
                    verifiedAt: null,
                    verifiedBy: null,
                    banned: false,
                    createdAt: Date.now(),
                    lastSeen: Date.now(),
                    authProvider: 'email'
                }};
                
                await db.ref('users/' + uid).set(userData);
                
                msg.innerText = '✅ تم إنشاء الحساب بنجاح! جاري التوجيه...';
                msg.className = 'msg success';
                
                setTimeout(() => {{
                    window.location.replace('index.html');
                }}, 1000);
            }} catch (error) {{
                btn.disabled = false;
                btn.innerHTML = '<i class="fas fa-heart"></i> إنشاء حساب';
                
                let errorMsg = '❌ حدث خطأ غير متوقع';
                switch (error.code) {{
                    case 'auth/email-already-in-use':
                        errorMsg = '❌ البريد الإلكتروني مستخدم بالفعل';
                        break;
                    case 'auth/weak-password':
                        errorMsg = '❌ كلمة المرور ضعيفة جداً';
                        break;
                    case 'auth/invalid-email':
                        errorMsg = '❌ صيغة البريد الإلكتروني غير صالحة';
                        break;
                    case 'auth/operation-not-allowed':
                        errorMsg = '❌ التسجيل غير مفعل، راجع إعدادات Firebase';
                        break;
                    default:
                        errorMsg = '❌ خطأ: ' + (error.message || 'غير معروف');
                }}
                msg.innerText = errorMsg;
                msg.className = 'msg';
            }}
        }}

        // Google Sign-In/Up
        async function doGoogleLogin() {{
            const provider = new firebase.auth.GoogleAuthProvider();
            provider.setCustomParameters({{
                prompt: 'select_account'
            }});
            await handleGoogleAuth(provider, 'login');
        }}

        async function doGoogleRegister() {{
            const provider = new firebase.auth.GoogleAuthProvider();
            provider.setCustomParameters({{
                prompt: 'select_account'
            }});
            await handleGoogleAuth(provider, 'register');
        }}

        async function handleGoogleAuth(provider, type) {{
            const msg = document.getElementById(type === 'login' ? 'loginMsg' : 'regMsg');
            const btn = document.getElementById(type === 'login' ? 'btnGoogleLogin' : 'btnGoogleRegister');
            
            msg.innerText = '';
            msg.className = 'msg';
            
            if (btn) {{
                btn.disabled = true;
                btn.innerHTML = '<span class="spinner"></span> جاري المصادقة...';
            }}
            
            try {{
                const result = await auth.signInWithPopup(provider);
                const user = result.user;
                const isNewUser = result.additionalUserInfo?.isNewUser;
                
                // إذا كان مستخدماً جديداً، أنشئ بياناته
                if (isNewUser || type === 'register') {{
                    const uid = user.uid;
                    const userRef = db.ref('users/' + uid);
                    const snapshot = await userRef.once('value');
                    
                    if (!snapshot.exists()) {{
                        const avatarUrl = user.photoURL || (DICEBEAR_URL + '?seed=' + uid);
                        const coverColor = COVER_COLORS[Math.floor(Math.random() * COVER_COLORS.length)];
                        const displayName = user.displayName || 'مستخدم ' + uid.substring(0, 6);
                        
                        const userData = {{
                            username: displayName,
                            email: user.email,
                            bio: '',
                            website: '',
                            location: '',
                            contactEmail: user.email,
                            avatarUrl: avatarUrl,
                            hasCustomAvatar: !!user.photoURL,
                            coverImageUrl: '',
                            hasCustomCover: false,
                            coverColor: coverColor,
                            followers: {{}},
                            following: {{}},
                            totalLikes: 0,
                            totalPosts: 0,
                            isVerified: user.emailVerified || false,
                            verifiedAt: user.emailVerified ? Date.now() : null,
                            verifiedBy: user.emailVerified ? 'google' : null,
                            banned: false,
                            createdAt: Date.now(),
                            lastSeen: Date.now(),
                            authProvider: 'google'
                        }};
                        
                        await userRef.set(userData);
                    }}
                }}
                
                msg.innerText = '✅ تم تسجيل الدخول بنجاح! جاري التوجيه...';
                msg.className = 'msg success';
                
                setTimeout(() => {{
                    window.location.replace('index.html');
                }}, 800);
            }} catch (error) {{
                if (btn) {{
                    btn.disabled = false;
                    btn.innerHTML = '<img src="https://www.google.com/favicon.ico" alt="Google" width="20" height="20" style="border-radius:50%;"> متابعة باستخدام Google';
                }}
                
                let errorMsg = '❌ حدث خطأ غير متوقع';
                switch (error.code) {{
                    case 'auth/popup-closed-by-user':
                        errorMsg = '❌ تم إغلاق نافذة تسجيل الدخول';
                        break;
                    case 'auth/popup-blocked':
                        errorMsg = '❌ تم حظر النافذة المنبثقة، الرجاء السماح بها';
                        break;
                    case 'auth/cancelled-popup-request':
                        errorMsg = '❌ تم إلغاء الطلب';
                        break;
                    case 'auth/account-exists-with-different-credential':
                        errorMsg = '❌ يوجد حساب مسجل بنفس البريد الإلكتروني بطريقة مختلفة';
                        break;
                    case 'auth/network-request-failed':
                        errorMsg = '❌ فشل الاتصال بالشبكة';
                        break;
                    default:
                        errorMsg = '❌ خطأ: ' + (error.message || 'غير معروف');
                }}
                msg.innerText = errorMsg;
                msg.className = 'msg';
                
                console.error('Google Auth Error:', error);
            }}
        }}

        // Shake animation for invalid input
        function shakeElement(element) {{
            if (!element) return;
            element.style.animation = 'shake 0.5s ease';
            setTimeout(() => {{
                element.style.animation = '';
            }}, 500);
        }}

        // Add shake keyframes dynamically
        const shakeStyle = document.createElement('style');
        shakeStyle.textContent = `
            @keyframes shake {{
                0%, 100% {{ transform: translateX(0); }}
                10%, 30%, 50%, 70%, 90% {{ transform: translateX(-5px); }}
                20%, 40%, 60%, 80% {{ transform: translateX(5px); }}
            }}
        `;
        document.head.appendChild(shakeStyle);

        // Enter key handler
        document.querySelectorAll('input').forEach(input => {{
            input.addEventListener('keydown', function(e) {{
                if (e.key === 'Enter') {{
                    e.preventDefault();
                    if (document.getElementById('formLogin').classList.contains('active')) {{
                        doLogin();
                    }} else {{
                        doRegister();
                    }}
                }}
            }});
        }});

        // Auto-redirect if already logged in
        if (typeof auth !== 'undefined') {{
            auth.onAuthStateChanged(user => {{
                if (user) {{
                    window.location.replace('index.html');
                }}
            }});
        }}

        console.log('💎 MNAENCA Auth v2.0 Ready | Firebase v10.12.0 | Google Auth Enabled');
    </script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 💎 3. index.html - الرئيسية (فيديو طبيعي + نص أسفل الفيديو)
# ═══════════════════════════════════════════════════════════

def build_index():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>💎 MNAENCA | الرئيسية</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        
        #loaderScreen{{
            position:fixed;inset:0;z-index:9999;
            background:radial-gradient(ellipse at top, #0f172a, #05140b, #020617);
            display:flex;align-items:center;justify-content:center;
            flex-direction:column;gap:16px;
        }}
        .spinner-big{{
            width:50px;height:50px;
            border:4px solid rgba(16,185,129,0.2);
            border-top-color:var(--accent);
            border-radius:50%;
            animation:spin 0.8s linear infinite;
        }}

        .topbar{{
            position:fixed;top:10px;left:10px;right:10px;z-index:100;
            display:flex;justify-content:space-between;align-items:center;
            padding:8px 16px;
            background:rgba(5,20,11,0.7);
            backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);
            border:1px solid var(--border);
            border-radius:50px;
            box-shadow:0 8px 32px rgba(16,185,129,0.08);
        }}
        .logo-icon{{
            width:34px;height:34px;
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            border-radius:50%;display:flex;align-items:center;justify-content:center;
            font-weight:900;font-size:12px;
            animation:glowPulse 2s ease-in-out infinite;
        }}
        .logo-text{{
            font-weight:800;font-size:17px;
            background:linear-gradient(to bottom,#fff,#a7f3d0);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
            margin-left:8px;
        }}
        .tabs{{display:flex;gap:4px;background:var(--glass);border-radius:30px;padding:3px}}
        .tab{{
            background:none;border:none;color:rgba(255,255,255,0.5);
            padding:7px 16px;cursor:pointer;border-radius:25px;
            font-size:13px;font-weight:500;transition:all 0.3s;
        }}
        .tab.active{{background:rgba(16,185,129,0.25);color:#fff}}
        .top-icons{{display:flex;gap:16px}}
        .top-icon{{
            background:none;border:none;color:rgba(255,255,255,0.7);
            font-size:18px;cursor:pointer;transition:all 0.3s;position:relative;
        }}
        .top-icon:hover{{color:var(--accent2)}}
        .notif-badge{{
            position:absolute;top:-6px;right:-6px;
            min-width:18px;height:18px;
            background:#ef4444;
            border-radius:10px;
            border:2px solid var(--bg);
            display:none;
            align-items:center;justify-content:center;
            font-size:9px;font-weight:bold;padding:0 5px;
        }}

        .videos-wrap{{
            height:100vh;overflow-y:scroll;
            scroll-snap-type:y mandatory;
            scrollbar-width:none;-ms-overflow-style:none;
        }}
        .videos-wrap::-webkit-scrollbar{{display:none}}
        
        /* ✨ بطاقة الفيديو - عرض طبيعي مع نص أسفل الفيديو */
        .vid-card{{
            height:100vh;
            scroll-snap-align:start;
            position:relative;
            background:#000;
            display: flex;
            flex-direction: column;
        }}

        /* ✨ حاوية الفيديو - عرض طبيعي بدون تكبير */
        .video-container {{
            position: relative;
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #000;
            overflow: hidden;
        }}

        .vid-card video {{
            width: 100%;
            height: 100%;
            max-height: 100%;
            object-fit: contain;
            opacity:0;
            transition:opacity 0.6s ease;
        }}
        .vid-card.active video {{opacity:1;}}

        /* ✨ منطقة النص أسفل الفيديو */
        .vid-info{{
            position: relative;
            padding: 12px 60px 100px 16px;
            background: linear-gradient(to top, rgba(0,0,0,0.95), rgba(0,0,0,0.7), transparent);
            z-index:20;
            flex-shrink: 0;
            min-height: 120px;
        }}
        .author-row{{display:flex;align-items:center;gap:10px;margin-bottom:6px}}
        .author-avatar{{
            width:40px;height:40px;border-radius:50%;overflow:hidden;
            cursor:pointer;position:relative;
            background:linear-gradient(135deg, #10b981, #34d399, #a7f3d0);
            padding:2px;flex-shrink:0;
            animation:storyRing 3s ease-in-out infinite;
        }}
        @keyframes storyRing{{0%,100%{{box-shadow:0 0 15px rgba(16,185,129,0.4)}}50%{{box-shadow:0 0 25px rgba(52,211,153,0.8)}}}}
        .author-avatar img{{width:100%;height:100%;object-fit:cover;border-radius:50%;border:2px solid var(--bg)}}
        .author-name{{
            font-weight:700;font-size:14px;cursor:pointer;
            display:flex;align-items:center;gap:6px;flex-wrap:wrap;
        }}
        .verified-badge-main{{
            background:linear-gradient(135deg, #10b981, #34d399);
            color:#fff;font-size:9px;padding:1px 4px;border-radius:50%;
            display:inline-flex;align-items:center;justify-content:center;
            width:16px;height:16px;font-weight:bold;
            box-shadow:0 0 12px rgba(167,243,208,0.6);
        }}
        .btn-follow{{
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            padding:4px 12px;border-radius:20px;font-size:10px;
            font-weight:700;border:none;color:#fff;cursor:pointer;
            box-shadow:0 4px 15px rgba(16,185,129,0.4);
            transition:all 0.3s;white-space:nowrap;
        }}
        .btn-follow:hover{{box-shadow:0 8px 25px rgba(16,185,129,0.7);}}
        .caption{{font-size:13px;margin-bottom:4px;line-height:1.4;opacity:0.9}}
        .tag{{color:var(--accent2);cursor:pointer;font-weight:500}}
        .music{{font-size:11px;opacity:0.7;display:flex;align-items:center;gap:6px;cursor:pointer;margin-top:4px}}
        .music-wave{{display:flex;gap:2px;align-items:flex-end;height:14px}}
        .music-wave span{{width:2px;background:var(--accent2);border-radius:1px;animation:musicWave 1s ease-in-out infinite}}
        .music-wave span:nth-child(1){{height:6px;animation-delay:0s}}
        .music-wave span:nth-child(2){{height:12px;animation-delay:0.15s}}
        .music-wave span:nth-child(3){{height:4px;animation-delay:0.3s}}
        .music-wave span:nth-child(4){{height:10px;animation-delay:0.45s}}
        .music-wave span:nth-child(5){{height:3px;animation-delay:0.6s}}
        @keyframes musicWave{{0%,100%{{transform:scaleY(1)}}50%{{transform:scaleY(1.8)}}}}

        /* 💧 Watermark */
        .watermark-overlay{{
            position:absolute;top:20px;right:20px;
            z-index:15;pointer-events:none;
            display:flex;align-items:center;gap:6px;
            opacity:0.5;
        }}
        .watermark-overlay span{{
            font-weight:700;font-size:12px;
            text-shadow:0 2px 8px rgba(0,0,0,0.6);
            color:#fff;
        }}

        .side-btns{{
            position:absolute;right:12px;bottom:140px;
            display:flex;flex-direction:column;gap:20px;z-index:20;
        }}
        .sbtn{{
            display:flex;flex-direction:column;align-items:center;gap:3px;
            background:none;border:none;color:#fff;cursor:pointer;
            font-size:10px;transition:transform 0.15s;
        }}
        .sbtn:active{{transform:scale(0.85)}}
        .sbtn i{{font-size:26px;filter:drop-shadow(0 3px 8px rgba(0,0,0,0.5))}}
        .sbtn.liked i{{color:var(--accent);animation:likePop 0.4s ease}}
        @keyframes likePop{{0%{{transform:scale(1)}}50%{{transform:scale(1.4)}}100%{{transform:scale(1)}}}}
        .sbtn .cnt{{font-weight:700;font-size:10px}}

        /* 📤 Share Panel */
        .share-panel{{
            position:fixed;bottom:0;left:0;right:0;
            background:rgba(5,20,11,0.98);
            backdrop-filter:blur(40px);
            border-top:2px solid var(--accent);
            border-radius:24px 24px 0 0;
            padding:24px 20px 40px;
            z-index:500;
            transform:translateY(100%);
            transition:transform 0.4s cubic-bezier(0.4,0,0.2,1);
        }}
        .share-panel.show{{transform:translateY(0)}}
        .share-panel h3{{font-size:17px;font-weight:700;margin-bottom:20px;text-align:center;color:var(--accent2)}}
        .share-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:20px}}
        .share-item{{
            display:flex;flex-direction:column;align-items:center;gap:8px;
            cursor:pointer;transition:transform 0.2s;
        }}
        .share-item:hover{{transform:scale(1.1)}}
        .share-item .share-icon{{
            width:56px;height:56px;border-radius:16px;
            display:flex;align-items:center;justify-content:center;
            font-size:24px;transition:all 0.3s;
        }}
        .share-item span{{font-size:11px;opacity:0.7}}

        /* 💬 TikTok Style Comments */
        .comments-panel{{
            position:fixed;bottom:0;left:0;right:0;
            background:rgba(5,20,11,0.98);
            backdrop-filter:blur(40px);
            border-top:2px solid var(--accent);
            border-radius:24px 24px 0 0;
            padding:0;
            z-index:500;
            max-height:70vh;
            display:flex;flex-direction:column;
            transform:translateY(100%);
            transition:transform 0.4s cubic-bezier(0.4,0,0.2,1);
        }}
        .comments-panel.show{{transform:translateY(0)}}
        .comments-header{{
            display:flex;justify-content:space-between;align-items:center;
            padding:16px 20px;border-bottom:1px solid var(--border);
            flex-shrink:0;
        }}
        .comments-header h3{{font-size:16px;font-weight:700;display:flex;align-items:center;gap:8px}}
        .comments-list{{flex:1;overflow-y:auto;padding:12px 16px;}}
        .comment-item{{
            display:flex;gap:10px;padding:12px 0;
            border-bottom:1px solid rgba(16,185,129,0.06);
            animation:fadeIn 0.3s ease;
        }}
        .comment-avatar{{
            width:36px;height:36px;border-radius:50%;
            overflow:hidden;flex-shrink:0;
            border:2px solid rgba(16,185,129,0.2);
        }}
        .comment-avatar img{{width:100%;height:100%;object-fit:cover}}
        .comment-body{{flex:1;min-width:0}}
        .comment-user{{font-weight:600;font-size:13px;margin-bottom:2px;display:flex;align-items:center;gap:5px}}
        .comment-text{{font-size:13px;line-height:1.4;word-break:break-word}}
        .comment-actions{{display:flex;gap:16px;margin-top:6px;font-size:11px}}
        .comment-actions span{{cursor:pointer;opacity:0.6;display:flex;align-items:center;gap:4px;transition:opacity 0.2s}}
        .comment-actions span:hover{{opacity:1}}
        .comment-time{{font-size:10px;opacity:0.4}}
        .reply-item{{margin-right:46px;padding:8px 0;border-bottom:1px solid rgba(16,185,129,0.04);display:flex;gap:8px;}}
        .reply-item .comment-avatar{{width:28px;height:28px}}
        .comment-input-row{{
            display:flex;gap:8px;padding:12px 16px;
            border-top:1px solid var(--border);
            background:rgba(5,20,11,0.95);
            flex-shrink:0;
        }}
        .comment-input-row input{{
            flex:1;padding:12px 16px;border-radius:30px;
            background:rgba(16,185,129,0.04);border:1px solid var(--border);
            color:#fff;font-size:13px;outline:none;
        }}
        .comment-input-row button{{
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            border:none;color:#fff;padding:10px 18px;border-radius:30px;
            font-weight:700;cursor:pointer;white-space:nowrap;font-size:13px;
        }}

        /* 💎 Fullscreen Video Player */
        .fullscreen-player {{
            position:fixed;top:0;left:0;width:100vw;height:100vh;
            background:#000;z-index:9999;display:flex;align-items:center;
            justify-content:center;opacity:0;pointer-events:none;
            transition:opacity 0.3s ease;flex-direction:column;
        }}
        .fullscreen-player.active {{opacity:1;pointer-events:auto}}
        .fullscreen-player video {{max-width:100%;max-height:85vh;object-fit:contain;cursor:pointer}}
        .close-player{{
            position:absolute;top:20px;left:20px;
            background:rgba(0,0,0,0.5);backdrop-filter:blur(10px);
            border:1px solid rgba(16,185,129,0.4);color:#fff;
            width:44px;height:44px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            cursor:pointer;font-size:20px;z-index:10001;transition:all 0.3s;
        }}
        .close-player:hover{{background:rgba(16,185,129,0.3);box-shadow:0 0 20px rgba(16,185,129,0.5)}}

        /* 📱 FLOATING BOTTOM NAV */
        .nav-bottom{{
            position:fixed;bottom:12px;left:12px;right:12px;
            display:flex;justify-content:space-around;align-items:center;
            padding:8px 0;
            background:rgba(5,20,11,0.8);
            backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);
            z-index:100;
            border:1px solid var(--border);
            border-radius:40px;
            box-shadow:0 -8px 32px rgba(16,185,129,0.06);
        }}
        .nav-item{{
            display:flex;flex-direction:column;align-items:center;gap:3px;
            background:none;border:none;color:rgba(255,255,255,0.5);
            font-size:10px;cursor:pointer;transition:all 0.3s;text-decoration:none;
        }}
        .nav-item i{{font-size:22px}}
        .nav-item.active{{color:var(--accent2)}}
        .btn-add{{
            width:48px;height:48px;
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            border-radius:50%;display:flex;align-items:center;justify-content:center;
            margin-top:-30px;cursor:pointer;
            box-shadow:0 10px 30px rgba(16,185,129,0.6),0 0 40px rgba(16,185,129,0.2);
            border:none;color:#fff;font-size:20px;
            z-index:101;transition:all 0.3s;text-decoration:none;
        }}
        .btn-add:hover{{transform:scale(1.1);box-shadow:0 15px 40px rgba(16,185,129,0.8)}}

        /* ✨ RESPONSIVE: عرض أفقي للشاشات الكبيرة */
        @media screen and (min-width: 800px) {{
            .vid-card {{
                flex-direction: row;
            }}
            .video-container {{
                flex: 1;
            }}
            .vid-card video {{
                max-height: 100vh;
            }}
            .vid-info {{
                width: 350px;
                padding: 20px;
                background: linear-gradient(to left, rgba(0,0,0,0.9), rgba(0,0,0,0.3));
                display: flex;
                flex-direction: column;
                justify-content: flex-end;
            }}
            .side-btns {{
                position: static;
                flex-direction: row;
                gap: 25px;
                justify-content: center;
                margin-top: 20px;
            }}
            .side-btns .sbtn i {{
                font-size: 24px;
            }}
        }}

        @media screen and (orientation: landscape) and (max-width: 800px) {{
            .vid-card {{
                flex-direction: row;
            }}
            .video-container {{
                flex: 1;
            }}
            .vid-info {{
                position: absolute;
                bottom: 0;
                left: 0;
                right: 70px;
                background: linear-gradient(to top, rgba(0,0,0,0.9), transparent);
                padding: 40px 16px 16px;
                min-height: auto;
            }}
            .side-btns {{
                position: absolute;
                right: 10px;
                bottom: 20px;
                flex-direction: column;
            }}
        }}
    </style>
</head>
<body>

<div id="loaderScreen">
    <div class="spinner-big"></div>
    <p style="color:rgba(255,255,255,0.5);font-size:15px">💎 MNAENCA جاري التحميل...</p>
</div>

<div id="mainApp">
    <div class="desktop-sidebar">
        <div class="sidebar-logo"><div class="logo-icon">💎</div> MNAENCA</div>
        <div class="sidebar-nav-item active" onclick="window.location.href='index.html'"><i class="fas fa-home"></i> الرئيسية</div>
        <div class="sidebar-nav-item" onclick="openSearch()"><i class="fas fa-search"></i> بحث</div>
        <div class="sidebar-nav-item" onclick="openNotifs()"><i class="fas fa-bell"></i> الإشعارات</div>
        <div class="sidebar-nav-item" onclick="window.location.href='chat.html'"><i class="fas fa-envelope"></i> الرسائل</div>
        <div class="sidebar-nav-item" onclick="window.location.href='profile.html'"><i class="fas fa-user"></i> ملفي</div>
        <div style="margin-top: auto; border-top: 1px solid var(--border); padding-top: 20px;">
            <div class="sidebar-nav-item" onclick="window.location.href='upload.html'"><i class="fas fa-plus-circle" style="color: var(--accent);"></i> رفع فيديو</div>
            <div class="sidebar-nav-item" onclick="auth.signOut();window.location.href='auth.html'"><i class="fas fa-sign-out-alt"></i> خروج</div>
        </div>
    </div>

    <div style="flex: 1; display: flex; flex-direction: column; height: 100vh; position: relative; background: #000;">
        <div class="topbar">
            <div style="display:flex;align-items:center">
                <div class="logo-icon">💎</div>
                <span class="logo-text">MNAENCA</span>
            </div>
            <div class="tabs">
                <button class="tab" onclick="switchFeed('following')">متابَعين</button>
                <button class="tab active" onclick="switchFeed('forYou')">لك</button>
            </div>
            <div class="top-icons">
                <i class="fas fa-search top-icon" onclick="openSearch()"></i>
                <i class="fas fa-bell top-icon" onclick="openNotifs()"><span class="notif-badge" id="notifBadge"></span></i>
            </div>
        </div>

        <div class="videos-wrap" id="videosWrap">
            <div style="display:flex;align-items:center;justify-content:center;height:100vh;color:rgba(255,255,255,0.5);flex-direction:column;gap:12px">
                <i class="fas fa-video" style="font-size:48px;opacity:0.3;color:#10b981"></i>
                <p>لا توجد فيديوهات بعد</p>
                <p style="font-size:12px;opacity:0.5">ارفع أول فيديو! 💎</p>
            </div>
        </div>

        <div class="fullscreen-player" id="fullscreenPlayer" onclick="if(event.target===this)closePlayer()">
            <button class="close-player" onclick="closePlayer()"><i class="fas fa-times"></i></button>
            <video id="fullscreenVideo" controls playsinline></video>
        </div>

        <div class="share-panel" id="sharePanel">
            <h3><i class="fas fa-share-alt"></i> مشاركة</h3>
            <div class="share-grid">
                <div class="share-item" onclick="shareTo('whatsapp')"><div class="share-icon" style="background:rgba(37,211,102,0.15);color:#25D366"><i class="fab fa-whatsapp"></i></div><span>WhatsApp</span></div>
                <div class="share-item" onclick="shareTo('telegram')"><div class="share-icon" style="background:rgba(0,136,204,0.15);color:#0088cc"><i class="fab fa-telegram"></i></div><span>Telegram</span></div>
                <div class="share-item" onclick="shareTo('facebook')"><div class="share-icon" style="background:rgba(24,119,242,0.15);color:#1877F2"><i class="fab fa-facebook"></i></div><span>Facebook</span></div>
                <div class="share-item" onclick="shareTo('twitter')"><div class="share-icon" style="background:rgba(29,161,242,0.15);color:#1DA1F2"><i class="fab fa-twitter"></i></div><span>X</span></div>
                <div class="share-item" onclick="shareTo('copy')"><div class="share-icon" style="background:rgba(16,185,129,0.15);color:#10b981"><i class="fas fa-link"></i></div><span>نسخ الرابط</span></div>
            </div>
        </div>
        <div class="overlay" id="shareOverlay" style="display:none;z-index:499" onclick="closeSharePanel()"></div>

        <div class="comments-panel" id="commentsPanel">
            <div class="comments-header">
                <h3><i class="fas fa-comments" style="color:var(--accent)"></i> التعليقات <span id="commentsCount" style="font-size:13px;opacity:0.5"></span></h3>
                <button class="btn-close-overlay" onclick="closeCommentsPanel()"><i class="fas fa-times"></i></button>
            </div>
            <div class="comments-list" id="commentsList"></div>
            <div class="comment-input-row">
                <input type="text" id="commentInput" placeholder="أضف تعليقاً..." onkeydown="if(event.key==='Enter')addComment()">
                <button onclick="addComment()"><i class="fas fa-paper-plane"></i> نشر</button>
            </div>
        </div>
        <div class="overlay" id="commentsOverlay" style="display:none;z-index:499" onclick="closeCommentsPanel()"></div>

        <div class="nav-bottom">
            <button class="nav-item active"><i class="fas fa-home"></i><span>الرئيسية</span></button>
            <button class="nav-item" onclick="openSearch()"><i class="fas fa-search"></i><span>بحث</span></button>
            <a href="upload.html" class="btn-add"><i class="fas fa-plus"></i></a>
            <a href="chat.html" class="nav-item"><i class="fas fa-envelope"></i><span>رسائل</span></a>
            <a href="profile.html" class="nav-item"><i class="fas fa-user"></i><span>ملفي</span></a>
        </div>

        <div class="toast-msg" id="toast">✅ تم النسخ</div>
    </div>
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
    let currentCommentVideoId = null;
    let replyingTo = null;

    function openPlayer(url, title) {{
        const player = document.getElementById('fullscreenPlayer');
        const video = document.getElementById('fullscreenVideo');
        player.classList.add('active');
        video.src = url;
        video.load();
        video.play();
    }}
    window.openPlayer = openPlayer;

    function closePlayer() {{
        const player = document.getElementById('fullscreenPlayer');
        const video = document.getElementById('fullscreenVideo');
        video.pause();video.src='';player.classList.remove('active');
    }}

    function openSharePanel(url) {{
        currentShareUrl = url;
        document.getElementById('sharePanel').classList.add('show');
        document.getElementById('shareOverlay').style.display = 'block';
    }}
    function closeSharePanel() {{
        document.getElementById('sharePanel').classList.remove('show');
        document.getElementById('shareOverlay').style.display = 'none';
    }}
    function shareTo(platform) {{
        const url = encodeURIComponent(currentShareUrl);
        const text = encodeURIComponent('شاهد هذا الفيديو على MNAENCA 💎');
        let shareUrl = '';
        switch(platform) {{
            case 'whatsapp': shareUrl = 'https://wa.me/?text=' + text + '%20' + url; break;
            case 'telegram': shareUrl = 'https://t.me/share/url?url=' + url + '&text=' + text; break;
            case 'facebook': shareUrl = 'https://www.facebook.com/sharer/sharer.php?u=' + url; break;
            case 'twitter': shareUrl = 'https://twitter.com/intent/tweet?url=' + url + '&text=' + text; break;
            case 'copy':
                navigator.clipboard.writeText(currentShareUrl).then(() => {{showToast('✅ تم نسخ الرابط');closeSharePanel();}});
                return;
        }}
        if(shareUrl) window.open(shareUrl, '_blank');
        closeSharePanel();
    }}

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
                    return `<div class="reply-item"><div class="comment-avatar"><img src="${{rAvatar}}" alt=""></div><div style="flex:1;min-width:0"><div class="comment-user" style="font-size:12px">@${{rUser.username}} <span class="comment-time">${{formatTimeAgo(r.timestamp)}}</span></div><div class="comment-text" style="font-size:12px">${{r.text}}</div></div></div>`;
                }}).join('');
            }}
            return `<div class="comment-item"><div class="comment-avatar"><img src="${{avatar}}" alt=""></div><div class="comment-body"><div class="comment-user">@${{user.username}} ${{user.isVerified ? '<span class="verified-badge-main"><i class="fas fa-check"></i></span>' : ''}} <span class="comment-time">${{formatTimeAgo(c.timestamp)}}</span></div><div class="comment-text">${{c.text}}</div><div class="comment-actions"><span onclick="replyToComment('${{c.id}}', '@${{user.username}}')"><i class="fas fa-reply"></i> رد</span><span>${{c.likes || 0}} <i class="fas fa-heart"></i></span></div>${{repliesHTML}}</div></div>`;
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
        const commentData = {{userId: currentUser.uid, username: currentUserData?.username || 'مستخدم', text: text, timestamp: Date.now(), likes: 0}};
        if(replyingTo) {{
            await db.ref('videos/' + currentCommentVideoId + '/comments/' + replyingTo + '/replies').push(commentData);
            replyingTo = null;
            input.placeholder = 'أضف تعليقاً...';
        }} else {{
            await db.ref('videos/' + currentCommentVideoId + '/comments').push(commentData);
        }}
        input.value = '';
        await loadComments();
    }}
    window.addComment = addComment;

    auth.onAuthStateChanged(async (user) => {{
        if(!user) {{ window.location.replace('auth.html'); return; }}
        currentUser = user;
        try {{
            const snap = await db.ref('users/' + user.uid).get();
            if(snap.exists()) currentUserData = {{uid: user.uid, ...snap.val()}};
        }} catch(e) {{}}

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
                badge.style.display = count > 0 ? 'flex' : 'none';
                if(count > 0) badge.innerText = count;
            }}
        }});

        db.ref('presence/' + user.uid).set(true);
        db.ref('presence/' + user.uid).onDisconnect().remove();
        db.ref('users/' + user.uid + '/lastSeen').set(Date.now());
        setInterval(() => {{ db.ref('users/' + user.uid + '/lastSeen').set(Date.now()); }}, 60000);

        document.getElementById('loaderScreen').style.display = 'none';
        document.getElementById('mainApp').style.display = 'flex';
    }});

    function renderVideos() {{
        const container = document.getElementById('videosWrap');
        if(!container) return;
        let filtered = currentFeed === 'forYou' ? allVideos : allVideos.filter(v => currentUserData?.following?.[v.sender]);
        if(!filtered.length) {{
            container.innerHTML = `<div style="display:flex;align-items:center;justify-content:center;height:100vh;color:rgba(255,255,255,0.5);flex-direction:column;gap:12px"><i class="fas fa-video" style="font-size:48px;opacity:0.3;color:#10b981"></i><p>${{currentFeed === 'forYou' ? 'لا توجد فيديوهات بعد' : 'تابع مستخدمين لرؤية فيديوهاتهم'}}</p></div>`;
            return;
        }}
        container.innerHTML = '';
        filtered.forEach(video => {{
            const isLiked = video.likedBy && video.likedBy[currentUser?.uid];
            const user = allUsers[video.sender] || {{username: video.senderName || 'مستخدم'}};
            const isFollowing = currentUserData?.following && currentUserData.following[video.sender];
            const commentsCount = video.comments ? Object.keys(video.comments).length : 0;
            const caption = (video.description || '').replace(/#(\\w+)/g, '<span class="tag">#$1</span>');
            const avatarUrl = user.avatarUrl || (DICEBEAR_URL + '?seed=' + video.sender);
            const verifiedBadgeHtml = user.isVerified ? '<span class="verified-badge-main"><i class="fas fa-check"></i></span>' : '';
            const musicHtml = video.music ? `<div class="music-wave">${{[1,2,3,4,5].map(()=>'<span></span>').join('')}}</div> ${{video.music}}` : 'Original Sound';

            const div = document.createElement('div');
            div.className = 'vid-card';
            div.innerHTML = `
                <div class="watermark-overlay"><span>💎 MNAENCA</span></div>
                <div class="video-container">
                    <video loop playsinline muted data-src="${{video.url}}" poster="${{video.thumbnail || ''}}"></video>
                </div>
                <div class="vid-info">
                    <div class="author-row">
                        <div class="author-avatar" onclick="openUserProfile('${{video.sender}}')"><img src="${{avatarUrl}}" alt="avatar"></div>
                        <div class="author-name"><span onclick="openUserProfile('${{video.sender}}')">@${{user.username}}</span>${{verifiedBadgeHtml}}${{currentUser?.uid !== video.sender ? `<button class="btn-follow" onclick="event.stopPropagation();toggleFollow('${{video.sender}}', this)">${{isFollowing ? '<i class="fas fa-user-check"></i> متابع' : '<i class="fas fa-user-plus"></i> متابعة'}}</button>` : ''}}</div>
                    </div>
                    <div class="caption">${{caption}}</div>
                    <div class="music">${{musicHtml}}</div>
                </div>
                <div class="side-btns">
                    <button class="sbtn" onclick="toggleMute()"><i class="fas ${{isMuted ? 'fa-volume-mute' : 'fa-volume-up'}}"></i></button>
                    <button class="sbtn like-btn ${{isLiked ? 'liked' : ''}}" onclick="toggleLike('${{video.id}}', this)"><i class="fas fa-heart"></i><span class="cnt">${{video.likes || 0}}</span></button>
                    <button class="sbtn" onclick="openCommentsPanel('${{video.id}}')"><i class="fas fa-comment"></i><span class="cnt">${{commentsCount}}</span></button>
                    <button class="sbtn" onclick="openPlayer('${{video.url}}', 'video.mp4')"><i class="fas fa-expand"></i></button>
                    <button class="sbtn" onclick="openSharePanel('${{video.url}}')"><i class="fas fa-share"></i></button>
                </div>`;
            const videoEl = div.querySelector('video');
            videoEl.addEventListener('dblclick', e => {{
                e.stopPropagation();
                const likeBtn = div.querySelector('.like-btn');
                if(likeBtn) toggleLike(video.id, likeBtn);
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

    function toggleMute() {{ isMuted = !isMuted; document.querySelectorAll('video').forEach(v => v.muted = isMuted); }}
    function switchFeed(feed) {{ currentFeed = feed; document.querySelectorAll('.tab').forEach(t => t.classList.remove('active')); event.target.classList.add('active'); renderVideos(); }}

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
        const countSpan = btn.querySelector('.cnt');
        if(countSpan) countSpan.innerText = likes;
    }}

    async function toggleFollow(userId, btn) {{
        if(!currentUser || currentUser.uid === userId) return;
        const userRef = db.ref('users/' + currentUser.uid + '/following/' + userId);
        const targetRef = db.ref('users/' + userId + '/followers/' + currentUser.uid);
        const snap = await userRef.get();
        if(snap.exists()) {{ await userRef.remove(); await targetRef.remove(); btn.innerHTML = '<i class="fas fa-user-plus"></i> متابعة'; }}
        else {{ await userRef.set(true); await targetRef.set(true); btn.innerHTML = '<i class="fas fa-user-check"></i> متابع'; }}
    }}

    async function openNotifs() {{
        const snap = await db.ref('notifications/' + currentUser.uid).once('value');
        const ns = snap.val() || {{}};
        const items = Object.values(ns).reverse();
        let notifHTML = '';
        if(!items.length) {{
            notifHTML = '<div style="text-align:center;opacity:0.5;padding:40px"><i class="fas fa-bell" style="font-size:48px;color:#10b981;margin-bottom:12px;display:block"></i><p>لا توجد إشعارات</p></div>';
        }} else {{
            items.forEach(n => {{
                notifHTML += `<div style="display:flex;gap:12px;padding:14px;border-bottom:1px solid rgba(16,185,129,0.1);align-items:center;animation:fadeIn 0.3s ease"><div style="width:40px;height:40px;border-radius:50%;background:rgba(16,185,129,0.15);display:flex;align-items:center;justify-content:center;font-size:18px;color:#10b981"><i class="fas fa-bell"></i></div><div><div style="font-weight:600">${{n.from || 'مستخدم'}}</div><div style="font-size:12px;opacity:0.6;margin-top:2px">${{n.msg || ''}}</div><div style="font-size:10px;opacity:0.3;margin-top:4px">${{new Date(n.timestamp).toLocaleString('ar-SA')}}</div></div></div>`;
            }});
        }}
        await db.ref('notifications/' + currentUser.uid).remove();
        const badge = document.getElementById('notifBadge');
        if(badge) badge.style.display = 'none';
        showOverlay('🔔 الإشعارات', notifHTML);
    }}

    function openSearch() {{
        showOverlay('🔍 بحث', `<input type="text" id="searchQ" onkeyup="doSearch()" placeholder="ابحث عن مستخدمين، فيديوهات..." style="width:100%;padding:14px;border-radius:30px;background:rgba(16,185,129,0.04);border:1px solid rgba(16,185,129,0.15);color:#fff;font-size:14px;outline:none;margin-bottom:16px"><div id="searchR"></div>`);
        window.doSearch = function() {{
            const query = document.getElementById('searchQ').value.toLowerCase();
            const resultsDiv = document.getElementById('searchR');
            if(!query) {{ resultsDiv.innerHTML = ''; return; }}
            const users = Object.values(allUsers).filter(u => u.username?.toLowerCase().includes(query));
            const vids = allVideos.filter(v => (v.description || '').toLowerCase().includes(query));
            resultsDiv.innerHTML = `${{users.length ? `<div style="margin-bottom:16px"><h4 style="font-size:12px;opacity:0.5;margin-bottom:8px"><i class="fas fa-users"></i> مستخدمين</h4>${{users.map(u => `<div onclick="openUserProfile('${{u.uid || Object.keys(allUsers).find(k=>allUsers[k]===u)}}')" style="display:flex;align-items:center;gap:10px;padding:10px;cursor:pointer;border-bottom:1px solid rgba(16,185,129,0.1)"><img src="${{u.avatarUrl || (DICEBEAR_URL + '?seed=' + (u.uid || u.username))}}" style="width:40px;height:40px;border-radius:50%"><div>@${{u.username}} ${{u.isVerified ? '<span class="verified-badge-main"><i class="fas fa-check"></i></span>' : ''}}</div></div>`).join('')}}</div>` : ''}}${{vids.length ? `<div><h4 style="font-size:12px;opacity:0.5;margin-bottom:8px"><i class="fas fa-video"></i> فيديوهات</h4>${{vids.map(v => `<div onclick="openPlayer('${{v.url}}', 'video.mp4')" style="display:flex;align-items:center;gap:10px;padding:10px;cursor:pointer;border-bottom:1px solid rgba(16,185,129,0.1)"><i class="fas fa-play-circle" style="color:#10b981;font-size:20px"></i><span style="font-size:13px">${{(v.description || 'فيديو').substring(0, 40)}}</span></div>`).join('')}}</div>` : ''}}${{!users.length && !vids.length ? '<div style="text-align:center;opacity:0.5;padding:30px">لا توجد نتائج</div>' : ''}}`;
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
    window.openSharePanel = openSharePanel;
    window.closeSharePanel = closeSharePanel;
    window.shareTo = shareTo;
    window.openCommentsPanel = openCommentsPanel;
    window.closeCommentsPanel = closeCommentsPanel;
    window.openUserProfile = openUserProfile;
    window.toggleFollow = toggleFollow;
    window.toggleLike = toggleLike;

    console.log('💎 MNAENCA Index Ready ✨');
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 💎 4. profile.html - ملف شخصي محترف 2.0 (مطور بالكامل)
# ═══════════════════════════════════════════════════════════

def build_profile():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💎 MNAENCA | ملف شخصي</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{min-height:100vh;overflow-y:auto;overflow-x:hidden;}}
        .cover-section{{position:relative;width:100%;height:260px;overflow:hidden;cursor:pointer}}
        .cover-img{{width:100%;height:130%;object-fit:cover;transition:transform 0.1s linear;transform:translateY(0)}}
        .cover-gradient{{position:absolute;inset:0;background:linear-gradient(to bottom,transparent 30%,rgba(5,20,11,0.4) 60%,rgba(5,20,11,0.95) 100%);pointer-events:none;z-index:1}}
        .cover-glow{{position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(16,185,129,0.15) 0%,transparent 70%);pointer-events:none;z-index:2}}
        .cover-edit-btn{{position:absolute;top:12px;left:12px;background:rgba(0,0,0,0.5);backdrop-filter:blur(15px);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:5;border:1px solid rgba(16,185,129,0.3);color:#fff;font-size:14px;transition:all 0.3s;box-shadow:0 4px 15px rgba(0,0,0,0.3)}}
        .cover-edit-btn:hover{{background:rgba(16,185,129,0.4);box-shadow:0 0 20px rgba(16,185,129,0.5)}}
        .btn-back{{position:fixed;top:20px;right:20px;background:rgba(0,0,0,0.5);backdrop-filter:blur(15px);width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:50;border:1px solid var(--border);color:#fff;font-size:16px;transition:all 0.3s}}
        .btn-back:hover{{background:rgba(16,185,129,0.3);box-shadow:0 0 20px rgba(16,185,129,0.4)}}
        .avatar-wrap{{position:relative;z-index:2;margin-top:-60px;display:flex;justify-content:center}}
        .avatar-lg{{width:120px;height:120px;border-radius:50%;overflow:hidden;cursor:pointer;background:linear-gradient(135deg,#10b981,#34d399,#a7f3d0);padding:3px;box-shadow:0 0 30px rgba(16,185,129,0.4),0 0 60px rgba(16,185,129,0.1);animation:avatarGlow 3s ease-in-out infinite}}
        @keyframes avatarGlow{{0%,100%{{box-shadow:0 0 30px rgba(16,185,129,0.4),0 0 60px rgba(16,185,129,0.1)}}50%{{box-shadow:0 0 40px rgba(52,211,153,0.7),0 0 80px rgba(16,185,129,0.3)}}}}
        .avatar-lg img{{width:100%;height:100%;object-fit:cover;border-radius:50%;border:3px solid var(--bg)}}
        .avatar-edit-btn{{position:absolute;bottom:5px;right:5px;width:30px;height:30px;background:var(--accent);border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;border:2px solid var(--bg);color:#fff;font-size:12px;box-shadow:0 0 15px rgba(16,185,129,0.5)}}
        .online-dot{{position:absolute;top:10px;right:10px;width:18px;height:18px;background:#22c55e;border-radius:50%;border:3px solid var(--bg);z-index:3;box-shadow:0 0 10px rgba(34,197,94,0.6)}}
        .profile-info{{padding:20px 20px 10px;text-align:center}}
        .username{{font-size:22px;font-weight:800;margin-bottom:4px;display:flex;align-items:center;justify-content:center;gap:8px}}
        .bio-text{{font-size:13px;opacity:0.7;margin-bottom:8px;max-width:320px;margin-left:auto;margin-right:auto;line-height:1.5}}
        .contact-info{{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-bottom:8px;font-size:12px}}
        .contact-info a{{color:var(--accent2);text-decoration:none;display:flex;align-items:center;gap:5px;background:var(--card);padding:6px 14px;border-radius:20px;border:1px solid var(--border);transition:all 0.3s}}
        .contact-info a:hover{{background:rgba(16,185,129,0.15);box-shadow:0 0 15px rgba(16,185,129,0.2)}}
        .last-seen{{font-size:11px;opacity:0.5;display:flex;align-items:center;justify-content:center;gap:5px;margin-top:6px}}
        
        /* ✨ إحصائيات متحركة */
        .stats-row{{
            display:flex;justify-content:center;gap:20px;
            margin:15px 20px;padding:18px;
            background:rgba(16,185,129,0.04);
            backdrop-filter:blur(20px);border-radius:20px;
            border:1px solid var(--border);
            box-shadow:0 8px 32px rgba(0,0,0,0.2);
        }}
        .stat-item{{
            text-align:center;cursor:pointer;transition:all 0.3s;
            padding:8px 16px;border-radius:16px;
            position:relative;flex:1;
        }}
        .stat-item:hover{{
            background:rgba(16,185,129,0.08);
            transform:translateY(-3px);
            box-shadow:0 8px 25px rgba(16,185,129,0.15);
        }}
        .stat-item:active{{transform:scale(0.95)}}
        .stat-val{{font-size:22px;font-weight:800;color:var(--accent2);transition:all 0.3s}}
        .stat-item:hover .stat-val{{color:#fff;text-shadow:0 0 20px rgba(52,211,153,0.8)}}
        .stat-lbl{{font-size:11px;opacity:0.6;margin-top:4px;font-weight:500}}
        .stat-icon-mini{{font-size:16px;margin-bottom:4px;opacity:0.5}}
        .stat-item:hover .stat-icon-mini{{opacity:1}}
        
        .action-btns{{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:0 20px 20px}}
        .btn{{background:rgba(16,185,129,0.06);border:1px solid var(--border);padding:10px 20px;border-radius:25px;color:#fff;cursor:pointer;font-size:13px;transition:all 0.3s;display:flex;align-items:center;gap:6px;backdrop-filter:blur(10px)}}
        .btn:hover{{background:rgba(16,185,129,0.15);border-color:var(--accent);box-shadow:0 0 20px rgba(16,185,129,0.2)}}
        .btn-primary{{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;font-weight:700;color:#fff;box-shadow:0 8px 25px rgba(16,185,129,0.4)}}
        .btn-primary:hover{{transform:translateY(-2px);box-shadow:0 12px 35px rgba(16,185,129,0.6)}}
        .btn-outline{{background:transparent;border:2px solid var(--accent);color:var(--accent2);font-weight:600}}
        
        /* 🎬 قسم الفيديوهات */
        .section-header{{
            display:flex;justify-content:space-between;align-items:center;
            padding:20px 20px 12px;
        }}
        .section-title{{font-size:16px;font-weight:700;display:flex;align-items:center;gap:8px}}
        .btn-see-all{{
            background:rgba(16,185,129,0.1);border:1px solid var(--border);
            color:var(--accent2);padding:6px 14px;border-radius:20px;
            font-size:12px;cursor:pointer;transition:all 0.3s;
            display:flex;align-items:center;gap:6px;
        }}
        .btn-see-all:hover{{background:rgba(16,185,129,0.2);box-shadow:0 0 15px rgba(16,185,129,0.2)}}
        
        .videos-grid{{
            display:grid;grid-template-columns:repeat(3,1fr);
            gap:3px;padding:0 8px 20px;
        }}
        .video-grid-item{{
            aspect-ratio:9/16;position:relative;overflow:hidden;
            cursor:pointer;background:#000;border-radius:4px;
            transition:all 0.3s;
        }}
        .video-grid-item:hover{{transform:scale(1.02);z-index:2;box-shadow:0 8px 30px rgba(0,0,0,0.5)}}
        .video-grid-item img{{width:100%;height:100%;object-fit:cover;transition:transform 0.3s}}
        .video-grid-item:hover img{{transform:scale(1.1)}}
        .video-grid-item .grid-overlay{{
            position:absolute;inset:0;
            background:linear-gradient(to top,rgba(0,0,0,0.7) 0%,transparent 50%);
            opacity:0;transition:opacity 0.3s;
        }}
        .video-grid-item:hover .grid-overlay{{opacity:1}}
        .video-grid-item .grid-play-icon{{
            position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
            font-size:28px;color:#fff;z-index:1;opacity:0;
            transition:all 0.3s;
        }}
        .video-grid-item:hover .grid-play-icon{{opacity:1;transform:translate(-50%,-50%) scale(1.2)}}
        .video-grid-item .grid-info{{
            position:absolute;bottom:8px;left:6px;right:6px;
            display:flex;justify-content:space-between;
            z-index:1;opacity:0;transition:opacity 0.3s;
        }}
        .video-grid-item:hover .grid-info{{opacity:1}}
        .grid-info span{{
            font-size:10px;color:#fff;display:flex;align-items:center;
            gap:3px;background:rgba(0,0,0,0.5);padding:3px 8px;
            border-radius:10px;
        }}
        
        /* 📝 قسم المنشورات */
        .posts-section{{padding:0 16px 20px;margin-bottom:20px}}
        .post-card{{
            background:rgba(16,185,129,0.04);border:1px solid var(--border);
            border-radius:20px;padding:18px;margin-bottom:12px;
            backdrop-filter:blur(10px);transition:all 0.3s;
            animation:fadeIn 0.4s ease;
        }}
        .post-card:hover{{border-color:rgba(16,185,129,0.3);box-shadow:0 8px 30px rgba(16,185,129,0.08)}}
        .post-header{{display:flex;align-items:center;gap:10px;margin-bottom:10px}}
        .post-avatar{{width:40px;height:40px;border-radius:50%;overflow:hidden;border:2px solid rgba(16,185,129,0.2)}}
        .post-avatar img{{width:100%;height:100%;object-fit:cover}}
        .post-user-info h4{{font-size:14px;font-weight:600}}
        .post-user-info span{{font-size:10px;opacity:0.5}}
        .post-content{{font-size:14px;line-height:1.6;margin-bottom:12px}}
        .post-actions{{display:flex;gap:20px;font-size:12px}}
        .post-actions span{{cursor:pointer;opacity:0.5;display:flex;align-items:center;gap:5px;transition:all 0.2s}}
        .post-actions span:hover{{opacity:1;color:var(--accent2)}}
        
        .empty-state{{text-align:center;opacity:0.5;padding:40px 20px}}
        .empty-state i{{font-size:48px;color:var(--accent);margin-bottom:12px;display:block}}
        .badge-verified{{background:linear-gradient(135deg,#10b981,#34d399);color:#fff;font-size:12px;padding:3px 6px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;font-weight:bold;box-shadow:0 0 15px rgba(167,243,208,0.6);animation:verifyGlow 2s ease-in-out infinite}}
        @keyframes verifyGlow{{0%,100%{{box-shadow:0 0 15px rgba(167,243,208,0.6)}}50%{{box-shadow:0 0 25px rgba(167,243,208,0.9)}}}}
        
        /* ✨ Modal للمتابعين */
        .modal-overlay{{
            position:fixed;inset:0;background:rgba(0,0,0,0.8);
            backdrop-filter:blur(20px);z-index:500;
            display:flex;align-items:flex-end;justify-content:center;
            animation:fadeIn 0.3s ease;
        }}
        .modal-sheet{{
            width:100%;max-width:500px;max-height:80vh;
            background:rgba(5,20,11,0.98);
            border:1px solid var(--border);
            border-radius:28px 28px 0 0;
            overflow:hidden;display:flex;flex-direction:column;
            box-shadow:0 -20px 60px rgba(0,0,0,0.5);
            animation:slideUp 0.4s cubic-bezier(0.4,0,0.2,1);
        }}
        .modal-header{{
            display:flex;justify-content:space-between;align-items:center;
            padding:18px 20px;border-bottom:1px solid var(--border);
            flex-shrink:0;
        }}
        .modal-header h3{{font-size:17px;font-weight:700;color:var(--accent2)}}
        .modal-body{{flex:1;overflow-y:auto;padding:10px 0}}
        .user-list-item{{
            display:flex;align-items:center;gap:12px;
            padding:12px 20px;cursor:pointer;
            transition:background 0.2s;animation:fadeIn 0.3s ease;
        }}
        .user-list-item:hover{{background:rgba(16,185,129,0.04)}}
        .user-list-avatar{{width:48px;height:48px;border-radius:50%;overflow:hidden;border:2px solid rgba(16,185,129,0.2);flex-shrink:0}}
        .user-list-avatar img{{width:100%;height:100%;object-fit:cover}}
        .user-list-info{{flex:1;min-width:0}}
        .user-list-info h4{{font-size:14px;font-weight:600;display:flex;align-items:center;gap:6px}}
        .user-list-info p{{font-size:11px;opacity:0.5;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
        .btn-follow-sm{{
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            border:none;color:#fff;padding:7px 16px;border-radius:20px;
            font-size:11px;font-weight:600;cursor:pointer;
            transition:all 0.3s;flex-shrink:0;
            box-shadow:0 4px 12px rgba(16,185,129,0.3);
        }}
        .btn-follow-sm:hover{{box-shadow:0 6px 18px rgba(16,185,129,0.5)}}
        .btn-follow-sm.following{{background:rgba(16,185,129,0.1);border:1px solid var(--border);color:#fff;box-shadow:none}}
        
        /* 🎬 Modal مشغل الفيديو */
        .video-modal{{
            position:fixed;inset:0;background:#000;
            z-index:600;display:flex;align-items:center;
            justify-content:center;
            animation:fadeIn 0.3s ease;
        }}
        .video-modal video{{max-width:100%;max-height:90vh;object-fit:contain}}
        .video-modal-close{{
            position:absolute;top:16px;left:16px;
            background:rgba(0,0,0,0.5);backdrop-filter:blur(10px);
            border:1px solid var(--border);color:#fff;
            width:40px;height:40px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            cursor:pointer;font-size:18px;z-index:5;
        }}
        
        /* Edit Panel */
        .edit-panel{{position:fixed;bottom:0;left:0;right:0;background:rgba(5,20,11,0.98);backdrop-filter:blur(40px);border-top:2px solid var(--accent);border-radius:24px 24px 0 0;padding:24px 20px 40px;z-index:200;transform:translateY(100%);transition:transform 0.4s cubic-bezier(0.4,0,0.2,1);max-height:80vh;overflow-y:auto;box-shadow:0 -10px 40px rgba(16,185,129,0.1)}}
        .edit-panel.show{{transform:translateY(0)}}
        .edit-panel h3{{font-size:18px;font-weight:700;margin-bottom:20px;color:var(--accent2);text-align:center}}
        .edit-panel label{{display:block;font-size:12px;opacity:0.7;margin-bottom:6px;margin-top:14px}}
        .edit-panel input,.edit-panel textarea{{width:100%;padding:12px 16px;border-radius:14px;background:var(--card);border:1px solid var(--border);color:#fff;font-size:14px;outline:none;resize:none;font-family:'Segoe UI',sans-serif;transition:border 0.3s}}
        .edit-panel input:focus,.edit-panel textarea:focus{{border-color:var(--accent);box-shadow:0 0 15px rgba(16,185,129,0.15)}}
        .edit-actions{{display:flex;gap:10px;margin-top:20px}}
        .edit-actions button{{flex:1;padding:12px;border-radius:25px;font-weight:700;cursor:pointer;font-size:14px;transition:all 0.3s}}
        .btn-save{{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;color:#fff}}
        .btn-cancel{{background:var(--card);border:1px solid var(--border);color:#fff}}
        .overlay-panel{{position:fixed;inset:0;background:rgba(0,0,0,0.7);z-index:150;display:none}}
        .overlay-panel.show{{display:block}}
        
        /* New Post Creator */
        .post-creator{{
            background:rgba(16,185,129,0.04);border:1px solid var(--border);
            border-radius:20px;padding:16px;margin:0 16px 20px;
            backdrop-filter:blur(10px);
        }}
        .post-creator textarea{{
            width:100%;padding:12px;border-radius:14px;
            background:var(--card);border:1px solid var(--border);
            color:#fff;font-size:13px;outline:none;resize:none;
            font-family:'Segoe UI',sans-serif;min-height:60px;
            margin-bottom:10px;
        }}
        .post-creator textarea:focus{{border-color:var(--accent)}}
        .post-creator-actions{{display:flex;justify-content:flex-end}}
        .btn-post{{
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            border:none;color:#fff;padding:8px 20px;border-radius:20px;
            font-weight:700;cursor:pointer;font-size:12px;
            box-shadow:0 4px 12px rgba(16,185,129,0.3);
        }}

        /* Admin Panel */
        .admin-panel{{padding:0 8px;margin:0 8px 100px 8px}}
        .admin-panel h3{{color:#a7f3d0;font-size:20px;margin-bottom:20px;display:flex;align-items:center;gap:10px;font-weight:700}}
        .admin-stats-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-bottom:24px}}
        .stat-card{{background:rgba(16,185,129,0.06);border:1px solid rgba(16,185,129,0.15);border-radius:16px;padding:16px;display:flex;align-items:center;gap:14px;backdrop-filter:blur(10px)}}
        .stat-icon{{width:44px;height:44px;border-radius:12px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-size:20px;box-shadow:0 4px 15px rgba(16,185,129,0.3)}}
        .stat-info h4{{font-size:12px;color:rgba(255,255,255,0.5);margin-bottom:4px;font-weight:500}}
        .stat-info span{{font-size:22px;font-weight:800}}
        .admin-user-item{{display:flex;align-items:center;justify-content:space-between;padding:10px 8px;border-bottom:1px solid rgba(255,255,255,0.03);transition:background 0.2s;border-radius:8px}}
        .admin-user-item:hover{{background:rgba(16,185,129,0.04)}}
        .admin-user-info{{display:flex;align-items:center;gap:12px;flex:1;min-width:0;cursor:pointer}}
        .admin-avatar{{width:40px;height:40px;border-radius:50%;overflow:hidden;border:2px solid rgba(16,185,129,0.3);flex-shrink:0}}
        .admin-avatar img{{width:100%;height:100%;object-fit:cover}}
        .admin-user-details h4{{font-weight:600;font-size:15px}}
        .admin-user-details p{{font-size:11px;color:rgba(255,255,255,0.4);margin-top:2px}}
        .admin-user-actions{{display:flex;gap:8px;align-items:center;flex-shrink:0}}
        .admin-btn{{border:none;border-radius:20px;padding:8px 16px;font-size:12px;font-weight:700;cursor:pointer;transition:all 0.2s;display:flex;align-items:center;gap:5px}}
        .btn-ban{{background:rgba(255,255,255,0.1);color:#fff;border:1px solid rgba(255,255,255,0.1)}}
        .btn-unban{{background:rgba(34,197,94,0.1);color:#4ade80;border:1px solid rgba(34,197,94,0.2)}}
        .btn-verify{{background:linear-gradient(135deg,#10b981,#34d399);color:#fff;box-shadow:0 4px 12px rgba(16,185,129,0.3)}}
        .btn-delete-video{{background:rgba(239,68,68,0.1);color:#f87171;border:1px solid rgba(239,68,68,0.2)}}
        .btn-delete-video:hover{{background:rgba(239,68,68,0.3)}}
    </style>
</head>
<body>

<div class="load-center" id="loader" style="display:flex;align-items:center;justify-content:center;min-height:80vh;flex-direction:column;gap:12px;color:rgba(255,255,255,0.5)">
    <div class="spinner"></div><span>💎 تحميل الملف...</span>
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

    <!-- ✨ إحصائيات محسنة -->
    <div class="stats-row">
        <div class="stat-item" onclick="showUsersModal('following')">
            <div class="stat-icon-mini"><i class="fas fa-user-friends"></i></div>
            <div class="stat-val" id="statFollowing">0</div>
            <div class="stat-lbl">يتابع</div>
        </div>
        <div class="stat-item" onclick="showUsersModal('followers')">
            <div class="stat-icon-mini"><i class="fas fa-users"></i></div>
            <div class="stat-val" id="statFollowers">0</div>
            <div class="stat-lbl">متابع</div>
        </div>
        <div class="stat-item">
            <div class="stat-icon-mini"><i class="fas fa-heart"></i></div>
            <div class="stat-val" id="statLikes">0</div>
            <div class="stat-lbl">إعجابات</div>
        </div>
        <div class="stat-item" onclick="scrollToPosts()">
            <div class="stat-icon-mini"><i class="fas fa-feather-alt"></i></div>
            <div class="stat-val" id="statPosts">0</div>
            <div class="stat-lbl">منشورات</div>
        </div>
    </div>

    <div class="action-btns" id="actionsBar"></div>

    <!-- 📝 منشئ المنشورات (للملف الشخصي فقط) -->
    <div class="post-creator" id="postCreator" style="display:none">
        <textarea id="newPostContent" placeholder="ماذا يدور في ذهنك؟ 💎" maxlength="500"></textarea>
        <div class="post-creator-actions">
            <button class="btn-post" onclick="createPost()"><i class="fas fa-paper-plane"></i> نشر</button>
        </div>
    </div>

    <!-- 🎬 قسم الفيديوهات -->
    <div class="section-header">
        <div class="section-title"><i class="fas fa-video" style="color:var(--accent)"></i> الفيديوهات <span id="videosCount" style="font-size:12px;opacity:0.5;margin-right:6px"></span></div>
        <button class="btn-see-all" onclick="showAllVideos()"><span>عرض الكل</span> <i class="fas fa-chevron-left" style="font-size:10px"></i></button>
    </div>
    <div class="videos-grid" id="videosGrid"></div>

    <!-- 📝 قسم المنشورات -->
    <div class="section-header" id="postsHeader">
        <div class="section-title"><i class="fas fa-feather-alt" style="color:var(--accent)"></i> المنشورات <span id="postsCount" style="font-size:12px;opacity:0.5;margin-right:6px"></span></div>
    </div>
    <div class="posts-section" id="postsSection"></div>
</div>

<!-- ✨ Modal المتابعين/المتابَعين -->
<div id="usersModal" style="display:none"></div>

<!-- 🎬 Modal مشغل الفيديو -->
<div id="videoModal" style="display:none"></div>

<div class="overlay-panel" id="overlayPanel" onclick="closeEditPanel()"></div>
<div class="edit-panel" id="editPanel">
    <h3>💎 لوحة تعديل الملف الشخصي</h3>
    <label>👤 اسم المستخدم</label>
    <input type="text" id="editUsername" placeholder="اسم المستخدم">
    <label>📝 السيرة الذاتية</label>
    <textarea id="editBio" placeholder="اكتب شيئاً عن نفسك..." rows="3"></textarea>
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
    let allPosts = [];

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
        const ps = await db.ref('posts').once('value');
        const postsData = ps.val() || {{}};
        allPosts = Object.entries(postsData).map(([k, v]) => ({{id: k, ...v}})).sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
    }}

    async function loadProfile() {{
        const u = allUsers[profileUserId];
        if(!u) {{ document.getElementById('content').innerHTML = '<div class="empty-state" style="padding-top:100px"><i class="fas fa-user-slash"></i><p>المستخدم غير موجود</p></div>'; return; }}
        
        const emeraldVerifiedBadge = u.isVerified ? '<span class="badge-verified"><i class="fas fa-check"></i></span>' : '';
        document.getElementById('nameDisplay').innerHTML = '@' + (u.username || 'مستخدم') + ' ' + emeraldVerifiedBadge;
        document.getElementById('bioDisplay').innerText = u.bio || '';
        
        const contactInfo = document.getElementById('contactInfo');
        let contactHTML = '';
        if(u.website) contactHTML += `<a href="${{u.website}}" target="_blank"><i class="fas fa-globe"></i> ${{u.website.replace('https://','').replace('http://','')}}</a>`;
        if(u.contactEmail) contactHTML += `<a href="mailto:${{u.contactEmail}}"><i class="fas fa-envelope"></i> ${{u.contactEmail}}</a>`;
        contactInfo.innerHTML = contactHTML;
        
        document.getElementById('statFollowing').innerText = Object.keys(u.following || {{}}).length;
        document.getElementById('statFollowers').innerText = Object.keys(u.followers || {{}}).length;
        
        const uvs = allVideos.filter(v => v.sender === profileUserId);
        document.getElementById('statLikes').innerText = uvs.reduce((s, v) => s + (v.likes || 0), 0);
        
        const userPosts = allPosts.filter(p => p.userId === profileUserId);
        document.getElementById('statPosts').innerText = userPosts.length;
        document.getElementById('videosCount').innerText = '(' + uvs.length + ')';
        document.getElementById('postsCount').innerText = '(' + userPosts.length + ')';
        
        const coverImg = document.getElementById('coverImg');
        if(u.coverImageUrl) {{ coverImg.src = u.coverImageUrl; coverImg.style.display = 'block'; }}
        else {{ document.getElementById('coverSection').style.background = u.coverColor || COVER_COLORS[0]; coverImg.style.display = 'none'; }}
        
        document.getElementById('avatarImg').src = u.avatarUrl || (DICEBEAR_URL + '?seed=' + profileUserId);
        
        if(isOwnProfile) {{
            document.getElementById('avatarEditBtn').style.display = 'flex';
            document.getElementById('coverEditBtn').style.display = 'flex';
            document.getElementById('postCreator').style.display = 'block';
        }}
        
        const lastSeen = document.getElementById('lastSeenDisplay');
        if(!isOwnProfile) {{
            const presenceSnap = await db.ref('presence/' + profileUserId).get();
            const isOnline = presenceSnap.val();
            document.getElementById('onlineDot').style.display = isOnline ? 'block' : 'none';
            lastSeen.innerHTML = isOnline ? '<i class="fas fa-circle" style="color:#22c55e;font-size:8px"></i> نشط الآن' : '<i class="fas fa-clock"></i> آخر ظهور: ' + formatTime(u.lastSeen || u.createdAt);
        }} else {{
            lastSeen.innerHTML = '';
        }}

        // Render video grid
        const grid = document.getElementById('videosGrid');
        grid.innerHTML = '';
        if(!uvs.length) {{ 
            grid.innerHTML = '<div class="empty-state" style="grid-column:1/-1"><i class="fas fa-video-slash"></i><p>لا توجد فيديوهات</p></div>'; 
        }} else {{
            const displayVideos = uvs.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0)).slice(0, 9);
            displayVideos.forEach(v => {{
                const d = document.createElement('div');
                d.className = 'video-grid-item';
                d.onclick = () => playVideo(v.url);
                d.innerHTML = `
                    ${{v.thumbnail ? `<img src="${{v.thumbnail}}" style="width:100%;height:100%;object-fit:cover" loading="lazy">` : '<div style="width:100%;height:100%;background:#111;display:flex;align-items:center;justify-content:center"><i class="fas fa-play" style="color:#555;font-size:24px"></i></div>'}}
                    <div class="grid-overlay"></div>
                    <div class="grid-play-icon"><i class="fas fa-play-circle"></i></div>
                    <div class="grid-info"><span><i class="fas fa-heart"></i> ${{v.likes || 0}}</span><span><i class="fas fa-comment"></i> ${{v.comments ? Object.keys(v.comments).length : 0}}</span></div>
                `;
                grid.appendChild(d);
            }});
        }}

        // Render posts
        renderPosts(userPosts);

        const actionsBar = document.getElementById('actionsBar');
        if(isOwnProfile) {{
            actionsBar.innerHTML = `
                <button class="btn btn-primary" onclick="openEditPanel()"><i class="fas fa-edit"></i> تعديل الملف</button>
                <button class="btn" onclick="window.location.href='chat.html'"><i class="fas fa-envelope"></i> الرسائل</button>
                <button class="btn" onclick="copyProfile()"><i class="fas fa-share-alt"></i> مشاركة</button>
                <button class="btn btn-outline" onclick="auth.signOut();window.location.href='auth.html'"><i class="fas fa-sign-out-alt"></i> خروج</button>`;
        }} else {{
            const isFollowing = currentUserData?.following?.[profileUserId];
            actionsBar.innerHTML = `
                <button class="btn btn-follow ${{isFollowing ? 'following' : ''}}" id="followBtn" onclick="toggleFollowUser()" style="${{isFollowing ? 'background:rgba(16,185,129,0.1);border:1px solid var(--border);box-shadow:none' : 'background:linear-gradient(135deg,var(--accent),var(--accent2));box-shadow:0 8px 25px rgba(16,185,129,0.4)'}}">
                    ${{isFollowing ? '<i class="fas fa-user-check"></i> متابع' : '<i class="fas fa-user-plus"></i> متابعة'}}
                </button>
                <button class="btn btn-primary" onclick="window.location.href='chat.html?uid=${{profileUserId}}'"><i class="fas fa-comment"></i> مراسلة</button>
                <button class="btn" onclick="copyProfile()"><i class="fas fa-share-alt"></i> مشاركة</button>`;
        }}
        
        if(isOwnProfile && ADMIN_EMAILS.includes(currentUser?.email)) {{ loadAdminPanel(); }}
    }}

    function renderPosts(userPosts) {{
        const section = document.getElementById('postsSection');
        if(!userPosts.length) {{
            section.innerHTML = '<div class="empty-state"><i class="fas fa-feather-alt"></i><p>لا توجد منشورات</p></div>';
            return;
        }}
        section.innerHTML = userPosts.slice(0, 10).map(p => {{
            const user = allUsers[p.userId] || {{}};
            const avatar = user.avatarUrl || (DICEBEAR_URL + '?seed=' + p.userId);
            return `<div class="post-card">
                <div class="post-header">
                    <div class="post-avatar"><img src="${{avatar}}" alt="" loading="lazy"></div>
                    <div class="post-user-info">
                        <h4>@${{user.username || 'مستخدم'}} ${{user.isVerified ? '<span class="badge-verified" style="width:16px;height:16px;font-size:9px"><i class="fas fa-check"></i></span>' : ''}}</h4>
                        <span>${{formatTime(p.timestamp)}}</span>
                    </div>
                </div>
                <div class="post-content">${{p.content}}</div>
                <div class="post-actions">
                    <span onclick="likePost('${{p.id}}')"><i class="far fa-heart"></i> ${{p.likes || 0}}</span>
                    <span><i class="far fa-comment"></i> ${{p.comments || 0}}</span>
                    ${{isOwnProfile ? `<span onclick="deletePost('${{p.id}}')" style="color:var(--danger)"><i class="fas fa-trash"></i> حذف</span>` : ''}}
                </div>
            </div>`;
        }}).join('');
    }}

    // ✨ Modal عرض المتابعين/المتابَعين
    async function showUsersModal(type) {{
        const u = allUsers[profileUserId];
        const list = type === 'followers' ? (u?.followers || {{}}) : (u?.following || {{}});
        const ids = Object.keys(list);
        const title = type === 'followers' ? 'المتابِعون' : 'المتابَعون';
        
        let html = `<div class="modal-overlay" onclick="closeModal()">
            <div class="modal-sheet" onclick="event.stopPropagation()">
                <div class="modal-header">
                    <h3><i class="fas ${{type === 'followers' ? 'fa-users' : 'fa-user-friends'}}"></i> ${{title}} (${{ids.length}})</h3>
                    <button class="btn-close-overlay" onclick="closeModal()"><i class="fas fa-times"></i></button>
                </div>
                <div class="modal-body">`;
        
        if(!ids.length) {{
            html += '<div class="empty-state"><i class="fas fa-user-slash"></i><p>لا يوجد</p></div>';
        }} else {{
            for(const id of ids) {{
                const user = allUsers[id];
                if(!user) continue;
                const avatar = user.avatarUrl || (DICEBEAR_URL + '?seed=' + id);
                const isFollowingMe = currentUserData?.following?.[id];
                html += `<div class="user-list-item" onclick="openUserProfile('${{id}}')">
                    <div class="user-list-avatar"><img src="${{avatar}}" alt="" loading="lazy"></div>
                    <div class="user-list-info">
                        <h4>@${{user.username || 'مستخدم'}} ${{user.isVerified ? '<span class="badge-verified" style="width:16px;height:16px;font-size:9px"><i class="fas fa-check"></i></span>' : ''}}</h4>
                        <p>${{user.bio || '💎 عضو في MNAENCA'}}</p>
                    </div>
                    ${{id !== currentUser?.uid ? `<button class="btn-follow-sm ${{isFollowingMe ? 'following' : ''}}" onclick="event.stopPropagation();toggleFollowModal('${{id}}', this)">${{isFollowingMe ? '<i class="fas fa-user-check"></i> متابع' : '<i class="fas fa-user-plus"></i> متابعة'}}</button>` : ''}}
                </div>`;
            }}
        }}
        
        html += `</div></div></div>`;
        document.getElementById('usersModal').innerHTML = html;
        document.getElementById('usersModal').style.display = 'block';
    }}

    function closeModal() {{
        document.getElementById('usersModal').innerHTML = '';
        document.getElementById('usersModal').style.display = 'none';
    }}

    async function toggleFollowModal(userId, btn) {{
        if(!currentUser || currentUser.uid === userId) return;
        const userRef = db.ref('users/' + currentUser.uid + '/following/' + userId);
        const targetRef = db.ref('users/' + userId + '/followers/' + currentUser.uid);
        const snap = await userRef.get();
        if(snap.exists()) {{
            await userRef.remove(); await targetRef.remove();
            btn.innerHTML = '<i class="fas fa-user-plus"></i> متابعة';
            btn.classList.remove('following');
        }} else {{
            await userRef.set(true); await targetRef.set(true);
            btn.innerHTML = '<i class="fas fa-user-check"></i> متابع';
            btn.classList.add('following');
        }}
        await loadAll();
    }}

    // 🎬 تشغيل الفيديو داخل Modal
    function playVideo(url) {{
        document.getElementById('videoModal').innerHTML = `
            <div class="video-modal" onclick="closeVideoModal()">
                <button class="video-modal-close" onclick="closeVideoModal()"><i class="fas fa-times"></i></button>
                <video src="${{url}}" controls autoplay playsinline onclick="event.stopPropagation()"></video>
            </div>`;
        document.getElementById('videoModal').style.display = 'block';
    }}

    function closeVideoModal() {{
        document.getElementById('videoModal').innerHTML = '';
        document.getElementById('videoModal').style.display = 'none';
    }}

    // 📝 عرض كل الفيديوهات
    function showAllVideos() {{
        const uvs = allVideos.filter(v => v.sender === profileUserId).sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
        let html = `<div class="modal-overlay" onclick="closeAllVideos()">
            <div class="modal-sheet" onclick="event.stopPropagation()" style="max-height:90vh">
                <div class="modal-header">
                    <h3><i class="fas fa-video"></i> جميع الفيديوهات (${{uvs.length}})</h3>
                    <button class="btn-close-overlay" onclick="closeAllVideos()"><i class="fas fa-times"></i></button>
                </div>
                <div class="modal-body" style="display:grid;grid-template-columns:repeat(3,1fr);gap:3px;padding:10px">`;
        
        if(!uvs.length) {{
            html += '<div class="empty-state" style="grid-column:1/-1"><i class="fas fa-video-slash"></i><p>لا توجد فيديوهات</p></div>';
        }} else {{
            uvs.forEach(v => {{
                html += `<div class="video-grid-item" onclick="playVideo('${{v.url}}');closeAllVideos()">
                    ${{v.thumbnail ? `<img src="${{v.thumbnail}}" loading="lazy">` : ''}}
                    <div class="grid-overlay"></div>
                    <div class="grid-play-icon"><i class="fas fa-play-circle"></i></div>
                    <div class="grid-info"><span><i class="fas fa-heart"></i> ${{v.likes || 0}}</span></div>
                </div>`;
            }});
        }}
        
        html += `</div></div></div>`;
        document.getElementById('videoModal').innerHTML = html;
        document.getElementById('videoModal').style.display = 'block';
    }}

    function closeAllVideos() {{
        document.getElementById('videoModal').innerHTML = '';
        document.getElementById('videoModal').style.display = 'none';
    }}

    // 📝 إنشاء منشور
    async function createPost() {{
        const content = document.getElementById('newPostContent').value.trim();
        if(!content || !currentUser) return;
        await db.ref('posts').push({{
            userId: currentUser.uid,
            content: content,
            likes: 0,
            comments: 0,
            timestamp: Date.now()
        }});
        document.getElementById('newPostContent').value = '';
        await db.ref('users/' + currentUser.uid + '/totalPosts').set((currentUserData?.totalPosts || 0) + 1);
        await loadAll();
        await loadProfile();
        showToast('✅ تم نشر المنشور');
    }}

    async function likePost(postId) {{
        if(!currentUser) return;
        const ref = db.ref('posts/' + postId);
        const snap = await ref.get();
        const post = snap.val();
        if(!post) return;
        let likes = (post.likes || 0) + 1;
        await ref.update({{likes}});
        await loadAll();
        await loadProfile();
    }}

    async function deletePost(postId) {{
        if(!confirm('هل أنت متأكد من حذف هذا المنشور؟')) return;
        await db.ref('posts/' + postId).remove();
        await loadAll();
        await loadProfile();
        showToast('🗑️ تم حذف المنشور');
    }}

    function scrollToPosts() {{
        document.getElementById('postsHeader').scrollIntoView({{behavior: 'smooth'}});
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
        if(snap.exists()) {{
            await userRef.remove(); await targetRef.remove();
            btn.innerHTML = '<i class="fas fa-user-plus"></i> متابعة';
            btn.style.background = 'linear-gradient(135deg,var(--accent),var(--accent2))';
            btn.style.boxShadow = '0 8px 25px rgba(16,185,129,0.4)';
        }} else {{
            await userRef.set(true); await targetRef.set(true);
            btn.innerHTML = '<i class="fas fa-user-check"></i> متابع';
            btn.style.background = 'rgba(16,185,129,0.1)';
            btn.style.boxShadow = 'none';
            btn.style.border = '1px solid var(--border)';
        }}
        await loadAll(); await loadProfile();
    }}
    
    async function copyProfile() {{
        const u = allUsers[profileUserId];
        const text = `👤 @${{u.username || 'مستخدم'}}\n📝 ${{u.bio || ''}}\n💎 MNAENCA 2026`;
        try {{ await navigator.clipboard.writeText(text); }} catch(e) {{ const ta = document.createElement('textarea'); ta.value = text; document.body.appendChild(ta); ta.select(); document.execCommand('copy'); document.body.removeChild(ta); }}
        showToast('✅ تم نسخ معلومات الملف الشخصي');
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
        const postsSection = document.getElementById('postsSection');
        if(!postsSection) return;
        const oldPanel = document.getElementById('adminPanelContainer');
        if(oldPanel) oldPanel.remove();
        
        const adminDiv = document.createElement('div');
        adminDiv.id = 'adminPanelContainer';
        adminDiv.className = 'admin-panel';
        
        const totalUsers = Object.keys(allUsers).length;
        const totalVideos = allVideos.length;
        const totalVerified = Object.values(allUsers).filter(u => u.isVerified).length;
        const totalBanned = Object.values(allUsers).filter(u => u.banned).length;
        
        adminDiv.innerHTML = `<h3><i class="fas fa-crown"></i> لوحة تحكم الأدمن</h3>
            <div class="admin-stats-grid">
                <div class="stat-card"><div class="stat-icon"><i class="fas fa-users"></i></div><div class="stat-info"><h4>المستخدمين</h4><span>${{totalUsers}}</span></div></div>
                <div class="stat-card"><div class="stat-icon" style="background:linear-gradient(135deg,#f59e0b,#10b981)"><i class="fas fa-video"></i></div><div class="stat-info"><h4>فيديوهات</h4><span>${{totalVideos}}</span></div></div>
                <div class="stat-card"><div class="stat-icon"><i class="fas fa-check-circle"></i></div><div class="stat-info"><h4>موثقين</h4><span>${{totalVerified}}</span></div></div>
                <div class="stat-card"><div class="stat-icon" style="background:linear-gradient(135deg,#ef4444,#dc2626)"><i class="fas fa-ban"></i></div><div class="stat-info"><h4>محظورين</h4><span>${{totalBanned}}</span></div></div>
            </div>
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;color:rgba(255,255,255,0.6);font-size:13px;font-weight:600;border-bottom:1px solid rgba(16,185,129,0.1);padding-bottom:8px">
                <span>📋 قائمة المستخدمين</span><span style="font-size:11px">${{totalUsers}} إجمالي</span>
            </div>
            <div id="adminDynamicList"></div>
            <div style="display:flex;justify-content:space-between;align-items:center;margin-top:24px;margin-bottom:14px;color:rgba(255,255,255,0.6);font-size:13px;font-weight:600;border-bottom:1px solid rgba(16,185,129,0.1);padding-bottom:8px">
                <span>🎬 جميع الفيديوهات</span><span style="font-size:11px">${{totalVideos}} إجمالي</span>
            </div>
            <div id="adminVideosList"></div>`;
        
        postsSection.after(adminDiv);
        loadAdminUsersList();
        loadAdminVideosList();
    }}

    function loadAdminUsersList() {{
        const listContainer = document.getElementById('adminDynamicList');
        if(!listContainer) return;
        const usersArray = Object.entries(allUsers).sort(([, a], [, b]) => (b.createdAt || 0) - (a.createdAt || 0)).slice(0, 15);
        if(!usersArray.length) {{ listContainer.innerHTML = '<div style="text-align:center;opacity:0.5;padding:20px">لا يوجد مستخدمون</div>'; return; }}
        listContainer.innerHTML = usersArray.map(([id, u]) => {{
            const avatar = u.avatarUrl || (DICEBEAR_URL + '?seed=' + id);
            const isVerified = u.isVerified;
            const isBanned = u.banned;
            const verifiedBadgeHtml = isVerified ? '<span class="badge-verified"><i class="fas fa-check"></i></span>' : '';
            let actionBtns = '';
            if(isBanned) {{
                actionBtns = `<button class="admin-btn btn-unban" onclick="toggleBanUser('${{id}}')"><i class="fas fa-undo"></i> إلغاء الحظر</button>`;
            }} else {{
                actionBtns = `<button class="admin-btn btn-verify" onclick="toggleVerifyUser('${{id}}')">${{isVerified ? '<i class="fas fa-times-circle"></i> إلغاء' : '<i class="fas fa-check-circle"></i> توثيق'}}</button><button class="admin-btn btn-ban" onclick="toggleBanUser('${{id}}')"><i class="fas fa-ban"></i> حظر</button>`;
            }}
            return `<div class="admin-user-item">
                <div class="admin-user-info" onclick="openUserProfile('${{id}}')">
                    <div class="admin-avatar"><img src="${{avatar}}"></div>
                    <div class="admin-user-details"><h4>@${{u.username || 'مستخدم'}} ${{verifiedBadgeHtml}}</h4><p>${{u.email || ''}}</p></div>
                </div>
                <div class="admin-user-actions">${{actionBtns}}</div>
            </div>`;
        }}).join('');
    }}

    function loadAdminVideosList() {{
        const listContainer = document.getElementById('adminVideosList');
        if(!listContainer) return;
        const videosArray = allVideos.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0)).slice(0, 20);
        if(!videosArray.length) {{ listContainer.innerHTML = '<div style="text-align:center;opacity:0.5;padding:20px">لا توجد فيديوهات</div>'; return; }}
        listContainer.innerHTML = videosArray.map(v => {{
            const user = allUsers[v.sender] || {{username: v.senderName || 'مستخدم'}};
            const desc = (v.description || 'بدون وصف').substring(0, 40);
            return `<div class="admin-user-item">
                <div class="admin-user-info">
                    <div class="admin-avatar" style="border-radius:8px;width:50px;height:70px">${{v.thumbnail ? `<img src="${{v.thumbnail}}" style="object-fit:cover">` : ''}}</div>
                    <div class="admin-user-details"><p style="font-size:12px">${{desc}}</p><span style="font-size:10px;opacity:0.4">@${{user.username}} · ❤️ ${{v.likes || 0}}</span></div>
                </div>
                <div class="admin-user-actions"><button class="admin-btn btn-delete-video" onclick="deleteVideo('${{v.id}}')"><i class="fas fa-trash"></i> حذف</button></div>
            </div>`;
        }}).join('');
    }}

    window.deleteVideo = async function(videoId) {{
        if(!confirm('هل أنت متأكد من حذف هذا الفيديو؟')) return;
        try {{ await db.ref('videos/' + videoId).remove(); showToast('🗑️ تم حذف الفيديو بنجاح'); await loadAll(); await loadProfile(); loadAdminVideosList(); }} catch(e) {{ showToast('❌ فشل حذف الفيديو'); }}
    }};
    
    window.toggleVerifyUser = async function(id) {{
        const snap = await db.ref('users/' + id).once('value');
        const data = snap.val();
        if(!data) return;
        const newState = !data.isVerified;
        if(!confirm(`تأكيد ${{newState ? 'توثيق' : 'إلغاء توثيق'}} @${{data.username || 'المستخدم'}}؟`)) return;
        await db.ref('users/' + id).update({{isVerified: newState, verifiedAt: newState ? Date.now() : null, verifiedBy: newState ? currentUser.uid : null}});
        await loadAll(); await loadProfile(); showToast(`✅ تم ${{newState ? 'توثيق' : 'إلغاء توثيق'}} المستخدم`);
        loadAdminUsersList();
    }};
    
    window.toggleBanUser = async function(id) {{
        const snap = await db.ref('users/' + id).once('value');
        const data = snap.val();
        if(!data) return;
        const newState = !data.banned;
        if(!confirm(`تأكيد ${{newState ? 'حظر' : 'إلغاء حظر'}} @${{data.username || 'المستخدم'}}؟`)) return;
        await db.ref('users/' + id).update({{banned: newState, bannedAt: newState ? Date.now() : null, bannedBy: newState ? currentUser.uid : null}});
        await loadAll(); await loadProfile(); showToast(`✅ تم ${{newState ? 'حظر' : 'إلغاء حظر'}} المستخدم`);
        loadAdminUsersList();
    }};
    
    window.openUserProfile = function(id) {{
        if(id === currentUser?.uid) window.location.href = 'profile.html';
        else window.location.href = 'profile.html?uid=' + id;
    }};

    console.log('💎 MNAENCA Profile 2.0 Ready ✨');
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 💎 5. upload.html - رفع فيديو
# ═══════════════════════════════════════════════════════════

def build_upload():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💎 MNAENCA | رفع فيديو</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{min-height:100vh;overflow-y:auto;padding-bottom:100px}}
        .header{{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);background:rgba(5,20,11,0.8);backdrop-filter:blur(20px);position:sticky;top:0;z-index:10}}
        .btn-back{{background:rgba(16,185,129,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px;text-decoration:none}}
        .container{{max-width:500px;margin:0 auto;padding:20px}}
        .dropzone{{border:2px dashed rgba(16,185,129,0.3);border-radius:20px;padding:50px 20px;text-align:center;cursor:pointer;background:var(--glass);margin-bottom:20px;transition:all 0.3s}}
        .dropzone:hover{{border-color:var(--accent);background:rgba(16,185,129,0.05)}}
        .dropzone i{{font-size:48px;color:var(--accent)}}
        .dropzone video{{width:100%;max-height:250px;object-fit:contain;margin-top:12px;border-radius:12px;display:none}}
        .form-card{{background:rgba(16,185,129,0.03);border:1px solid var(--border);border-radius:20px;padding:20px}}
        .form-card label{{display:block;font-size:13px;opacity:0.7;margin-bottom:6px;margin-top:12px}}
        .form-card textarea,.form-card input{{width:100%;padding:14px 16px;border-radius:16px;background:rgba(16,185,129,0.04);border:1px solid var(--border);color:#fff;font-size:14px;outline:none;resize:none;font-family:'Segoe UI',sans-serif}}
        .progress-wrap{{display:none;margin:16px 0}}
        .progress-bar{{background:rgba(255,255,255,0.1);border-radius:30px;height:6px;overflow:hidden}}
        .progress-fill{{background:linear-gradient(90deg,var(--accent),var(--accent2));height:100%;border-radius:30px;width:0%;transition:width 0.3s}}
        .progress-text{{text-align:center;font-size:12px;margin-top:6px;color:var(--accent2)}}
        .btn-upload{{width:100%;padding:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;border-radius:30px;color:#fff;font-weight:700;font-size:15px;cursor:pointer;margin-top:16px;box-shadow:0 10px 25px rgba(16,185,129,0.4);transition:all 0.3s}}
        .btn-upload:hover{{transform:translateY(-2px);box-shadow:0 15px 35px rgba(16,185,129,0.6)}}
        .btn-upload:disabled{{opacity:0.5;transform:none;box-shadow:none}}
        .status{{text-align:center;margin-top:12px;font-size:13px;min-height:20px}}
        .upload-details{{display:flex;justify-content:space-between;font-size:12px;color:rgba(255,255,255,0.5);margin-top:10px}}
    </style>
</head>
<body>
<div class="header"><a href="index.html" class="btn-back"><i class="fas fa-arrow-right"></i></a><h2><i class="fas fa-cloud-upload-alt" style="color:var(--accent)"></i> رفع فيديو جديد</h2></div>
<div class="container">
    <div class="dropzone" onclick="document.getElementById('videoFile').click()">
        <i class="fas fa-cloud-upload-alt" id="uploadIcon"></i>
        <p style="margin:10px 0" id="dropText">اضغط لاختيار فيديو</p>
        <span style="font-size:11px;opacity:0.5">MP4 - حتى 100MB</span>
        <video id="preview" controls></video>
    </div>
    <input type="file" id="videoFile" accept="video/*" style="display:none" onchange="onFilePick(this)">
    <div class="form-card">
        <label><i class="fas fa-pen" style="color:var(--accent)"></i> وصف الفيديو</label>
        <textarea id="vidDesc" placeholder="اكتب وصفاً... #هاشتاقات" rows="3"></textarea>
        <label><i class="fas fa-music" style="color:var(--accent)"></i> الموسيقى</label>
        <input type="text" id="vidMusic" placeholder="Original Sound">
        <div class="progress-wrap" id="progressWrap">
            <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
            <div class="progress-text" id="progressText">0%</div>
            <div class="upload-details"><span id="uploadedSize">0 MB</span><span id="totalSize">0 MB</span></div>
        </div>
        <button class="btn-upload" id="uploadBtn" onclick="upload()"><i class="fas fa-heart"></i> رفع الفيديو</button>
        <div class="status" id="status"></div>
    </div>
</div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null,currentUserData=null,selectedFile=null;
    auth.onAuthStateChanged(async u=>{{if(!u){{window.location.href='auth.html';return}}currentUser=u;const snap=await db.ref('users/'+u.uid).get();if(snap.exists())currentUserData={{uid:u.uid,...snap.val()}}}});
    
    function onFilePick(inp){{
        const f=inp.files[0];
        if(!f) return;
        if(!f.type.startsWith('video/')){{showStatus('❌ الرجاء اختيار ملف فيديو صحيح','#ef4444');inp.value='';return}}
        if(f.size>100*1024*1024){{showStatus('❌ حجم الفيديو يجب أن يكون أقل من 100MB','#ef4444');inp.value='';return}}
        selectedFile=f;
        const r=new FileReader();
        r.onload=e=>{{const v=document.getElementById('preview');v.src=e.target.result;v.style.display='block';document.getElementById('uploadIcon').style.display='none';document.getElementById('dropText').style.display='none'}};
        r.readAsDataURL(f);
        const fileSizeMB=(f.size/(1024*1024)).toFixed(2);
        document.getElementById('totalSize').innerText=fileSizeMB+' MB';
        document.getElementById('progressWrap').style.display='block';
        document.getElementById('progressFill').style.width='0%';
        document.getElementById('progressText').innerText='0%';
        document.getElementById('uploadedSize').innerText='0 MB';
        document.getElementById('uploadBtn').disabled=false;
        showStatus('✅ الفيديو جاهز للرفع','#4ade80');
    }}

    async function upload(){{
        if(!selectedFile){{showStatus('❌ الرجاء اختيار فيديو أولاً','#ef4444');return}}
        if(!currentUser){{showStatus('❌ الرجاء تسجيل الدخول أولاً','#ef4444');return}}
        const desc=document.getElementById('vidDesc').value;
        const music=document.getElementById('vidMusic').value||'Original Sound';
        const btn=document.getElementById('uploadBtn');
        const pw=document.getElementById('progressWrap');
        const pf=document.getElementById('progressFill');
        const pt=document.getElementById('progressText');
        const us=document.getElementById('uploadedSize');
        btn.disabled=true;pw.style.display='block';pf.style.width='0%';pt.innerText='0%';
        showStatus('⏳ جاري رفع الفيديو...','#f59e0b');
        const fd=new FormData();fd.append('file',selectedFile);fd.append('upload_preset',UPLOAD_PRESET);
        const xhr=new XMLHttpRequest();
        xhr.open('POST','https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/video/upload');
        xhr.upload.onprogress=e=>{{if(e.lengthComputable){{const percent=Math.round(e.loaded/e.total*100);pf.style.width=percent+'%';pt.innerText=percent+'%';const loadedMB=(e.loaded/(1024*1024)).toFixed(2);const totalMB=(e.total/(1024*1024)).toFixed(2);us.innerText=loadedMB+' MB';document.getElementById('totalSize').innerText=totalMB+' MB'}}}};
        xhr.onload=async()=>{{
            try{{
                const r=JSON.parse(xhr.responseText);
                if(r.secure_url){{
                    await db.ref('videos/').push({{url:r.secure_url,thumbnail:r.secure_url.replace(/\.(mp4|mov|avi)$/i,'.jpg'),description:desc,music:music,sender:currentUser.uid,senderName:currentUserData?.username,likes:0,likedBy:{{}},comments:{{}},timestamp:Date.now()}});
                    showStatus('✅ تم رفع الفيديو بنجاح! سيتم التحويل للرئيسية...','#4ade80');
                    setTimeout(()=>window.location.href='index.html',1500);
                }}else{{showStatus('❌ فشل الرفع: '+(r.error?.message||'استجابة غير صحيحة'),'#ef4444');btn.disabled=false}}
            }}catch(e){{showStatus('❌ خطأ في معالجة الرد من الخادم','#ef4444');btn.disabled=false}}
        }};
        xhr.onerror=()=>{{showStatus('❌ فشل رفع الفيديو - تحقق من اتصالك بالإنترنت','#ef4444');btn.disabled=false}};
        xhr.send(fd);
    }}
    function showStatus(msg,color){{const s=document.getElementById('status');s.innerText=msg;s.style.color=color}}
    console.log('💎 MNAENCA Upload Ready');
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 💎 6. chat.html - دردشة
# ═══════════════════════════════════════════════════════════

<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover, user-scalable=no">
    <title>💎 MNAENCA | دردشة متطورة</title>
    
    <!-- Firebase SDKs -->
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    
    <!-- Font Awesome -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    
    <style>
        :root {
            --accent: #10b981;
            --accent2: #059669;
            --border: rgba(16,185,129,0.2);
            --bg-dark: #05140b;
        }
        *{margin:0;padding:0;box-sizing:border-box}
        body{
            height:100vh;height:100dvh;
            display:flex;flex-direction:column;
            background:var(--bg-dark);
            overflow:hidden;
            font-family:'Segoe UI',Tahoma,sans-serif;
            color:#fff;
        }
        
        /* --- Loader & Spinner --- */
        .spinner{
            width:44px;height:44px;
            border:4px solid rgba(16,185,129,0.2);
            border-top-color:var(--accent);
            border-radius:50%;
            animation:spin 0.8s linear infinite;
        }
        @keyframes spin{to{transform:rotate(360deg)}}
        
        /* --- Toast --- */
        .toast-msg{
            position:fixed;bottom:30px;left:50%;transform:translateX(-50%);
            background:rgba(0,0,0,0.85);color:#fff;padding:12px 28px;
            border-radius:50px;font-size:14px;font-weight:600;
            backdrop-filter:blur(10px);border:1px solid rgba(16,185,129,0.3);
            pointer-events:none;opacity:0;transition:all 0.4s cubic-bezier(0.16,1,0.3,1);
            z-index:999;
        }
        .toast-msg.show{opacity:1;bottom:40px}

        /* --- Header --- */
        .header{
            display:flex;align-items:center;gap:12px;
            padding:14px 16px;border-bottom:1px solid var(--border);
            background:rgba(5,20,11,0.9);backdrop-filter:blur(20px);
            flex-shrink:0;z-index:10;
        }
        .btn-back{
            background:rgba(16,185,129,0.1);border:1px solid var(--border);
            width:38px;height:38px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            color:#fff;cursor:pointer;font-size:16px;
            text-decoration:none;flex-shrink:0;transition:all 0.3s;
        }
        .btn-back:hover{background:rgba(16,185,129,0.25)}
        .header-title{flex:1;min-width:0}
        .header h2{font-size:16px;font-weight:700}
        .header h2 i{color:var(--accent);margin-left:6px}

        /* --- Conversation List --- */
        .conv-list{flex:1;overflow-y:auto;padding:8px 0}
        .conv-item{
            display:flex;align-items:center;gap:12px;
            padding:14px 16px;border-bottom:1px solid rgba(16,185,129,0.06);
            cursor:pointer;transition:background 0.2s;
            animation:fadeIn 0.3s ease;
        }
        @keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
        .conv-item:hover{background:rgba(16,185,129,0.04)}
        .chat-avatar{
            width:50px;height:50px;border-radius:50%;overflow:hidden;
            border:2px solid rgba(16,185,129,0.3);flex-shrink:0;
            background:rgba(16,185,129,0.1);
        }
        .chat-avatar img{width:100%;height:100%;object-fit:cover}
        .conv-info{flex:1;min-width:0}
        .conv-name{
            font-weight:600;font-size:15px;margin-bottom:3px;
            display:flex;align-items:center;gap:6px;
        }
        .conv-last{
            font-size:12px;color:rgba(255,255,255,0.4);
            white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
        }

        /* --- Chat Messages --- */
        .chat-msgs{
            flex:1;overflow-y:auto;padding:16px 12px;
            display:flex;flex-direction:column;gap:8px;
            background:#030d07;scroll-behavior:smooth;
        }
        .bubble{
            max-width:80%;padding:10px 16px;
            border-radius:20px;word-break:break-word;
            font-size:14px;position:relative;
            animation:msgIn 0.35s cubic-bezier(0.16,1,0.3,1);
            line-height:1.5;
        }
        @keyframes msgIn{from{opacity:0;transform:translateY(12px) scale(0.95)}to{opacity:1;transform:translateY(0) scale(1)}}
        .bubble.sent{
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            align-self:flex-end;color:#fff;
            border-bottom-right-radius:6px;
            box-shadow:0 4px 15px rgba(16,185,129,0.2);
        }
        .bubble.received{
            background:rgba(16,185,129,0.08);
            align-self:flex-start;
            border:1px solid rgba(16,185,129,0.12);
            border-bottom-left-radius:6px;
        }
        .bubble img{
            max-width:200px;border-radius:14px;cursor:pointer;
            margin-top:6px;display:block;
        }
        .bubble audio{
            margin-top:6px;width:200px;height:36px;
            border-radius:18px;outline:none;
        }
        .bubble .time{
            font-size:9px;opacity:0.5;margin-top:6px;
            text-align:left;direction:ltr;
        }
        
        /* Copy button on each message */
        .bubble .copy-msg-btn{
            position:absolute;top:-8px;left:-8px;
            width:26px;height:26px;border-radius:50%;
            background:rgba(0,0,0,0.7);border:1px solid rgba(255,255,255,0.2);
            color:#fff;font-size:11px;cursor:pointer;
            display:none;align-items:center;justify-content:center;
            transition:all 0.2s;z-index:5;
        }
        .bubble:hover .copy-msg-btn{display:flex}
        .bubble .copy-msg-btn:hover{background:var(--accent);border-color:var(--accent)}

        /* --- Input Bar --- */
        .input-bar{
            display:flex;gap:8px;padding:10px 12px;
            background:rgba(5,20,11,0.95);backdrop-filter:blur(20px);
            border-top:1px solid rgba(16,185,129,0.2);
            align-items:center;flex-shrink:0;z-index:10;
            min-height:60px;position:relative;
        }
        .input-bar input{
            flex:1;padding:12px 18px;border-radius:30px;
            background:rgba(16,185,129,0.06);
            border:1px solid rgba(16,185,129,0.25);
            color:#fff;font-size:14px;outline:none;
            transition:all 0.3s;min-width:0;
        }
        .input-bar input:focus{
            border-color:var(--accent);
            box-shadow:0 0 15px rgba(16,185,129,0.15);
            background:rgba(16,185,129,0.1);
        }
        .input-bar input::placeholder{color:rgba(255,255,255,0.35)}
        .btn-icon{
            width:42px;height:42px;
            background:rgba(16,185,129,0.1);
            border:1px solid rgba(16,185,129,0.2);
            border-radius:50%;color:#fff;cursor:pointer;
            font-size:18px;display:flex;align-items:center;
            justify-content:center;flex-shrink:0;
            transition:all 0.3s;
        }
        .btn-icon:hover{background:rgba(16,185,129,0.25);border-color:var(--accent)}
        .btn-send{
            width:44px;height:44px;
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            border:none;border-radius:50%;color:#fff;
            cursor:pointer;font-size:18px;
            display:flex;align-items:center;justify-content:center;
            flex-shrink:0;box-shadow:0 6px 20px rgba(16,185,129,0.4);
            transition:all 0.3s;
        }
        .btn-send:hover{transform:scale(1.05);box-shadow:0 8px 25px rgba(16,185,129,0.6)}
        .btn-send:active{transform:scale(0.95)}
        
        /* Recording button */
        .btn-record{
            width:42px;height:42px;
            background:rgba(239,68,68,0.2);
            border:2px solid rgba(239,68,68,0.5);
            border-radius:50%;color:#ef4444;cursor:pointer;
            font-size:18px;display:flex;align-items:center;
            justify-content:center;flex-shrink:0;
            transition:all 0.3s;
        }
        .btn-record.recording{
            animation:pulse-record 1s infinite;
            background:rgba(239,68,68,0.4);
            border-color:#ef4444;
        }
        @keyframes pulse-record{
            0%,100%{box-shadow:0 0 0 0 rgba(239,68,68,0.5)}
            50%{box-shadow:0 0 0 14px rgba(239,68,68,0)}
        }
        .recording-timer{
            position:absolute;top:-30px;left:50%;transform:translateX(-50%);
            background:rgba(0,0,0,0.8);color:#ef4444;
            padding:4px 14px;border-radius:20px;
            font-size:12px;font-weight:700;
            display:none;
        }
        .recording-timer.active{display:block}

        /* --- Empty State --- */
        .empty-state{
            text-align:center;padding:50px 20px;
            color:rgba(255,255,255,0.4);
        }
        .empty-state i{font-size:60px;color:var(--accent);opacity:0.3;margin-bottom:16px;display:block}
        .empty-state p{font-size:15px;margin-bottom:6px}
        .empty-state span{font-size:12px;opacity:0.5}

        /* --- Chat Header Info --- */
        .chat-header-info{
            display:flex;align-items:center;gap:12px;
            flex:1;min-width:0;
        }
        .chat-header-avatar{
            width:40px;height:40px;border-radius:50%;overflow:hidden;
            border:2px solid rgba(16,185,129,0.3);flex-shrink:0;
        }
        .chat-header-avatar img{width:100%;height:100%;object-fit:cover}
    </style>
</head>
<body>

<!-- Loader -->
<div id="loader" style="flex:1;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px">
    <div class="spinner"></div>
    <span style="color:rgba(255,255,255,0.5)">💎 جاري تحميل الدردشة...</span>
</div>

<!-- Conversations View -->
<div id="convView" style="display:none;flex:1;flex-direction:column;overflow:hidden">
    <div class="header">
        <a href="index.html" class="btn-back"><i class="fas fa-arrow-right"></i></a>
        <div class="header-title"><h2><i class="fas fa-comments"></i> المحادثات</h2></div>
    </div>
    <div class="conv-list" id="convList"></div>
    <div class="empty-state" id="convEmpty" style="display:none">
        <i class="fas fa-comment-slash"></i>
        <p>لا توجد محادثات</p>
        <span>ابدأ محادثة من ملف المستخدم</span>
    </div>
</div>

<!-- Chat View -->
<div id="chatView" style="display:none;flex:1;flex-direction:column;overflow:hidden">
    <div class="header">
        <button class="btn-back" onclick="showConvs()"><i class="fas fa-arrow-right"></i></button>
        <div class="chat-header-info">
            <div class="chat-header-avatar" id="chatAvatar"><img src="" alt=""></div>
            <div style="flex:1;min-width:0">
                <div style="font-weight:700;font-size:15px" id="chatName">محادثة</div>
                <div style="font-size:11px;opacity:0.5" id="chatOnline"></div>
            </div>
        </div>
        <button class="btn-icon" onclick="copyChat()" title="نسخ المحادثة كاملة"><i class="fas fa-copy"></i></button>
    </div>
    <div class="chat-msgs" id="msgsList">
        <div class="empty-state"><i class="fas fa-comments"></i><p>ابدأ المحادثة</p><span>أرسل رسالة للبدء 💎</span></div>
    </div>
    <div class="input-bar" style="position:relative">
        <span class="recording-timer" id="recTimer">00:00</span>
        <button class="btn-icon" onclick="sendImage()" title="إرسال صورة"><i class="fas fa-image"></i></button>
        <button class="btn-record" id="btnRecord" onclick="toggleRecording()" title="تسجيل صوتي"><i class="fas fa-microphone"></i></button>
        <input type="text" id="msgInput" placeholder="اكتب رسالتك هنا..." autocomplete="off" onkeydown="if(event.key==='Enter')sendMsg()">
        <button class="btn-send" onclick="sendMsg()"><i class="fas fa-paper-plane"></i></button>
    </div>
</div>

<!-- Toast -->
<div class="toast-msg" id="toastMsg">✅ تم</div>

<script>
    // ==================== FIREBASE CONFIGURATION ====================
    // بيانات مشروعك بالضبط
    const firebaseConfig = {
        apiKey: "AIzaSyCqDvG98pEqmZHKZienquJEq6gS1kNjK8M",
        authDomain: "muvg-42126.firebaseapp.com",
        databaseURL: "https://muvg-42126-default-rtdb.europe-west1.firebasedatabase.app",
        projectId: "muvg-42126",
        storageBucket: "muvg-42126.firebasestorage.app",
        messagingSenderId: "514075097173",
        appId: "1:514075097173:web:6fab4e9598549691cc7cdc",
        measurementId: "G-4VP8E6WJ48"
    };

    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);
    const db = firebase.database();
    const auth = firebase.auth();

    // ==================== CLOUDINARY CONFIGURATION ====================
    // بيانات السحابة الخاصة بك
    const CLOUD_NAME = 'trz3ktjf';      // اسم السحابة من الرابط
    const UPLOAD_PRESET = 's44_kk';     // upload preset الخاص بك

    // ==================== CONSTANTS ====================
    const DICEBEAR_URL = 'https://api.dicebear.com/7.x/avataaars/svg';

    // ==================== STATE ====================
    let currentUser = null;
    let allUsers = {};
    let chatUserId = null;

    // Recording state
    let mediaRecorder = null;
    let audioChunks = [];
    let recordingStartTime = null;
    let recordingTimerInterval = null;
    let isRecording = false;

    // ==================== AUTH ====================
    auth.onAuthStateChanged(async (u) => {
        if (!u) {
            window.location.href = 'auth.html';
            return;
        }
        currentUser = u;
        console.log('✅ تم تسجيل الدخول:', currentUser.uid);
        
        const us = await db.ref('users').once('value');
        allUsers = us.val() || {};
        document.getElementById('loader').style.display = 'none';

        const params = new URLSearchParams(window.location.search);
        const targetUid = params.get('uid');
        if (targetUid) {
            openChat(targetUid);
        } else {
            showConvs();
        }

        // Update lastSeen every 60 seconds
        setInterval(() => {
            if (currentUser) db.ref('users/' + currentUser.uid + '/lastSeen').set(Date.now());
        }, 60000);
    });

    // ==================== CONVERSATIONS ====================
    function showConvs() {
        document.getElementById('chatView').style.display = 'none';
        document.getElementById('convView').style.display = 'flex';
        chatUserId = null;
        loadConvs();
    }

    async function loadConvs() {
        const cl = document.getElementById('convList');
        const ce = document.getElementById('convEmpty');
        cl.innerHTML = '';

        const snap = await db.ref('private_messages').once('value');
        const all = snap.val() || {};
        const found = new Set();

        Object.keys(all).forEach(cid => {
            const [u1, u2] = cid.split('_');
            const other = u1 === currentUser.uid ? u2 : u2 === currentUser.uid ? u1 : null;
            if (other && !found.has(other) && allUsers[other]) found.add(other);
        });

        if (!found.size) {
            ce.style.display = 'block';
            return;
        } else {
            ce.style.display = 'none';
        }

        found.forEach(uid => {
            const u = allUsers[uid];
            const d = document.createElement('div');
            d.className = 'conv-item';
            d.innerHTML = `
                <div class="chat-avatar">
                    <img src="${u?.avatarUrl || (DICEBEAR_URL + '?seed=' + uid)}" 
                         alt="" onerror="this.src='${DICEBEAR_URL}?seed=${uid}'">
                </div>
                <div class="conv-info">
                    <div class="conv-name">
                        @${u?.username || 'مستخدم'} 
                        ${u?.isVerified ? '<span style="color:#a7f3d0;font-size:12px"><i class="fas fa-check-circle"></i></span>' : ''}
                    </div>
                    <div class="conv-last">اضغط للدخول إلى المحادثة 💬</div>
                </div>`;
            d.onclick = () => openChat(uid);
            cl.appendChild(d);
        });
    }

    // ==================== CHAT ====================
    async function openChat(uid) {
        chatUserId = uid;
        const u = allUsers[uid];
        document.getElementById('chatName').innerText = '@' + (u?.username || 'مستخدم');
        document.getElementById('chatAvatar').querySelector('img').src = u?.avatarUrl || (DICEBEAR_URL + '?seed=' + uid);
        document.getElementById('convView').style.display = 'none';
        document.getElementById('chatView').style.display = 'flex';

        const onlineEl = document.getElementById('chatOnline');
        db.ref('presence/' + uid).on('value', s => {
            const online = s.val();
            onlineEl.innerHTML = online
                ? '<span style="color:#22c55e">● نشط الآن</span>'
                : 'آخر ظهور: ' + formatTime(u?.lastSeen);
        });

        await loadMsgs();
        document.getElementById('msgInput').focus();
    }

    function getChatId() {
        return [currentUser.uid, chatUserId].sort().join('_');
    }

    async function loadMsgs() {
        const ml = document.getElementById('msgsList');
        if (!chatUserId) return;

        const snap = await db.ref('private_messages/' + getChatId()).once('value');
        const ms = snap.val() || {};
        const msgsArr = Object.values(ms).sort((a, b) => a.timestamp - b.timestamp);

        if (!msgsArr.length) {
            ml.innerHTML = '<div class="empty-state"><i class="fas fa-comments"></i><p>ابدأ المحادثة</p><span>أرسل رسالة للبدء 💎</span></div>';
            return;
        }

        ml.innerHTML = msgsArr.map((m) => {
            const sent = m.senderId === currentUser.uid;
            let content = '';
            
            if (m.type === 'image') {
                content = `<img src="${m.imageUrl}" onclick="window.open('${m.imageUrl}','_blank')" loading="lazy">`;
            } else if (m.type === 'voice') {
                content = `<audio controls src="${m.voiceUrl}"></audio>`;
            } else {
                content = m.text;
            }

            // Escape message data for data attribute
            const msgData = encodeURIComponent(JSON.stringify(m));

            return `
                <div class="bubble ${sent ? 'sent' : 'received'}" data-msg='${msgData}'>
                    <button class="copy-msg-btn" onclick="copySingleMsg(this)" title="نسخ الرسالة">
                        <i class="fas fa-copy"></i>
                    </button>
                    ${content}
                    <div class="time">${new Date(m.timestamp).toLocaleTimeString('ar-SA', {hour:'2-digit', minute:'2-digit'})}</div>
                </div>`;
        }).join('');

        setTimeout(() => { ml.scrollTop = ml.scrollHeight; }, 100);
    }

    // ==================== SEND MESSAGE ====================
    async function sendMsg() {
        const inp = document.getElementById('msgInput');
        const txt = inp.value.trim();
        if (!txt || !chatUserId) return;
        inp.value = '';

        await db.ref('private_messages/' + getChatId()).push({
            senderId: currentUser.uid,
            text: txt,
            type: 'text',
            timestamp: Date.now()
        });
        await loadMsgs();
    }

    // ==================== SEND IMAGE ====================
    async function sendImage() {
        if (!chatUserId) {
            showToast('⚠️ افتح محادثة أولاً');
            return;
        }
        const inp = document.createElement('input');
        inp.type = 'file';
        inp.accept = 'image/*';
        inp.onchange = async (e) => {
            const file = e.target.files[0];
            if (!file) return;
            showToast('⏳ جاري رفع الصورة...');
            
            const fd = new FormData();
            fd.append('file', file);
            fd.append('upload_preset', UPLOAD_PRESET);
            
            try {
                const res = await fetch(`https://api.cloudinary.com/v1_1/${CLOUD_NAME}/image/upload`, { 
                    method: 'POST', 
                    body: fd 
                });
                const data = await res.json();
                console.log('Cloudinary Response:', data);
                
                if (data.secure_url) {
                    await db.ref('private_messages/' + getChatId()).push({
                        senderId: currentUser.uid,
                        type: 'image',
                        imageUrl: data.secure_url,
                        timestamp: Date.now()
                    });
                    await loadMsgs();
                    showToast('✅ تم إرسال الصورة');
                } else {
                    showToast('❌ فشل رفع الصورة: ' + (data.error?.message || 'خطأ غير معروف'));
                }
            } catch (e) {
                console.error('Upload Error:', e);
                showToast('❌ فشل رفع الصورة');
            }
        };
        inp.click();
    }

    // ==================== VOICE RECORDING ====================
    async function toggleRecording() {
        if (isRecording) {
            stopRecording();
        } else {
            startRecording();
        }
    }

    async function startRecording() {
        if (!chatUserId) {
            showToast('⚠️ افتح محادثة أولاً');
            return;
        }
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            mediaRecorder = new MediaRecorder(stream, { mimeType: 'audio/webm' });
            audioChunks = [];

            mediaRecorder.ondataavailable = (e) => {
                if (e.data.size > 0) audioChunks.push(e.data);
            };

            mediaRecorder.onstop = async () => {
                const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
                await uploadVoice(audioBlob);
                // Stop all tracks
                stream.getTracks().forEach(track => track.stop());
            };

            mediaRecorder.start();
            isRecording = true;
            recordingStartTime = Date.now();

            // Update UI
            const btnRecord = document.getElementById('btnRecord');
            btnRecord.classList.add('recording');
            btnRecord.innerHTML = '<i class="fas fa-stop"></i>';
            document.getElementById('recTimer').classList.add('active');
            updateRecordingTimer();
            recordingTimerInterval = setInterval(updateRecordingTimer, 1000);
            showToast('🎙️ جاري التسجيل...');
        } catch (err) {
            console.error('Mic Error:', err);
            showToast('❌ لا يمكن الوصول للميكروفون');
        }
    }

    function stopRecording() {
        if (mediaRecorder && mediaRecorder.state === 'recording') {
            mediaRecorder.stop();
            isRecording = false;

            // Reset UI
            const btnRecord = document.getElementById('btnRecord');
            btnRecord.classList.remove('recording');
            btnRecord.innerHTML = '<i class="fas fa-microphone"></i>';
            document.getElementById('recTimer').classList.remove('active');
            clearInterval(recordingTimerInterval);
            showToast('✅ تم إيقاف التسجيل');
        }
    }

    function updateRecordingTimer() {
        const elapsed = Math.floor((Date.now() - recordingStartTime) / 1000);
        const mins = Math.floor(elapsed / 60).toString().padStart(2, '0');
        const secs = (elapsed % 60).toString().padStart(2, '0');
        document.getElementById('recTimer').innerText = `${mins}:${secs}`;
    }

    async function uploadVoice(audioBlob) {
        if (!chatUserId) return;
        showToast('⏳ جاري رفع التسجيل الصوتي...');
        
        const fd = new FormData();
        fd.append('file', audioBlob, 'voice_' + Date.now() + '.webm');
        fd.append('upload_preset', UPLOAD_PRESET);
        // ملاحظة: Cloudinary يستخدم video upload للصوتيات

        try {
            const res = await fetch(`https://api.cloudinary.com/v1_1/${CLOUD_NAME}/video/upload`, { 
                method: 'POST', 
                body: fd 
            });
            const data = await res.json();
            console.log('Voice Upload Response:', data);
            
            if (data.secure_url) {
                await db.ref('private_messages/' + getChatId()).push({
                    senderId: currentUser.uid,
                    type: 'voice',
                    voiceUrl: data.secure_url,
                    timestamp: Date.now()
                });
                await loadMsgs();
                showToast('✅ تم إرسال التسجيل الصوتي');
            } else {
                showToast('❌ فشل رفع التسجيل: ' + (data.error?.message || 'خطأ غير معروف'));
            }
        } catch (e) {
            console.error('Voice Upload Error:', e);
            showToast('❌ فشل رفع التسجيل الصوتي');
        }
    }

    // ==================== COPY MESSAGES ====================
    // نسخ رسالة فردية
    function copySingleMsg(btn) {
        const bubble = btn.closest('.bubble');
        const encodedMsg = bubble.getAttribute('data-msg');
        if (!encodedMsg) return;
        
        try {
            const msg = JSON.parse(decodeURIComponent(encodedMsg));
            let textToCopy = '';
            
            if (msg.type === 'text') {
                textToCopy = msg.text;
            } else if (msg.type === 'image') {
                textToCopy = msg.imageUrl;
            } else if (msg.type === 'voice') {
                textToCopy = msg.voiceUrl;
            }

            copyToClipboard(textToCopy);
            showToast('✅ تم نسخ الرسالة');
        } catch (e) {
            showToast('❌ خطأ في النسخ');
        }
    }

    // نسخ المحادثة كاملة
    async function copyChat() {
        if (!chatUserId) return;
        
        const snap = await db.ref('private_messages/' + getChatId()).once('value');
        const msgs = snap.val() || {};
        let text = '💬 محادثة MNAENCA\n' + '─'.repeat(30) + '\n';
        
        Object.values(msgs).sort((a, b) => a.timestamp - b.timestamp).forEach(m => {
            const sender = m.senderId === currentUser.uid ? 'أنت' : (allUsers[m.senderId]?.username || 'مستخدم');
            let content = '';
            
            if (m.type === 'image') {
                content = '[📷 صورة] ' + m.imageUrl;
            } else if (m.type === 'voice') {
                content = '[🎙️ تسجيل صوتي] ' + m.voiceUrl;
            } else {
                content = m.text;
            }
            
            const time = new Date(m.timestamp).toLocaleTimeString('ar-SA');
            text += `\n${sender} (${time}):\n${content}\n`;
        });
        
        await copyToClipboard(text);
        showToast('✅ تم نسخ المحادثة كاملة');
    }

    async function copyToClipboard(text) {
        try {
            await navigator.clipboard.writeText(text);
        } catch (e) {
            // Fallback for older browsers
            const ta = document.createElement('textarea');
            ta.value = text;
            ta.style.position = 'fixed';
            ta.style.opacity = '0';
            document.body.appendChild(ta);
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
        }
    }

    // ==================== UTILS ====================
    function showToast(msg) {
        const toast = document.getElementById('toastMsg');
        toast.innerText = msg;
        toast.classList.add('show');
        clearTimeout(toast._timeout);
        toast._timeout = setTimeout(() => toast.classList.remove('show'), 2500);
    }

    function formatTime(ts) {
        if (!ts) return 'غير معروف';
        const diff = Date.now() - ts;
        const mins = Math.floor(diff / 60000);
        const hours = Math.floor(diff / 3600000);
        const days = Math.floor(diff / 86400000);
        if (mins < 1) return 'الآن';
        if (mins < 60) return 'منذ ' + mins + ' د';
        if (hours < 24) return 'منذ ' + hours + ' س';
        if (days < 7) return 'منذ ' + days + ' يوم';
        return new Date(ts).toLocaleDateString('ar-SA');
    }

    console.log('💎 MNAENCA Chat Pro Ready ✨');
    console.log('📁 Cloudinary:', CLOUD_NAME);
    console.log('🔥 Firebase:', firebaseConfig.projectId);
    console.log('🎯 Features: Text | Image | Voice | Copy Single | Copy All');
</script>
</body>
</html>

# ═══════════════════════════════════════════════════════════
# 💎 7. explore.html - استكشاف
# ═══════════════════════════════════════════════════════════

def build_explore():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><title>💎 MNAENCA | استكشاف</title>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
<style>{COMMON_CSS}body{{min-height:100vh;overflow-y:auto;background:var(--bg)}}.header{{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(5,20,11,0.8);backdrop-filter:blur(20px);z-index:10}}.btn-back{{background:rgba(16,185,129,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px;text-decoration:none}}.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;padding:2px}}.thumb{{aspect-ratio:9/16;background:rgba(16,185,129,0.05);display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;overflow:hidden}}.thumb img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}.thumb i{{position:absolute;font-size:24px;color:#fff;z-index:1;opacity:0;transition:opacity 0.3s}}.thumb:hover i{{opacity:1}}.thumb .views{{position:absolute;bottom:4px;left:4px;font-size:10px;background:rgba(0,0,0,0.6);padding:2px 6px;border-radius:10px;z-index:2}}</style></head>
<body><div class="header"><a href="index.html" class="btn-back"><i class="fas fa-arrow-right"></i></a><h2><i class="fas fa-globe" style="color:var(--accent)"></i> استكشاف</h2></div><div class="grid" id="exploreGrid"><div class="spinner" style="grid-column:1/-1;padding:50px"></div></div>
<script src="firebase-config.js"></script>
<script>let currentUser=null;auth.onAuthStateChanged(async u=>{{if(!u){{window.location.href='auth.html';return}}currentUser=u;loadExplore()}});async function loadExplore(){{const snap=await db.ref('videos').once('value');const videos=snap.val()||{{}};const allVids=Object.entries(videos).map(([k,v])=>({{id:k,...v}})).sort((a,b)=>(b.likes||0)-(a.likes||0));const g=document.getElementById('exploreGrid');if(!allVids.length){{g.innerHTML='<div style="text-align:center;padding:60px;grid-column:1/-1;opacity:0.5"><i class="fas fa-video-slash" style="font-size:48px;color:var(--accent);margin-bottom:12px;display:block"></i><p>لا توجد فيديوهات</p></div>';return}}g.innerHTML=allVids.map(v=>`<div class="thumb" onclick="window.open('${{v.url}}','_blank')">${{v.thumbnail?`<img src="${{v.thumbnail}}" loading="lazy">`:''}}<i class="fas fa-play"></i><span class="views"><i class="fas fa-heart" style="color:#10b981;margin-right:4px"></i>${{v.likes||0}}</span></div>`).join('')}}</script></body></html>"""

# ═══════════════════════════════════════════════════════════
# 💎 8. notifications.html - إشعارات
# ═══════════════════════════════════════════════════════════

def build_notifications():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><title>💎 MNAENCA | إشعارات</title>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
<style>{COMMON_CSS}body{{min-height:100vh;overflow-y:auto;background:var(--bg)}}.header{{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(5,20,11,0.8);backdrop-filter:blur(20px);z-index:10}}.btn-back{{background:rgba(16,185,129,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px;text-decoration:none}}.notif-item{{display:flex;gap:12px;padding:14px 16px;border-bottom:1px solid var(--border);align-items:center;animation:fadeIn 0.3s ease}}.notif-icon{{width:44px;height:44px;border-radius:50%;background:rgba(16,185,129,0.1);display:flex;align-items:center;justify-content:center;font-size:18px;color:var(--accent);flex-shrink:0}}</style></head>
<body><div class="header"><a href="index.html" class="btn-back"><i class="fas fa-arrow-right"></i></a><h2><i class="fas fa-bell" style="color:var(--accent)"></i> الإشعارات</h2></div><div id="notifsList"><div class="spinner"></div></div>
<script src="firebase-config.js"></script>
<script>let currentUser=null;auth.onAuthStateChanged(async u=>{{if(!u){{window.location.href='auth.html';return}}currentUser=u;loadNotifs()}});async function loadNotifs(){{const snap=await db.ref('notifications/'+currentUser.uid).once('value');const ns=snap.val()||{{}};const c=document.getElementById('notifsList');const items=Object.values(ns).reverse();if(!items.length){{c.innerHTML='<div style="text-align:center;opacity:0.5;padding:60px"><i class="fas fa-bell" style="font-size:48px;color:var(--accent);margin-bottom:12px;display:block"></i><p>لا توجد إشعارات</p></div>';return}}c.innerHTML=items.map(n=>`<div class="notif-item"><div class="notif-icon"><i class="fas fa-bell"></i></div><div><div style="font-weight:600;font-size:14px">${{n.from||'مستخدم'}}</div><div style="font-size:12px;opacity:0.6;margin-top:3px">${{n.msg||''}}</div><div style="font-size:10px;opacity:0.3;margin-top:4px">${{new Date(n.timestamp).toLocaleString('ar-SA')}}</div></div></div>`).join('');await db.ref('notifications/'+currentUser.uid).remove()}}</script></body></html>"""

# ═══════════════════════════════════════════════════════════
# 💎 9. settings.html - إعدادات
# ═══════════════════════════════════════════════════════════

def build_settings():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><title>💎 MNAENCA | إعدادات</title>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
<style>{COMMON_CSS}body{{min-height:100vh;overflow-y:auto;background:var(--bg)}}.header{{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(5,20,11,0.8);backdrop-filter:blur(20px);z-index:10}}.btn-back{{background:rgba(16,185,129,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px;text-decoration:none}}.setting-item{{display:flex;justify-content:space-between;align-items:center;padding:16px;border-bottom:1px solid var(--border);cursor:pointer;transition:background 0.2s}}.setting-item:hover{{background:var(--glass)}}.setting-item i{{color:var(--accent);font-size:18px;width:30px}}.btn-danger{{background:rgba(239,68,68,0.2);border:1px solid rgba(239,68,68,0.3);color:#f87171;padding:12px 24px;border-radius:30px;cursor:pointer;font-size:14px;margin:20px auto;display:block;transition:all 0.3s}}.btn-danger:hover{{background:rgba(239,68,68,0.3);box-shadow:0 0 20px rgba(239,68,68,0.2)}}</style></head>
<body><div class="header"><a href="index.html" class="btn-back"><i class="fas fa-arrow-right"></i></a><h2><i class="fas fa-cog" style="color:var(--accent)"></i> الإعدادات</h2></div><div style="padding:8px 0"><div class="setting-item" onclick="window.location.href='profile.html'"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-user"></i><span>تعديل الملف الشخصي</span></div><i class="fas fa-chevron-left" style="opacity:0.5"></i></div><div class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-lock"></i><span>الخصوصية</span></div><i class="fas fa-chevron-left" style="opacity:0.5"></i></div><div class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-globe"></i><span>اللغة</span></div><span style="opacity:0.5;font-size:13px">العربية</span></div><div class="setting-item"><div style="display:flex;align-items:center;gap:12px"><i class="fas fa-info-circle"></i><span>حول التطبيق</span></div><span style="opacity:0.5;font-size:13px">v2026.4 💎</span></div><button class="btn-danger" onclick="if(confirm('هل أنت متأكد من تسجيل الخروج؟')){{auth.signOut();window.location.href='auth.html'}}"><i class="fas fa-sign-out-alt"></i> تسجيل الخروج</button></div>
<script src="firebase-config.js"></script><script>auth.onAuthStateChanged(u=>{{if(!u)window.location.href='auth.html'}});</script></body></html>"""

# ═══════════════════════════════════════════════════════════
# 💎 10. profile-videos.html - جميع الفيديوهات
# ═══════════════════════════════════════════════════════════

def build_profile_videos():
    """صفحة عرض جميع فيديوهات المستخدم"""
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💎 MNAENCA | جميع الفيديوهات</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{min-height:100vh;overflow-y:auto;background:var(--bg)}}
        .header{{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(5,20,11,0.8);backdrop-filter:blur(20px);z-index:10}}
        .btn-back{{background:rgba(16,185,129,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px;text-decoration:none}}
        .videos-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:3px;padding:8px}}
        .video-grid-item{{aspect-ratio:9/16;position:relative;overflow:hidden;cursor:pointer;background:#000;border-radius:4px}}
        .video-grid-item img{{width:100%;height:100%;object-fit:cover}}
        .video-grid-item .grid-overlay{{position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,0.7) 0%,transparent 50%);opacity:0;transition:opacity 0.3s}}
        .video-grid-item:hover .grid-overlay{{opacity:1}}
        .video-grid-item .grid-info{{position:absolute;bottom:8px;left:6px;right:6px;display:flex;justify-content:space-between;z-index:1;opacity:0;transition:opacity 0.3s}}
        .video-grid-item:hover .grid-info{{opacity:1}}
        .grid-info span{{font-size:10px;color:#fff;display:flex;align-items:center;gap:3px;background:rgba(0,0,0,0.5);padding:3px 8px;border-radius:10px}}
    </style>
</head>
<body>
<div class="header"><a href="profile.html" class="btn-back"><i class="fas fa-arrow-right"></i></a><h2><i class="fas fa-video" style="color:var(--accent)"></i> جميع الفيديوهات</h2></div>
<div class="videos-grid" id="videosGrid"><div class="spinner" style="grid-column:1/-1;padding:50px"></div></div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null;
    auth.onAuthStateChanged(async u=>{{
        if(!u){{window.location.href='auth.html';return}}
        currentUser=u;
        const params=new URLSearchParams(window.location.search);
        const uid=params.get('uid')||u.uid;
        const snap=await db.ref('videos').once('value');
        const allVideos=Object.entries(snap.val()||{{}}).map(([k,v])=>({{id:k,...v}}));
        const uvs=allVideos.filter(v=>v.sender===uid).sort((a,b)=>(b.timestamp||0)-(a.timestamp||0));
        const g=document.getElementById('videosGrid');
        if(!uvs.length){{g.innerHTML='<div style="text-align:center;padding:60px;grid-column:1/-1;opacity:0.5"><i class="fas fa-video-slash" style="font-size:48px;color:var(--accent);margin-bottom:12px;display:block"></i><p>لا توجد فيديوهات</p></div>';return}}
        g.innerHTML=uvs.map(v=>`<div class="video-grid-item" onclick="window.open('${{v.url}}','_blank')">${{v.thumbnail?`<img src="${{v.thumbnail}}" loading="lazy">`:''}}<div class="grid-overlay"></div><div class="grid-info"><span><i class="fas fa-heart"></i> ${{v.likes||0}}</span><span><i class="fas fa-comment"></i> ${{v.comments?Object.keys(v.comments).length:0}}</span></div></div>`).join('');
    }});
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 💎 MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  💎  MNAENCA 2026 - EMERALD GREEN LUXURY EDITION  ✨  ║
║     PROFILE 2.0 - Advanced Professional Version          ║
║     10 Files - 4000+ Lines                               ║
║                                                          ║
║  🎬 NATURAL VIDEO DISPLAY (No Zoom/Crop)               ║
║  📝 TEXT BELOW VIDEO                                    ║
║  📱 RESPONSIVE (Mobile + Landscape + Desktop)          ║
║  👥 Followers/Following Modal with Actions              ║
║  🎬 Video Player Modal (In-App)                         ║
║  📝 Posts System (Create/Like/Delete)                   ║
║  📊 Enhanced Animated Statistics                        ║
║  🎨 Premium Glass Effects                                ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    section("BUILDING FILES - إنشاء الملفات")
    
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
    write("profile-videos.html", build_profile_videos())
    
    for f in os.listdir(OUTPUT_DIR):
        src = os.path.join(OUTPUT_DIR, f)
        dst = os.path.join('.', f)
        if os.path.isfile(src):
            shutil.copy2(src, dst)
    
    print(f"""
{'='*60}
  💎 BUILD COMPLETE - تم الإنشاء بنجاح! ✨
{'='*60}

  📊 إحصائيات:
     • {TOTAL_LINES} إجمالي عدد الأسطر
     • 10 ملفات تم إنشاؤها

  📁 الملفات:
     1. firebase-config.js    → إعدادات Firebase + Cloudinary
     2. auth.html             → ✨ تسجيل دخول + اشتراك مطور
     3. index.html            → 🎬 الرئيسية (فيديو طبيعي + نص أسفل)
     4. profile.html          → ✨ ملف شخصي 2.0 متطور
     5. upload.html           → رفع فيديو مع تتبع التقدم
     6. chat.html             → دردشة خاصة
     7. explore.html          → استكشاف
     8. notifications.html    → الإشعارات
     9. settings.html         → إعدادات
     10. profile-videos.html  → صفحة جميع الفيديوهات

  🆕 التحسينات الجديدة:
     • 🎬 عرض الفيديو بشكله الطبيعي (contain) بدون تكبير
     • 📝 النص يظهر أسفل الفيديو في تخطيط منفصل
     • 📱 دعم كامل للعرض الأفقي (Landscape)
     • 🖥️ دعم الشاشات الكبيرة (Desktop)
     • 🔐 واجهة تسجيل دخول واشتراك مطورة بالكامل
     • 💬 نظام تعليقات متقدم مع ردود
     • 📤 نظام مشاركة متعدد المنصات
     • 👥 نافذة منبثقة للمتابعين مع أزرار متابعة
     • 📝 نظام منشورات متكامل
     • 🛡️ لوحة تحكم أدمن متكاملة

  💎 MNAENCA PROFILE 2.0 READY! ✨
{'='*60}
    """)

if __name__ == "__main__":
    main()
