sala = float(input('Digite seu salário:'))
if sala < 1000:
    aum = sala + (sala * 20 / 100)
    print(f'Seu salário {sala} com aumento de 20% fica por {aum}')
elif sala >= 1000 and sala < 2000:
    aum = sala + (sala * 15 / 100)
    print(f'Seu salário {sala} com aumento de 15% fica por {aum}')
else:
    aum = sala + (sala * 10 / 100)
    print(f'Seu salário {sala} com aumento de 10% fica por {aum}')
