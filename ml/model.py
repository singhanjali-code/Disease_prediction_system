import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
df = pd.read_csv('ml/Training.csv')

# Separate symptoms and disease
X = df.drop('prognosis', axis=1)
y = df['prognosis']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Check accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model
pickle.dump(model, open('ml/disease_model.pkl', 'wb'))

# Save symptom list
symptoms = list(X.columns)
pickle.dump(symptoms, open('ml/symptoms.pkl', 'wb'))

print("Model saved successfully!")
print(f"Total symptoms: {len(symptoms)}")