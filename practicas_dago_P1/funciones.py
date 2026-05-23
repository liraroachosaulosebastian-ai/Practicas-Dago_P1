"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
    nombre=input("Escribe el nombre: ").strip().upper()
    apellidos=input("Escribe los apellidos: ").strip().upper()

    print(f"El nombre completo del alumno es {nombre} {apellidos}")

funcion1()

 #3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nombre, apellidos):
    
   print(f"El nombre completo del alumno es {nombre} {apellidos}")

funcion3("Saulo", "Lira")
 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    nombre=input("Escribe el nombre: ").strip().upper()
    apellidos=input("Escribe los apellidos: ").strip().upper()

    print(f"El nombre completo del alumno es {nombre} {apellidos}")
    return nombre, apellidos
nombre,apellidos = funcion2()
 #4.- Funcion que recibe parametros y regresa valor

def funcion3(nombre, apellidos):
    
    print(f"El nombre completo es: {nombre} {apellidos}")
    
    return nombre, apellidos
nombre, apellidos = funcion3(nombre, apellidos)
#Invocar las funciones
funcion1()

nombre=input("nombre: ").strip().upper()
apellidos=input("apellidos: ").strip().upper()
funcion3(nombre,apellidos)

nombre,apellidos=funcion2()
print(f"el nombre del alumno es: ") 