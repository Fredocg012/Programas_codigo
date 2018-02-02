// Incluímos la libreria externa para poder utilizarla
#include <LiquidCrystal.h> // Entre los símbolos <> buscará en la carpeta de librerías configurada

// Definimos las constantes
#define COLS 16 // Columnas del LCD
#define ROWS 2 // Filas del LCD

// Lo primero is inicializar la librería indicando los pins de la interfaz
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

void setup() {
  // Configuración monitor serie
  Serial.begin(9600);
 
  // Configuramos las filas y las columnas del LCD en este caso 16 columnas y 2 filas
  lcd.begin(COLS, ROWS);
}

void loop() {
  // Limpiamos la pantalla
  lcd.clear();
 
  // Situamos el cursor en la columna 0 fila 0
  lcd.setCursor(0,0);
 
  // Escribimos Hola Mundo!!!!!!
  lcd.print("Bienvenidos a");
  // Situamos el cursor en la columna 0 fila 1
  lcd.setCursor(0,1);
 
  // Escribimos Probando el LCD.
  lcd.print("CompuTec.");
 
  // Esperamos 2 segundos igual a 2000 milisegundos
  delay(2000);
}
