adm = [['ericafonso@gmail.com', 'eric12345', 102030405060]]
usuarios = []
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
    while opc < 0 and opc > 4:
        print('Digite uma opção válida')
        opc = int(input('Digite a opçâo desejada: '))

    if opc == 1:
        tipo = input('Deseja logar como usuário[1] ou administrador[2]: ')
        while tipo != '1' and tipo != '2':
            print('Opção não existente.')
            tipo = input('Deseja logar como usuário ou administrador(adm): ')

        if tipo == '1':
            login = input('Digite o seu e-mail: ')
            while '@' not in login and '.com' not in login:
                print('E-mail inválido')
                login = input('Digite o seu e-mail: ')
            
            senha = input('Digite sua senha(mínimo de 8 caracteres): ')
            while len(senha) < 8:
                print('Senha com menos de 8 caracteres.')
                senha = input('Digite sua senha(mínimo de 8 caracteres): ')
            
            usuarios.append([login, senha])
            print('Usuário cadastrado com sucesso!')

        elif tipo == '2':
            login_adm = input('Digite e-mail de cadastro: ')
            while '@' not in login_adm and '.com' not in login_adm:
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
            print('4. Remover serviços/produtos')
            print('0. Voltar a menu anterior')

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
                    print('Produto cadastrado com sucesso!')

                elif escolha == 2:
                    procedimento = input('Digite o serviço que deseja cadastrar: ').upper()
                    valor = float(input('Digite o valor do serviço cadastrado: '))
                    while valor < 0:
                        print('Valor inválido. Digite um valor maior que 0.')
                        valor = float(input('Digite o valor do serviço cadastrado: '))

                    horarios = int(input('Digite quantos horarios disponíveis: '))
                    while horarios < 0 and horarios > 24:
                        print('Quantidade de valores incoerentes.')
                        horarios = int(input('Digite quantos horarios disponíveis: '))
                    horario = []
                    for i in range(horarios):
                        hora = int(input(f'Digite a {i+1}° hora cadastrada: '))
                        while hora < 0 and hora > 24:
                            print('Horário inexistente.')
                            hora = int(input(f'Digite a {i+1}° hora cadastras(ex: 09:00): '))
                        horario.append(hora)                    

                    servicos.append([procedimento, valor, horario])
                    print('Serviço cadastrado com sucesso!')
            
            elif opcao == 2:
                escolha = int(input('Deseja buscar produto[1] ou serviço[2]: '))
                while escolha != 1 and escolha != 2:
                    print('opção inválida.')
                    escolha = int(input('Deseja buscar produto[1] ou serviço[2]: '))

                if escolha == 1:
                    if len(produtos) == 0:
                        print('Nenhum produto cadastrado')
                    else:
                        busca = input('Digite qual produto deseja buscar:').upper()
                        for produto in produtos:
                            if busca in produto[0]:
                                print(produto[0])
                                print(f'Valor: {produto[1]} reais')
                                print('Quantiade', produto[2])


                elif escolha == 2:
                    if len(servicos) == 0:
                        print('Nenhum serviço cadastrado')
                    else:
                        busca = input('Digite o serviço que deseja buscar: ').upper()
                        for servico in servicos:
                            if busca in servico:
                                print(f'Serviço: {servico[0]}  Valor: {servico[1]}$ reais')
                                print('Horários:')
                                for hora in servico[2]:
                                    print(f'{hora}:00 horas')

            elif opcao == 3:
                escolha = input('Deseja atualizar um produto[P] ou serviço[S]').upper()
                while escolha != 'P' and escolha != 'S':
                    print('Opção inválida. Digite uma opção viável.')
                    escolha = input('Deseja atualizar um produto[P] ou serviço[S]').upper()

                if escolha == 'P':
                    for i in range(len(produtos)):
                        print(f'{i+1} - Produto: {produtos[i][0]} - Valor: {produtos[i][1]} reais - Quantidade: {produtos[i][2]}')

                    produto_alvo = input('Digite o produto que deseja alterar: ').upper()
                    for p in range(len(produtos)):
                        if produtos[i][0] == produto_alvo:
                            while True:
                                escolha_mudanca = int(input('Deseja alterar o nome[1], valor[2], quantidade[3] ou sair[0]: '))
                                while escolha_mudanca != 1 and escolha_mudanca != 2 and escolha_mudanca != 3:
                                    print('Digite uma opção entre as oferecidas.')
                                    escolha_mudanca = int(input('Deseja alterar o nome[1], valor[2] ou quantidade[3]: '))
                                if escolha_mudanca == 1:
                                    novo_valor = input('Digite o novo nome que o produto irá receber: ')
                                    produtos[i][0] = novo_valor
                                    print('Alterado com sucesso')
                                
                                elif escolha_mudanca == 2:
                                    novo_valor = float(input('Diigte o novo valor para o produto designado: '))
                                    produtos[i][1] = novo_valor

                                elif escolha_mudanca == 3:
                                    novo_valor = int(input('Digite a nova quantidade do produto: '))
                                    produtos[i][2] = novo_valor
                                
                                elif escolha_mudanca == 0:
                                    break


