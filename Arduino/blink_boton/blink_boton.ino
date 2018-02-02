int btn = 0; // valor leido del boton

void setup() {

// Asignación de entradas y salidas

pinMode(8, INPUT); // el boton es la entrada

pinMode(11, OUTPUT); // el led es la salida

}

void loop() {

btn = digitalRead(8); // primero se "lee" el valor del boton

digitalWrite(11, btn); // luego se "escribe" en el pin de salida

}
