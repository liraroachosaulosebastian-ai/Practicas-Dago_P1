def longitud_circunferencia(radio):
    return 2 * 3.1416 * radio

resultados = []
continuar = "S"

while continuar == "S":
    radio = float(input("Radio: "))
    resultado = longitud_circunferencia(radio)
    resultados.append(resultado)
    print("Longitud de la circunferencia:", resultado)

    continuar = input("¿Deseas calcular otro? (S/N): ").upper()

print("\nResultados en lista:", resultados)
print("Resultados en tupla:", tuple(resultados))
print("Resultados en set:", set(resultados))
print("Promedio:", sum(resultados)/len(resultados))
