     
int triggerPin = 7;
int echoPin = 6;
void setup()
{
  Serial.begin(9600);
  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop()
{
  long duration;
  long distance;
  // Make the triggerPin LOW initially
  digitalWrite(triggerPin, LOW); 
  delayMicroseconds(2);
  // Next three lines generate a HIGH pulse of 10 microseconds = This is equal to frequency of 100KHz
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  // PulseIn measures how long it takes for the HIGH signal to return
  duration = pulseIn(echoPin, HIGH);
  // 1 mm distance takes 2.9 microseconds. Distance = time taken/2 divided by 2.9
  distance = (duration/2) / 2.9;
  Serial.println(distance);
}

