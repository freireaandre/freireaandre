from Conta import Pessoa, Conta

contas = []

def listar():
    for conta in contas:
        print(f" Cliente: {conta.titular.nome} numero da conta {conta.numero} o saldo {conta.saldo} ")

def pesquisa_contas(numero):
    for conta in contas:
        if numero == conta.numero:
            return conta
            

def menu():

    escolha = int(input("Escolha uma opcao:\
                        \n1 para listar contas\
                        \n2 para inserir contas\
                        \n3 para depositar\
                        \n4 para sacar\
                        \n5 para tranferir\
                        \n0 para sair\n"))
    return escolha

def main():
    escolha = menu()
    while escolha != 0:
        match(escolha):
            case 1:
                listar()
            case 2:
                nome = input("Digite o nome do cliente: ")
                idade = input("digite sua idade: ")
                pessoa = Pessoa(nome, idade)
                contas.append(Conta(pessoa))
            case 3:
                valor = float(input("Digite o valor a ser depositado: "))
                numero_conta = int(input("Digite o numero da conta: "))
                conta = pesquisa_contas(numero_conta)
                deposito_ocorreu = conta.depositar(valor)
                if deposito_ocorreu:
                    print(f"Desito no valor de {valor} ocerreu com sucesso, saldo {conta.saldo}")
                else:
                    print("Ocorreu um erro ao depositar.")
            case 4:
                valor = float(input("Digite o valor a ser sacado: "))
                numero_conta = int(input("Digite o numero da conta: "))
                conta = pesquisa_contas(numero_conta)
                saque_ocorreu = conta.sacar(valor)

                if saque_ocorreu:
                    print(f"Saque de {valor} feito com sucesso!")
                else:
                    print(f"Verifique seu saldo, saque do valor {valor} não realizado.")
            case 5:
                # Tranferencia
                valor = float(input("digite o valor a ser tranferido: "))
                numero_conta = int(input("digite o numero da sua conta: " )) 
                conta_transferencia = int(input("digite o numero da conta a ser tranferida: "))
                conta = pesquisa_contas(numero_conta)
                conta_destino = pesquisa_contas(conta_transferencia)
                transferencia_ocorrida = conta.tranferir(conta_destino,valor)
                if transferencia_ocorrida:
                    print(f"transferencia de {valor} feita para {numero_conta.numero} feita com sucesso ")
                else:
                    print(f"verifique seu saldo, transferencia do valor {valor} para {conta_destino.numero} nao realizado")

                
        escolha = menu()

if __name__ == '__main__':
    main()