mochila = ['Espada enferrujada', 'poção da vida', 'escudo de madeira']
mochila.append('cajado mágico')
print(mochila)
mochila.remove('Espada enferrujada')
print(mochila)
for pocao in mochila:
    if pocao == "poção de mana":
        print('A poção está disponível')
    else:
        print('A poção não está disponivel')
