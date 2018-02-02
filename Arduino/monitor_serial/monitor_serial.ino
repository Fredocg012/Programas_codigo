void setup() {

// initialize serial:

Serial.begin(9600);

delay(5000);

Serial.println("Hola!");

}

void loop() {

delay(500);

Serial.print("Ha pasado ");

delay(500);

Serial.println("un segundo");

}
