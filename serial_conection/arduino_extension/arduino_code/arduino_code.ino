#include "UART.h"
#include "TOUCH_SCREEN.h"

void setup(){
  uart_init();
  reset_filter();
}

void loop(){
  if(UART_PORT.available()){
      char caracter;
      int Numbers[20];
      int bufferSize=0;

        if(uart_get(&caracter,&bufferSize,Numbers)){
          switch (caracter){
            case 's'://Raspberry request screen position
              #ifdef SCREEN_WO_RESOLUTION
                reset_range_values();
              #endif
              int screen_pos[2];
              
                if(bufferSize == 2){
                  for(int i = 0;i<Numbers[0];i++){
                    screen_pos[0]=get_x_value();
                    screen_pos[1]=get_y_value();

                    average_filter(screen_pos);
                    UART_PORT.println("s"+String(screen_pos[0])+","+String(screen_pos[1])); 
                    delay(Numbers[1]);
                  }
                  #ifdef SCREEN_WO_RESOLUTION
                    UART_PORT.println("x_min = "+String(x_range[0])+" ,x_max = "+String(x_range[1]));    
                    UART_PORT.println("y_min = "+String(y_range[0])+" ,y_max = "+String(y_range[1]));   
                  #endif
                }
                else{
                  UART_PORT.println("Buffer length doesn't match");        
                }
              break;

            case 'a':
              if(bufferSize == 2){
                  pinMode(A0,INPUT);
                  pinMode(A1,INPUT);
                    for(int i = 0;i<Numbers[0];i++){
                      UART_PORT.println("a"+String(analogRead(A0))+","+String(analogRead(A1)));
                      delay(Numbers[1]);
                    }
              }
              else{
                UART_PORT.println("Buffer length doesn't match");        
              }            
              break;
              
             default:
              UART_PORT.println("Action was not defined");
              uart_help();
              break;
          }
        }
        else{
          UART_PORT.println("Invalid Input");
          uart_help();
        }
  }
}

void uart_help(void){
  UART_PORT.println("sX,T - Get touch screen data X times each T (in milliseconds)");
  UART_PORT.println("   -Example: s10,100 (Get 10 touch screen position each 100 milliseconds");
  UART_PORT.println("aX,D - Get A0-A1 analogInput X times each T (in milliseconds)");
  UART_PORT.println("   -Example: a11,250 (Get 11 A0-A1 analog read each 250 milliseconds)");
  UART_PORT.println(" ");
}

