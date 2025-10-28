adm = [['ericafonso@gmail.com', 'eric12345', 102030405060]]
usuarios = []
pet = []
produtos = [['SHAMPOO', 12.00, 50], ['PERFUME', 25.00, 100], ['RAÇÃO PEDIGREE', 40.00, 75]]
servicos = []

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
        while tipo != 'adm' and tipo != 'usuario':
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
                dono_nome = input('Digite o seu nome ou o nome do tutor do pet: ')
                pet.append([nome_pet, idade_pet, tipo_animal, {dono_nome}])
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
        while True:
            confirm1 = input('Digite o seu e-mail de cadastro: ')
            confirm2 = int(input('Digite o seu ID de verificação: '))
            acesso = False
            for info in adm:
                if info[0] == confirm1 and info[2] == confirm2:
                    acesso = True
                    break

            if acesso:
                print('Acesso para o gerenciamento de produtos realizado com sucesso!')
                break
            else:
                print('E-mail ou ID de verificação incorretos.')

        opcao = 9999999
        while opcao != 0:
            print('------------MENU DE OPERAÇÕES-----------------')
            print('1. Cadastrar novo serviço/produto')
            print('2. Buscar serviços/produtos')
            print('3. Atualizar serviços/produtos')
            print('4. Remover serviços/produtos.')

            opcao = int(input('Digite a opção desejada: '))

            if opcao == 1:
                escolha = int(input('Deseja cadastrar produto[1] ou serviço[2]: '))
                while escolha != 1 and escolha != 2:
                    print('Opção inválida.')
                    escolha = int(input('Deseja cadastrar produto[1] ou serviço[2]: '))

                if escolha == 1:
                    item = input('Digite o nome do produto que deseja cadastrar: ').upper()
                    valor = float(input('Digite o valor do produto cadastrado: '))
                    while valor < 0:
                        print('Valor inválido. Digite um valor maior que 0.')
                        valor = float(input('Digite o valor do produto cadastrado: '))
                    quantidade = int(input('Digite a quantidade de produtos em estoque: '))
                    produtos.append([item, valor, quantidade])

                elif escolha == 2:
                    procedimento = input('Digite o serviço que deseja cadastrar: ').upper()
                    valor = float(input('Digite o valor do serviço cadastrado: '))
                    while valor < 0:
                        print('Valor inválido. Digite um valor maior que 0.')
                        valor = float(input('Digite o valor do serviço cadastrado: '))

                    horarios = int(input('Digite quantos horarios disponíveis: '))
                    horario = []
                    disponibilidade = []
                    for i in range(horarios):
                        hora = int(input('Digite as horas cadastras: '))
                        reserva = int(input('Esse horário está disponivel[1] ou reservado[2]: '))
                        while reserva != 1 and reserva != 2:
                            print('Opçaõ inválida.')
                            reserva = int(input('Esse horário está disponivel[1] ou reservado[2]: '))
                        if reserva == 1:
                            situacao = 'disponível'

                        elif reserva == 2:
                            situacao = 'reservado'
                        
                        disponibilidade.append(situacao)
                        horario.append(hora)                    

                    servicos.append([procedimento, valor, horario, disponibilidade])
            
            elif opcao == 2:
                escolha = int(input('Deseja buscar produto[1] ou serviço[2]: '))
                while escolha != 1 and escolha != 2:
                    print('opção inválida.')
                    escolha = int(input('Deseja buscar produto[1] ou serviço[2]: '))

                if escolha == 1:
                    busca = input('Digite qual produto deseja buscar:').upper()
                    for produto in produtos:
                        if busca in produto[0]:
                            print(produto[0])
                            print(f'Valor: {produto[1]}$ reais')
                            print('Quantiade', produto[2])
                                
   
                elif escolha == 2:
                    busca = input('Digite o serviço que deseja buscar: ').upper()
                    for servico in servicos:
                        if busca in servico:
                            print(servico[0])
                            print(f'Valor: {servico[1]}')
                            for horas in horario: 
                                print('Horários:', servico[2][0],':00 horas', end=' ')
                                print(servico[3])

            
            
            
               

