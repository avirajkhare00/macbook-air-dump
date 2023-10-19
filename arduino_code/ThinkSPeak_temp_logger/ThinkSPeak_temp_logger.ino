#include <SoftwareSerial.h>
#define SSID "HackerEarth_Guest"
#define PASS "BeMyGuest"

#define IP "184.106.153.149" // thingspeak.com
String GET = "GET /update?api_key=KBKXNPUKSE0FZIOV&test1=";
SoftwareSerial monitor(10, 11); // RX, TX

boolean connectWiFi();
int lm35Pin = 0;

void setup()
{
  monitor.begin(115200);
  Serial.begin(115200);
  sendDebug("AT");
  delay(5000);
  if(monitor.find("OK")){
    Serial.println("RECEIVED: OK");
    connectWiFi();
  }
}

int count = 3000;

void loop(){
  int reading = analogRead(lm35Pin);
  float temperature = (100 * reading * 5)/1024;
  String tempF = String(temperature);
  updateTemp(tempF);
  delay(10000);
  count++;
}

void sendDebug(String cmd){
  monitor.println(cmd);
  Serial.println(cmd);
} 

void updateTemp(String tenmpF){
  String cmd = "AT+CIPSTART=\"TCP\",\"";
  cmd += IP;
  cmd += "\",80";
  sendDebug(cmd);
  delay(2000);
  if(monitor.find("Error")){
    Serial.println("CIPSTART : RECEIVED: Error");
    return;
  }
  else
  {
    Serial.println("CIPSTART : RECEIVED: OK");
    
  }
  
  cmd = GET;
  cmd += tenmpF;
  cmd += "\r\n";
  String cmd2 = "AT+CIPSEND=";
  cmd2 += cmd.length();
  cmd2 += "\r\n";
  Serial.println(cmd2);
  monitor.print(cmd2);
  if(monitor.find(">")){
      Serial.println("CIPSEND WAITING : RECEIVED: >");
  }else{
    Serial.println("CIPSEND WAITING: RECEIVED: Error");
  }    
  delay(5000);
  monitor.print(cmd);
  Serial.println(cmd);
  delay(5000);

  
  if(monitor.find("OK")){
    Serial.println("CIPSEND : RECEIVED: OK");
  }else{
    Serial.println("CIPSEND : RECEIVED: Error");
  }
}

 
boolean connectWiFi(){
  Serial.println("AT+CWMODE=3");
  monitor.println("AT+CWMODE=3");
  delay(2000);
  String cmd="AT+CWJAP=\"";
  cmd+=SSID;
  cmd+="\",\"";
  cmd+=PASS;
  cmd+="\"";
  cmd += "\r\n";
  sendDebug(cmd);
  delay(5000);
  if(monitor.find("OK")){
    Serial.println("Connect Wifi : RECEIVED: OK");
    return true;
  }else{
    Serial.println("Connect Wifi RECEIVED: Error");
    return false;
  }
}
