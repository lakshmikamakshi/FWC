//----------------------Skeleton Code--------------------//
#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>
#include<Arduino.h>
//    Can be client or even host   //
#ifndef STASSID
#define STASSID "K"  // Replace with your network credentials
#define STAPSK  "iamroot01"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;


void OTAsetup() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    delay(5000);
    ESP.restart();
  }
  ArduinoOTA.begin();
}

void OTAloop() {
  ArduinoOTA.handle();
}
int X=2,Y=3,Z=4,W=5;
int x,y,z,w,o;
void setup()
{
	otasetup();
pinMode(X,INPUT);
pinMode(Y,INPUT);
pinMode(Z,INPUT);
pinMode(W,INPUT);
pinMode(6,OUTPUT);
}
void loop()
{
	otaloop();
x = digitalRead(X);
y = digitalRead(Y);
z = digitalRead(Z);
w = digitalRead(W);
o = (!x&&!z)||(!y&&z)||(x&&z&&!w); 
digitalWrite(8,o);
}
