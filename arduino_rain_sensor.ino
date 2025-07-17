
const int rainSensorPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(rainSensorPin);
  Serial.println(sensorValue);
  delay(1000);
}
