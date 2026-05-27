salario = float(input('Digite o seu sálario atual: R$'))
aumento = (salario * 13.5 / 100)
aumento2 = aumento + salario
print(f'O seu sálario de {salario} vai aumentar em 13,5%, ou seja, R${aumento:.2f} tornando seu sálario final por {aumento2:.2f}')