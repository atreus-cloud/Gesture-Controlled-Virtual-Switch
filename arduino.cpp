int ledPin = 13;  // LED on pin 13
int motorPin = 9; // Motor on pin 9 

//start
void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(motorPin, OUTPUT);
  Serial.begin(9600);  
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    
    if (command == '1') {
      digitalWrite(ledPin, HIGH);  //on
      analogWrite(motorPin, 255);  //full speed
    } else {
      digitalWrite(ledPin, LOW);   //off
      analogWrite(motorPin, 0);    //stop the motor
    }
  }
}
