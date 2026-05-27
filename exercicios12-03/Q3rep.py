num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
if num1 > num2 > num3:
    maior = num3
    medio = num2
    menor = num1
elif num2 > num1 > num3:
    maior = num3
    medio = num1
    menor = num2
elif num1 > num3 > num2:
    maior = num2
    medio = num3
    menor = num1
elif num3 > num1 > num2:
    maior = num2
    medio = num1
    menor = num3
elif num3 > num2 > num1:
    maior = num1
    medio = num2
    menor = num3
elif num2 > num3 > num1:
    maior = num1
    medio = num3
    menor = num2
print('A ordem crescente dos números é', maior, medio, menor)
print('E a descrecente é ', menor, medio, maior)
    