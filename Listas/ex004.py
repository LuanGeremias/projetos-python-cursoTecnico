produtos = ['teclado', 'mouse', 'monitor', 'webcan']
produtos.append('fone de ouvido')
print(produtos)
produtos.remove('mouse')
print(produtos)
x = produtos.index('monitor')
produtos[x] = 'tela curva'
print(produtos)