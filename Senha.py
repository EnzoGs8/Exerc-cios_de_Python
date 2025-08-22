senha=input('Digite a sua senha: ')

while len(senha)<8:
    print('Senha invalida! Deventer 8 caracteres')
    senha=input('tente novamente: ')
print('Senha Criada com sucesso')    