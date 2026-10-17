dist = float(input("Qual a distância da entrega em Km? "))
peso = float(input("Qual o peso da encomenda em Kg? "))
tipo = input("É entrega normal ou urgente ? (N ou U)").upper()

if tipo == "N":
    print("Entrega normal não tem acréscimo.")
    if dist <= 10:
        distp = 15
        print("A distancia vai custar R$ {:.2f}".format(distp))
        if peso <= 5:
            print("O peso não da acréscimo. Vai pagar R$ {:.2f} de frete".format(distp))
        elif peso <= 10:
            pesop = 10
            print("O peso da acréscimo de R$ {:.2f} . Vai pagar R$ {:.2f} de frete".format(pesop, pesop + distp))
        else:
            pesop = 20
            print("O peso da acréscimo de R$ {:.2f} . Vai pagar R$ {:.2f} de frete".format(pesop, pesop + distp))
    elif dist <= 30:
        distp = 25
        print("A distancia vai custar R$ {:.2f}".format(distp))
        if peso <= 5:
            print("O peso não da acréscimo. Vai pagar R$ {:.2f} de frete".format(distp))
        elif peso <= 10:
            pesop = 10
            print("O peso da acréscimo de R$ {:.2f} . Vai pagar R$ {:.2f} de frete".format(pesop, pesop + distp))
        else:
            pesop = 20
            print("O peso da acréscimo de R$ {:.2f} . Vai pagar R$ {:.2f} de frete".format(pesop, pesop + distp))
    else:
        distp = 40
        print("A distancia vai custar R$ {:.2f}".format(distp))
        if peso <= 5:
            print("O peso não da acréscimo. Vai pagar R$ {:.2f} de frete".format(distp))
        elif peso <= 10:
            pesop = 10
            print("O peso da acréscimo de R$ {:.2f} . Vai pagar R$ {:.2f} de frete".format(pesop, pesop + distp))
        else:
            pesop = 20
            print("O peso da acréscimo de R$ {:.2f} . Vai pagar R$ {:.2f} de frete".format(pesop, pesop + distp))
elif tipo == "U":
    print("Entrega urgente tem 30% De acréscimo.")
    if dist <= 10:
        distp = 15
        print("A distancia vai custar R$ {:.2f}".format(distp))
        if peso <= 5:
            print("O peso não da acréscimo. Vai pagar R$ {:.2f} de frete".format(distp * 1.30))
        elif peso <= 10:
            pesop = 10
            print("O peso da acréscimo de R$ {:.2f} . Vai pagar R$ {:.2f} de frete".format(pesop, (pesop + distp) * 1.30))
        else:
            pesop = 20
            print("O peso da acréscimo de R$ {:.2f} . Vai pagar R$ {:.2f} de frete".format(pesop, (pesop + distp) * 1.30))
    elif dist <= 30:
        distp = 25
        print("A distancia vai custar R$ {:.2f}".format(distp))
        if peso <= 5:
            print("O peso não da acréscimo. Vai pagar R$ {:.2f} de frete".format(distp * 1.30))
        elif peso <= 10:
            pesop = 10
            print("O peso da acréscimo de R$ {:.2f} . Vai pagar R$ {:.2f} de frete".format(pesop, (pesop + distp) * 1.30))
        else:
            pesop = 20
            print("O peso da acréscimo de R$ {:.2f} . Vai pagar R$ {:.2f} de frete".format(pesop, (pesop + distp) * 1.30))
    else:
        distp = 40
        print("A distancia vai custar R$ {:.2f}".format(distp))
        if peso <= 5:
            print("O peso não da acréscimo. Vai pagar R$ {:.2f} de frete".format(distp * 1.30))
        elif peso <= 10:
            pesop = 10
            print("O peso da acréscimo de R$ {:.2f} . Vai pagar R$ {:.2f} de frete".format(pesop, (pesop + distp) * 1.30))
        else:
            pesop = 20
            print("O peso da acréscimo de R$ {:.2f} . Vai pagar R$ {:.2f} de frete".format(pesop, (pesop + distp) * 1.30))
else:
    print("Tipo inválido tente novamente (N ou U)")