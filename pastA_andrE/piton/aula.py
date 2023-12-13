nome=input("digite seu nome: ")
idade=int(input("digite sua idade: "))
def valor_plano(idade=None, valor=None):
    if idade == None or valor == None:
        return print("valores idade e valores sao obrigatorios")
    print(f"vc tem {idade} anos e o valor do plano é {valor} por mes ")
if idade >= 0 and idade <= 18:
    valor_plano(idade, "95,80")
elif idade >=18 and idade <= 24:
   valor_plano(idade, "117,90")
elif idade>24 and idade <= 28:
    valor_plano(idade,"137,90")
elif idade>28 and idade <= 36:
    valor_plano(idade,"163,90")
elif idade>36 and idade <=45:
    valor_plano(idade,"170,90")
elif idade > 45 and idade<=60:
    valor_plano(idade,"250,00")
else:
    valor_plano()