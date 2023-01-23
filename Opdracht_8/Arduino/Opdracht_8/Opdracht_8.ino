const int leds[] = {2, 4};
const int inputPins[] = {10, 11};
int inputValues[] = {LOW, LOW}

void setup() {
  Serial.begin(9600);
  for(int i = 0; i <= 1; i++){
    pinMode(leds[i], OUTPUT);
  }
  for(int i = 0; i <= 1; i++){
    pinMode(inputPins[i], INPUT);
  }
}

void loop() {
  for(int i = 0; i <= 1; i++){
    inputValues[i] = digitalRead(inputPins[i]);

    if(inputValues[i] == HIGH)
      digitalWrite(leds[i], HIGH);
    else
      digitalWrite(leds[i], LOW);
  }
}
