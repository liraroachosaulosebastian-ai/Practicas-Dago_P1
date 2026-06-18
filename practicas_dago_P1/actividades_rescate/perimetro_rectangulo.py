def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

resultados = []
continuar = "S"

while continuar == "S":
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    resultado = perimetro_rectangulo(base, altura)
    resultados.append(resultado)
    print("Perímetro del rectángulo:", resultado)

    continuar = input("¿Deseas calcular otro? (S/N): ").upper()

print("\nResultados en lista:", resultados)
print("Resultados en tupla:", tuple(resultados))
print("Resultados en set:", set(resultados))
print("Promedio:", sum(resultados)/len(resultados))