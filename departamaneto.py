departamento = input("Digite o departamento (Financeiro, RH, Vendas, TI, Marketing): ").strip().lower()

if departamento == "financeiro":
    print("Recomendação: Computadores desktop de alto desempenho e monitores duplos.")
elif departamento == "rh":
    print("Recomendação: Laptops leves e softwares de gestão de pessoas.")
elif departamento == "vendas":
    print("Recomendação: Tablets e smartphones para mobilidade.")
elif departamento == "ti":
    print("Recomendação: Computadores de alta performance e servidores dedicados.")
elif departamento == "marketing":
    print("Recomendação: Laptops potentes com softwares de edição gráfica.")
else:
    print("Departamento não encontrado. Por favor, verifique o nome digitado.")