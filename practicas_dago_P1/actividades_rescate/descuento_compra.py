def descuento_compra(precio, descuento):
    return precio - (precio * descuento)

resultados = []
continuar = "S"

while continuar == "S":
    precio = float(input("Precio: "))
    desc = float(input("Descuento (ej. 0.2 para 20%): "))
    resultado = descuento_compra(precio, desc)
    resultados.append(resultado)
    print("Precio final:", resultado)

    continuar = input("¿Deseas calcular otro? (S/N): ").upper()

print("\nResultados en lista:", resultados)
print("Resultados en tupla:", tuple(resultados))
print("Resultados en set:", set(resultados))
print("Promedio:", sum(resultados)/len(resultados))
