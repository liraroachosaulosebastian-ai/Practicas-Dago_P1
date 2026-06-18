def volumen_cubo(lado):
    return lado**3

resultados = []
continuar = "S"

while continuar == "S":
    lado = float(input("Lado: "))
    resultado = volumen_cubo(lado)
    resultados.append(resultado)
    print("Volumen del cubo:", resultado)

    continuar = input("¿Deseas calcular otro? (S/N): ").upper()

print("\nResultados en lista:", resultados)
print("Resultados en tupla:", tuple(resultados))
print("Resultados en set:", set(resultados))
print("Promedio:", sum(resultados)/len(resultados))
