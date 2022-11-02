

//declaring the blink module
module helloworldfpga(
    input x,
    input y,
    input z,
    input w,
    output wire o,
);
     reg	led;
always@(x,y,z,w)
begin
led=(!x&!z)|(!y&z)|(x&z&!w); //reset the led
end
    assign o = led;
endmodule
//end of the module




