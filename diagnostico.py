febre=input('Você sente febre?  (S/N)')
if febre == "S":
    dor_de_cabeça=input('Você está com dor de cabeça (S/N)')
    if dor_de_cabeça == "S":
        print('Possível diagnóstico: Gripe')
    else:
        print('Possivel diagnóstico? infecção leve.')
else:
    coriza=input('Você está com coriza? (S/N)')
    if coriza == 's':
        print("Possivel resfriado comum")
    else:
        print('Possivel diagnostico: Outra Condição ou Estado Normal')