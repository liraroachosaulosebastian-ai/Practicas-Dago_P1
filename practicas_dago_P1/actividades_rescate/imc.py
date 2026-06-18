def imc(peso, altura):
    return peso / (altura**2)

resultados = []
continuar = "S"

while continuar == "S":
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    resultado = imc(peso, altura)
    resultados.append(resultado)
    print("Índice de Masa Corporal:", resultado)

    continuar = input("¿Deseas calcular otro? (S/N): ").upper()

print("\nResultados en lista:", resultados)
print("Resultados en tupla:", tuple(resultados))
print("Resultados en set:", set(resultados))
print("Promedio:", sum(resultados)/len(resultados))
