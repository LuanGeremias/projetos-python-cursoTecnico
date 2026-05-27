preco = float(input('Digite o preço da compra: R$'))
desc = preco * 7 / 100
desc2 = preco - desc
print(f'Sua compra de R${preco} vai ter um desconto de 7%, ou seja, de R${desc} ficando pelo preço final de R${desc2}')
