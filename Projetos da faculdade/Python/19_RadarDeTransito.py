vel = int(input("Qual foi a velocidade registrada? "))
if vel <= 100 :
    print("Sem infração.")
elif vel > 100 and vel < 100 * 1.20:
    print("Infração media. Valor da multa R$130.16")
elif vel >= 100 * 1.20 and vel < 100 * 1.50:
    print("Infração grave. Valor da multa R$195.23")
elif vel >= 100 * 1.50:
    print("Infração gravíssima. Valor da multa R$880.41")