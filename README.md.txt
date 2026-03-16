# 🏥 Pharmacy CRM System - Python GUI

هذا المشروع هو نظام إدارة (CRM) متكامل تم تطويره باستخدام لغة **Python**، ويهدف إلى إدارة العمليات اليومية في الصيدليات أو المخازن الطبية، مع واجهة مستخدم رسومية (GUI) سهلة التعامل.

## 🚀 الميزات الرئيسية (Features)
- **إدارة البيانات (CRUD):** إضافة، حذف، تعديل، وعرض بيانات الأدوية والعملاء.
- **قاعدة بيانات مدمجة:** يعتمد على **SQLite** لضمان سرعة واستقرار حفظ البيانات.
- **منطق منفصل (Logic Separation):** تم فصل منطق الأعمال (Logic) عن واجهة المستخدم (GUI) لضمان نظافة الكود وسهولة صيانته.
- **واجهة مستخدم احترافية:** تم تصميم الواجهة لسهولة الاستخدام والسرعة.

## 🛠 التقنيات المستخدمة (Tech Stack)
- **Language:** Python 3.x
- **GUI Library:** Tkinter (أو PyQt حسب ما استخدمت)
- **Database:** SQLite
- **Source Control:** Git & GitHub

## 📂 هيكل المشروع (Project Structure)
```text
CRM/
├── src/
│   ├── main.py        # نقطة انطلاق البرنامج
│   ├── gui.py         # واجهة المستخدم
│   ├── logic.py       # العمليات الحسابية ومنطق النظام
│   └── database.py    # التعامل مع قاعدة البيانات
├── requirements.txt   # المكتبات المطلوبة
└── .gitignore         # استبعاد الملفات غير الضرورية

⚙️ كيف تشغل المشروع على جهازك؟
قم بعمل Clone للمستودع:
git clone [https://github.com/ahmed1eid/Python-CRUDS-GUI.git](https://github.com/ahmed1eid/Python-CRUDS-GUI.git)

قم بإنشاء بيئة افتراضية:

python -m venv venv

قم بتفعيل البيئة وتثبيت المكتبات:

Bash
pip install -r requirements.txt
قم بتشغيل البرنامج:

Bash
python src/main.py
👤 المطور
أحمد عيد (Ahmed Eid)

طالب هندسة برمجيات بجامعة النيل.

Full-stack Developer.