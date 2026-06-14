# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).
def borrarpantalla():
    print("\033c")


def funcion1():
    nombre=input("Escribe el nombre: ").strip().upper()
    apellidos=input("Escribe los apellidos: ").strip().upper()

    print(f"El nombre completo del alumno es {nombre} {apellidos}")



def funcion3(nombre, apellidos):
    
   print(f"El nombre completo del alumno es {nombre} {apellidos}")



def funcion2():
    nombre=input("Escribe el nombre: ").strip().upper()
    apellidos=input("Escribe los apellidos: ").strip().upper()

    print(f"El nombre completo del alumno es {nombre} {apellidos}")
    return nombre, apellidos


def funcion4(nombre, apellidos):
    
    print(f"El nombre completo es: {nombre} {apellidos}")
    
    return nombre, apellidos
