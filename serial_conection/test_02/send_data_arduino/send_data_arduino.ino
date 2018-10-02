void setup(){
  Serial.begin(115200);
}

void loop(){
  for(int i = 0;i<10;i++){
    Serial.print(i);
    delay(500);
  }
}
