"""
Ejercicio:

1. Crea una función que calcule el área de un triángulo rectángulo.
2. Inicializa las estructuras de datos necesarias para almacenar los resultados:
   - Una lista
   - Una tupla
   - Un set
   - Un diccionario
3. Implementa un ciclo que permita repetir el cálculo de la misma figura tantas veces como el usuario lo desee.
4. Dentro del ciclo:
   - Solicita la base y la altura del triángulo.
   - Calcula el área usando la función creada.
   - Guarda el resultado en la lista y en el diccionario.
   - Pregunta si se desea repetir el proceso.
5. Al finalizar el ciclo:
   - Convierte los resultados a tupla y set.
   - Calcula el promedio de todas las áreas registradas.
   - Imprime en pantalla el contenido de la lista, la tupla, el set y el diccionario.
   - Muestra el promedio calculado.
"""
print("\033c")
cont = "S"
areas_lista=[]
areas_dic={}
contador=0

def area_triangulo(base, altura):
    return (base * altura) / 2

while cont == "S":
    base = float(input("Ingresa una base: "))
    altura = float(input("Ingresa la altura: "))
    
    area = area_triangulo(base, altura)
    print(f"El área del triángulo es: {area:.2f}")

    areas_lista.append(area)
    contador+=1
    areas_dic[f"triangulo{contador}"]=area


    cont = input("¿Desea ingresar otros datos (S/N)? ").upper().strip()
    areas_tuple=tuple(areas_lista)
    areas_sets=set(areas_lista)

    if len(areas_lista):
        prom= sum(areas_lista)/len(areas_lista)
        print("\n -------resultados-------")
        print("Lista:",areas_lista)
        print("tuple:",areas_tuple)
        print("lista de valores sin repetir",areas_sets)
        print("Diccionario",areas_dic)
        print(f"El promedio de todas las áreas es: {prom:.2f}")
        

