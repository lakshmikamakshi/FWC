#include <avr/io.h>

extern void init(void);

extern void logic(void);


 int main (void)
{
  while (1) {
	  
	  init();
	 	  logic();
  }
  return 0;

}
