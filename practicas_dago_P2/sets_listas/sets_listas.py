#Solucion 1
emails=[]
continuar="S"
while continuar=="S":
    emails.append(int(input("ingresa un email:")).lower().strip())
    continuar=input("Deseas ingresar un nuevo email (S/N)").upper().strip()

print(emails)
set_emails=set(emails)  
emails=list(set_emails)
print(emails)

#Solucion 2
list_emails=[]

cont=True
while cont:
    list_emails.insert(0,input("Ingresa un email: ").lower().strip())
    opc=input("¿Deseas ingresar otro email (S/N)? ").upper().strip()
    if cont=="N":
        cont=False
set_emails=set(list_emails)
list_emails=list(set_emails)
print(list_emails)