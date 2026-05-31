#include <dht.h>  // This is for the temperature humidity sensor
#include <LiquidCrystal_I2C.h>  // This is for the LCD I2C Module

dht DHT;

#define DHT11_PIN 8
LiquidCrystal_I2C lcd(0x3F, 16, 2);
int relayPin = 5;

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Temp.: ");
  lcd.setCursor(0, 1);
  lcd.print("Humi.: ");
  pinMode(relayPin, OUTPUT);
}

void loop() {
  // Temperature Humidity Sensor
  int chk = DHT.read11(DHT11_PIN);
  int tempC = DHT.temperature;
  int humi = DHT.humidity;
  int tempF = ((tempC * 9) / 5) + 32;

  // LCD
  lcd.setCursor(7, 1);
  lcd.print(humi);
  lcd.setCursor(7, 0);
  lcd.print(tempC);
  lcd.print(char(223));
  lcd.print("C");
  delay(2000);
  
  // Relay
  if (tempC >= 27) {
    digitalWrite(relayPin, HIGH);
  }
  else if (tempC < 27) {
    digitalWrite(relayPin, LOW);
  }
  lcd.setCursor(7, 0);
  lcd.print(tempF);
  lcd.print(char(223));
  lcd.print("F");
  delay(2000);

}
