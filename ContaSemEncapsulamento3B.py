class contasemencapsulamento:
    def __init__(self, titular, saldo, senha):
        # Todos são públicos
        self.titular = titular
        self.saldo = saldo
        self.senha = senha

    def ver_saldo(self, senha_digitada):
        # Verificar se a senha esta correta
        if senha_digitada == self.senha:
            print(f"Saldo de {self.titular}: R${self.saldo:.2f}")
        else:
            print("Senha Incorreta, Acesso negado.")

# Teste
conta1 = contasemencapsulamento('Sara', 1000.00, '1234')

# Consulta com senha incorreta
conta1.ver_saldo('1234')

# Alterando dados diretamente (Problema)
conta1.saldo = 999_999.99
conta1.senha ='0000'
conta1.titular = "Novo Titular"

# Consulta com a senha alterada indevidamente
conta1.ver_saldo('0000')
