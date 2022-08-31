.include "/home/kamakshi/FWC/assignments/assignment_2/m328Pdef.inc"


ldi r17, 0b00000000
out DDRB ,r17
ldi r17,0b11011111
out PORTB,r17
main:
  in r17,PINB
  mov r19,r17
  ldi r18,0b00000001
  and r19,r18            ; x = r19
  mov r16,r17
  ldi r18,0b00000010
  and r16,r18
  ldi r23, 0b00000001
  rcall loopw
  mov r20,r16;y=r20
  mov r16,r17
  ldi r18,0b00000100
  and r16,r18   
  ldi r23,0b00000010
  rcall loopw
  mov r21,r16;z=r21
  mov r16,r17
  ldi r18,0b00001000
  and r16,r18  
  ldi r23,0b00000011
  rcall loopw
  mov r22,r16  ;w=r22 
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
  ldi r23,0b00000010
  rcall loopv
  ldi r16,0b00000100
  out DDRD ,r16
  out PORTD,r19  

  rjmp main
loopw:
lsr r16
dec r23
brne loopw
ret
loopw:
lsl r19
dec r23
brne loopw
ret

