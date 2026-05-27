while True:
    quant = float(input('Digite quando de dinheiro você tem: [0 para parar] R$'))
    if quant == 0:
        break
    if quant < 5000:
        print(f'Insento de imposto')
    if quant >= 5000 and quant < 7400:
        imposto = quant * 14 / 100
        imposto = quant + imposto
        print(f'Com imposto de 14% seu dinheiro fica por :R${imposto}')
    if quant >= 7400:
        imposto = quant * 27 / 100
        imposto = quant + imposto
        print(f'Com imposto de 14% seu dinheiro fica por :R${imposto}')
print('=== ENCERRADO ===')