import datetime

escolha = ""
while escolha != 'n':
    ano_de_nascimento = int(input("Digite o ano de ascimento do usuario:"))
    mes_de_nascimento =int(input("Digite o mes (Numeros) que o usuario nasceu: "))
    ano_atual = datetime.date.today().year
    mes_atual = datetime.date.today().month
    idade =  ano_atual - ano_de_nascimento
    if mes_atual > 5:
        print("A idade do uuario é", idade)
    escolha = input('Deseja fazer uma nova verificação? S ou N').lower()
