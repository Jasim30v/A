#!/usr/bin/env python3
"""
👑 Dark AI Scraper - المرحلة الأولى
تحميل موقع ويب كامل وحفظه في مجلد website/
"""

import requests
from bs4 import BeautifulSoup
import os
import re
import json
import shutil
from urllib.parse import urljoin, urlparse
from pathlib import Path

# ═══════════════════════════ الإعدادات ═══════════════════════════
class ScraperConfig:
    # قم بتغيير هذه الإعدادات
    WEBSITE_URL = "https://example.com"  # رابط الموقع
    OUTPUT_FOLDER = "website"            # مجلد الحفظ
    
    # خيارات التحميل
    DOWNLOAD_CSS = True
    DOWNLOAD_JS = True
    DOWNLOAD_IMAGES = True
    DOWNLOAD_FONTS = True
    
    # إعدادات متقدمة
    USER_AGENT = "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36"
    TIMEOUT = 30
    MAX_RETRIES = 3
    
    @classmethod
    def load_from_env(cls):
        """تحميل الإعدادات من متغيرات البيئة"""
        if os.environ.get('WEBSITE_URL'):
            cls.WEBSITE_URL = os.environ['WEBSITE_URL']
        if os.environ.get('OUTPUT_FOLDER'):
            cls.OUTPUT_FOLDER = os.environ['OUTPUT_FOLDER']

