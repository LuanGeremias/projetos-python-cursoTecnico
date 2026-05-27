salario = float(input('Digite seu salário: R$'))
if salario <= 100:
    aumento = salario * 20 / 100
elif salario > 1000 and salario <= 2000:
    aumento = salario * 15 / 100
else:
    aumento = salario * 10 / 100
print(f'Seu salário de R${salario} vai receber aumento de R${aumento}, ficando seu salári final por {salario + aumento}')