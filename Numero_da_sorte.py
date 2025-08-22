import random
numero=random.randint(1,5)
tentativas=5

while True:
    palpite=int(input('Digite um numero de 1 a 5: '))
    tentativas +=1
    if palpite<numero:
        print('O número é maior')
    elif palpite>numero:
        print('O número é menor')
    else:
        print('Você acertou o numero')
    break