print("\033c")
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=(23,45,23,33,25,100,-100)
print(numeros)

lista="["
for i in numeros:
   lista+=str(i)
   lista+=f"{i}, "
print(f"{lista}]")

lista="["
i in range (0,len(numeros))
lista+f"{numeros[i]}, "
print(f"{lista}]")

lista="["
i=0
while i<len(numeros):
     lista+=f"{numeros[i]}, "
     i+=1
     print(f"{lista}]")
   


# #Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
palabras=("Hola","NBA","Ganador","Perdedor")
palabra=int(input("Dame la palabra a buscar: "))
encontro=palabras in palabras

# #1er forma  
if encontro==True:
   print(f"esta palabra {palabra}, no se encuentra en la lista") 
else:
   print("no esta en la lista ")


#2DA FORMA
palabras=("Hola","NBA","Ganador","Perdedor")
palabra=int(input("Dame la palabra a buscar: "))

encontre=False
for i in palabras:
 if i==palabra:
       encontre=True 
       if encontro==True:
        print(f"esta palabra {palabra}, no se encuentra en la lista") 
       else:
          print(f"esta palabra {palabra}, no se encuentra en la lista") 

# #3er FORMA
for i in palabras:
  if i==palabra:
       encontre=True 
       if encontro==True:
        print(f"esta palabra {palabra}, no se encuentra en la lista") 
       else:
           print(f"esta palabra {palabra}, no se encuentra en la lista") 

palabras=("Hola","NBA","Ganador","Perdedor")
palabra=int(input("Dame la palabra a buscar: "))

i=0
encontre=False
while i<len(palabras):
  if palabra [i]==palabra:
      encontre=True
      i+=1

if encontre==True:
    print(f"esta palabra {palabra}, no se encontro la palabra")
else:  
   print(f"esta palabra {palabra}, no se encontro la palabra")
  
palabras=("Hola","NBA","Ganador","Perdedor")
palabra=int(input("Dame la palabra a buscar: "))


encontre=False
for i in range (0,len(palabras)):
  if palabra [i]==palabra:
      encontre=True

if encontre==True:
    print(f"esta palabra {palabra}, no se encontro la palabra")
else:  
    print(f"esta palabra {palabra}, no se encontro la palabra")
  


#Ejemplo 3 Añadir elementos a la lista

lista=[]
true="S"
while true=="S":
    valor=input("dame in valor de la lista").upper().strip()
    lista.append(valor)
    true=input("deseas añadir otro elemento a la lista S/N?").upper().strip()

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda=[
         ["carlos","6181234567"]
         ["juan","6182334567"]
         ["tony","6182342323"]
       ]

print(agenda)

# for i in agenda:
#     print(i)


for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])
        
        
        for r in range(0,3):
         for c in range(0,2):
          print(agenda[r][c])