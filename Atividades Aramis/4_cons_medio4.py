
km = float(input("Digite a qtd de km percorrido: "))
lt = float(input("Digite a qtd de litros gastos: "))

consumo = round(km / lt, 2)

print(f"O consumo medio do veiculo é: {consumo}km/l")