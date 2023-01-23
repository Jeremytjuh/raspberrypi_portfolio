// 3 input, 4 output
const int raspPins[] = {10, 11};
unsigned long lastTime = 0;
bool ledState = false;


void setup() {
  Serial.begin(9600);
  pinMode(raspPins[0], INPUT); // Zet de pin voor de Raspberry Pi als ingang
  pinMode(raspPins[1], OUTPUT); // Zet de tweede pin voor de Raspberry Pi als ingang
  digitalWrite(raspPins[1], LOW);
}

void loop() {
  Serial.println(digitalRead(raspPins[0]));
  unsigned long currentTime = millis();
  if (digitalRead(raspPins[0]) == LOW) {
    if (currentTime - lastTime >= 1000){
      lastTime = currentTime;
      if(ledState){
        digitalWrite(raspPins[1], HIGH);
        ledState = false;
      } else {
        digitalWrite(raspPins[1], LOW);
        ledState = true;
      }
    }
  }
}
