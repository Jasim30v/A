#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║  👑 JOKER SCRAPER - Android + Website Generator          ║
║  يحتوي على جميع ملفات الأندرويد كقوالب جاهزة                ║
║  يعمل مع build-apk.yml لأي مشروع                          ║
║  فقط غير المتغيرات في CONFIG وسيبنى كل شيء تلقائياً         ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import json

# ═══════════════════════════════════════════════════════════════
# 👑 CONFIGURATION - غير هذه المتغيرات فقط لكل مشروع
# ═══════════════════════════════════════════════════════════════

CONFIG = {
    "app_name": "MNAENCA",
    "app_id": "com.mnaenca.app",
    "app_version": "1.0.0",
    "app_color": "#020617",
    "firebase_apiKey": "AIzaSyCqDvG98pEqmZHKZienquJEq6gS1kNjK8M",
    "firebase_authDomain": "muvg-42126.firebaseapp.com",
    "firebase_databaseURL": "https://muvg-42126-default-rtdb.europe-west1.firebasedatabase.app",
    "firebase_projectId": "muvg-42126",
    "firebase_storageBucket": "muvg-42126.firebasestorage.app",
    "firebase_messagingSenderId": "514075097173",
    "firebase_appId": "1:514075097173:web:6fab4e9598549691cc7cdc",
    "firebase_measurementId": "G-4VP8E6WJ48",
    "cloudinary_cloud_name": "dmqyd0haj",
    "cloudinary_upload_preset": "s3_gok",
    "admin_emails": ["jasim28v@gmail.com"],
    "primary_color": "#0ea5e9",
    "secondary_color": "#06b6d4",
}

OUTPUT_DIR = "output"

# ═══════════════════════════════════════════════════════════════
# 🤖 ANDROID FILES - قوالب الأندرويد الكاملة
# ═══════════════════════════════════════════════════════════════

def generate_android_manifest():
    """ملف AndroidManifest.xml"""
    return f'''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="{CONFIG['app_id']}">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.DOWNLOAD_WITHOUT_NOTIFICATION" />
    <uses-permission android:name="android.permission.ACCESS_DOWNLOAD_MANAGER" />
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.RECORD_AUDIO" />
    <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.WAKE_LOCK" />

    <uses-feature android:name="android.hardware.camera" android:required="false" />
    <uses-feature android:name="android.hardware.camera.autofocus" android:required="false" />
    <uses-feature android:name="android.hardware.microphone" android:required="false" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:label="{CONFIG['app_name']}"
        android:supportsRtl="true"
        android:theme="@style/AppTheme.Splash"
        android:hardwareAccelerated="true"
        android:usesCleartextTraffic="true"
        android:requestLegacyExternalStorage="true"
        android:windowSoftInputMode="adjustResize"
        android:largeHeap="true"
        android:networkSecurityConfig="@xml/network_security_config">

        <activity
            android:name=".MainActivity"
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|locale|smallestScreenSize|screenLayout|uiMode"
            android:label="{CONFIG['app_name']}"
            android:theme="@style/AppTheme.Splash"
            android:launchMode="singleTask"
            android:exported="true"
            android:screenOrientation="portrait">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="{CONFIG['app_id']}" />
            </intent-filter>
        </activity>

        <provider
            android:name="androidx.core.content.FileProvider"
            android:authorities="{CONFIG['app_id']}.fileprovider"
            android:exported="false"
            android:grantUriPermissions="true">
            <meta-data
                android:name="android.support.FILE_PROVIDER_PATHS"
                android:resource="@xml/file_paths" />
        </provider>
    </application>
</manifest>'''

def generate_network_security_config():
    """ملف network_security_config.xml"""
    return '''<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <base-config cleartextTrafficPermitted="true">
        <trust-anchors>
            <certificates src="system" />
        </trust-anchors>
    </base-config>
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">localhost</domain>
        <domain includeSubdomains="true">10.0.2.2</domain>
        <domain includeSubdomains="true">firebaseio.com</domain>
        <domain includeSubdomains="true">firebaseapp.com</domain>
        <domain includeSubdomains="true">cloudinary.com</domain>
        <domain includeSubdomains="true">res.cloudinary.com</domain>
    </domain-config>
</network-security-config>'''

