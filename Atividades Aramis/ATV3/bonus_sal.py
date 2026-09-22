
salario = float(input("Digite o salario do funcionario: "))
anostrab = int(input("Digite a quantidade de anos de empresa: "))

if anostrab >= 2 and anostrab <= 5:
    bonus = (salario * 0.05)
    salfinal = (bonus + salario)
    print(f"O salario original é de: {salario}, o bonus é de: {bonus} e o salario final é de:{salfinal}")

elif anostrab > 5 and salario < 3000.00:
    bonus = (salario * 0.10)
    salfinal = (bonus + salario)
    print(f"O salario original é de: {salario}, o bonus é de: {bonus} e o salario final é de:{salfinal}")

elif anostrab > 5 and salario >= 3000.00:
    bonus = (salario * 0.15)
    salfinal = (bonus + salario)
    print(f"O salario original é de: {salario}, o bonus é de: {bonus} e o salario final é de:{salfinal}")

else:
    print(f"O salario original é: {salario}, o bonus é 0 e o salario final é {salario}")