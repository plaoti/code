#include <Servo.h>



// Arduino pin assignment

#define PIN_LED   9   // LED active-low
#define PIN_TRIG  12  // sonar sensor TRIGGER
#define PIN_ECHO  13  // sonar sensor ECHO
#define PIN_SERVO 10  // servo motor



// configurable parameters for sonar
#define SND_VEL 346.0     // sound velocity at 24 celsius degree (unit: m/sec)
#define INTERVAL 25       // sampling interval (unit: msec)
#define PULSE_DURATION 10 // ultra-sound Pulse Duration (unit: usec)
#define _DIST_MIN 180.0   // minimum distance to be measured (unit: mm = 18cm)
#define _DIST_MAX 360.0   // maximum distance to be measured (unit: mm = 36cm)


#define TIMEOUT ((INTERVAL / 2) * 1000.0) // maximum echo waiting time (unit: usec)
#define SCALE (0.001 * 0.5 * SND_VEL) // coefficent to convert duration to distance

#define _EMA_ALPHA 0.3    // EMA weight of new sample (range: 0 to 1)
                          // Setting EMA to 1 effectively disables EMA filter.

#define _DUTY_MIN 544   // servo full clockwise position (0 degree)
#define _DUTY_NEU 1472  // servo neutral position (90 degree)
#define _DUTY_MAX 2400  // servo full counterclockwise position (180 degree)


// global variables
float dist_ema, dist_prev = _DIST_MIN; // unit: mm
unsigned long last_sampling_time;       // unit: ms

Servo myservo;

void setup() {
  // initialize GPIO pins
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_TRIG, OUTPUT);    // sonar TRIGGER
  pinMode(PIN_ECHO, INPUT);     // sonar ECHO
  digitalWrite(PIN_TRIG, LOW);  // turn-off Sonar  

  myservo.attach(PIN_SERVO);
  myservo.writeMicroseconds(_DUTY_NEU);

  dist_prev = _DIST_MIN;
  dist_ema = _DIST_MIN;



  Serial.begin(57600);

}



void loop() {

  float dist_raw, dist_filtered;
  int duty_target;

  if (millis() < last_sampling_time + INTERVAL)
    return;
    
  dist_raw = USS_measure(PIN_TRIG, PIN_ECHO);

  if (dist_raw < _DIST_MIN || dist_raw > _DIST_MAX || dist_raw == 0.0) {
    dist_filtered = dist_prev;    
    digitalWrite(PIN_LED, HIGH);
  } 
  else {
    dist_filtered = dist_raw;
    dist_prev = dist_raw;
    digitalWrite(PIN_LED, LOW);
  }

  //ema
  dist_ema = _EMA_ALPHA * dist_filtered + (1.0 - _EMA_ALPHA) * dist_ema;



  if (dist_ema <= _DIST_MIN) {
    duty_target = _DUTY_MIN;
  } 
  else if (dist_ema >= _DIST_MAX) {
    duty_target = _DUTY_MAX;
  } 
  else {
    duty_target = _DUTY_MIN + (int)((dist_ema - _DIST_MIN) * (_DUTY_MAX - _DUTY_MIN) / (_DIST_MAX - _DIST_MIN));
  }



  myservo.writeMicroseconds(duty_target);

  Serial.print("Min:");      Serial.print(_DIST_MIN);
  Serial.print(",dist:");     Serial.print(dist_filtered);
  Serial.print(",ema:");      Serial.print(dist_ema);
  Serial.print(",Servo:");    Serial.print(myservo.read());
  Serial.print(",Max:");      Serial.print(_DIST_MAX);
  Serial.println("");

  last_sampling_time += INTERVAL;

}



float USS_measure(int TRIG, int ECHO)

{
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(PULSE_DURATION);
  digitalWrite(TRIG, LOW);
  
  return pulseIn(ECHO, HIGH, TIMEOUT) * SCALE;

}
