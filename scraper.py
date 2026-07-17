import os

# اسم المشروع
PROJECT_NAME = "MyApp"
BASE_PATH = PROJECT_NAME

# هيكل المجلدات والملفات
STRUCTURE = {
    # ملفات جذر المشروع
    "build.gradle.kts": """plugins {
    id("com.android.application") version "8.2.2" apply false
    id("org.jetbrains.kotlin.android") version "1.9.22" apply false
}
""",
    "settings.gradle.kts": """pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}

dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.name = "MyApp"
include(":app")
""",
    "gradle.properties": """org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
android.useAndroidX=true
kotlin.code.style=official
android.nonTransitiveRClass=true
""",
    ".gitignore": """*.iml
.gradle
/local.properties
/.idea
.DS_Store
/build
/captures
.externalNativeBuild
.cxx
local.properties
""",

    # مجلد app
    "app/build.gradle.kts": """plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.example.myapp"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.example.myapp"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    kotlinOptions {
        jvmTarget = "17"
    }
}

dependencies {
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.appcompat:appcompat:1.6.1")
    implementation("com.google.android.material:material:1.11.0")
    implementation("androidx.constraintlayout:constraintlayout:2.1.4")
}
""",
    "app/proguard-rules.pro": """# Add project specific ProGuard rules here.
""",

    # AndroidManifest.xml
    "app/src/main/AndroidManifest.xml": """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:supportsRtl="true"
        android:theme="@style/Theme.MyApp">

        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

    </application>

</manifest>
""",

    # MainActivity.kt
    "app/src/main/java/com/example/myapp/MainActivity.kt": """package com.example.myapp

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
}
""",

    # Layout
    "app/src/main/res/layout/activity_main.xml": """<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout 
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#1a1a2e">

    <TextView
        android:id="@+id/titleText"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="🚀 أهلاً بك في تطبيقك!"
        android:textSize="28sp"
        android:textColor="#e94560"
        android:textStyle="bold"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
""",

    # Values
    "app/src/main/res/values/strings.xml": """<resources>
    <string name="app_name">تطبيقي الرائع</string>
</resources>
""",

    "app/src/main/res/values/colors.xml": """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="black">#FF000000</color>
    <color name="white">#FFFFFFFF</color>
</resources>
""",

    "app/src/main/res/values/themes.xml": """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="Theme.MyApp" parent="Theme.MaterialComponents.DayNight.DarkActionBar">
        <item name="colorPrimary">#e94560</item>
        <item name="colorPrimaryVariant">#0f3460</item>
        <item name="colorOnPrimary">#FFFFFF</item>
    </style>
</resources>
""",

    # GitHub Actions
    ".github/workflows/build-apk.yml": """name: Build APK

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v4

      - name: ☕ Set up JDK 17
        uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'

      - name: 📦 Cache Gradle
        uses: actions/cache@v4
        with:
          path: |
            ~/.gradle/caches
            ~/.gradle/wrapper
          key: \${{ runner.os }}-gradle-\${{ hashFiles('**/*.gradle*', '**/gradle-wrapper.properties') }}
          restore-keys: |
            \${{ runner.os }}-gradle-

      - name: 🔧 Grant execute permission for gradlew
        run: chmod +x gradlew

      - name: 🏗️ Build debug APK
        run: ./gradlew assembleDebug

      - name: 📤 Upload Debug APK
        uses: actions/upload-artifact@v4
        with:
          name: app-debug
          path: app/build/outputs/apk/debug/app-debug.apk
""",
}


def create_project():
    """خلق جميع مجلدات وملفات المشروع"""
    
    print("=" * 50)
    print("🚀 جاري خلق مشروع أندرويد كامل...")
    print("=" * 50)
    
    for file_path, content in STRUCTURE.items():
        full_path = os.path.join(BASE_PATH, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"✅ تم إنشاء: {file_path}")
    
    # إنشاء مجلد mipmap فارغ للآيكون (اختياري)
    os.makedirs(os.path.join(BASE_PATH, "app/src/main/res/mipmap-hdpi"), exist_ok=True)
    os.makedirs(os.path.join(BASE_PATH, "app/src/main/res/mipmap-mdpi"), exist_ok=True)
    os.makedirs(os.path.join(BASE_PATH, "app/src/main/res/mipmap-xhdpi"), exist_ok=True)
    os.makedirs(os.path.join(BASE_PATH, "app/src/main/res/mipmap-xxhdpi"), exist_ok=True)
    
    print("=" * 50)
    print(f"🎉 تم خلق المشروع بنجاح في مجلد: {BASE_PATH}/")
    print("📁 ارفع هذا المجلد إلى GitHub وسيبني تلقائياً!")
    print("=" * 50)


if __name__ == "__main__":
    create_project()
