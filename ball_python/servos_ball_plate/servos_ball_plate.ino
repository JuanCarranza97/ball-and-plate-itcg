//move servos with pyhton
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include "UART.h"

#define LED 13

Adafruit_PWMServoDriver servos = Adafruit_PWMServoDriver(0x40);

unsigned int pos0=152; // ancho de pulso en cuentas para pocicion 0°
unsigned int pos180=585; // ancho de pulso en cuentas para la pocicion 180°

int servo_home[6]={75,72,75,100,70,85};
int pca_channels[6]={0,1,2,8,9,10};

void setup() {
  pinMode(LED,OUTPUT);
  servos.begin();  
  servos.setPWMFreq(50);
  servos_init();
  uart_init();
}


void loop() {
    if(UART_PORT.available()){
      char caracter;
      int Numbers[20];
      int bufferSize=0;
      int number_servo;
      int grade_servo;
      int g_servos[6];

        if(uart_get(&caracter,&bufferSize,Numbers)){
          switch(caracter){
            case 's'://Grados de servos individuales (s0,100)(numero de servo, grados) 
                if(bufferSize == 2){
                    number_servo=Numbers[0];
                    grade_servo=Numbers[1];
                    if(number_servo< 5 or number_servo>0 or grade_servo<180 or grade_servo>0){  
                        setServo(number_servo,grade_servo); 
                    }
                    UART_PORT.print("Servo: ");
                    UART_PORT.print(number_servo);
                    UART_PORT.print(" Grados: ");
                    UART_PORT.println(grade_servo);
                }
              break;

              case 'p':
                  if(bufferSize == 6){
                      for(int i=0; i<=5; i++){
                        number_servo=pca_channels[i];
                        grade_servo=Numbers[i];
                        if(number_servo< 5 or number_servo>0 or grade_servo<180 or grade_servo>0){  
                          setServo(number_servo,grade_servo); 
                       }
                    }
                     UART_PORT.println(" Servo 1: "+String(Numbers[0])+" Servo 2: "+String(Numbers[1])+" Servo 3: "+String(Numbers[2])+" Servo 4: "+String(Numbers[3])+" Servo 5: "+String(Numbers[4])+" Servo 6: "+String(Numbers[5]));
                  }
               break;

               case 'l':
                   if(bufferSize == 1){
                      if(Numbers[0] == 1)  digitalWrite(LED,HIGH);
                      if(Numbers[0] == 0)  digitalWrite(LED,LOW);
                    }
               break;
           }
        }
        else{
          UART_PORT.println("Buffer length doesn't match");        
        }
    }
 }


void servos_init(void){
  for(int i=0; i<=5; i++){
    setServo(pca_channels[i],servo_home[i]);
    delay(500);
  }
}

void setServo(uint8_t n_servo, int angulo) {
  int duty;
  duty=map(angulo,0,180,pos0, pos180);
  servos.setPWM(n_servo, 0, duty);  
}
