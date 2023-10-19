#include <Servo.h>

Servo myServo;

int const potPin = A0;
int potVal;
int angle;

void setup() {
  // put your setup code here, to run once:
  myServo.attach(10);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to ru n repeatedly:
  potVal = 500;
  Serial.print ("potVal: ");
  Serial.print (potVal);
  angle = map (potVal, 140, 160, 0, 179);
  Serial.print (", angle: ");
  Serial.println (angle);

  myServo.write (angle);
  
  delay(1000);

}
