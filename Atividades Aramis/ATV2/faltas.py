
faltas = int(input("Digite o numero de faltas que vc tem: "))
limite = 10

if faltas > limite:
    print("Vc está acima do limite de faltas")
elif faltas == limite:
    print("Vc está no limite de faltas e nao pode mais faltar")
else:
    print(f"Você possui {faltas} faltas, o limite é 10")