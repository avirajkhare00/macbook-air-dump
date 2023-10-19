#include <Servo.h>

Servo myServo;

int const potPin = A0;
int potVal;
int angle;

void setup() {
  // put your setup code here, to run once:
  myServo.attach(9);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  potVal = analogRead(potPin);
  Serial.print ("potVal: ");
  Serial.print (potVal);
  angle = map (potVal, 10, 160, 0, 179);
  Serial.print (", angle: ");
  Serial.println (angle);

  myServo.write (angle);
  
  delay(1000); // we are giving timer of because capacitor needs to get recharged.

 }
