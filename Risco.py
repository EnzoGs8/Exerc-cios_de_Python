risco=input('Digite o tipo de risco. Operacional, Financeiro ou de Mercado: ')

if risco == 'Operacional':
    print('Risco Operacional')
elif risco == 'Financeiro':
    print('Risco Financeiro')
elif risco == 'Mercado':
    print('Risco de Mercado')
else:
    print('O tipo de risco não foi identificado')