# ═══════════════════════════ السكريبر ═══════════════════════════
class WebsiteScraper:
    def __init__(self, config):
        self.config = config
        self.session = self._create_session()
        self.downloaded_files = set()
        self.total_size = 0
        
    def _create_session(self):
        """إنشاء جلسة طلب"""
        session = requests.Session()
        session.headers.update({
            'User-Agent': self.config.USER_AGENT,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        })
        return session
    
    def _download_file(self, url, filepath):
        """تحميل ملف مع إعادة المحاولة"""
        if url in self.downloaded_files:
            return True
            
        for attempt in range(self.config.MAX_RETRIES):
            try:
                response = self.session.get(url, timeout=self.config.TIMEOUT, stream=True)
                response.raise_for_status()
                
                os.makedirs(os.path.dirname(filepath), exist_ok=True)
                
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                file_size = os.path.getsize(filepath)
                self.total_size += file_size
                self.downloaded_files.add(url)
                
                print(f"  ✅ {os.path.basename(filepath)} ({file_size:,} bytes)")
                return True
                
            except Exception as e:
                if attempt < self.config.MAX_RETRIES - 1:
                    print(f"  ⚠️ محاولة {attempt + 1} فشلت: {os.path.basename(filepath)}")
                    continue
                else:
                    print(f"  ❌ فشل: {os.path.basename(filepath)} - {str(e)[:50]}")
                    return False
        return False
    
    def _process_css(self, css_content, base_url, css_folder):
        """معالجة CSS وتحميل الموارد"""
        def replace_url(match):
            url = match.group(1).strip('\'"')
            if url.startswith(('data:', 'http://', 'https://')):
                if url.startswith('data:'):
                    return match.group(0)
                    
            full_url = urljoin(base_url, url)
            if urlparse(full_url).netloc != urlparse(base_url).netloc:
                return match.group(0)
            
            filename = os.path.basename(urlparse(full_url).path) or 'resource'
            local_path = os.path.join(css_folder, filename)
            
            if self._download_file(full_url, local_path):
                return f"url('{filename}')"
            return match.group(0)
        
        return re.sub(r'url\(([^)]+)\)', replace_url, css_content)
    
    def _process_html(self, html_content, base_url, page_folder):
        """معالجة HTML وتحميل الموارد"""
        soup = BeautifulSoup(html_content, 'lxml')
        
        # تحميل CSS
        if self.config.DOWNLOAD_CSS:
            for link in soup.find_all('link', rel='stylesheet'):
                href = link.get('href')
                if href:
                    full_url = urljoin(base_url, href)
                    filename = os.path.basename(urlparse(full_url).path) or 'style.css'
                    css_path = os.path.join(page_folder, 'css', filename)
                    
                    if self._download_file(full_url, css_path):
                        link['href'] = f"css/{filename}"
                        
                        # معالجة محتوى CSS
                        try:
                            with open(css_path, 'r', encoding='utf-8') as f:
                                css_content = f.read()
                            processed = self._process_css(css_content, full_url, os.path.join(page_folder, 'css'))
                            with open(css_path, 'w', encoding='utf-8') as f:
                                f.write(processed)
                        except:
                            pass
        
        # تحميل JavaScript
        if self.config.DOWNLOAD_JS:
            for script in soup.find_all('script', src=True):
                src = script.get('src')
                if src:
                    full_url = urljoin(base_url, src)
                    filename = os.path.basename(urlparse(full_url).path) or 'script.js'
                    js_path = os.path.join(page_folder, 'js', filename)
                    
                    if self._download_file(full_url, js_path):
                        script['src'] = f"js/{filename}"
        
        # تحميل الصور
        if self.config.DOWNLOAD_IMAGES:
            for img in soup.find_all('img', src=True):
                src = img.get('src')
                if src:
                    full_url = urljoin(base_url, src)
                    filename = os.path.basename(urlparse(full_url).path) or 'image.png'
                    img_path = os.path.join(page_folder, 'images', filename)
                    
                    if self._download_file(full_url, img_path):
                        img['src'] = f"images/{filename}"
        
        return str(soup)
    
    def scrape(self):
        """بدء التحميل"""
        print("=" * 60)
        print("👑 Dark AI Scraper - المرحلة الأولى")
        print("=" * 60)
        print(f"🌐 الموقع: {self.config.WEBSITE_URL}")
        print(f"📁 المجلد: {self.config.OUTPUT_FOLDER}")
        print("=" * 60)
        print()
        
        # تنظيف المجلد القديم
        if os.path.exists(self.config.OUTPUT_FOLDER):
            print("🧹 تنظيف المجلد القديم...")
            shutil.rmtree(self.config.OUTPUT_FOLDER)
        
        # تحميل الصفحة الرئيسية
        print("📥 تحميل الصفحة الرئيسية...")
        try:
            response = self.session.get(self.config.WEBSITE_URL, timeout=self.config.TIMEOUT)
            response.raise_for_status()
            html_content = response.text
            print(f"✅ تم التحميل ({len(html_content):,} bytes)")
        except Exception as e:
            print(f"❌ فشل تحميل الموقع: {e}")
            return False
        
        # معالجة وحفظ
        print("\n🔧 معالجة الملفات...")
        processed_html = self._process_html(html_content, self.config.WEBSITE_URL, self.config.OUTPUT_FOLDER)
        
        # حفظ الصفحة الرئيسية
        index_path = os.path.join(self.config.OUTPUT_FOLDER, 'index.html')
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(processed_html)
        
        # إحصائيات
        print("\n" + "=" * 60)
        print("📊 إحصائيات:")
        print(f"  📁 الملفات: {len(self.downloaded_files)}")
        print(f"  💾 الحجم: {self.total_size / 1024:.1f} KB")
        print("=" * 60)
        print("✅ تم الانتهاء - جاهز للمرحلة الثانية!")
        
        # حفظ ملف معلومات
        info = {
            'url': self.config.WEBSITE_URL,
            'files': len(self.downloaded_files),
            'size': self.total_size,
            'timestamp': __import__('datetime').datetime.now().isoformat()
        }
        with open(os.path.join(self.config.OUTPUT_FOLDER, 'scraper_info.json'), 'w') as f:
            json.dump(info, f, indent=2)
        
        return True

# ═══════════════════════════ التشغيل ═══════════════════════════
if __name__ == "__main__":
    ScraperConfig.load_from_env()
    
    if ScraperConfig.WEBSITE_URL == "https://example.com":
        print("⚠️ تحذير: لم تقم بتغيير رابط الموقع!")
        print("قم بتعديل WEBSITE_URL في الملف أو استخدم متغير البيئة WEBSITE_URL")
        exit(1)
    
    scraper = WebsiteScraper(ScraperConfig)
    success = scraper.scrape()
    exit(0 if success else 1)
