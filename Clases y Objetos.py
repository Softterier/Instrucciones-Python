~~ snake case se utiliza para el nombre de las variables al principio de cada palabra, el gión bajo:  separado_por_guines_bajos;  nombre_primero y nombre_primer_preferido
~~ camel case se utilica para el nombre de las variables al principio de cada palabra, mayuscula: primerLetraEnMayusculaElRestoEnMinuscula
~~ Pascal case se utilica para el nombre de las variables al principio de cada palabra, mayuscula: TodasLasPrimerasLetraEnMayusculaElRestoEnMinuscula

~~ Clase Celular Recomendacio para notificar las Clases y Objetos

class Celular():[
  marca = "Samsung"
  modelo = "S23"
  camaraF = "48MP" 

~~ atributos estaticos ~~
celular1 = Celular()
celular2 = Celular()
celular3 = Celular()
celular4 = Celular()

~~ muestra los valores de los campos ~~
  
print(celular1.marca)
print(celular1.modelo)
print(celular1.camaraF)

~~ actualiza los valores de los campos ~~

celular1.marca =  "Motorola"
celular2.modelo= "G86"
celular3.camaraF= "52MP"

~~ Instancia dentro de una Clase (multiples) 

~~ Un objeto es una instancia de una clase ~~

  
