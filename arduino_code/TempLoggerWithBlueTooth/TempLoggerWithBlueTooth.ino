#include <SoftwareSerial.h>
SoftwareSerial btSerial(10, 11); // RX, TX

int lm35Pin = 1;
void setup()
{
   Serial.begin(9600);
   btSerial.begin(9600);  // HC-05 default speed in AT command
}

void loop()
{
   int reading = analogRead(lm35Pin);
   float temperature = (100 * reading * 5)/1024;
  
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" *C");
  
  btSerial.write("Temperature:   ");
  String temp = String(temperature);
  btSerial.print(temp);
  btSerial.write(" *C");
   
   delay(1000);
}

