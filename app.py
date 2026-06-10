from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Load model and symptoms
model = pickle.load(open('ml/disease_model.pkl', 'rb'))
symptoms_list = pickle.load(open('ml/symptoms.pkl', 'rb'))

# Create database
def init_db():
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS predictions
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                symptoms TEXT,
                disease TEXT,
                confidence FLOAT,
                date TEXT)''')
    conn.commit()
    conn.close()

# Home route
@app.route('/')
def home():
    return render_template('index.html', 
                         symptoms=symptoms_list)

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        selected_symptoms = request.json.get('symptoms', [])
        
        input_data = np.zeros(len(symptoms_list))
        for symptom in selected_symptoms:
            if symptom in symptoms_list:
                index = symptoms_list.index(symptom)
                input_data[index] = 1
        
        prediction = model.predict([input_data])[0]
        probability = model.predict_proba([input_data])[0].max()
        confidence = round(probability * 100, 2)
        
        # Save to database
        conn = sqlite3.connect('predictions.db')
        c = conn.cursor()
        c.execute('''INSERT INTO predictions 
                    (symptoms, disease, confidence, date)
                    VALUES (?, ?, ?, ?)''',
                    (str(selected_symptoms), 
                     prediction, 
                     confidence,
                     datetime.now().strftime("%Y-%m-%d %H:%M")))
        conn.commit()
        conn.close()
        
        return jsonify({
            'disease': prediction,
            'confidence': confidence,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        })

# History route
@app.route('/history')
def history():
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    c.execute('SELECT * FROM predictions ORDER BY id DESC LIMIT 10')
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)
from flask import send_file
import csv
import sqlite3

@app.route('/download_csv')
def download_csv():
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()

    c.execute("SELECT * FROM predictions")
    rows = c.fetchall()

    conn.close()

    with open('prediction_history.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Change column names according to your table
        writer.writerow(['ID', 'Symptoms', 'Prediction'])

        for row in rows:
            writer.writerow(row)

    return send_file(
        'prediction_history.csv',
        as_attachment=True
    )

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
    