
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if n1 < 0 or n2 < 0:
    print("Nota invalida")

elif n1 > 10 or n2 > 10:
    print("Nota invalida")

else:
    print(f"Sua média é de: {media}")