def generate_file_paths():
    """ملف file_paths.xml"""
    return '''<?xml version="1.0" encoding="utf-8"?>
<paths>
    <external-path name="external" path="." />
    <external-files-path name="external_files" path="." />
    <cache-path name="cache" path="." />
    <external-cache-path name="external_cache" path="." />
    <files-path name="files" path="." />
</paths>'''

def generate_styles():
    """ملف styles.xml"""
    return f'''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="AppTheme" parent="Theme.AppCompat.Light.NoActionBar">
        <item name="colorPrimary">{CONFIG['app_color']}</item>
        <item name="colorPrimaryDark">{CONFIG['app_color']}</item>
        <item name="colorAccent">{CONFIG['primary_color']}</item>
        <item name="android:statusBarColor">{CONFIG['app_color']}</item>
        <item name="android:navigationBarColor">{CONFIG['app_color']}</item>
        <item name="android:windowBackground">@color/windowBackground</item>
        <item name="android:windowSoftInputMode">adjustResize</item>
    </style>

    <style name="AppTheme.Splash" parent="AppTheme">
        <item name="android:windowBackground">@drawable/splash_background</item>
        <item name="android:statusBarColor">{CONFIG['app_color']}</item>
        <item name="android:navigationBarColor">{CONFIG['app_color']}</item>
        <item name="android:windowFullscreen">true</item>
        <item name="android:windowContentOverlay">@null</item>
        <item name="android:backgroundDimEnabled">false</item>
    </style>
</resources>'''

def generate_colors():
    """ملف colors.xml"""
    return f'''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="windowBackground">{CONFIG['app_color']}</color>
    <color name="primaryColor">{CONFIG['app_color']}</color>
    <color name="splashBackground">{CONFIG['app_color']}</color>
    <color name="ic_launcher_background">{CONFIG['app_color']}</color>
</resources>'''

def generate_strings():
    """ملف strings.xml"""
    return f'''<?xml version='1.0' encoding='utf-8'?>
<resources>
    <string name="app_name">{CONFIG['app_name']}</string>
    <string name="title_activity_main">{CONFIG['app_name']}</string>
    <string name="package_name">{CONFIG['app_id']}</string>
</resources>'''

def generate_splash_background():
    """ملف splash_background.xml"""
    return f'''<?xml version="1.0" encoding="utf-8"?>
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item>
        <shape>
            <solid android:color="{CONFIG['app_color']}" />
        </shape>
    </item>
    <item
        android:gravity="center"
        android:width="250dp"
        android:height="250dp">
        <bitmap
            android:src="@drawable/splash"
            android:gravity="center"
            android:filter="true" />
    </item>
</layer-list>'''

def generate_ic_launcher_background():
    """ملف ic_launcher_background.xml"""
    return f'''<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="{CONFIG['app_color']}"/>
</shape>'''

def generate_ic_launcher_adaptive():
    """ملف ic_launcher.xml للأيقونة التكيفية"""
    return '''<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background"/>
    <foreground android:drawable="@drawable/ic_launcher_foreground"/>
</adaptive-icon>'''

def generate_ic_launcher_round_adaptive():
    """ملف ic_launcher_round.xml للأيقونة التكيفية"""
    return '''<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background"/>
    <foreground android:drawable="@drawable/ic_launcher_foreground"/>
</adaptive-icon>'''

