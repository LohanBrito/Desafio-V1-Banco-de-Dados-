menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opção = input(menu)
    
    if opção == "1":
        valor = float(input("Valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor: .2f}\n"

        else:
            print("Valor inválida")

    elif opção == "2":
        valor = float(input("Qual o valor desejado para o saque:"))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
           print("Operação Falhou! Saldo Excedido!")

        elif excedeu_limite:
           print("Limite de saque Excedido!")
        
        elif excedeu_saques:
           print("Número de saques excedido!")

        elif valor > 0:
           saldo -= valor
           extrato += f"Saque: R$ {valor: .2f}\n"
           numero_saques += 1
        
        else:
            print("Operação falhaou! Valor inválido!")

    elif opção == "3":
        print("\n-------- EXTRATO --------")
        print("Sem movimentações" if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('--------         --------')

    elif opção == "4":
        break

    else:
        print("Obrigado por usar nossos serviços!\nVolte Sempre")
