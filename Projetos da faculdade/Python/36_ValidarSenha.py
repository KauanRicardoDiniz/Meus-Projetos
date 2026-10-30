#Desenvolva um validador de senha, indicando que a senha deve ter um caracter maísculo, um minúsculo, um número e pelos 8 caracteres.
senha = input("Crie sua senha: ").strip()
while True:
    if not any(caractere.isdigit() for caractere in senha) or not any(caractere.isupper() for caractere in senha) or not any(caractere.islower() for caractere in senha) or len(senha) < 8:
        print("A senha deve ter um caracter maiúsculo, um minúsculo, um número e pelos 8 caracteres.")
        senha = input("Crie sua senha: ").strip()
    else:
        print("Senha criada com sucesso!")
        break
