def celsius_a_fahrenheit(C):
    return (9/5) * C + 32

resultados = []
continuar = "S"

while continuar == "S":
    C = float(input("Temperatura en Celsius: "))
    resultado = celsius_a_fahrenheit(C)
    resultados.append(resultado)
    print("Temperatura en Fahrenheit:", resultado)

    continuar = input("¿Deseas convertir otra? (S/N): ").upper()

print("\nResultados en lista:", resultados)
print("Resultados en tupla:", tuple(resultados))
print("Resultados en set:", set(resultados))
print("Promedio:", sum(resultados)/len(resultados))
