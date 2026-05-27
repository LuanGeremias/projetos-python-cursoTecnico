while True:
    print('''Opções: 1 somar
            2 subtrair
            3 multiplicar
            4 dividir''')
    op = int(input('Digite a opção: [0 para sair]'))
    if op < 1 or op > 4:
        break
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    while op != 0:
        if op == 1:
            print(f'A soma dos números é {num1 + num2}')
        elif op == 2:
            print(f'A subtração dos números é {num1 - num2}')
        elif op == 3:
            print(f'A multiplicação dos números é {num1 * num2}')
        else:
            print(f'A divisão dos números é {num1 / num2}')
        op = int(input('Digite a opção: [0 para sair]'))
if op == 0:
    print('Encerrado!')
else:
    print('Numero inválido')