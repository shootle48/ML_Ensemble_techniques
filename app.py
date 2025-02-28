from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# โหลดโมเดลที่บันทึกไว้ (เช่น VOTE_model จาก VotingClassifier)
with open('best_diabetes_model.pkl', 'rb') as f:
    model = pickle.load(f)

# โหลดข้อมูลสำหรับแสดงตาราง (ในที่นี้ใช้ไฟล์ diabetes2.csv)
data = pd.read_csv('diabetes2.csv')
data_html = data.to_html(classes='dataframe', header="true", index=False)

@app.route('/')
def home():
    return render_template('index.html', tables=[data_html], titles=data.columns.values)

@app.route('/predict', methods=['POST'])
def predict():
    # รับข้อมูลเฉพาะฟีเจอร์ที่โมเดลต้องการ: Glucose, Insulin, BMI
    try:
        Glucose = float(request.form['Glucose'])
        Insulin = float(request.form['Insulin'])
        BMI = float(request.form['BMI'])
    except ValueError:
        return render_template('index.html',
                               prediction_text='กรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง',
                               tables=[data_html],
                               titles=data.columns.values)

    # เตรียมข้อมูลสำหรับทำนายให้เป็น array 2 มิติ
    input_features = np.array([[Glucose, Insulin, BMI]])

    # ทำนายผลด้วยโมเดลที่บันทึกไว้
    prediction = model.predict(input_features)
    if prediction[0] == 1:
        outcome = 'เป็นเบาหวาน'
        prediction_class = 'positive'
    else:
        outcome = 'ไม่เป็นเบาหวาน'
        prediction_class = 'negative'

    return render_template('index.html',
                           prediction_text='ผลลัพธ์: {}'.format(outcome),
                           prediction_class=prediction_class,
                           tables=[data_html],
                           titles=data.columns.values)
# ส่วนนี้เพื่อให้เราทดสอบใน local ได้
# แต่บน Vercel จะไม่ถูกเรียก
if __name__ == "__main__":
    app.run(debug=True)
