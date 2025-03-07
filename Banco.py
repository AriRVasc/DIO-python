menu = """
Escolha uma das opções:
[d] Depositar
[s] Sacar
[e] Retirar Extrato
[q] Sair
"""

QTDE_SAQUES = 3
LIMITE_SAQUE = 500.00
qtd_saque = 0
saldo = 0
extrato = ""

while True:
    opcao = input(menu).strip().lower()  # Remove espaços em branco e padroniza em minúsculas

    if opcao == "d":
        try:
            deposito = float(input("Informe o valor do depósito: ").strip())
            if deposito > 0:
                saldo += deposito
                extrato += f"Foi depositado R$: {deposito:.2f}\n"
                print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
            else:
                print("Valor inválido! Digite um valor maior que zero.")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: ").strip())

            if valor > saldo:
                print("Você não possui saldo suficiente!")

            elif valor > LIMITE_SAQUE:
                print(f"Este valor ultrapassa o limite de saque de R$ {LIMITE_SAQUE:.2f}!")

            elif qtd_saque >= QTDE_SAQUES:
                print("Você atingiu a quantidade máxima de saques diários.")

            elif valor > 0:
                saldo -= valor
                qtd_saque += 1
                extrato += f"Foi realizado um saque de R$: {valor:.2f}\n"
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor informado é inválido para esta operação!")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    elif opcao == "e":
        print("\n################################")
        print("Extrato:\n")
        print("Não foram realizadas operações" if not extrato else extrato)
        print(f"Seu saldo atual é: R$ {saldo:.2f}\n")
        print("################################\n")

    elif opcao == "q":
        print("Saindo do sistema. Obrigado por usar nosso banco!")
        break

    else:
        print("Opção inválida! Por favor, escolha uma das opções do menu.")
