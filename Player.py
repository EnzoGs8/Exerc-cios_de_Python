def Players(classe, save):
   
    save_vazio = ["save1, save2, save3, save4"]

    if classe == "Arqueiro" and save in save_vazio:
        print("Salvando em um save vaziol...")
    elif classe == "Mago" and save in save_vazio:
        print("Salvando em um save vaziol...")
    elif classe == "Gladiador" and save in save_vazio:
        print("Salvando em um save vaziol...")
    elif classe == "Assassino" and save in save_vazio:
        print("Salvando em um save vaziol...")
    else:
        print("Erro! Save já utilizado, classe já escolhida ou todos os saves estão cheios")

Players = input("Qual classe gostaria de selecionar?: ").lower()
dia = input(": ").lower()

resultado = Players(classe, save)
print(resultado)