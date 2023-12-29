~~ Pilar Fundamental Programacion POO ~~
~~ Persona >> Estudiante ~~
~~ Clase padre, clase hija ~~


class Persona:
    def __init__(self,nombre, edad, nacionalidad, tipo_documento, num_documento, estado_vivo):
  self nombre, edad, nacionalidad, tipo_documento, num_documento, estado_vivo
self.nombre, edad, nacionalidad, tipo_documento, num_documento, estado_vivo
self.edad, nacionalidad, tipo_documento, num_documento, estado_vivo
self.nacionalidad, tipo_documento, num_documento, estado_vivo
self.tipo_documento, num_documento, estado_vivo
self.num_documento, estado_vivo
self.estado_vivo


~~ Herencia simple vs Herencia Gerarquica vs Herencia multiple ~~

Class Empleado:
pass
  def __init__(self,nombre, edad, nacionalidad, tipo_documento, num_documento, estado_vivo, trabajo, salario):
  self.trabajo = trabajo
  self.trabajo = salario

def hablar(self)
  print("Hasta aqui va bien el código")

~~ Clase padre Persona **
  
Class Empleado(persona):
 def __init__(self,trabajo,salario):
  super().__init__():
  self.trabajo = trabajo
  self.trabajo = salario


roberto=Empleado(nombre: Any, edad: Any, nacionalidad: Any, tipo_documento: Any, num_documento: Any, estado_vivo: Any)- None
roberto = empleado("Roberto", 43, "Argentino")

print(roberto.nombre)
print(roberto.edad)
print(roberto.nacionalidad)

>Roberto
>43
>Argentino

~~ Metodos Heredados, que viene del codigo arriva declarado, en la clase base esta accediento de la clase padre ~~

  def presentarse(self):
    return f'{super().mostrar_habilidad()}'
    return f'{super().mostrar_habilidad()}'

herencia = issubclass(EmpleadoArtista,Artista)
print(Herencia)
>True

herencia = issubclass(Artista,Persona)
print(Herencia)
>False

herencia = issubclass(EmpleadoArtista,Artista)
instancia=isinstance(robreto,EmpleadoArtista)
print(Instancia)
>True




