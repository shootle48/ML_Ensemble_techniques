# Diabetes Prediction Web Application

เว็บแอปพลิเคชันสำหรับทำนายโรคเบาหวานโดยใช้โมเดล Machine Learning ที่พัฒนาด้วย Flask

## 📋 คุณสมบัติ

- **ทำนายโรคเบาหวาน** โดยใช้ข้อมูล 3 ตัวแปร: ระดับน้ำตาลในเลือด, ระดับอินซูลิน, และค่า BMI
- **โมเดล Machine Learning** ที่ใช้ Voting Classifier รวมหลายอัลกอริทึม
- **UI ที่ใช้งานง่าย** พร้อม responsive design
- **แสดงข้อมูลตาราง** สำหรับอ้างอิงและเลือกข้อมูลทดสอบ
- **QR Code** สำหรับเข้าใช้งานผ่าน LINE

## 🚀 การติดตั้งและรัน

### ความต้องการของระบบ

- Python 3.9+
- Flask
- scikit-learn
- pandas
- numpy

### การติดตั้ง

1. Clone repository หรือดาวน์โหลดไฟล์

2. ติดตั้ง dependencies:
```bash
pip install -r requirements.txt
```

3. รันแอปพลิเคชัน:
```bash
python app.py
```

4. เปิดเบราว์เซอร์และไปที่ `http://localhost:8080`

## 📊 โมเดล Machine Learning

แอปพลิเคชันใช้ **Voting Classifier** ที่รวมโมเดลต่างๆ ดังนี้:

- **Logistic Regression** (LoR)
- **K-Nearest Neighbors** (kNN)
- **Decision Tree** (DT)
- **Gradient Boosting** (GB)
- **Random Forest** (RF)
- **Genetic Algorithm Feature Selection** (GA)
- **AdaBoost** (Adaboost)

### ข้อมูลที่ใช้ในการทำนาย

1. **Glucose** - ระดับน้ำตาลในเลือด (mg/dL)
2. **Insulin** - ระดับอินซูลิน (μU/mL)
3. **BMI** - ค่าดัชนีมวลกาย (kg/m²)

## 🎯 การใช้งาน

1. **กรอกข้อมูล** ในฟอร์ม:
   - ระดับน้ำตาลในเลือด (เช่น 90)
   - ระดับอินซูลิน (เช่น 15)
   - ค่า BMI (เช่น 22.5)

2. **กดปุ่ม Predict** เพื่อทำนายผล

3. **ดูผลลัพธ์** ที่จะแสดงว่า "เป็นเบาหวาน" หรือ "ไม่เป็นเบาหวาน"

4. **ใช้ตาราง** (กดปุ่ม "แสดงข้อมูลตาราง") เพื่อดูข้อมูลตัวอย่างและสามารถคลิกเลือกข้อมูลจากตารางเพื่อกรอกในฟอร์มได้

## 📁 โครงสร้างไฟล์

```
├── app.py                 # ไฟล์หลักของ Flask application
├── train.py              # สคริปต์สำหรับเทรนโมเดล
├── diabetes2.csv         # ข้อมูลสำหรับเทรนและแสดงผล
├── best_diabetes_model.pkl # โมเดลที่บันทึกไว้
├── requirements.txt      # รายการ dependencies
├── Procfile             # สำหรับ deployment
├── static/
│   ├── style.css        # ไฟล์ CSS
│   ├── script.js        # ไฟล์ JavaScript
│   ├── logo.png         # โลโก้
│   └── qrcode.png       # QR Code
└── templates/
    └── index.html       # หน้าเว็บหลัก
```

## 🎨 คุณสมบัติของ UI

- **Responsive Design** - ใช้งานได้ทั้งบนมือถือและคอมพิวเตอร์
- **Gradient Background** - พื้นหลังสีไล่โทน
- **Animation Effects** - เอฟเฟกต์การเคลื่อนไหวที่สวยงาม
- **Interactive Table** - ตารางที่สามารถคลิกเลือกข้อมูลได้
- **Form Validation** - ตรวจสอบข้อมูลก่อนส่ง

## 🔧 การปรับแต่ง

### การเปลี่ยนโมเดล

หากต้องการเทรนโมเดลใหม่:

1. แก้ไขไฟล์ `train.py`
2. รันสคริปต์: `python train.py`
3. โมเดลใหม่จะถูกบันทึกเป็น `best_diabetes_model.pkl`

### การเปลี่ยนข้อมูล

แทนที่ไฟล์ `diabetes2.csv` ด้วยข้อมูลใหม่ (ต้องมีคอลัมน์เดียวกัน)

## 📱 การ Deploy

### Heroku

1. สร้าง Heroku app
2. Push โค้ดไปยัง Heroku
3. Heroku จะใช้ `Procfile` ในการรันแอป

### Local Development

```bash
# ตั้งค่า environment variables (ถ้าจำเป็น)
export PORT=8080

# รันแอป
python app.py
```

## 🤝 การมีส่วนร่วม

หากต้องการปรับปรุงหรือเพิ่มคุณสมบัติ:

1. Fork repository
2. สร้าง feature branch
3. Commit การเปลี่ยนแปลง
4. สร้าง Pull Request

## 📄 License

โปรเจกต์นี้เป็น open source และสามารถใช้งานได้อย่างอิสระ

## 📞 ติดต่อ

หากมีคำถามหรือต้องการความช่วยเหลือ สามารถติดต่อผ่าน:
- สแกน QR Code ในแอปพลิเคชัน
- หรือสร้าง Issue ใน repository นี้

---

**หมายเหตุ**: แอปพลิเคชันนี้สร้างขึ้นเพื่อการศึกษาและการสาธิต ไม่ควรใช้เป็นเครื่องมือวินิจฉัยทางการแพทย์จริง