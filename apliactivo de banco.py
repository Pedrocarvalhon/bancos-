from datetime import datetime

# ===================== CRIAR CONTA =====================
def criar_conta():
    print("\n===== CRIAÇÃO DE CONTA =====")
    nome = input("Digite seu nome: ")
    agencia = input("Digite a agência: ")
    conta = input("Digite o número da conta: ")
    senha = input("Crie uma senha: ")

    cliente = {
        'nome': nome,
        'agencia': agencia,
        'conta': conta,
        'senha': senha,
        'saldo': 0.0,   # começa sem dinheiro
        'pix': {},
        'cartao_limite': 1000.0,  # limite inicial
        'extrato': []
    }

    print("\n✅ Conta criada com sucesso!\n")
    return cliente

# ===================== LOGIN =====================
def login(cliente):
    print("\n======= LOGIN ==========")
    agencia = input("Agência: ")
    conta = input("Conta: ")
    senha = input("Senha: ")

    if agencia != cliente['agencia'] or conta != cliente['conta'] or senha != cliente['senha']:
        print("⚠️ Dados incorretos.\n")
        return False
    return True

# ===================== PÁGINA INICIAL =====================
def mostrar_pagina_inicial(cliente):
    print("\n=========== BEM-VINDO ===============")
    print(f"Nome: {cliente['nome']}")
    print(f"Agência: {cliente['agencia']}")
    print(f"Saldo: R${cliente['saldo']:.2f}")
    print(f"Cartão virtual: R${cliente['cartao_limite']:.2f}\n")

# ===================== MENU =====================
def menu():
    print("============== MENU ==============")
    print("1 - Consultar chaves Pix")
    print("2 - Cadastrar nova chave Pix")
    print("3 - Fazer Pix")
    print("4 - Depósito")
    print("5 - Saque")
    print("6 - Alterar limite do cartão")
    print("7 - Alterar senha")
    print("8 - Mostrar extrato")
    print("0 - Sair")
    print("==================================")

# ===================== OPERAÇÕES =====================
def consultar_chave_pix(cliente):
    print("\n===== SUAS CHAVES PIX =====")
    if not cliente['pix']:
        print("Nenhuma chave Pix cadastrada.")
    else:
        for tipo, chave in cliente['pix'].items():
            print(f"{tipo.capitalize()}: {chave}")
    input("\n👉 Pressione ENTER para voltar ao menu...")

def cadastrar_chave_pix(cliente):
    print("\n===== CADASTRAR CHAVE PIX =====")
    tipo = input("Digite o tipo da chave (cpf, celular, email, aleatoria): ").lower()
    nova_chave = input("Digite a nova chave Pix: ")
    cliente['pix'][tipo] = nova_chave
    registrar_extrato(cliente, f"Nova chave Pix cadastrada ({tipo}): {nova_chave}")
    print("✅ Chave Pix cadastrada com sucesso!")
    input("\n👉 Pressione ENTER para voltar ao menu...")

def fazer_pix(cliente):
    print("\n===== FAZER PIX =====")
    try:
        valor = float(input("Digite o valor do Pix: ").replace(",", "."))
    except ValueError:
        print("⚠️ Valor inválido.")
        return

    destino = input("Digite a chave Pix do destinatário: ")

    if cliente['saldo'] - valor < -cliente.get('cartao_limite', 0):
        print("⚠️ Saldo + limite insuficiente.")
    else:
        cliente['saldo'] -= valor
        registrar_extrato(cliente, f"Pix de R$ {valor:.2f} enviado para {destino}")
        print(f"✅ Pix de R$ {valor:.2f} realizado com sucesso!")
        print(f"Saldo atual: R$ {cliente['saldo']:.2f}")

    input("\n👉 Pressione ENTER para voltar ao menu...")


def deposito(cliente):
    print("\n===== DEPÓSITO =====")
    valor = float(input("Digite o valor do depósito: "))
    cliente['saldo'] += valor
    registrar_extrato(cliente, f"Depósito realizado: R$ {valor:.2f}")
    print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
    input("\n👉 Pressione ENTER para voltar ao menu...")

def saque(cliente):
    print("\n===== SAQUE =====")
    valor = float(input("Digite o valor do saque: "))

    # também permite saldo negativo
    cliente['saldo'] -= valor
    registrar_extrato(cliente, f"Saque realizado: R$ {valor:.2f}")
    print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")

    input("\n👉 Pressione ENTER para voltar ao menu...")

def alterar_limite_cartao(cliente):
    print("\n===== ALTERAR LIMITE DO CARTÃO =====")
    novo_limite = float(input("Digite o novo limite do cartão: "))
    cliente['cartao_limite'] = novo_limite
    registrar_extrato(cliente, f"Limite do cartão alterado para R$ {novo_limite:.2f}")
    print(f"✅ Limite alterado para R$ {novo_limite:.2f}")
    input("\n👉 Pressione ENTER para voltar ao menu...")

def alterar_senha(cliente):
    print("\n===== ALTERAR SENHA =====")
    nova_senha = input("Digite a nova senha: ")
    cliente['senha'] = nova_senha
    registrar_extrato(cliente, "Senha alterada com sucesso.")
    print("✅ Senha alterada com sucesso!")
    input("\n👉 Pressione ENTER para voltar ao menu...")

def registrar_extrato(cliente, descricao):
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    cliente['extrato'].append(f"[{data}] {descricao}")

def mostrar_extrato(cliente):
    print("\n===== EXTRATO =====")
    if not cliente['extrato']:
        print("Nenhuma movimentação encontrada.")
    else:
        for item in cliente['extrato']:
            print("-", item)
    print(f"\nSaldo atual: R$ {cliente['saldo']:.2f}")
    print("====================")
    input("\n👉 Pressione ENTER para voltar ao menu...")

# ===================== MAIN =====================
def main():
    print("===== BEM-VINDO AO BANCO =====")
    escolha = input("Você já tem conta? (s/n): ").lower()

    if escolha == 's':
        # Cliente fixo para teste
        cliente = {
            'nome': 'Pedro Carvalho',
            'agencia': '011',
            'conta': 'teste',
            'senha': 'brunna19',
            'saldo': 1500.0,
            'pix': {
                'cpf': "040.747.111-17"
            },
            'cartao_limite': 1800.0,
            'extrato': []
        }
    else:
        cliente = criar_conta()

    if not login(cliente):
        return

    mostrar_pagina_inicial(cliente)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            consultar_chave_pix(cliente)
        elif opcao == '2':
            cadastrar_chave_pix(cliente)
        elif opcao == '3':
            fazer_pix(cliente)
        elif opcao == '4':
            deposito(cliente)
        elif opcao == '5':
            saque(cliente)
        elif opcao == '6':
            alterar_limite_cartao(cliente)
        elif opcao == '7':
            alterar_senha(cliente)
        elif opcao == '8':
            mostrar_extrato(cliente)
        elif opcao == '0':
            print("\n✅ Obrigado por usar nosso caixa eletrônico. Até mais!")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

# ===================== INICIAR PROGRAMA =====================
if __name__ == "__main__":
    main()
