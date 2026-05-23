#inicio 
contador=0
total_sueldos=0
continuar="S"


while continuar == "S":

    nombre=input("ingrese el nombre: ")
    horas_tra=int(input("ingrese las horas trabajadas: "))
    sueldo_horas=float(input("ingrese el sueldo por horas:"))

    sueldo_base= horas_tra * sueldo_horas

    if horas_tra==10:
      porcentaje=0.20
    elif horas_tra==15:
      porcentaje=0.30
    elif horas_tra==20:
     porcentaje=0.15
    elif horas_tra > 25: 
     porcentaje=0.08

    aumento=sueldo_base * porcentaje
    sueldo_neto= sueldo_base + aumento 

    print(f"aumento a pagar: {aumento}")
    print(f"sueldo neto: {sueldo_neto}")

    contador=contador+1
    total_sueldos=total_sueldos + sueldo_neto

    continuar=input("¿desea ingresar otro trabajador? (S/N):")


print(f"total de trabajadores ingresados: {contador}")
print(f"monto total de sueldos netos: {total_sueldos}")

#fin
