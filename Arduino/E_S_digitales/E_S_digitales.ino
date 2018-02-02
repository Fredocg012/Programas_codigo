/*

El siguiente codigo muestra el uso de las funciones digitalRead(),

digitalWrite() y pinMode().

La experiencia consiste en un boton, que al ser apretado toma valor

HIGH y se enciende el LED.

Ademas, ahora se mostrara en la serial, el estado de los pines.

*/

int btn = 0; // valor leido del boton

void setup() {

// Asignación de entradas y salidas

pinMode(8, INPUT); // el boton es la entrada

pinMode(11, OUTPUT); // el led es la salida

Serial.begin(9600); // Se inicia la comunicacion serial

delay(2000);

}

void loop() {

Serial.print("El boton tiene valor ");

btn = digitalRead(8); // primero se "lee" el valor del boton

Serial.println(btn); // se muestra el valor de btn en la serial

digitalWrite(11, btn); // luego se "escribe" en el pin de salida

delay(500); // se agrega un retardo

}
