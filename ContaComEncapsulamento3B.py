class ContaBancaria:
    def __init__(self, titular, saldo_inicial, senha):
        
        self.titular = titular
        self._saldo = float(saldo_inicial)
        self._senha = str(senha)

    def ver_saldo(self, senha_digitada):
        # Verificar se a senha esta correta
        if str(senha_digitada) == self._senha:
            print(f"Saldo de {self.titular}: R${self._saldo:.2f}")
        else:
            print("Senha Incorreta, Acesso negado.")

# Teste
conta2 = ContaBancaria('Sara', 1000.00, '1234')

# Consulta com senha incorreta
conta2.titular = 'Sara Atualizado'
conta2.ver_saldo('1234')

conta2._saldo = 50.00
conta2.ver_saldo('1234')

try:
    print(conta2.__senha)
except AttributeError:
    print("Atributo privado não pode ser acessado diretamente!")