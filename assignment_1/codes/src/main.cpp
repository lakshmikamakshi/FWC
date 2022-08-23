#include<Arduino.h>
int X=2,Y=3,Z=4,W=5;
int x,y,z,w,o;
void setup()
{
pinMode(X,INPUT);
pinMode(Y,INPUT);
pinMode(Z,INPUT);
pinMode(W,INPUT);
pinMode(8,OUTPUT);
}
void loop()
{
x = digitalRead(X);
y = digitalRead(Y);
z = digitalRead(Z);
w = digitalRead(W);
o = (!x&&!z)||(!y&&z)||(x&&z&&!w); 
digitalWrite(8,o);
}
