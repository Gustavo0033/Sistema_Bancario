import textwrap


def menu():
    menu = """\n
    ============= MENU ============
    [D]\tDepósitar
    [S]\tSacar
    [E]\tExtrato
    [NC]\tNova conta
    [LC]\tListar contas
    [NU]\tNovo usuario
    [Q]\tSair
    
    ==> """

    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print("\n === Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques > limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente!")
    elif excedeu_limite:
        print("Operação falhou! O valor de saque excede o limite!")
    elif excedeu_saque:
        print("Operação falhou! Número máximo de saques excedido!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Sauqe realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou, o valor informado é inválido")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n ============= EXTRATO ==============")
    print("Não foram realizadas moviemntações." if not extrato else extrato)
    print(f"\n Saldo: \t\tR$ {saldo:.2f}")
    print("==============================================")


def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("á existe uma usuário com esse CPF!")
        return

    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla - estado): ")

    usuarios.append({"nome": nome, "data_nacimento": data_nascimento,"cpf": cpf, "endereco": endereco})

    print("========== Usuário criado com sucesso! ================")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None



def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seuc cpf (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n ============ Conta criada com sucesso! =========")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")



def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C\C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))




def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "D":
            valor = float(input("Informe o valor de depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "S":
            valor = float(input("Informe o valor de saque: "))

            saldo, extrato =  sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques = LIMITE_SAQUE
            )

        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "NU":
            criar_usuario(usuarios)

        elif opcao == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "LC":
            listar_contas(contas)
        elif opcao == "Q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")



main()