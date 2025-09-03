from datetime import datetime


cliente = {
    'nome': 'pedro carvalho',
    'agencia': '011',
    'conta': '14073642-0',
    'senha': 'pedro19@',
    'saldo': 1500.0,
    'pix': {
        'cpf': "040.747.111-17",
        'celular': "11999998888",
        'email': "pedrocarvalho@gmail.com"
    },
    'cartao_limite': 1800.0,
    'extrato': []
}


def login(cliente):
    print("===== LOGIN =====")
    agencia = input("Agência: ")
    conta = input("Conta: ")
    senha = input("Senha: ")

    if agencia != cliente['agencia'] or conta != cliente['conta'] or senha != cliente['senha']:
        print("⚠️ Dados incorretos.\n")
        return False
    return True

def mostrar_pagina_inicial(cliente):
    print("\n===== BEM-VINDO =====")
    print(f"Nome: {cliente['nome']}")
    print(f"Agência: {cliente['agencia']}")
    print(f"Saldo: R${cliente['saldo']:.2f}\n")

def menu():
    print("===== MENU =====")
    print("1 - Consultar chaves Pix")
    print("2 - Cadastrar nova chave Pix")
    print("3 - Fazer Pix")
    print("4 - Depósito")
    print("5 - Saque")
    print("6 - Alterar limite do cartão")
    print("7 - Alterar senha")
    print("8 - Mostrar extrato")
    print("0 - Sair")


def consultar_chave_pix(cliente):
    print("\n===== SUAS CHAVES PIX =====")
    for tipo, chave in cliente['pix'].items():
        print(f"{tipo.capitalize()}: {chave}")

def cadastrar_chave_pix(cliente):
    tipo = input("Digite o tipo da chave (cpf, celular, email, aleatoria): ").lower()
    nova_chave = input("Digite a nova chave Pix: ")
    cliente['pix'][tipo] = nova_chave
    registrar_extrato(cliente, f"Nova chave Pix cadastrada ({tipo}): {nova_chave}")
    print("✅ Chave Pix cadastrada com sucesso!")

def fazer_pix(cliente):
    valor = float(input("Digite o valor do Pix: "))
    if valor > cliente['saldo']:
        print("⚠️ Saldo insuficiente.")
    else:
        destino = input("Digite a chave Pix do destinatário: ")
        cliente['saldo'] -= valor
        registrar_extrato(cliente, f"Pix de R$ {valor:.2f} enviado para {destino}")
        print(f"✅ Pix de R$ {valor:.2f} realizado com sucesso!")


def deposito(cliente):
    valor = float(input("Digite o valor do depósito: "))
    cliente['saldo'] += valor
    registrar_extrato(cliente, f"Depósito realizado: R$ {valor:.2f}")
    print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")

def saque(cliente):
    valor = float(input("Digite o valor do saque: "))
    if valor > cliente['saldo']:
        print("⚠️ Saldo insuficiente.")
    else:
        cliente['saldo'] -= valor
        registrar_extrato(cliente, f"Saque realizado: R$ {valor:.2f}")
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")

def alterar_limite_cartao(cliente):
    novo_limite = float(input("Digite o novo limite do cartão: "))
    cliente['cartao_limite'] = novo_limite
    registrar_extrato(cliente, f"Limite do cartão alterado para R$ {novo_limite:.2f}")
    print(f"✅ Limite alterado para R$ {novo_limite:.2f}")

def alterar_senha(cliente):
    nova_senha = input("Digite a nova senha: ")
    cliente['senha'] = nova_senha
    registrar_extrato(cliente, "Senha alterada com sucesso.")
    print("✅ Senha alterada com sucesso!")


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
    print(f"Saldo atual: R$ {cliente['saldo']:.2f}")
    print("====================\n")


def main():
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
            print("✅ Obrigado por usar nosso caixa eletrônico. Até mais!")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
