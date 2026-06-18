def area_trapecio(B, b, h):
    return ((B + b) * h) / 2

resultados = []
continuar = "S"

while continuar == "S":
    B = float(input("Base mayor: "))
    b = float(input("Base menor: "))
    h = float(input("Altura: "))
    resultado = area_trapecio(B, b, h)
    resultados.append(resultado)
    print("Área del trapecio:", resultado)

    continuar = input("¿Deseas calcular otro? (S/N): ").upper()

print("\nResultados en lista:", resultados)
print("Resultados en tupla:", tuple(resultados))
print("Resultados en set:", set(resultados))
print("Promedio:", sum(resultados)/len(resultados))
