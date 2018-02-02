//PARPADEO DE LED

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT); //Declaramos el pin 13 como salida
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(13, HIGH); //Encendemos el LED
  delay(2000);            //Esperamos 1 segundo
  digitalWrite(13, LOW);  //Apagamos el LED
  delay(2000);            //Esperamos 1 segundo
}
