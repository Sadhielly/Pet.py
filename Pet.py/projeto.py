adm = [['ericafonso@gmail.com', 'eric12345', 102030405060]]
usuarios = [['sadhi.elly@gmail.com', 'sadhi1234'],['vitoroque@gmail.com', 'tigrevitinho123']]
produtos = [['SHAMPOO', 12.00, 50], ['PERFUME', 25.00, 100], ['RAÇÃO PEDIGREE', 40.00, 75]]
servicos = [['BANHO', 30.0, [[13, 'disponível'], [11, 'disponível']]], ['SPA', 100.0, [[15, 'disponível']]], ['AULA DE ADESTRAMENTO', 1200.0, [[19, 'disponível'], [12, 'disponível']]]]

opc = 90000
print('BEM VINDO AO PETSERTÃO - O MELHOR SERVIÇO DE ATENDIMENTO A ANIMAIS DA REGIÃO!!!!!')
while opc != 0:
    print('--------------- MENU ---------------')
    print('1. Cadastrar')
    print('2. Gerenciar petshop')
    print('3. Produtos e serviços')
    print('0. Sair')

    opc = int(input('Digite a opçâo desejada: '))
    while opc < 0 and opc > 4:
        print('Digite uma opção válida')
        opc = int(input('Digite a opçâo desejada: '))

    if opc == 1:
        tipo = input('Deseja cadastrar-se como usuário[1] ou administrador[2]: ')
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

        print('--- ÁREA DO ADMINISTRADOR ---')
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

    elif opc == 3:
        
        print('--- ÁREA DO CLIENTE ---')
        while True:
            email_cliente = input('Digite o seu e-mail de cadastro: ')
            senha_cliente = input('Digite sua senha: ')
            logado = False
            for u in usuarios:
                if u[0] == email_cliente and u[1] == senha_cliente:
                    logado = True
                    break

            if logado:
                print(f'Bem-vindo(a) ao PetSertão!')
                break
            else:
                print('E-mail ou senha incorretos.')

            carrinho = []  
            agendamentos = [] 
            escolha_cliente = 99999
            while escolha_cliente != 0:
                print('----------- MENU CLIENTE -----------')
                print('1. Comprar produto')
                print('2. Agendar serviço')
                print('3. Ver carrinho')
                print('4. Ver meus agendamentos')
                print('0. Sair da área do cliente')

                escolha_cliente = int(input('Digite a opção desejada: '))

                
                if escolha_cliente == 1:
                    while True:
                        if len(produtos) == 0:
                            print('Nenhum produto disponível no momento.')
                            break
                        else:
                            print('--- PRODUTOS DISPONÍVEIS ---')
                            for i in range(len(produtos)):
                                print(f'{i} - {produtos[i][0]} | R$ {produtos[i][1]} | Estoque: {produtos[i][2]}')

                            indice = int(input('Digite o índice do produto que deseja comprar: '))
                            while indice < 0 and indice >= len(produtos):
                                print('Índice inválido.')
                                indice = int(input('Digite o índice do produto que deseja comprar: '))

                            qtd = int(input('Quantas unidades deseja comprar? '))
                            while qtd <= 0 and qtd > produtos[indice][2]:
                                print('Quantidade inválida ou quantidade maior que o estoque disponível!')
                                qtd = int(input('Quantas unidades deseja comprar? '))

                            total = produtos[indice][1] * qtd
                            carrinho.append([produtos[indice][0], qtd, total])
                            produtos[indice][2] -= qtd
                            print(f'{qtd}x {produtos[indice][0]} adicionados ao carrinho. Total: R${total}')

                            escolha = int(input('Deseja continuar comprando? Sim[S] ou Não[N]')).upper()
                            while escolha != 'S' and escolha != 'N':
                                print('Opção inválida!. Tente novamente.')
                                escolha = int(input('Deseja continuar comprando? Sim[S] ou Não[N]')).upper()
                            if escolha == 'N':
                                break
                
                elif escolha_cliente == 2:
                    if len(servicos) == 0:
                        print('Nenhum serviço disponível no momento.')
                    else:
                        print('--- SERVIÇOS DISPONÍVEIS ---')
                        for i in range(len(servicos)):
                            print(f'{i} - {servicos[i][0]} | R$ {servicos[i][1]}')

                        indice_serv = int(input('Digite o índice do serviço que deseja agendar: '))
                        while indice_serv < 0 or indice_serv >= len(servicos):
                            print('Índice inválido.')
                            indice_serv = int(input('Digite o índice do serviço que deseja agendar: '))

                        print('Horários disponíveis:')
                        disponiveis = []
                        for i in range(len(servicos[indice_serv][2])):
                            h = servicos[indice_serv][2][i]
                            if h[1] == 'disponível':
                                    print(f'{i} - {h[0]}:00')
                                    disponiveis.append(i)

                            if not disponiveis:
                                print('Nenhum horário disponível.')
                            else:
                                indice_hora = int(input('Escolha o índice do horário desejado: '))
                                if indice_hora in disponiveis:
                                    servicos[indice_serv][2][indice_hora][1] = 'reservado'
                                    agendamentos.append([servicos[indice_serv][0], servicos[indice_serv][2][indice_hora][0]])
                                    print('Serviço agendado com sucesso!')
                                else:
                                    print('Horário inválido ou indisponível.')

                elif escolha_cliente == 3:
                    if len(carrinho) == 0:
                        print('Carrinho vazio.')
                    else:
                        print('--- ITENS NO SEU CARRINHO ---')
                        total_compra = 0
                        for item in carrinho:
                            print(f'{item[1]}x {item[0]} - Total: R${item[2]}')
                            total_compra += item[2]
                        print(f'Valor total da compra: R${total_compra}')
                        finalizar = input('Deseja finalizar a compra? Sim[S] ou Não[N]: ').upper()
                        while finalizar != 'S' and finalizar != 'N':
                            print('Opção inválida! Tente novamente.')
                            finalizar = input('Deseja finalizar a compra? [S/N]: ').upper()
                        if finalizar == 'S':
                            print('Compra finalizada com sucesso! Obrigado por comprar no PetSertão')
                            carrinho.clear()

                elif escolha_cliente == 4:
                    if len(agendamentos) == 0:
                        print('Nenhum agendamento realizado.')
                    else:
                        print('--- MEUS AGENDAMENTOS ---')
                        for a in agendamentos:
                            print(f'Serviço: {a[0]} - Horário: {a[1]}:00')


                elif escolha_cliente == 0:
                    break

                else:
                    print('Opção inválida.')

        opcao = 9999999
        while opcao != 0:
            print('----------- MENU DE OPERAÇÕES -----------')
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
                            hora = int(input(f'Digite a {i+1}° hora cadastras: '))
                            
                        situacao = 'disponível'
                        horario.append([hora, situacao])                    

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
                        busca = input('Digite qual produto deseja buscar: ').upper()
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
                                    print(f'{hora[0]}:00 horas - situação: {hora[1]}')

            elif opcao == 3:
                escolha = input('Deseja atualizar um produto[P] ou serviço[S]: ').upper()
                while escolha != 'P' and escolha != 'S':
                    print('Opção inválida. Digite uma opção viável.')
                    escolha = input('Deseja atualizar um produto[P] ou serviço[S]: ').upper()

                if escolha == 'P':
                    for i in range(len(produtos)):
                        print(f'{i+1} - Produto: {produtos[i][0]} - Valor: {produtos[i][1]} reais - Quantidade: {produtos[i][2]}')

                    produto_alvo = input('Digite o nome produto que deseja alterar: ').upper()
                    for p in range(len(produtos)):
                        if produtos[p][0] == produto_alvo:
                            while True:
                                escolha_mudanca = int(input('Deseja alterar o nome[1], valor[2], quantidade[3] ou sair[0]: '))
                                while escolha_mudanca != 1 and escolha_mudanca != 2 and escolha_mudanca != 3 and escolha_mudanca != 0:
                                    print('Digite uma opção entre as oferecidas.')
                                    escolha_mudanca = int(input('Deseja alterar o nome[1], valor[2] ou quantidade[3]: '))

                                if escolha_mudanca == 1:
                                    novo_nome = input('Digite o novo nome que o produto irá receber: ').upper()
                                    produtos[p][0] = novo_nome
                                    print('Nome alterado com sucesso')
                                
                                elif escolha_mudanca == 2:
                                    novo_valor = float(input('Digite o novo valor para o produto designado: '))
                                    produtos[p][1] = novo_valor
                                    print('Valor alterado com sucesso!')

                                elif escolha_mudanca == 3:
                                    nova_quantidade = int(input('Digite a nova quantidade do produto: '))
                                    produtos[p][2] = nova_quantidade
                                    print('Quantidade alterada com sucesso!')
                                
                                elif escolha_mudanca == 0:
                                    break
                
                elif escolha == 'S':
                    for i in range(len(servicos)):
                        print(f'{i} - Serviço: {servicos[i][0]} - Valor: {servicos[i][1]}$')
                    
                    servico_indice = int(input('Digite o indice do serviço que deseja alterar: '))
                    while True:
                        escolha_mudanca = int(input('Deseja alterar o nome[1], valor[2], horário[3] ou sair[0]:'))
                        while escolha_mudanca != 1 and escolha_mudanca != 2 and escolha_mudanca != 3 and escolha_mudanca != 0:
                            print('Digite uma opção válida.')
                            escolha_mudanca = int(input('Deseja alterar o nome[1], valor[2], horário[3], situação[4] ou sair[0]:'))
                                
                        if escolha_mudanca == 1:
                            novo_nome = input('Digite o novo nome do serviço: ').upper()
                            servicos[servico_indice][0] = novo_nome
                            print('Nome alterado com sucesso!')

                        elif escolha_mudanca == 2:
                            novo_valor = float(input('Digite o novo valor do serviço: '))
                            servicos[servico_indice][1] = novo_valor
                            print('Valor alterado com sucesso!')

                        elif escolha_mudanca == 3:
                            print('Horários:')                                
                            for h in range(len(servicos[servico_indice][2])):
                                print(f'{h} - {servicos[servico_indice][2][h][0]}:00')

                            indice = int(input('Digite o índice do horário que deseja alterar: '))
                            novo_horário = int(input('Digite o novo horário: '))
                            servicos[servico_indice][2][indice][0] = novo_horário
                            print('Horário alterado com sucesso!')
                            
                        elif escolha_mudanca == 0:
                            break

            elif opcao == 4:
                escolha = input('Deseja remover um produto[P] ou serviço[S]: ').upper()
                while escolha != 'P' and escolha != 'S':
                    print('Digite uma opção válida.')
                    escolha = input('Deseja remover um produto[P] ou serviço[S]: ').upper()

                if escolha == 'P':
                    print('Produtos presentes no estoque:')
                    for i in range(len(produtos)):
                        print(f'{i} - {produtos[i][0]}')

                    indice = int(input('Digite o índice do produto que deseja remover: '))
                    while indice < 0 and indice > len(produtos):
                        print('Opção inválida! Tente novamente.')
                        indice = int(input('Digite o índice do produto que deseja remover: '))
                    produtos.pop(indice)
                    print('Produto removido.')
                
                elif escolha == 'S':
                    print('Serviços cadastrados:')
                    for i in range(len(servicos)):
                        print(f'{i} - {servicos[i][0]}')
                    
                    indice = int(input('Digite o indice do serviço que deseja remover: '))
                    servicos.pop(indice)
                    print('Serviço removido.')


