int estado = 0;                //guarda el estado del botón
int estadoAnterior = 0;        //guardar el estado anterior del botón
int salida = 0;                //0 = LED está apagado, 1 = LED encendido
int precio=250;

void setup() {
  pinMode(8, INPUT);           //declaramos el botón como entrada
  pinMode(4, OUTPUT);          //declaramos el LED cono salida
}

void loop() {
  estado = digitalRead(8);     //leer el estado del botón
  
  if((estado == HIGH) && (estadoAnterior == LOW)){
    salida = 1 - salida;
    delay(20);
  }

  estadoAnterior = estado;     //guarda el valor actual
  
  if(precio==250){
    if(salida == 1){             //el estado está en alto
      digitalWrite(4, HIGH);     //encendemos el LED
    }
    else {                       //apagamos el LED
      digitalWrite(4, LOW);
    }
  }
  
}
