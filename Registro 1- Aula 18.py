T = int(input("Quantas pessoas acessaram o link?: "))

pri_link = 4 * T
seg_link = 2 * T
ter_link = 1 * T


if T < 1:
    print("Erro, precisa de pelo menos 1 pessoa")
elif T > 1000:
    print("Erro, precisa de menos de 1000 pessoas")
else:
    print('O numero de pessoas que acessaram no terceiro link foram ', ter_link, 'No segundo foram', seg_link, 'e no primeiro link foi ', pri_link)