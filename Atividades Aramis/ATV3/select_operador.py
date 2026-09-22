n1 = float(input("Digite o primeiro nmr: "))
n2 = float(input("Digite o segundo nmr: "))

operador = input("Digite o operador para definir o que vai acontecer com os 2 numeros digitados: +, -, *, /: ")

if operador == "+":
    print(n1 + n2)

elif operador == "-":
    print(n1 - n2)

elif operador == "*":
    print(n1 * n2)

elif operador == "/":
    print(n1 / n2)

else:
    print("Operador inválido")