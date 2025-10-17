// File: arduino.ino
// Project: Automatic Thief Detector
// Author: Preeti Dasdeepa

// Components: PIR motion sensor, Buzzer, LED
int pirPin = 8;      // PIR sensor connected to digital pin 8
int buzzer = 9;      // Buzzer on pin 9
int led = 10;        // LED on pin 10
int motionState = 0; // 0 = no motion, 1 = motion detected

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.println("System ready. Monitoring...");
}

void loop() {
  motionState = digitalRead(pirPin);

  if (motionState == HIGH) {
    digitalWrite(buzzer, HIGH);
    digitalWrite(led, HIGH);
    Serial.println("⚠️ Motion detected! Possible intrusion!");
    delay(2000); // Alarm duration
  } else {
    digitalWrite(buzzer, LOW);
    digitalWrite(led, LOW);
  }
  delay(500);
}
