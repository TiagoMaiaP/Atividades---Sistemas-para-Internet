
valorprod = float(input("Digite o valor do produto: "))
valordesc = float(input("Digite o percentual do valor do desconto: "))

desc = (valorprod * valordesc) / 100
vlrfinal = round(valorprod - desc, 2)

print(f"O valor do produto com o desconto é de: R${vlrfinal}.")