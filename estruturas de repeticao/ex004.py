while True:
    num = int(input('''1 para somar
2 para subtrair
3 para dividir
4 para multiplicar
0 para parar
Digite sua opção: '''))
    if num == 0:
        break
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    if num == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif num == 2:
        if num1 > num2:
            print(f'{num1} - {num2} = {num1 - num2}')
        elif num2 > num1:
            print(f'{num2} - {num1} = {num1 - num2}')
        else:
            print(f'{num1} - {num2} = {num1 - num2}')
    elif num == 3:
        if num1 > num2:
            print(f'{num1} / {num2} = {num1 / num2}')
        elif num2 > num1:
            print(f'{num2} / {num1} = {num1 / num2}')
        else:
            print(f'{num1} / {num2} = {num1 / num2}')
    elif num == 4: 
        print(f'{num1} * {num2} = {num1 * num2}')
    else:
        print('Número incorreto')
