def salario_semanal(horas, pago_hora):
    return horas * pago_hora

resultados = []
continuar = "S"

while continuar == "S":
    horas = float(input("Horas trabajadas: "))
    pago = float(input("Pago por hora: "))
    resultado = salario_semanal(horas, pago)
    resultados.append(resultado)
    print("Salario semanal:", resultado)

    continuar = input("¿Deseas calcular otro? (S/N): ").upper()

print("\nResultados en lista:", resultados)
print("Resultados en tupla:", tuple(resultados))
print("Resultados en set:", set(resultados))
print("Promedio:", sum(resultados)/len(resultados))