def generate_main_activity():
    """ملف MainActivity.java"""
    return f'''package {CONFIG['app_id']};

import android.os.Bundle;
import android.os.Build;
import android.view.WindowManager;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.webkit.DownloadListener;
import android.webkit.URLUtil;
import android.webkit.CookieManager;
import android.webkit.WebChromeClient;
import android.app.DownloadManager;
import android.net.Uri;
import android.os.Environment;
import android.content.Intent;
import android.content.ActivityNotFoundException;
import android.widget.Toast;
import androidx.core.view.WindowCompat;
import com.getcapacitor.BridgeActivity;
import com.getcapacitor.Plugin;

public class MainActivity extends BridgeActivity {{

    @Override
    protected void onCreate(Bundle savedInstanceState) {{
        super.onCreate(savedInstanceState);

        // إعدادات الكيبورد
        getWindow().setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_ADJUST_RESIZE);

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {{
            WindowCompat.setDecorFitsSystemWindows(getWindow(), false);
        }}

        // إعداد WebView للتحميل
        setupWebView();
    }}

    private void setupWebView() {{
        WebView webView = getBridge().getWebView();

        if (webView != null) {{
            WebSettings settings = webView.getSettings();

            // الإعدادات الأساسية
            settings.setJavaScriptEnabled(true);
            settings.setDomStorageEnabled(true);
            settings.setDatabaseEnabled(true);
            settings.setAllowFileAccess(true);
            settings.setAllowContentAccess(true);
            settings.setAllowFileAccessFromFileURLs(true);
            settings.setAllowUniversalAccessFromFileURLs(true);
            settings.setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);
            settings.setLoadWithOverviewMode(true);
            settings.setUseWideViewPort(true);
            settings.setSupportZoom(true);
            settings.setBuiltInZoomControls(true);
            settings.setDisplayZoomControls(false);
            settings.setCacheMode(WebSettings.LOAD_DEFAULT);
            settings.setMediaPlaybackRequiresUserGesture(false);

            // كوكيز
            CookieManager.getInstance().setAcceptCookie(true);
            CookieManager.getInstance().setAcceptThirdPartyCookies(webView, true);

            // دعم التحميل
            webView.setDownloadListener(new DownloadListener() {{
                @Override
                public void onDownloadStart(String url, String userAgent, String contentDisposition, String mimetype, long contentLength) {{
                    try {{
                        DownloadManager.Request request = new DownloadManager.Request(Uri.parse(url));
                        request.setMimeType(mimetype);
                        request.addRequestHeader("User-Agent", userAgent);
                        request.setDescription("جاري التحميل...");
                        request.setTitle(URLUtil.guessFileName(url, contentDisposition, mimetype));
                        request.allowScanningByMediaScanner();
                        request.setNotificationVisibility(DownloadManager.Request.VISIBILITY_VISIBLE_NOTIFY_COMPLETED);
                        request.setDestinationInExternalPublicDir(Environment.DIRECTORY_DOWNLOADS, URLUtil.guessFileName(url, contentDisposition, mimetype));

                        DownloadManager dm = (DownloadManager) getSystemService(DOWNLOAD_SERVICE);
                        dm.enqueue(request);
                        Toast.makeText(MainActivity.this, "✅ بدء التحميل...", Toast.LENGTH_SHORT).show();
                    }} catch (Exception e) {{
                        // فتح الرابط في المتصفح كبديل
                        try {{
                            Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
                            startActivity(intent);
                        }} catch (ActivityNotFoundException ex) {{
                            Toast.makeText(MainActivity.this, "❌ لا يوجد متصفح", Toast.LENGTH_SHORT).show();
                        }}
                    }}
                }}
            }});

            webView.setWebChromeClient(new WebChromeClient());
            webView.setWebViewClient(new WebViewClient());
        }}
    }}
}}'''

def generate_capacitor_config():
    """ملف capacitor.config.json"""
    return json.dumps({
        "appId": CONFIG['app_id'],
        "appName": CONFIG['app_name'],
        "webDir": "www",
        "bundledWebRuntime": False,
        "server": {
            "androidScheme": "https",
            "allowNavigation": ["*"],
            "cleartext": True,
            "hostname": "localhost"
        },
        "android": {
            "allowMixedContent": True,
            "captureInput": True,
            "webContentsDebuggingEnabled": True,
            "keyboardStyle": "DARK",
            "resizeOnFullScreen": True,
            "useLegacyBridge": False
        },
        "plugins": {
            "SplashScreen": {
                "launchShowDuration": 0,
                "launchAutoHide": True,
                "launchFadeOutDuration": 0,
                "backgroundColor": CONFIG['app_color'],
                "androidSplashResourceName": "splash",
                "androidScaleType": "FIT_CENTER",
                "showSpinner": False,
                "splashFullScreen": True,
                "splashImmersive": True
            },
            "Keyboard": {
                "resize": "body",
                "style": "DARK",
                "resizeOnFullScreen": True
            },
            "StatusBar": {
                "style": "LIGHT",
                "backgroundColor": CONFIG['app_color'],
                "overlaysWebView": False
            }
        }
    }, indent=2)

