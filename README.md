# Disease Prediction System

## Overview

The Disease Prediction System is a machine learning-based web application that predicts diseases based on user-selected symptoms. The application uses a trained machine learning model to analyze symptoms and provide disease predictions through an interactive web interface.

## Features

* Symptom-based disease prediction
* Machine Learning model integration using Scikit-learn
* User-friendly web interface built with Flask
* Prediction history storage using SQLite
* View recent prediction history
* Download prediction history as CSV
* Responsive frontend using HTML, CSS, and JavaScript

## Tech Stack

### Backend

* Python
* Flask
* SQLite

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Frontend

* HTML
* CSS
* JavaScript

## Project Structure

Disease_prediction_system/

├── app.py

├── model.py

├── predictions.db

├── templates/

│   └── index.html

├── static/

│   ├── style.css

│   └── script.js

└── README.md

## Installation

1. Clone the repository:

```bash
git clone https://github.com/singhanjali-code/Disease_prediction_system.git
```

2. Navigate to the project directory:

```bash
cd Disease_prediction_system
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Usage

1. Select one or more symptoms.
2. Click the Predict button.
3. View the predicted disease.
4. Check prediction history.
5. Download prediction history as a CSV file.

## Future Enhancements

* User authentication
* Prediction confidence scores
* Advanced analytics dashboard
* Cloud deployment
* Improved UI/UX

## Author

Anjali Singh

## License

This project is developed for educational and portfolio purposes.
