#Construa um programa que simule o funcionamento de um caixa rápido de supermercado. O programa deve solicitar a leitura do preço de vários produtos comprados por um cliente de forma contínua. Como o caixa não sabe de antemão quantos itens o cliente está levando, a entrada de dados só deve ser interrompida quando o operador digitar o valor 0 (zero).
c = 0
s = 0
while True:
    produto = float(input("Qual o preço do produto ? R$ "))
    if produto == 0:
        break
    c += 1
    s += produto
print(f"Voce vai levar {c} produtos, vai custar R$ {s}")