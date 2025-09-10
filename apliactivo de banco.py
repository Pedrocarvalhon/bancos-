from datetime import datetime

class Cliente:
    def __init__(self, nome, agencia, conta, senha, saldo=0.0, limite=1000.0):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.senha = senha
        self.saldo = saldo
        self.pix = {}
        self.cartao_limite = limite
        self.extrato = []
        #cadastro novo
    def mostrar_dados(self):
        print("\n=========== BEM-VINDO ===============")
        print(f"Nome: {self.nome}")
        print(f"Agência: {self.agencia}")
        print(f"Conta: {self.conta}")
        print(f"Saldo: R${self.saldo:.2f}")
        print(f"Cartão virtual: R${self.cartao_limite:.2f}\n")

    def registrar_extrato(self, descricao):
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.extrato.append(f"[{data}] {descricao}")

    def consultar_pix(self):
        print("\n===== SUAS CHAVES PIX =====")
        if not self.pix:
            print("Nenhuma chave Pix cadastrada.")
        else:
            for tipo, chave in self.pix.items():
                print(f"{tipo.capitalize()}: {chave}")

    def cadastrar_pix(self, tipo, chave):
        self.pix[tipo] = chave
        self.registrar_extrato(f"Nova chave Pix cadastrada ({tipo}): {chave}")
        print("✅ Chave Pix cadastrada com sucesso!")

    def fazer_pix(self, valor, destino):
        if valor > self.saldo:
            print("⚠️ Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.registrar_extrato(f"Pix de R$ {valor:.2f} enviado para {destino}")
            print(f"✅ Pix de R$ {valor:.2f} enviado para {destino}!")

    def deposito(self, valor):
        self.saldo += valor
        self.registrar_extrato(f"Depósito: R$ {valor:.2f}")
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")

    def saque(self, valor):
        if valor > self.saldo:
            print("⚠️ Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.registrar_extrato(f"Saque: R$ {valor:.2f}")
            print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")

    def alterar_limite(self, novo_limite):
        self.cartao_limite = novo_limite
        self.registrar_extrato(f"Limite do cartão alterado para R$ {novo_limite:.2f}")
        print(f"✅ Novo limite: R$ {novo_limite:.2f}")

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        self.registrar_extrato("Senha alterada com sucesso.")
        print("✅ Senha alterada com sucesso!")

    def mostrar_extrato(self):
        print("\n===== EXTRATO =====")
        if not self.extrato:
            print("Nenhuma movimentação encontrada.")
        else:
            for item in self.extrato:
                print("-", item)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("====================")


class Banco:
    def __init__(self):
        self.clientes = []

    def criar_conta(self, nome, agencia, conta, senha):
        cliente = Cliente(nome, agencia, conta, senha)
        self.clientes.append(cliente)
        print("✅ Conta criada com sucesso!")
        return cliente

    def login(self, agencia, conta, senha):
        for cliente in self.clientes:
            if cliente.agencia == agencia and cliente.conta == conta and cliente.senha == senha:
                return cliente
        return None


# ===================== PROGRAMA =====================
def main():
    banco = Banco()

    print("===== 🏦 BEM-VINDO ao Banco🏦 =====")
    escolha = input("Você já tem conta? (s/n): ").lower()

    if escolha == 's':
        # cadastra cliente fixo
        cliente = banco.criar_conta("Pedro Carvalho", "011", "teste", "brunna19")
        cliente.saldo = 1500
        cliente.cartao_limite = 1800
        cliente.cadastrar_pix("cpf", "040.747.111-17")
    else:
        nome = input("Nome: ")
        agencia = input("Agência: ")
        conta = input("Conta: ")
        senha = input("Senha: ")
        cliente = banco.criar_conta(nome, agencia, conta, senha)

    # Login
    print("\n======= LOGIN ==========")
    agencia = input("Agência: ")
    conta = input("Conta: ")
    senha = input("Senha: ")

    usuario = banco.login(agencia, conta, senha)
    if not usuario:
        print("⚠️ Login inválido!")
        return

    usuario.mostrar_dados()

    while True:
        print("\n=========== MENU ===========")
        print("1 - Consultar Pix")
        print("2 - Cadastrar Pix")
        print("3 - Fazer Pix")
        print("4 - Depósito")
        print("5 - Saque")
        print("6 - Alterar limite do cartão")
        print("7 - Alterar senha")
        print("8 - Mostrar extrato")
        print("0 - Sair")
        print("============================")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            usuario.consultar_pix()
        elif opcao == '2':
            tipo = input("Tipo da chave: ")
            chave = input("Digite a chave: ")
            usuario.cadastrar_pix(tipo, chave)
        elif opcao == '3':
            valor = float(input("Valor do Pix: "))
            destino = input("Chave do destinatário: ")
            senha = input("digite a senha para confima o pix:")
            usuario.fazer_pix(valor, destino)
        elif opcao == '4':
            valor = float(input("Valor do depósito: "))
            usuario.deposito(valor)
        elif opcao == '5':
            valor = float(input("Valor do saque: "))
            usuario.saque(valor)
        elif opcao == '6':
            novo_limite = float(input("Novo limite: "))
            usuario.alterar_limite(novo_limite)
        elif opcao == '7':
            nova_senha = input("Nova senha: ")
            usuario.alterar_senha(nova_senha)
        elif opcao == '8':
            usuario.mostrar_extrato()
        elif opcao == '0':
            print("✅ Obrigado por usar nosso banco. Até mais!")
            break
        else:
            print("⚠️ Opção inválida.")


if __name__ == "__main__":
    main()

