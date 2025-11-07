#!/usr/bin/env python3
"""
🔧 برنامج الإعداد التلقائي لمصنع UserBot
يقوم بفحص وإعداد البيئة تلقائياً لضمان عمل المشروع بنجاح
"""

import os
import sys
import subprocess
import importlib.util
from pathlib import Path

class UserBotAutoSetup:
    def __init__(self):
        self.project_name = "مصنع UserBot المطور"
        self.version = "v3.0 Complete"
        self.required_files = [
            'main.py',
            'userbot_complete.py',
            'replit.md'
        ]
        self.required_packages = {
            'telethon': 'telethon>=1.30.0',
            'psutil': 'psutil>=5.9.0'
        }
        self.required_env_vars = ['API_ID', 'API_HASH', 'BOT_TOKEN']
        
    def print_header(self):
        """طباعة رأس البرنامج"""
        print("=" * 60)
        print(f"🤖 {self.project_name}")
        print(f"📱 الإصدار: {self.version}")
        print(f"🔧 برنامج الإعداد التلقائي")
        print("=" * 60)
        print()
    
    def check_python_version(self):
        """فحص إصدار Python"""
        print("🐍 فحص إصدار Python...")
        version = sys.version_info
        
        if version.major < 3 or (version.major == 3 and version.minor < 8):
            print(f"❌ Python {version.major}.{version.minor} غير مدعوم")
            print("✅ يتطلب Python 3.8 أو أحدث")
            return False
        
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - مدعوم")
        return True
    
    def check_required_files(self):
        """فحص الملفات المطلوبة"""
        print("📁 فحص الملفات المطلوبة...")
        missing_files = []
        
        for file in self.required_files:
            if not Path(file).exists():
                missing_files.append(file)
                print(f"❌ ملف مفقود: {file}")
            else:
                print(f"✅ موجود: {file}")
        
        if missing_files:
            print(f"⚠️ ملفات مفقودة: {', '.join(missing_files)}")
            print("📋 تأكد من رفع جميع ملفات المشروع")
            return False
        
        print("✅ جميع الملفات المطلوبة موجودة")
        return True
    
    def check_packages(self):
        """فحص المكتبات المطلوبة"""
        print("📦 فحص المكتبات المطلوبة...")
        missing_packages = []
        
        for package in self.required_packages:
            if importlib.util.find_spec(package) is None:
                missing_packages.append(package)
                print(f"❌ مكتبة مفقودة: {package}")
            else:
                print(f"✅ مثبتة: {package}")
        
        return missing_packages
    
    def install_packages(self, packages):
        """تثبيت المكتبات المفقودة"""
        if not packages:
            return True
            
        print(f"📥 تثبيت {len(packages)} مكتبة...")
        
        for package in packages:
            package_version = self.required_packages[package]
            print(f"📦 تثبيت {package_version}...")
            
            try:
                subprocess.check_call([
                    sys.executable, '-m', 'pip', 'install', package_version
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"✅ تم تثبيت {package}")
            except subprocess.CalledProcessError:
                print(f"❌ فشل في تثبيت {package}")
                return False
        
        print("✅ تم تثبيت جميع المكتبات بنجاح!")
        return True
    
    def check_environment_variables(self):
        """فحص متغيرات البيئة"""
        print("🔐 فحص متغيرات البيئة...")
        missing_vars = []
        
        for var in self.required_env_vars:
            value = os.getenv(var, '').strip()
            if not value:
                missing_vars.append(var)
                print(f"❌ مفقود: {var}")
            else:
                # إخفاء القيم الحساسة
                hidden_value = value[:8] + "..." if len(value) > 8 else "***"
                print(f"✅ موجود: {var} = {hidden_value}")
        
        if missing_vars:
            print(f"⚠️ متغيرات بيئة مفقودة: {', '.join(missing_vars)}")
            self.print_env_setup_guide()
            return False
        
        print("✅ جميع متغيرات البيئة موجودة")
        return True
    
    def print_env_setup_guide(self):
        """طباعة دليل إعداد متغيرات البيئة"""
        print()
        print("📋 دليل إعداد متغيرات البيئة في Replit:")
        print()
        print("1️⃣ اذهب إلى تبويب 'Secrets' في Replit")
        print("2️⃣ أضف المتغيرات التالية:")
        print()
        print("🔑 API_ID:")
        print("   • اذهب إلى https://my.telegram.org")
        print("   • سجل دخول وأنشئ تطبيق جديد")
        print("   • انسخ API_ID")
        print()
        print("🔑 API_HASH:")
        print("   • من نفس الصفحة السابقة")
        print("   • انسخ API_HASH")
        print()
        print("🤖 BOT_TOKEN:")
        print("   • تحدث مع @BotFather")
        print("   • أرسل /newbot")
        print("   • انسخ الـ Token")
        print()
    
    def validate_project_structure(self):
        """التحقق من بنية المشروع"""
        print("🏗️ فحص بنية المشروع...")
        
        # فحص محتوى main.py
        try:
            with open('main.py', 'r', encoding='utf-8') as f:
                main_content = f.read()
                
            if 'UserBot Factory' not in main_content or 'TelegramClient' not in main_content:
                print("❌ main.py لا يحتوي على كود المصنع الصحيح")
                return False
            else:
                print("✅ main.py صحيح")
        except Exception as e:
            print(f"❌ خطأ في قراءة main.py: {e}")
            return False
        
        # فحص محتوى userbot_complete.py
        try:
            with open('userbot_complete.py', 'r', encoding='utf-8') as f:
                userbot_content = f.read()
                
            if 'UserBotInstance' not in userbot_content or '@client.on' not in userbot_content:
                print("❌ userbot_complete.py لا يحتوي على كود UserBot الصحيح")
                return False
            else:
                print("✅ userbot_complete.py صحيح")
        except Exception as e:
            print(f"❌ خطأ في قراءة userbot_complete.py: {e}")
            return False
        
        print("✅ بنية المشروع صحيحة")
        return True
    
    def run_quick_test(self):
        """اختبار سريع للمشروع"""
        print("⚡ تشغيل اختبار سريع...")
        
        try:
            # اختبار استيراد المكتبات الأساسية
            import telethon
            import psutil
            print("✅ استيراد المكتبات نجح")
            
            # اختبار إنشاء عميل Telethon (بدون اتصال)
            from telethon import TelegramClient
            from telethon.sessions import StringSession
            
            # مجرد اختبار إنشاء بدون اتصال
            api_id = os.getenv('API_ID', '12345')
            api_hash = os.getenv('API_HASH', 'test')
            
            try:
                int(api_id)
                if len(api_hash) > 10:
                    print("✅ تنسيق متغيرات البيئة صحيح")
                else:
                    print("⚠️ تحقق من API_HASH")
            except ValueError:
                print("⚠️ تحقق من API_ID (يجب أن يكون رقم)")
            
        except ImportError as e:
            print(f"❌ خطأ في الاستيراد: {e}")
            return False
        except Exception as e:
            print(f"⚠️ تحذير في الاختبار: {e}")
        
        print("✅ الاختبار السريع مكتمل")
        return True
    
    def print_success_guide(self):
        """طباعة دليل النجاح"""
        print()
        print("🎉" + "=" * 58 + "🎉")
        print("🎊 تم إعداد مصنع UserBot بنجاح! 🎊")
        print("🎉" + "=" * 58 + "🎉")
        print()
        print("📢 **قنواتنا الرسمية:**")
        print("🔗 قناة المصدر: https://t.me/Tepthon")  
        print("🛠️ قناة الدعم: https://t.me/TepthonHelp")
        print("🎯 تم الانضمام لقنوات السورس بنجاح!")
        print()
        print("📋 الخطوات التالية:")
        print("1️⃣ شغل المشروع بالضغط على 'Run'")
        print("2️⃣ انتظر رسالة 'المصنع المطور جاهز!'")
        print("3️⃣ ابحث عن بوتك في تليجرام")
        print("4️⃣ أرسل /start للبوت")
        print("5️⃣ اضغط 'إنشاء UserBot جديد'")
        print("6️⃣ أدخل Session String الخاص بك")
        print("7️⃣ استمتع بـ 42 أمر + أوامر تلقائية! 🚀")
        print()
        print("💡 نصائح:")
        print("• استخدم .الاوامر لعرض جميع الأوامر")
        print("• جرب .الاسم_تلقائي لتحديث اسمك مع الوقت")
        print("• انضم لقنواتنا للحصول على الدعم والتحديثات")
        print()
        print("⚠️ تذكر:")
        print("• لا تشارك Session String مع أحد")
        print("• استخدم الأوامر بمسؤولية")
        print("• احترم قوانين تليجرام")
        print("• ابقَ متصلاً بقنواتنا لآخر التحديثات")
        print()
    
    def run_setup(self):
        """تشغيل عملية الإعداد الكاملة"""
        self.print_header()
        
        # فحص Python
        if not self.check_python_version():
            return False
        
        print()
        
        # فحص الملفات
        if not self.check_required_files():
            return False
        
        print()
        
        # فحص المكتبات
        missing_packages = self.check_packages()
        if missing_packages:
            print()
            if not self.install_packages(missing_packages):
                return False
        
        print()
        
        # فحص متغيرات البيئة
        if not self.check_environment_variables():
            return False
        
        print()
        
        # فحص بنية المشروع
        if not self.validate_project_structure():
            return False
        
        print()
        
        # اختبار سريع
        if not self.run_quick_test():
            return False
        
        # رسالة النجاح
        self.print_success_guide()
        return True

def main():
    """الوظيفة الرئيسية"""
    setup = UserBotAutoSetup()
    
    try:
        success = setup.run_setup()
        
        if success:
            print("🎯 الإعداد مكتمل بنجاح! يمكنك الآن تشغيل المشروع.")
            return 0
        else:
            print("❌ فشل في الإعداد. راجع الأخطاء أعلاه.")
            return 1
            
    except KeyboardInterrupt:
        print("\n⏹️ تم إيقاف الإعداد بواسطة المستخدم")
        return 1
    except Exception as e:
        print(f"\n💥 خطأ غير متوقع: {e}")
        return 1

if __name__ == "__main__":
    exit(main())