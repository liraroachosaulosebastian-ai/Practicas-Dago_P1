def pago_energia(kWh, tarifa):
    return kWh * tarifa

resultados = []
continuar = "S"

while continuar == "S":
    kWh = float(input("Consumo en kWh: "))
    tarifa = float(input("Tarifa por kWh: "))
    resultado = pago_energia(kWh, tarifa)
    resultados.append(resultado)
    print("Costo de energía eléctrica:", resultado)

    continuar = input("¿Deseas calcular otro? (S/N): ").upper()

print("\nResultados en lista:", resultados)
print("Resultados en tupla:", tuple(resultados))
print("Resultados en set:", set(resultados))
print("Promedio:", sum(resultados)/len(resultados))
