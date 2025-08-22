import random

numero=random.randint(1,10000)

tentativa=0

while tentativa<5:
    palpite=int(input('Digite o seu palpite: '))
    tentativa+=1
    if palpite==numero:
        print('Você acertou o numero!')
        break
    elif palpite<numero:
        print('O numero é maior')
    else:
        print('O numero é menor')
if palpite!=numero:
    print(f'fim do jogo! O numero era: {numero}')