#define relayPin 8
#define sensorPin A0

void setup() {
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW);
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(sensorPin);
  int soilMoisture = map(sensorValue, 1023, 0, 0, 100);
  if (soilMoisture < 50) {
    digitalWrite(relayPin, HIGH);
  }
  else if (soilMoisture > 65) {
    digitalWrite(relayPin, LOW);
  }
  Serial.println(soilMoisture);
  delay(1000);
}
