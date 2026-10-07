tempo = int(input("Quantas horas você vai ficar no estacionamento ? "))

if tempo <= 0:
    print("TEMPO INVÁLIDO.")
elif tempo <= 2:
    print("Você tera que pagar R${:.2f} por {} hora/s.".format(tempo * 8, tempo))
elif tempo <= 5:
    print("Você tera que pagar R${:.2f} por {} horas.".format(tempo * 6, tempo))
else:
    print("Você tera que pagar R${:.2f} por {} horas.".format(tempo * 5, tempo))