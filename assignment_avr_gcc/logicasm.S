


#define __SFR_OFFSET 0
#include <avr/io.h>

.global logic

.section .text
logic:
  in r17,PINB
  mov r19,r17
  ldi r18,0b00000001
  and r19,r18            ; x = r19
  mov r20,r17
  ldi r18,0b00000010
  and r20,r18       
  lsr r20        ;y=r20
  mov r21,r17
  ldi r18,0b00000100
  and r21,r18   
  lsr r21
  lsr r21   ;z=r21
  mov r22,r17
  ldi r18,0b00001000
  and r22,r18  
  lsr r22
  lsr r22
  lsr r22      ;w=r22 
  ldi r18,0b00000001
  eor r22,r18          ;W'
  and r22,r21          ;z&&w'
  and r22,r19          ;x&&z&&w'=r22
  eor r20,r18          ;y'
  and r20,r21          ;y'z =r20
  eor r19,r18          ;x'
  eor r21,r18          ;z'
  and r19,r21          ;x'z'
  or r19,r20
  or r19,r22           ;final exp
  lsl r19
  lsl r19 
  ldi r16,0b00000100
  out DDRD ,r16
  out PORTD,r19  
  ret
start:
rjmp start


