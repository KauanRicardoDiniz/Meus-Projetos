# Desenvolva um programa que simule a tela de bloqueio de um aplicativo bancário. O sistema possui uma senha correta pré-definida (por exemplo, 123456). O usuário deve tentar acessar o sistema digitando sua senha. Se erra 3 vezes diz que a senha foi bloqueada.
senha = int(input("Digite a senha: "))
count = 0
while senha != 123456:
    senha = int(input("Digite a senha: "))
    count += 1
    if count == 2 and senha != 123456:
        print("Aplicativo bloqueado temporariamente. Tente novamente mais tarde.")
        break
if senha == 123456:
    print("Seja bem vindo!")
