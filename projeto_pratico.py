menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """


saldo = 0 
extrato = ""
depositar = 0
sacar = 0
limite_saque = 500
limite_dia = 0


while True:
    opção = input(menu)
    
    # depositar
    if opção == "1":
        depositar = float(input ( "Qual valor deseja depositar: "))
        if depositar > 0:
            saldo += depositar
            print("Depósito efetuado com sucesso!")
            extrato += f"Depósito: {depositar: .2f} \n "
        else:
            print("Opção inválida!")
    #sacar
    if opção== "2":
        sacar = float(input("Qual o valor deseja sacar: "))
        if limite_dia <= 3:
            if sacar <= limite_saque:
                print("saque efetuado com sucesso!")
                saldo -= sacar
                extrato += f" saque: {sacar:.2f} "
            else: 
                print (f"Valor solicitado está acima do limite diário, limite diário R$ {limite_saque: .2f}")
        else: 
            print(" Você atingiu o limite diário de saques, favor tentar novamente após 24 horas")
        limite_dia += 1

     #exibir extrato
    if opção == "3":
        print(f"Suas movimentações em conta %s" %extrato)
        print("nao foram efetuadas alterações em sua conta" if not extrato else extrato)
        print(f"saldo total R$ {saldo: .2f}")
    # sair
    if opção == "4":
        break