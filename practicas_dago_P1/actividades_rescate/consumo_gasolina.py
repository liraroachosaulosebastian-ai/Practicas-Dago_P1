def consumo_gasolina(km, litros):
    return km / litros

resultados = []
continuar = "S"

while continuar == "S":
    km = float(input("Kilómetros recorridos: "))
    litros = float(input("Litros consumidos: "))
    resultado = consumo_gasolina(km, litros)
    resultados.append(resultado)
    print("Rendimiento (km/l):", resultado)

    continuar = input("¿Deseas calcular otro? (S/N): ").upper()

print("\nResultados en lista:", resultados)
print("Resultados en tupla:", tuple(resultados))
print("Resultados en set:", set(resultados))
print("Promedio:", sum(resultados)/len(resultados))
