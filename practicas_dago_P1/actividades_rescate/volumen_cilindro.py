def volumen_cilindro(radio, h):
    return 3.1416 * radio**2 * h

resultados = []
continuar = "S"

while continuar == "S":
    radio = float(input("Radio: "))
    h = float(input("Altura: "))
    resultado = volumen_cilindro(radio, h)
    resultados.append(resultado)
    print("Volumen del cilindro:", resultado)

    continuar = input("¿Deseas calcular otro? (S/N): ").upper()

print("\nResultados en lista:", resultados)
print("Resultados en tupla:", tuple(resultados))
print("Resultados en set:", set(resultados))
print("Promedio:", sum(resultados)/len(resultados))
