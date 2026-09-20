#define PIN_LED 13
int count = 0;
void setup() {
  Serial.begin(115200);
  
  pinMode(PIN_LED, OUTPUT);
}
void loop() {
  delay(1000);
  Serial.println(++count);
  digitalWrite(PIN_LED,0);
  delay(1000);
  digitalWrite(PIN_LED,1);
}
