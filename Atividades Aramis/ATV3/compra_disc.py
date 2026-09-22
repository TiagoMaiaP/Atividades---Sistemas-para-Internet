
compra = float(input("Digite o valor da compra: "))

if compra < 100:
    print(f"O valor da compra é: {compra}, o desconto é 0 e o valor total a ser pago é: {compra}")

elif compra >= 100 and compra <= 499.99:
    desc = (compra * 0.1)
    vlrfinal = (desc - compra) * -1
    print(f"O valor da compra é: {compra}, o desconto é {desc} e o valor total a ser pago é: {vlrfinal}")
    
else:
    desc = (compra * 0.15)
    vlrfinal = (desc - compra) * -1
    print(f"O valor da compra é: {compra}, o desconto é {desc} e o valor total a ser pago é: {vlrfinal}")
