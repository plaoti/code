#define PIN_LED 8
int n = 0;
void setup() {
  // put your setup code here, to run once:
  pinMode(PIN_LED, OUTPUT);
  Serial.begin(115200);
  digitalWrite(PIN_LED, LOW); 
  delay(5000);
}

void loop() {
  // put your main code here, to run repeatedly:
  n++;
  digitalWrite(PIN_LED, HIGH);
  delay(1000);
  for(int i=0;i<5;i++)
  {
    digitalWrite(PIN_LED,LOW);
    delay(100);
    digitalWrite(PIN_LED,HIGH);
    delay(100);
  }
  digitalWrite(PIN_LED,LOW);
  while(1)
  {
    
  }

}