def generate_build_gradle():
    """ملف build.gradle"""
    return f'''apply plugin: 'com.android.application'

android {{
    namespace '{CONFIG['app_id']}'
    compileSdk 34

    defaultConfig {{
        applicationId "{CONFIG['app_id']}"
        minSdk 22
        targetSdk 34
        versionCode 1
        versionName "{CONFIG['app_version']}"
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }}

    buildTypes {{
        release {{
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }}
    }}

    compileOptions {{
        sourceCompatibility JavaVersion.VERSION_17
        targetCompatibility JavaVersion.VERSION_17
    }}
}}

dependencies {{
    implementation fileTree(dir: 'libs', include: ['*.jar'])
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'androidx.core:core:1.12.0'
    implementation 'androidx.webkit:webkit:1.9.0'
    implementation project(':capacitor-android')
    implementation project(':capacitor-cordova-android-plugins')
}}'''

def generate_gradle_properties():
    """ملف gradle.properties"""
    return '''org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
android.useAndroidX=true
android.enableJetifier=true
kotlin.code.style=official
android.nonTransitiveRClass=true'''

def generate_proguard_rules():
    """ملف proguard-rules.pro"""
    return '''# Add project specific ProGuard rules here.
-keep class com.getcapacitor.** { *; }
-dontwarn com.getcapacitor.**
-keepattributes *Annotation*
-keepattributes SourceFile,LineNumberTable
-keep public class * extends android.app.Activity
-keep public class * extends android.app.Application
-keep public class * extends android.app.Service
-keep public class * extends android.content.BroadcastReceiver
-keep public class * extends android.content.ContentProvider
-keep class * implements android.os.Parcelable { public static final android.os.Parcelable$Creator *; }'''

def generate_firebase_config_js():
    """ملف firebase-config.js للموقع"""
    fb = CONFIG
    return f'''// 👑 {fb['app_name']} - Firebase Configuration
const firebaseConfig = {{
    apiKey: "{fb['firebase_apiKey']}",
    authDomain: "{fb['firebase_authDomain']}",
    databaseURL: "{fb['firebase_databaseURL']}",
    projectId: "{fb['firebase_projectId']}",
    storageBucket: "{fb['firebase_storageBucket']}",
    messagingSenderId: "{fb['firebase_messagingSenderId']}",
    appId: "{fb['firebase_appId']}",
    measurementId: "{fb['firebase_measurementId']}"
}};

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

const CLOUD_NAME = "{fb['cloudinary_cloud_name']}";
const UPLOAD_PRESET = "{fb['cloudinary_upload_preset']}";
const ADMIN_EMAILS = {json.dumps(fb['admin_emails'])};
const APP_NAME = "{fb['app_name']}";
const APP_VERSION = "{fb['app_version']}";
const PRIMARY_COLOR = "{fb['primary_color']}";

console.log('👑 %c'+APP_NAME+' v'+APP_VERSION+' Ready', 'color: '+PRIMARY_COLOR+'; font-size: 16px; font-weight: bold;');'''

# ═══════════════════════════════════════════════════════════════
# 🛠️ HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════

