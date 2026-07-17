#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║  👑 JOKER SCRAPER - Android + Website Generator          ║
║  يحتوي على جميع ملفات الأندرويد كقوالب جاهزة                ║
║  يعمل مع main.yml + build-apk.yml لأي مشروع               ║
║  فقط غير CONFIG وسيبنى كل شيء تلقائياً                     ║
╚══════════════════════════════════════════════════════════════╝
"""

import os, json, shutil

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

def w(p, c):
    fp = os.path.join(OUTPUT_DIR, p)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, 'w', encoding='utf-8') as f: f.write(c)
    print(f"  ✅ {p}")

def am():  # AndroidManifest
    c = CONFIG
    return f'''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="{c['app_id']}">
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.DOWNLOAD_WITHOUT_NOTIFICATION"/>
<uses-permission android:name="android.permission.CAMERA"/>
<uses-permission android:name="android.permission.RECORD_AUDIO"/>
<uses-permission android:name="android.permission.VIBRATE"/>
<application android:allowBackup="true" android:icon="@mipmap/ic_launcher" android:roundIcon="@mipmap/ic_launcher_round" android:label="{c['app_name']}" android:supportsRtl="true" android:theme="@style/AppTheme.Splash" android:hardwareAccelerated="true" android:usesCleartextTraffic="true" android:requestLegacyExternalStorage="true" android:windowSoftInputMode="adjustResize" android:largeHeap="true" android:networkSecurityConfig="@xml/network_security_config">
<activity android:name=".MainActivity" android:configChanges="orientation|keyboardHidden|keyboard|screenSize|locale|smallestScreenSize|screenLayout|uiMode" android:label="{c['app_name']}" android:theme="@style/AppTheme.Splash" android:launchMode="singleTask" android:exported="true" android:screenOrientation="portrait">
<intent-filter><action android:name="android.intent.action.MAIN"/><category android:name="android.intent.category.LAUNCHER"/></intent-filter>
</activity>
<provider android:name="androidx.core.content.FileProvider" android:authorities="{c['app_id']}.fileprovider" android:exported="false" android:grantUriPermissions="true">
<meta-data android:name="android.support.FILE_PROVIDER_PATHS" android:resource="@xml/file_paths"/>
</provider>
</application>
</manifest>'''

def nc(): return '''<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
<base-config cleartextTrafficPermitted="true"><trust-anchors><certificates src="system"/></trust-anchors></base-config>
<domain-config cleartextTrafficPermitted="true">
<domain includeSubdomains="true">localhost</domain>
<domain includeSubdomains="true">firebaseio.com</domain>
<domain includeSubdomains="true">firebaseapp.com</domain>
<domain includeSubdomains="true">cloudinary.com</domain>
</domain-config>
</network-security-config>'''

def fp(): return '''<?xml version="1.0" encoding="utf-8"?>
<paths>
<external-path name="external" path="."/>
<external-files-path name="external_files" path="."/>
<cache-path name="cache" path="."/>
<files-path name="files" path="."/>
</paths>'''

def st():
    c = CONFIG
    return f'''<?xml version="1.0" encoding="utf-8"?>
<resources>
<style name="AppTheme" parent="Theme.AppCompat.Light.NoActionBar">
<item name="colorPrimary">{c['app_color']}</item>
<item name="colorPrimaryDark">{c['app_color']}</item>
<item name="colorAccent">{c['primary_color']}</item>
<item name="android:statusBarColor">{c['app_color']}</item>
<item name="android:navigationBarColor">{c['app_color']}</item>
<item name="android:windowBackground">@color/windowBackground</item>
</style>
<style name="AppTheme.Splash" parent="AppTheme">
<item name="android:windowBackground">@drawable/splash_background</item>
<item name="android:windowFullscreen">true</item>
</style>
</resources>'''

def co(): return f'''<?xml version="1.0" encoding="utf-8"?>
<resources><color name="windowBackground">{CONFIG['app_color']}</color></resources>'''

def sr(): return f'''<?xml version='1.0' encoding='utf-8'?>
<resources><string name="app_name">{CONFIG['app_name']}</string></resources>'''

def sp(): return f'''<?xml version="1.0" encoding="utf-8"?>
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
<item><shape><solid android:color="{CONFIG['app_color']}"/></shape></item>
<item android:gravity="center" android:width="250dp" android:height="250dp">
<bitmap android:src="@drawable/splash" android:gravity="center"/>
</item>
</layer-list>'''

def ib(): return f'''<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
<solid android:color="{CONFIG['app_color']}"/>
</shape>'''

def ai(): return '''<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
<background android:drawable="@drawable/ic_launcher_background"/>
<foreground android:drawable="@drawable/ic_launcher_foreground"/>
</adaptive-icon>'''

def ma():
    c = CONFIG
    return f'''package {c['app_id']};
import android.os.Bundle;
import android.view.WindowManager;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.CookieManager;
import android.webkit.WebChromeClient;
import android.webkit.WebViewClient;
import android.app.DownloadManager;
import android.net.Uri;
import android.os.Environment;
import android.widget.Toast;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {{
@Override
protected void onCreate(Bundle s) {{
super.onCreate(s);
getWindow().setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_ADJUST_RESIZE);
WebView wv = getBridge().getWebView();
if(wv != null) {{
WebSettings ws = wv.getSettings();
ws.setJavaScriptEnabled(true);
ws.setDomStorageEnabled(true);
ws.setAllowFileAccess(true);
ws.setAllowContentAccess(true);
ws.setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);
ws.setMediaPlaybackRequiresUserGesture(false);
ws.setLoadWithOverviewMode(true);
ws.setUseWideViewPort(true);
CookieManager.getInstance().setAcceptCookie(true);
CookieManager.getInstance().setAcceptThirdPartyCookies(wv, true);
wv.setDownloadListener((url, ua, cd, mt, cl) -> {{
DownloadManager.Request r = new DownloadManager.Request(Uri.parse(url));
r.setTitle("تحميل");
r.setDestinationInExternalPublicDir(Environment.DIRECTORY_DOWNLOADS, "download");
r.setNotificationVisibility(DownloadManager.Request.VISIBILITY_VISIBLE_NOTIFY_COMPLETED);
((DownloadManager)getSystemService(DOWNLOAD_SERVICE)).enqueue(r);
Toast.makeText(this, "✅ تم التحميل", Toast.LENGTH_SHORT).show();
}});
wv.setWebChromeClient(new WebChromeClient());
wv.setWebViewClient(new WebViewClient());
}}
}}
}}'''

def cc():
    return json.dumps({
        "appId": CONFIG['app_id'], "appName": CONFIG['app_name'],
        "webDir": "www", "bundledWebRuntime": False,
        "server": {"androidScheme": "https", "cleartext": True, "allowNavigation": ["*"]},
        "android": {"allowMixedContent": True, "keyboardStyle": "DARK"},
        "plugins": {"SplashScreen": {"launchShowDuration": 0, "launchAutoHide": True, "backgroundColor": CONFIG['app_color'], "androidSplashResourceName": "splash", "androidScaleType": "FIT_CENTER", "showSpinner": False}}
    }, indent=2)

def bg():
    c = CONFIG
    return f'''apply plugin: 'com.android.application'
android {{ namespace '{c['app_id']}'; compileSdk 34
defaultConfig {{ applicationId "{c['app_id']}"; minSdk 22; targetSdk 34; versionCode 1; versionName "{c['app_version']}" }}
compileOptions {{ sourceCompatibility JavaVersion.VERSION_17; targetCompatibility JavaVersion.VERSION_17 }} }}
dependencies {{ implementation 'androidx.appcompat:appcompat:1.6.1'; implementation 'androidx.core:core:1.12.0'; implementation 'androidx.webkit:webkit:1.9.0'; implementation project(':capacitor-android'); implementation project(':capacitor-cordova-android-plugins') }}'''

def fc():
    c = CONFIG
    return f'''const firebaseConfig={{apiKey:"{c['firebase_apiKey']}",authDomain:"{c['firebase_authDomain']}",databaseURL:"{c['firebase_databaseURL']}",projectId:"{c['firebase_projectId']}",storageBucket:"{c['firebase_storageBucket']}",messagingSenderId:"{c['firebase_messagingSenderId']}",appId:"{c['firebase_appId']}",measurementId:"{c['firebase_measurementId']}"}};
firebase.initializeApp(firebaseConfig);const auth=firebase.auth();const db=firebase.database();
const CLOUD_NAME="{c['cloudinary_cloud_name']}";const UPLOAD_PRESET="{c['cloudinary_upload_preset']}";
const ADMIN_EMAILS={json.dumps(c['admin_emails'])};const APP_NAME="{c['app_name']}";
console.log("👑 "+APP_NAME+" Ready");'''

def ix():
    c = CONFIG
    return f'''<!DOCTYPE html><html lang="ar" dir="rtl"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>👑 {c['app_name']}</title>
<style>*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:'Segoe UI',sans-serif;background:{c['app_color']};color:#fff;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center}}h1{{background:linear-gradient(to bottom,#fff,{c['primary_color']});-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-size:48px}}</style>
</head><body><div><h1>👑 {c['app_name']}</h1><p>v{c['app_version']}</p></div></body></html>'''

def main():
    print(f"\n👑 JOKER SCRAPER - {CONFIG['app_name']} v{CONFIG['app_version']}\n")
    if os.path.exists(OUTPUT_DIR): shutil.rmtree(OUTPUT_DIR)
    
    b = "android/app/src/main"
    w(f"{b}/AndroidManifest.xml", am())
    w(f"{b}/res/xml/network_security_config.xml", nc())
    w(f"{b}/res/xml/file_paths.xml", fp())
    w(f"{b}/res/values/styles.xml", st())
    w(f"{b}/res/values/colors.xml", co())
    w(f"{b}/res/values/strings.xml", sr())
    w(f"{b}/res/drawable/splash_background.xml", sp())
    w(f"{b}/res/drawable/ic_launcher_background.xml", ib())
    w(f"{b}/res/mipmap-anydpi-v26/ic_launcher.xml", ai())
    w(f"{b}/res/mipmap-anydpi-v26/ic_launcher_round.xml", ai())
    w(f"android/app/src/main/java/{CONFIG['app_id'].replace('.','/')}/MainActivity.java", ma())
    w("capacitor.config.json", cc())
    w("android/build.gradle", bg())
    w("firebase-config.js", fc())
    w("index.html", ix())
    
    ww = os.path.join(OUTPUT_DIR, "www")
    os.makedirs(ww, exist_ok=True)
    for f in ["firebase-config.js", "index.html"]:
        s = os.path.join(OUTPUT_DIR, f)
        if os.path.exists(s): shutil.copy2(s, os.path.join(ww, f))
    for f in os.listdir(ww): shutil.copy2(os.path.join(ww, f), f)
    
    t = sum(1 for _ in os.walk(OUTPUT_DIR) for __ in _[2])
    print(f"\n✅ Done - {t} files\n")

if __name__ == "__main__": main()
