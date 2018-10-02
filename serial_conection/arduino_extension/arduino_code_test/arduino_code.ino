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
  Serial.begin(115200);
}

void loop(){
  update_screen();
  Serial.println("X = "+String(x_pos)+", Y = "+String(y_pos));
  delay(250);
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

