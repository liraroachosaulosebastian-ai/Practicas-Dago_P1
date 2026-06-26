print("\033c")

def area_triangulo(base, altura):
    return (base * altura) / 2

resultados=[]
continuar="S"

while continuar=="S":
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    resultado = area_triangulo(base, altura)
    resultados.append(resultado)
    print("Área del triángulo:", resultado)

    continuar = input("¿Deseas calcular otro? (S/N): ").upper().strip()

print("\nResultados en lista:", resultados)
print("Resultados en tupla:", tuple(resultados))
print("Promedio:", sum(resultados)/len(resultados))
