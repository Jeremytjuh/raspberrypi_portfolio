const int btnPin = 13;

const int leds[] = {3, 4};
const int raspPins[] = {10, 11};
int inputValues[] = {LOW, LOW};

void setup() {
  Serial.begin(9600);
  pinMode(leds[0], OUTPUT);  // Zet de pin voor de eerste led als uitgang
  pinMode(leds[1], OUTPUT);  // Zet de pin voor de tweede led als uitgang
  pinMode(raspPins[0], INPUT); // Zet de pin voor de Raspberry Pi als ingang
  pinMode(raspPins[1], OUTPUT); // Zet de tweede pin voor de Raspberry Pi als ingang
}

void loop() {
   Serial.println(digitalRead(btnPin));
  digitalWrite(raspPins[1], digitalRead(btnPin));

  Serial.println(digitalRead(raspPins[0]));
  digitalWrite(leds[0], digitalRead(raspPins[0]));
  
  if (digitalRead(raspPins[0]) == HIGH) {
    digitalWrite(leds[0], HIGH);
    digitalWrite(leds[1], LOW);
  } else {
    digitalWrite(leds[1], HIGH);
    digitalWrite(leds[0], LOW);
  }
}
