# Henrique Arnaud

print("Bem vindos à máquina de vendas")

torcida = int(5)
fandangos = int(7)
amendoim = int(4)

pepsi = int(4)
coca = int(6)
fanta = int(3)

escolha = ""
qntd = int()
preco = float(0)

while True:
    print("\nÍtens disponíveis:")
    print(f"1-Salgadinho Torcida: ({torcida})\t2-Salgadinho Fandangos: ({fandangos})\t3-Amendoim Torrado: ({amendoim})")
    print(f"4-Pepsi: ({pepsi})\t5-Coca-Cola: ({coca})\t6-Fanta Uva: ({fanta})")
    print("\nEscolha o ítem que deseja comprar digitando o índice (exemplo: 4 para escolher pepsi)")
    escolha = input()

    if escolha == "1":
        print("Quantas unidades de Torcida deseja comprar? (3,50R$/un)")
        qntd = int(input())
        if qntd < 0:
            print("Valor inválido, tente novamente mais tarde.")
        elif torcida >= qntd:
            torcida -= qntd
            preco = preco + (qntd*3.50)
        else:
            print("Quantidade superior a existente, tente novamente mais tarde.")

    elif escolha == "2":
        print("Quantas unidades de Fandangos deseja comprar? (3,00R$/un)")
        qntd = int(input())
        if qntd < 0:
            print("Valor inválido, tente novamente mais tarde.")
        elif fandangos >= qntd:
            fandangos -= qntd
            preco = preco + (qntd * 3.00)
        else:
            print("Quantidade superior a existente, tente novamente mais tarde.")

    elif escolha == "3":
        print("Quantas unidades de Amendoim Torrado deseja comprar? (2,00R$/un)")
        qntd = int(input())
        if qntd < 0:
            print("Valor inválido, tente novamente mais tarde.")
        elif amendoim >= qntd:
            amendoim -= qntd
            preco = preco + (qntd * 2.00)
        else:
            print("Quantidade superior a existente, tente novamente mais tarde.")

    elif escolha == "4":
        print("Quantas unidades de Pepsi deseja comprar? (3,50R$/un)")
        qntd = int(input())
        if qntd < 0:
            print("Valor inválido, tente novamente mais tarde.")
        elif pepsi >= qntd:
            pepsi -= qntd
            preco = preco + (qntd * 3.50)
        else:
            print("Quantidade superior a existente, tente novamente mais tarde.")

    elif escolha == "5":
        print("Quantas unidades de Coca-Cola deseja comprar? (4,00R$/un)")
        qntd = int(input())
        if qntd < 0:
            print("Valor inválido, tente novamente mais tarde.")
        elif coca >= qntd:
            coca -= qntd
            preco = preco + (qntd * 4.00)
        else:
            print("Quantidade superior a existente, tente novamente mais tarde.")

    elif escolha == "6":
        print("Quantas unidades de Fanta Uva deseja comprar? (3,00R$/un)")
        qntd = int(input())
        if qntd < 0:
            print("Valor inválido, tente novamente mais tarde.")
        elif fanta >= qntd:
            fanta -= qntd
            preco = preco + (qntd * 3.00)
        else:
            print("Quantidade superior a existente, tente novamente mais tarde.")

    while True:
        print("Deseja comprar mais alguma coisa? (resposta tem que ser sim ou nao)")
        escolha = input().lower()
        if escolha == "sim" or escolha == "nao":
            break
    if escolha == "nao":
        break
print(f"\nPreço total da compra: {preco}R$")
print("Obrigado por comprar conosco, volte sempre!")
