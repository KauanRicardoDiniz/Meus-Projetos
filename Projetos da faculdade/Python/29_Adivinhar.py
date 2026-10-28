from random import randint
from time import sleep
comp = randint(0, 10)
count = 0
print("-=-" * 20)
print("Vou pensar em um numero entre 0 e 10. tente adivinhar...")
print("-=-" * 20)
num = int(input("Digite um número de 0 a 10: "))
while num < 0 or num > 10:
    print("Número inválido! Digite de 0 a 10.")
    num = int(input("Digite um número de 0 a 10: "))
print("Processando...")
sleep(2)
while True:
    if num == comp:
        break
    count += 1
    if num < comp:
        print("Mais... Tente outra vez")
    else:
        print("Menos... Tente outra vez")  
    num = int(input("Digite um número de 0 a 10: "))
    while num < 0 or num > 10:
        print("Número inválido! Digite de 0 a 10.")
        num = int(input("Digite um número de 0 a 10: "))
    print("Processando...")
    sleep(2)
count += 1
print(f"Você adivinhou! Foram {count} tentativas.")