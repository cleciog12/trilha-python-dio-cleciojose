i=0
saldo = 0
extrato = ""
limite_s = 500
numero_saque = 0
limite_saque = 3
print("banco SantoClecio")

while True:
    if i==1:
        valor =float(input('Informe o valor a ser depositado:R$ '))
        if valor > 0:
            saldo += valor
            extrato +=f"Deposito:R$ {valor:.2f}\n"
        else:
            print('Operação falhou, o valor informado e invalido.')
    elif i== 2:
        print('Menu de saque!')
        valor=float(input('Digite o valor que deseja sacar:R$ '))
        sem_saldo = valor > saldo
        sem_limite = valor > limite_s
        limite_de_s = numero_saque>= limite_saque

        if sem_saldo:
            print('Operação invalida, voçê nao tem saldo suficiente')
        elif sem_limite:
            print('Operação invalida, voce exedeu o limide de saque')
        elif limite_de_s:
            print('Opereação invalida, voçê exedeu a quantidade de saques')
        elif valor >0:
            saldo -=valor
            numero_saque +=1
            extrato+= f"Saque R$ {valor:.2f}\n"
        else:
            print('Opereação invalida, o valor informado e invalido')

    elif i==3:
        print('\n###############EXTRATO##############')
        print(f"\nSaldo: R$ {saldo:.2f}")
        
        if extrato == "":
            print('Não foram encontrado movimentação na sua conta')
            



    elif i == 4:
        break
    else:
        print('Menu invalido')


    i =int(input('''
                 Digite um numero:
    
        1: para Deposito
        2: para saque
        3 para Extrato
        4 para sair
        Menu: '''))
    

print('ate logo!!!')
