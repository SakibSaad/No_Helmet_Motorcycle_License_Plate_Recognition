#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); // Change the address to match your I2C address

const int soundSensorPin = A0;
const int LEDR = 4;
const int LEDG = 6;
Servo servo;

void setup() {
  Serial.begin(9600);
  lcd.begin();                      
  lcd.backlight(); 
  servo.attach(10);
  pinMode(LEDR, OUTPUT); 
  pinMode(LEDG, OUTPUT);               
}

void servomotorclose(){
  digitalWrite(LEDR, HIGH);
  servo.write(90);
  delay(15000);
  digitalWrite(LEDR, LOW);
}

void servomotoropen(){
  digitalWrite(LEDG, HIGH);
  servo.write(0);
  delay(15000);
  digitalWrite(LEDG, LOW);
}

void loop() {
  int sensorValue = analogRead(soundSensorPin);
  float voltage = sensorValue * (5.0 / 1023.0); // Convert sensor value to voltage
  float dB = 20 * log10(voltage / 0.00631);    // Convert voltage to decibels (0.00631 is the voltage for 1 Pascal in air)
  
  // Print decibels to serial monitor
  Serial.print("Sound Level (dB): ");
  Serial.println(dB);

  if(dB>36.2){
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Road Close:");
    lcd.setCursor(0, 1);
    lcd.print(dB, 1); // Print decibels with 1 decimal place
    lcd.print(" dB");
    servomotorclose();
  }
  if(dB<36.2){
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Road Open:");
    lcd.setCursor(0, 1);
    lcd.print(dB, 1); // Print decibels with 1 decimal place
    lcd.print(" dB");
    servomotoropen();
  }
  
  // Display decibels on LCD
   // Delay for stability
}
