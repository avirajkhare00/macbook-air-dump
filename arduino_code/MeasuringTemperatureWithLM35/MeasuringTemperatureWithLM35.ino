int lm35Pin = 1;
int ledPin1 = 12;
int ledPin2 = 13;
void setup()
{
   Serial.begin(9600);
   
   pinMode(ledPin1, OUTPUT);
   pinMode(ledPin2, OUTPUT);
   
}

   
   


void loop()
{
  
  //int temprature = 0;
   int reading = analogRead(lm35Pin);
   //Serial.println(reading);
   int temperature = (5.0 * 100 * reading)/1024;
   Serial.println(temperature);

   if(temperature <= 20){
      digitalWrite(ledPin1, LOW);
      digitalWrite(ledPin2, HIGH);
    }

    else{
        digitalWrite(ledPin2, LOW);
        digitalWrite(ledPin1, HIGH);
      }
   
   delay(1000);
}

