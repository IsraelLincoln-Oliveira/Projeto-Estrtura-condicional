Valor = float(input("Digite o valor do produto: "))
if Valor < 200:
    Desconto = Valor * 0.05
    print("Parabéns! Você recebeu um desconto de 5% no valor do produto. O valor final do produto é: R$", Valor - Desconto)
elif Valor >= 200 and Valor < 300:
    Desconto = Valor * 0.10
    print("Parabéns! Você recebeu um desconto de 10% no valor do produto. O valor final do produto é: R$", Valor - Desconto)
else:
    Desconto = Valor * 0.15
    print("Parabéns! Você recebeu um desconto de 15% no valor do produto. O valor final do produto é: R$", Valor - Desconto)