def area_circulo(radio):
    return 3.1416 * radio**2

resultados = []
continuar = "S"

while continuar == "S":
    radio = float(input("Radio: "))
    resultado = area_circulo(radio)
    resultados.append(resultado)
    print("Área del círculo:", resultado)

    continuar = input("¿Deseas calcular otro? (S/N): ").upper()

print("\nResultados en lista:", resultados)
print("Resultados en tupla:", tuple(resultados))
print("Resultados en set:", set(resultados))
print("Promedio:", sum(resultados)/len(resultados))

