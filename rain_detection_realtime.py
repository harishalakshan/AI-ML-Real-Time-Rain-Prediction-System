
import serial
import numpy as np
from sklearn.ensemble import RandomForestClassifier

serial_port = '/dev/ttyUSB0'

model = RandomForestClassifier()

X = []
y = []

with serial.Serial(serial_port, 9600) as ser:
    ser.readline()
    while True:
        line = ser.readline().strip().decode('utf-8')
        sensor_value = int(line)

        label = 1 if sensor_value > 500 else 0

        X.append([sensor_value])
        y.append(label)

        model.fit(X, y)
        prediction = model.predict([[sensor_value]])

        print("Rain detected" if prediction[0] == 1 else "No rain")
