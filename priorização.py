severidade=int(input('Digite o nivel da severidade, 1 a 5: '))
probabilidade=int(input('Digite o nivel da probabilidade, 1 a 5: '))

if severidade >3 and probabilidade >3:
    print('Risco: Alta Prioridade')
elif severidade >3 or probabilidade >3:
    print('Risco: Média Prioridade')
else:
    print('Risco: Baixa Prioridade')