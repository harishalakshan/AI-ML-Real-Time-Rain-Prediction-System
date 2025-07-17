
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import serial

ser = serial.Serial('COM3', 9600)
ser.flushInput()

dataset = pd.read_csv('rain_data.csv')
X = dataset.drop('rain', axis=1)
y = dataset['rain']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

joblib.dump(clf, 'rain_detection_model.pkl')

while True:
    if ser.inWaiting() > 0:
        data = ser.readline().decode().rstrip()
        values = list(map(int, data.split(',')))
        prediction = clf.predict([values])
        print("Rain detected!" if prediction[0] == 1 else "No rain detected!")
