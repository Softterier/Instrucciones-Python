Class y Objects.py  SOY DALTO   Youtube

<__main__.celular object at 0x000001CB77F8D290>
PS C:/Users/Desktop/Curso de POO>

~~    self automatico del objeto -  Referencia a si mismo        ~~
~~ marca propiedad de self, modelo propiedad de self, camaraF propiedad de self ~~    
~~ esta Funcion de ejecuta automatiamente cuando ya esta creada o se esta creando ~~
~~ Funcion constructor, que es la que mira si esta definida la clase ~~
    
class Celular:
    def __init__(Self, marca, Modleo, camara):
    Self.marca
    Self.modelo
    Self.camaraF

Celular1 = Celular("Samsung", "523", "48MP") 

print(celular1.marca)

>Samsung
~~ Asi le pasamos los datos al objeto ~~

~~ Un Objeto puede hacer dos cosas, Propiedades y atributos, y la otra hacer acciones, que son metodos ~~
~~ El perro es negro con blanco, tiene patas, tiene hocico, pero tambien puede ladrar, mover la cola, dar la mano ~~
    
~~ Metodos (Es una función) ~~
~~ Las funciones creadas dentro de una clase se llaman metodos  llamar(PARAMETRO)~~

    def llamar(): 
      print("Estas haciendo un llamado desde un:")
    def Cortar():  
    print("Cortastes la llamada")  

  def llamar(): 
      print(f"Estas haciendo un llamado desde un:"{self.modelo}")
    def Cortar():  
    print(f"Cortastes la llamada""{self.modelo}")  

> Estas haciendo un llamado desde un: Samsung
> Cortastes la llamada: Samsung



def __init__


