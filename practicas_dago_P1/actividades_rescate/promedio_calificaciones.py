def promedio_calificaciones(c1, c2, c3):
    return (c1 + c2 + c3) / 3

resultados = []
continuar = "S"

while continuar == "S":
    c1 = float(input("Calificación 1: "))
    c2 = float(input("Calificación 2: "))
    c3 = float(input("Calificación 3: "))
    resultado = promedio_calificaciones(c1, c2, c3)
    resultados.append(resultado)
    print("Promedio de calificaciones:", resultado)

    continuar = input("¿Deseas calcular otro? (S/N): ").upper()

print("\nResultados en lista:", resultados)
print("Resultados en tupla:", tuple(resultados))
print("Resultados en set:", set(resultados))
print("Promedio:", sum(resultados)/len(resultados))
