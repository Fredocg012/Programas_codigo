#include <ejemplo.h>
#include <LiquidCrystal.h>
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

byte grado[8] =
 {
 0b00001100,
 0b00010010,
 0b00010010,
 0b00001100,
 0b00000000,
 0b00000000,
 0b00000000,
 0b00000000
 };

void setup() 
  {
      lcd.begin(16, 2); // Hay que inicializar el LCD
      lcd.createChar(1, grado);
      lcd.setCursor(0, 0); 
      lcd.print(main());
      lcd.write(1); 
  }
void loop() 
 {
 }
