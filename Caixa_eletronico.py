valor=int(input('Coloque a quantia do valor que quer sacar: '))
notas={50,20,10,5}
for nota in notas:
    quantidade=valor//nota
    if quantidade>0:
        print(f'{quantidade} nota(s) de R$ {nota}')
        valor-=quantidade*nota
if valor>0:
    print(f"Valor restante de R$ {valor} não pode")        