def write(path, content):
    """كتابة ملف"""
    full_path = os.path.join(OUTPUT_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ {path}")

# ═══════════════════════════════════════════════════════════════
# 👑 MAIN GENERATOR
# ═══════════════════════════════════════════════════════════════

def main():
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║  👑 JOKER SCRAPER - Android + Website Generator           ║
║  {CONFIG['app_name']} v{CONFIG['app_version']}
║  {CONFIG['app_id']}
╚══════════════════════════════════════════════════════════════╝
""")

    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 📁 1. ملفات الأندرويد
    print("🤖 [1/3] إنشاء ملفات الأندرويد...")
    
    ANDROID_BASE = "android/app/src/main"
    
    write(f"{ANDROID_BASE}/AndroidManifest.xml", generate_android_manifest())
    write(f"{ANDROID_BASE}/res/xml/network_security_config.xml", generate_network_security_config())
    write(f"{ANDROID_BASE}/res/xml/file_paths.xml", generate_file_paths())
    write(f"{ANDROID_BASE}/res/values/styles.xml", generate_styles())
    write(f"{ANDROID_BASE}/res/values/colors.xml", generate_colors())
    write(f"{ANDROID_BASE}/res/values/strings.xml", generate_strings())
    write(f"{ANDROID_BASE}/res/drawable/splash_background.xml", generate_splash_background())
    write(f"{ANDROID_BASE}/res/drawable/ic_launcher_background.xml", generate_ic_launcher_background())
    write(f"{ANDROID_BASE}/res/mipmap-anydpi-v26/ic_launcher.xml", generate_ic_launcher_adaptive())
    write(f"{ANDROID_BASE}/res/mipmap-anydpi-v26/ic_launcher_round.xml", generate_ic_launcher_round_adaptive())
    
    # MainActivity.java
    java_path = f"android/app/src/main/java/{CONFIG['app_id'].replace('.', '/')}/MainActivity.java"
    write(java_path, generate_main_activity())
    
    # 📁 2. ملفات Capacitor + Gradle
    print("\n⚙️ [2/3] إنشاء ملفات البناء...")
    
    write("capacitor.config.json", generate_capacitor_config())
    write("android/build.gradle", generate_build_gradle())
    write("android/gradle.properties", generate_gradle_properties())
    write("android/proguard-rules.pro", generate_proguard_rules())
    
    # 📁 3. ملفات الموقع الأساسية
    print("\n🌐 [3/3] إنشاء ملفات الموقع...")
    
    write("firebase-config.js", generate_firebase_config_js())
    
    # ملاحظة: ملفات HTML تضعها هنا أو تبنيها حسب مشروعك
    # هذا مثال لملف index.html بسيط
    write("index.html", f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>👑 {CONFIG['app_name']}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', sans-serif;
            background: {CONFIG['app_color']};
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            text-align: center;
        }}
        h1 {{
            background: linear-gradient(to bottom, #fff, {CONFIG['primary_color']});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 48px;
        }}
    </style>
</head>
<body>
    <div>
        <h1>👑 {CONFIG['app_name']}</h1>
        <p>v{CONFIG['app_version']}</p>
        <p>تم البناء بواسطة Joker Scraper 🃏</p>
    </div>
</body>
</html>""")

    # 📁 نسخ الملفات لمجلد www
    www_path = os.path.join(OUTPUT_DIR, "www")
    os.makedirs(www_path, exist_ok=True)
    
    for f in ["firebase-config.js", "index.html"]:
        src = os.path.join(OUTPUT_DIR, f)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(www_path, f))
    
    # 📊 إحصائيات
    total_files = sum(1 for _ in os.walk(OUTPUT_DIR) for f in _[2])
    total_size = sum(os.path.getsize(os.path.join(root, f)) 
                    for root, _, files in os.walk(OUTPUT_DIR) for f in files)
    
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║  ✅ BUILD COMPLETE - تم البناء بنجاح!                      ║
╠══════════════════════════════════════════════════════════════╣
║  📱 {CONFIG['app_name']} v{CONFIG['app_version']}
║  📁 {total_files} ملفات تم إنشاؤها
║  💾 {total_size/1024:.1f} KB الحجم الإجمالي
║  📂 {OUTPUT_DIR}/ ← جميع الملفات هنا
╠══════════════════════════════════════════════════════════════╣
║  🃏 JOKER READY FOR build-apk.yml                          ║
╚══════════════════════════════════════════════════════════════╝
""")

if __name__ == "__main__":
    main()
