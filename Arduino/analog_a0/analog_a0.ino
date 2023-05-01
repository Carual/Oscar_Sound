void setup(){
  Serial.begin(9600); // Inicializamos monitor serie para visualizar los valores de LDR.
}

void loop()
{
  ; // Leemos el valor del pinLDR y lo guardamos en la variable creada.
  Serial.print(int(99 - (analogRead(A0) / 10.33)));
  Serial.print(",");
  Serial.print(int(99 - (analogRead(A1) / 10.33)));
  Serial.print(",");
  Serial.print(int(99 - (analogRead(A2) / 10.33)));
  Serial.print(",");
  Serial.print(int(99 - (analogRead(A3) / 10.33)));
  Serial.print(",");
  Serial.print(int(99 - (analogRead(A4) / 10.33)));
  Serial.print(",");
  Serial.println(int(99 - (analogRead(A5) / 10.33)));
  delay(100);
}
