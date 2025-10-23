adm = []
usuarios = []
animal = []

opc = 90000
print('BEM VINDO AO PETSERTÃO - O MELHOR SERVIÇO DE ATENDIMENTO A ANIMAIS DA REGIÃO!!!!!')
while opc != 0:
    print('----------------MENU-------------------')
    print('1. Cadastrar usuário')
    print('2. Gerenciar petshop')
    print('3. Produtos e serviços')
    print('0. Sair')

    opc = int(input('Digite a opçâo desejada: '))

    if opc == 1:
        tipo = input('Deseja logar como usuário ou administrador(adm): ').lower()
        if tipo == 'usuario':
            for i in range(1):
                dados = []
                login = input('Digite o seu e-mail: ')
                if '@' in login:
                    senha = input('Digite sua senha: ')
                    if len(senha) >= 8:
                        dados.append(login)
                        dados.append(senha)
                        print('Cadastro realizado com sucesso!')
                        animal = input('Você deseja cadastrar seu pet? Digite sim ou não: ').lower()
                        if animal == 'sim':
                            for i in range(1):
                                dados_animal = []
                                nome_animal = input('Digite o nome do seu animal: ')
                                idade_animal = input('Digite a idade do seu animal: ')
                                if idade_animal != 0:
                                    raca_animal = input('Qual a raça de seu animal: ')
                                    dados_animal.append(nome_animal)
                                    dados_animal.append(idade_animal)
                                    dados_animal.append(raca_animal)
                                    dados.append(dados_animal)
                                    print('Cadastro de seu pet realizado com sucesso!')
                                    usuarios.append(dados)
                                else:
                                    print('Idade menor que 0.')                           
                        else:
                            break
                    else:
                        print('Senha com menos de 8 caracteres.')
                else:
                    print('E-mail inválido. Escolha a opção e tente novamente.')
                    break

        elif tipo == 'adm':
            for i in range(1):
                admin = []
                login_adm = input('Digite e-mail de cadastro: ')
                if '@' in login_adm: 
                    senha_adm = input('Digite senha de login: ')
                    if len(senha_adm) >= 8:
                        id_verify_adm = input('Crie um ID de verifição que possua 10 ou mais números: ')
                        if len(id_verify_adm) >= 10:
                            admin.append(login_adm)
                            admin.append(senha_adm)
                            admin.append(id_verify_adm)
                            adm.append(admin)
                            print('Cadastro realizado com sucesso!')
                        else:
                            print('ID de verificação não possui 10 digitos.')
                    else:
                        print('Senha com menos de 8 caracteres.')
                else:
                    print('E-mail inválido.')
        else:
            print('Opção de cadastro inválida')

    elif opc == 2:
        confirm1 = input('Digite o email de cadastro: ')
        confirm2 = int(input('Digite o ID de confirmação: '))
        if confirm1 in admin and confirm2 in admin:
            print('Acessado com sucesso!')
        else:
            print('Login ou senha inválido. Tente novamente.')
            continue
