import random

class Conta:
    def __init__(self, titular) -> None:
        self.titular = titular
        self.numero = random.randint(1000,9999)
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def tranferir(self, conta_transferencia, valor):
        deucerto = self.sacar(valor)
        if deucerto:
            return conta_tranferencia.depositar(valor)
        
    
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade