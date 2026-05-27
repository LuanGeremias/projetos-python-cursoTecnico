n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4
if media > 6:
    situa = 'Aprovado'
elif media >= 4 or media <= 6:
    situa = 'Recuperação'
else:
    situa = 'Reprovado'
print(f'Situação do aluno: {situa}')