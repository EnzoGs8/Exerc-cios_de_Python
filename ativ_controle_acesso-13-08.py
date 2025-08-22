cargo = input("Digite o cargo do funcionário (gerente, analista, estagiario): ").lower()
dia = input("Digite o dia da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira, sábado, domingo): ").lower()

dias_uteis = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

if cargo == "gerente":
 print("Acesso permitido")
elif cargo == "analista" and dia in dias_uteis:
 print("Acesso permitido")
elif cargo == "estagiario" and dia in dias_uteis:
 print("Acesso permitido")
else:
 print("Acesso negado")

