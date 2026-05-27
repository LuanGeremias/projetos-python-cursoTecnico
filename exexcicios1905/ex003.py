sexo = input('Digite o sexo: [M/F] ')
id = int(input('Digite a idade: '))
if sexo in 'Ff' and id >= 50:
    print('Elegível para aposentadoria')
elif sexo in 'Mm' and id >= 65:
    print('Elegível para aposentadoria')
else:
    print('Não elegível para aposentadoria')