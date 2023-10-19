int lm35Pin = 1;
void setup()
{
   Serial.begin(9600);
}
void loop()
{
   int reading = analogRead(lm35Pin);
   Serial.println(reading);
   int temperature = (5.0 * 100 * reading)/1024;
   Serial.println(temperature);
   delay(1000);
}

