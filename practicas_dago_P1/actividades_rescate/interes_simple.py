def interes_simple(P, r, t):
    return P * r * t

resultados = []
continuar = "S"

while continuar == "S":
    P = float(input("Capital: "))
    r = float(input("Tasa de interés: "))
    t = float(input("Tiempo: "))
    resultado = interes_simple(P, r, t)
    resultados.append(resultado)
    print("Interés simple:", resultado)

    continuar = input("¿Deseas calcular otro? (S/N): ").upper()

print("\nResultados en lista:", resultados)
print("Resultados en tupla:", tuple(resultados))
print("Resultados en set:", set(resultados))
print("Promedio:", sum(resultados)/len(resultados))
