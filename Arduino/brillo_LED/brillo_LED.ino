const int led = 3; //LED conectado al pin 3
const int pot = 0; //pot conectado al pin A0
int brillo;

void setup() {
  pinMode(led, OUTPUT); //Declaramos el LED como salida
  // los pins analogicos se declaran como entrada automáticamente
}

void loop() {
  brillo = analogRead(pot) / 4; //leemos el valor del potenciometro y lo dividimos entre 4
  analogWrite(led, brillo);     //para usarlo en analogwrite
}
