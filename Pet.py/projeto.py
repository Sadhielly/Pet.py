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
        tipo = input('Deseja logar como usuário ou administrador(adm): ')
        while tipo != 'adm and tipo != 'usuario':
            print('Opção não existente.')
            tipo = input('Deseja logar como usuário ou administrador(adm): ')

        if tipo == 'usuario':
            login = input('Digite o seu e-mail: ')
            while '@' not in login:
                print('E-mail inválido')
                login = input('Digite o seu e-mail: ')
            
            senha = input('Digite sua senha(mínimo de 8 caracteres): ')
            while len(senha) < 8:
                print('Senha com menos de 8 caracteres.')
                senha = input('Digite sua senha(mínimo de 8 caracteres): ')
            
            usuarios.append([login, senha])
            print('Usuário cadastrado com sucesso!')
            opc_animal = input('Deseja registrar seu pet? Digite sim ou não: ').lower()
            if opc_animal == 'sim':
                nome_pet = input('Digite o nome do seu pet: ')
                idade_pet = int(input('Digite a idade do seu pet: '))
                while idade_pet < 0 or idade_pet > 100:
                    print('Idade menor que 0 ou maior que 100 anos.')
                    idade_pet = int(input('Digite a idade do seu pet: '))
                tipo_animal = input('Qual o seu anima?(Gato, Cachorro, etc.): ')
                animal.append([nome_pet, idade_pet, tipo_animal])
                print('Seu pet foi cadastrado com sucesso!')
            else:
                continue

        elif tipo == 'adm':
            login_adm = input('Digite e-mail de cadastro: ')
            while '@' not in login_adm:
                print('E-mail inválido.')
                login_adm = input('Digite e-mail de cadastro: ')
            senha_adm = input('Digite sua senha(mínimo de 8 caracteres): ')
            while len(senha_adm) < 8:
                print('Senha com menos de 8 caracteres.')
                senha_adm = input('Digite sua senha(mínimo de 8 caracteres): ')
            id_verify_adm = int(input('Crie um ID de verifição que possua 10 ou mais números: '))
            while len(str(id_verify_adm)) < 10 or len(str(id_verify_adm)) > 10:
                print('ID de verificação não possui 10 números.')
                id_verify_adm = int(input('Crie um ID de verifição que possua 10 ou mais números: '))
            adm.append([login_adm, senha_adm, id_verify_adm])
            print('Cadastro do administrador realizada com sucesso!')
 
    elif opc == 2:
        confirm1 = input('Digite o seu e-mail de cadastro: ')
        confirm2 = int(input('Digite o seu ID de verificação: '))
        acesso = False
        for info in adm:
            if confirm1 in info and confirm2 in info:
                acesso = True
                break

        if acesso:
            print('Acesso para o gerenciamento de produtos realizado com sucesso!')
        else:
            print('E-mail ou ID de verificação incorretos.')
            continue

            
            
            
               
