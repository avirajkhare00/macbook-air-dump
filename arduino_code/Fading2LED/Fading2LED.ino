/*
 Fading

 This example shows how to fade an LED using the analogWrite() function.

 The circuit:
 * LED attached from digital pin 9 to ground.

 Created 1 Nov 2008
 By David A. Mellis
 modified 30 Aug 2011
 By Tom Igoe

 http://www.arduino.cc/en/Tutorial/Fading

 This example code is in the public domain.

 */

int ledPin1 = 9;    // PWM: 3, 5, 6, 9, 10, and 11. Provide 8-bit PWM output with the analogWrite() function.
int ledPin2 = 11;

void setup() {
  // nothing happens in setup
}
void loop() {
  // fade in from min to max in increments of 5 points:
  for (int fadeValue1 = 50, fadeValue2 = 255 ; fadeValue1 <= 255, fadeValue2 >=50 ; fadeValue1 += 5, fadeValue2-=5) {
    // sets the value (range from 0 to 255):
    analogWrite(ledPin1, fadeValue1);
    analogWrite(ledPin2, fadeValue2);
    // wait for 30 milliseconds to see the dimming effect
    delay(50);
  }

  // fade out from max to min in increments of 5 points:
  for (int fadeValue1 = 255, fadeValue2 = 50 ; fadeValue1 >= 50, fadeValue2 <=255; fadeValue1 -= 5, fadeValue2 +=5) {
    // sets the value (range from 0 to 255):
    analogWrite(ledPin1, fadeValue1);
    analogWrite(ledPin2, fadeValue2);

    // wait for 30 milliseconds to see the dimming effect
    delay(50);
  }
}
