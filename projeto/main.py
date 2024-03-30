from funcoes import cadastro_usuarios, validação_cadastro, tratamento_de_erro, salvar

# Salvar cada usuario dentro da lista usuarios 
usuarios = []  

# Laço de repetição para cadastrar usuarios
while True:
    # Chamada para cada informação do usuario para que o usuario preencha
    usuario = cadastro_usuarios()

    # Validar informações dadas pelo usuario
    if validação_cadastro(usuario[1], usuario[2], usuario[3]):

        # Tratamento de erro no nome é nivel de user
        if tratamento_de_erro(usuario[0], usuario[3]):  

        # Salvar os usuarios a cada repetição na lista usuarios
            usuarios.append(usuario)
            salvar(usuarios)
    # Comando de parada para quando usuario digitar "N" para sair do laço de repetição
    continuar = input('Quer continuar? (S/N)').upper()
    if continuar == 'S':    
        continue
    else:
        break


