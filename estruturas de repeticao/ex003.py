numeros = 0
while True:
    num = int(input('Digite um número: [Negativo para parar]'))
    numeros += 1
    if num < 0:
        break
print(f'Foram digitados {numeros} números')