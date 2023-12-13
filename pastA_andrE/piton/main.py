from classe import Pessoa

def main():
    pessoa=Pessoa("andre",23)
    print("execultando script...")

    print(pessoa.saudacao())

    if pessoa.maior_de_idade():
        print(f"{pessoa.nome} pode viajar sozinho! ")

    print(pessoa.destinatario())




if __name__ == "__main__":
    main()
