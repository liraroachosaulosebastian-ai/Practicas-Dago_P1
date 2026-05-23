'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''
1#
num = float(input("Ingresa un numero: "))

print(num * 1)
print(num * 2)
print(num * 3)
print(num * 4)
print(num * 5)
print(num * 6)
print(num * 7)
print(num * 8)
print(num * 9)
print(num * 10)

primer_n = 1

multi = num * primer_n
print(f"{num} X {primer_n} = {multi}")
primer_n += 1

multi = num * primer_n
print(f"{num} X {primer_n} = {multi}")
primer_n += 1

multi = num * primer_n
print(f"{num} X {primer_n} = {multi}")
primer_n += 1

multi = num * primer_n
print(f"{num} X {primer_n} = {multi}")
primer_n += 1

multi = num * primer_n
print(f"{num} X {primer_n} = {multi}")
primer_n += 1

multi = num * primer_n
print(f"{num} X {primer_n} = {multi}")
primer_n += 1

multi = num * primer_n
print(f"{num} X {primer_n} = {multi}")
primer_n += 1

multi = num * primer_n
print(f"{num} X {primer_n} = {multi}")
primer_n += 1

multi = num * primer_n
print(f"{num} X {primer_n} = {multi}")
primer_n += 1

multi = num * primer_n
print(f"{num} X {primer_n} = {multi}")
primer_n += 1

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- con estructuras de control
  2.- sin funciones

'''
print("\033c")
n2 = float(input("Ingresa un numero: "))

for nfor in range(1,11):
    multip = nfor * n2
    print(multip)
 
num3 = 0
while num3 >= 11:
     num3 += 1
     print(n2 * num3)


'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- con funciones

'''

def multiplicacion (n11, contadorf):
     
     multif = n11 * contadorf
     print (multif)
     contadorf += 1
     return contadorf

contadorf = 1
n11 = float(input("Ingresa un numero: "))
nf = multiplicacion(n11, contadorf)
nf = multiplicacion(n11, nf)
nf = multiplicacion(n11, nf)
nf = multiplicacion(n11, nf)
nf = multiplicacion(n11, nf)
nf = multiplicacion(n11, nf)
nf = multiplicacion(n11, nf)
nf = multiplicacion(n11, nf)
nf = multiplicacion(n11, nf)
nf = multiplicacion(n11, nf)
    
     
'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- con estructuras de control
  2.- con funciones

'''
num=float(input("ingrese un numero: "))
 
def multiplicacion(n11, contador):
     for i in range (10,0,1):
          nf=multiplicacion(n11,nf)
          