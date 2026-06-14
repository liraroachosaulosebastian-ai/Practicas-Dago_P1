#1er utilizar los modulos 
import modulos_1

modulos_1.borrarpantalla()
modulos_1.funcion1()

nom="Daniel"
ape="Carreon"

modulos_1.funcion3(nom,ape)

nombre,apellidos=modulos_1.funcion4(nom,ape)
print(f"Nombre: {nombre}\nApellidos: {apellidos}")


#2da formar de utilizar modulos

from modulos_1 import borrarpantalla,funcion4
nom="Daniel"
ape="Carreon"

modulos_1.funcion3(nom,ape)

nombre,apellidos=modulos_1.funcion4(nom,ape)
print(f"Nombre: {nombre}\nApellidos: {apellidos}")

