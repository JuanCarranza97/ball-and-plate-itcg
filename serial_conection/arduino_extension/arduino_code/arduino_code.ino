#include "UART.h"

//Arduino connections
#define X1    A0
#define X2    A1
#define Y1    A2
#define Y2    A3

//Touch Screen Settings
#define X_RESOLUTION   100 
#define Y_RESOLUTION   100
int x_pos,y_pos;

void setup(){
  uart_init();
}

void loop(){
  if(UART_PORT.available()){
      char caracter;
      int Numbers[20];
      int bufferSize=0;

        if(uart_get(&caracter,&bufferSize,Numbers)){
          switch (caracter){
            case 'P'://Raspberry request screen position
              if(bufferSize == 2){
                for(int i = 0;i<Numbers[0];i++){
                  update_screen();
                  UART_PORT.println("P"+String(x_pos)+","+String(y_pos)); 
                  delay(Numbers[1]);
                }      
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

void get_x_value(void){
  pinMode(Y1,INPUT);
  pinMode(Y2,INPUT);
  digitalWrite(Y2,LOW);
  
  pinMode(X1,OUTPUT);
  digitalWrite(X1,HIGH);
  pinMode(X2,OUTPUT);
  digitalWrite(X2,LOW);

  x_pos=(analogRead(Y1))/(1024/X_RESOLUTION); 
}

void get_y_value(void){
  pinMode(X1,INPUT);
  pinMode(X2,INPUT);
  digitalWrite(X2,LOW);
  pinMode(Y1,OUTPUT);
  digitalWrite(Y1,HIGH);
  pinMode(Y2,OUTPUT);
  digitalWrite(Y2,LOW);

  y_pos = (analogRead(X1))/(1024/Y_RESOLUTION);
}

void update_screen(void){
  get_x_value();
  get_y_value();
}

void uart_help(void){
  UART_PORT.println("sX,T - Get touch screen data X times each T (in milliseconds)");
  UART_PORT.println("   -Example: s10,100 (Get 10 touch screen position each 100 milliseconds");
  UART_PORT.println("aX,D - Get A0-A1 analogInput X times each T (in milliseconds)");
  UART_PORT.println("   -Example: a11,250 (Get 11 A0-A1 analog read each 250 milliseconds)");
  UART_PORT.println(" ");
}

