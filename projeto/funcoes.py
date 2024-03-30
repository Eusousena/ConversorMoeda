import json

# Função para salvar os usuarios dentro do arquivo
def salvar(usuarios):
    with open("usuarios.json", "w+") as arquivo:
        json.dump(usuarios, arquivo, indent=2)           


# Função para cadastrar as informações do usuarios
def cadastro_usuarios():
    nome = input('digite seu nome:')
    email = input('Digite seu email:')
    senha = input('digite sua senha:')
    nivel_acesso = input('Qual o seu nivel de acesso[USER/ADMIN]:').upper()
    return nome, email, senha, nivel_acesso

# Função para validar as informações dos usuarios
def validação_cadastro(email, senha, nivel_acesso):
    if email.find('@gmail.com') == -1:
        print('Email invalido tente novamente')
        return False
    elif len(senha) < 8:
        print("Sua senha deve ter 8 caracteres ou mais!")
        return False
    elif not 'USER' in nivel_acesso and 'ADMIM' in nivel_acesso:
        print('Nivel de acesso invalido')
        return False
    return True
    
# Função para tratamento de erros
def tratamento_de_erro(nome, nivel_acesso):
    try:
        if str.isdigit(nome):
            print("")
            return print("Seu nome só deve ter LETRAS!")
            print("")
        elif str.isdigit(nivel_acesso):
            return print("Nivel de acesso só pode ser USER ou ADMIM!")
    except ValueError:
        return print("Valor invalido tente novamente.")
    return nome, nivel_acesso
                