#define __SFR_OFFSET 0
#include <avr/io.h>

.global init

.section .text

init:
LDI r17, 0b00000000
OUT DDRB ,r17
LDI r17,0b11011111
OUT PORTB,r17
