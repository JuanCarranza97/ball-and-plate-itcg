#ifndef UART_1_H
#define UART_1_H

  #include <Arduino.h>
  
  #define UART_PORT          Serial
  #define UART_BAUD          115200
  
  #define CHAR_ENDS              '\n'
  #define NUMBERS_BETWEEN         ','

  #define UART_LOG

  void uart_init(void);
  bool uart_get(char *caracter_salida,int *size_,int _datos[]); 

#endif
