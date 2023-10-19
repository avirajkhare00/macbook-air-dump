/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the Uno and
  Leonardo, it is attached to digital pin 13. If you're unsure what
  pin the on-board LED is connected to on your Arduino model, check
  the documentation at http://www.arduino.cc

  This example code is in the public domain.

  modified 8 May 2014
  by Scott Fitzgerald
 */


// the setup function runs once when you press reset or power the board


int ledPin1 = 12;
int ledPin2 = 13;
int ledPin3 = 11;
int delayCount = 100;
void setup() {
  // initialize digital pin 13 as an output.
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(ledPin1, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(delayCount);
  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin2, HIGH);
  delay(delayCount);
  digitalWrite(ledPin2, LOW);
  digitalWrite(ledPin3, HIGH);    // turn the LED off by making the voltage LOW
  delay(delayCount);              // wait for a second
  digitalWrite(ledPin3, LOW);    // turn the LED off by making the voltage LOW
}
