#ifndef TERMINAL_H
#define TERMINAL_H

  #include <Arduino.h>

  #include "ARROB_CONFIG.h"
  
  //#define TERMINAL_LOG
  //#define TERMINAL_DEBUG
  
  typedef void (*terminalCallback)(int var[]);  

  typedef struct{
    terminalCallback Callback;
    const char caracter;
    int tam;
    const char *helpString;
    const char *actionString;
  }terminal_actions;

  void terminal_lab(void);
   
  void terminalAction_a(int var[]);
  void terminalAction_s(int var[]);
  void terminalAction_e(int var[]);
  void terminalAction_r(int var[]);
  /*void terminalAction_a(int var[],int tam);
  void terminalAction_B(int var[],int tam);
  void terminalAction_b(int var[],int tam);*/
#endif*/
