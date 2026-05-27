saldo = float(input('Digite o saldo da conta: '))
while op !=
    op = int(input('''1 para saque
    2 para depósito
    3 para consulta do saldo'''))
    if op == 1:
        saque = float(input('Digite a quantidade que deseja sacar: R$'))
        if saque > saldo:
            print('Valor inválido!')
        else:
            print(f'Voce sacou R${saque} ')
            print(f'Seu saldo ficou com {saldo - saque}')
    elif op == 2:
        depo = float(input('Digite a quantidade que deseja depositar: R$'))
        print(f'Seu saldo ficou com R${saldo + depo}')
    elif op == 3:
        print(f'Seu saldo está com R${saldo}')
    else:
        print('Opção invalida')


