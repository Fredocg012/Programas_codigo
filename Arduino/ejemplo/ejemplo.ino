int estado = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(8, INPUT); //declaramos el botón como entrada
  pinMode(4, OUTPUT); //declaramos el LED como salida
}

void loop() {
  // put your main code here, to run repeatedly:
  estado = digitalRead(8); //leer el estado del botón

  if(estado == HIGH){ //si estado esta en alto
    digitalWrite(4, HIGH); //encendemos el LED
  }
  else{
    digitalWrite(4, LOW);
  }
}
