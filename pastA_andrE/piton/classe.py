class Pessoa:
    def __init__(self, nome , idade):
        self.nome=nome
        self.idade=idade

    def saudacao(self):
        return f"ola boa tarde! meu nome é {self.nome} e tenho {self.idade} anos"
    
    def maior_de_idade(self):
        if self.idade >=18:
            return True
        return False
    

    def destinatario(self):
        if self.idade>=18:
            return f"para onde {self.nome} deseja viajar?"
        return False
    
    