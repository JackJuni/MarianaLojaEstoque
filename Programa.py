import Funções
# from Funções import *  -> Opção <-

while True:

    opcao = int(input('[0] Cadastrar novas roupas\n'
                      '[1] Retirar peças de roupas\n'
                      '[2] Parar o programa\n'
                      '[3] Ver a lista de roupas\n'
                      '[4] Adicionar peças de roupas\n'
                      '[5] Ver o histórico de remoção de roupas\n'
                      'Digite uma opção: '))

    if opcao == 0:
        # Cadastrar novas roupas

        nome = str(input('Digite um nome de roupa: '))
        cdb = str(input('Digite o código de barras: '))
        valor = float(input('Digite o preço: R$'))

        # As bermudas/shorts tem uma forma diferente de tamanhos
        op = int(input('Digite 1 se a peça é uma bermuda/shorts, se não, digite 0: '))

        if op == 0:

            q_u = int(input('Digite a quantidade para tamanhos Únicos(U): (0 Se nenhum) '))
            q_p = int(input('Digite a quantidade para tamanhos P: (0 Se nenhum) '))
            q_m = int(input('Digite a quantidade para tamanhos M: (0 Se nenhum) '))
            q_g = int(input('Digite a quantidade para tamanhos G: (0 Se nenhum) '))
            q_gg = int(input('Digite a quantidade para tamanhos GG: (0 Se nenhum) '))
            Funções.adicionarhistorico(cdb, nome,
                                       f'{q_u} Tamanhos U,{q_p} Tamanhos P, {q_m} Tamanhos M, {q_g} Tamanhos G, '
                                       f'{q_gg} Tamanhos GG', 'Novo Cadastro', valor)
            Funções.cadastrar(cdb, nome, valor, (q_u + q_p + q_m + q_g + q_gg), q_u, q_p, q_m, q_g, q_gg)

        else:
            q_36 = int(input('Digite a quantidade para tamanhos 36: (0 Se nenhum) '))
            q_38 = int(input('Digite a quantidade para tamanhos 38: (0 Se nenhum) '))
            q_40 = int(input('Digite a quantidade para tamanhos 40: (0 Se nenhum) '))
            q_42 = int(input('Digite a quantidade para tamanhos 42: (0 Se nenhum) '))
            q_44 = int(input('Digite a quantidade para tamanhos 44: (0 Se nenhum) '))
            q_46 = int(input('Digite a quantidade para tamanhos 46: (0 Se nenhum) '))

            print()

        print(f'\033[0;32mRoupa {nome} cadastrada com sucesso!\033[m')

    elif opcao == 1:
        # Retirar peças de roupas

        # Validação de código de barras
        while True:
            # Lista de roupas
            Funções.verlista()

            cdb = int(input('Digite o código de barras: '))
            barra_roupa = Funções.validacao_cdb(cdb)
            if barra_roupa:
                break
            else:
                print('\033[0;31m -> Código de barras inválido. Digite um código de barras válido. <- \033[m')

        # Troca dos tamanhos para os valores em que estão ocupados na lista para a validação
        # As variaveis de tam2 recebem a posição da lista
        # Isso faz algum sentido e eu não faço a menor ideia do pq faz sentido
        while True:
            tam = str(input('Qual o tamanho que você está retirando? (U, P, M, G, GG) ')).strip().upper()

            qt = int(input('Qual a quantidade de peças que deseja retirar? '))

            x = Funções.pegarvalor(cdb, nome=1, valor=1)

            Funções.adicionarhistorico(cdb, x[0], f'{qt} Tamanhos {tam}', 'Comprado', valor=x[1]*qt)

            if tam == 'U':
                tam = 4
            elif tam == 'P':
                tam = 5
            elif tam == 'M':
                tam = 6
            elif 'G' in tam:
                if tam.count('G') == 1:
                    tam = 7
                else:
                    tam = 8

            val = Funções.validacao_tr(cdb, tam, qt)

            # Se os dados inseridos puderem ser executados ele vai dar break
            if val:
                break
            else:
                print('\033[0;31m -> Os valores inseridos estão incorretos. Por favor verifique os dados inseridos <-'
                      '\033[m')
                Funções.verlista()

        q_t = Funções.pegarvalor(cdb, q_t=1)

        Funções.remocaoeadicao(cdb, tam, val-qt, q_t[0]-qt)
        print('Peça de roupa retirado com sucesso')

    elif opcao == 2:
        # Parar o programa
        break

    elif opcao == 3:
        # Ver lista de roupas

        Funções.verlista()

    elif opcao == 4:
        # Adicionar peças de roupas

        # Validação de código de barras (Para ver se o código de barras digitado existe)
        while True:
            Funções.verlista()
            cdb = int(input('Digite o código de barra da roupa: '))
            val = Funções.validacao_cdb(cdb)
            # Se o val for True quer dizer que já existe um código de barras desse sendo usado
            if val:
                break
            else:
                print('\033[0;31m -> Este código de barras não existe. Por favor digite um código de barras'
                      ' válido <-\033[m')

        tam = str(input('Qual o tamanho que você está adicionando? (U, P, M, G, GG) ')).strip().upper()
        qt = int(input('Deseja adicionar quantas unidades? '))

        x = Funções.pegarvalor(cdb, nome=1)

        Funções.adicionarhistorico(cdb, x[0], f'{qt} Tamanhos {tam}', 'Adicionada')

        if tam == 'U':
            tam = 4
        elif tam == 'P':
            tam = 5
        elif tam == 'M':
            tam = 6
        elif 'G' in tam:
            if tam.count('G') == 1:
                tam = 7
            else:
                tam = 8

        #  A validação vai servir para puxar quantas roupas do tamanho x tem, para assim eu poder atualizar no banco -
        # de dadosqt
        # qt -> quantidade
        qt2 = Funções.validacao_tr(cdb, tam, op=2)

        # q_t é a quantidade total
        q_t = Funções.pegarvalor(cdb, q_t=1)

        Funções.remocaoeadicao(cdb, tam, qt+qt2, q_t[0]+qt)
        print('Peças de roupas adicionado com sucesso')

    elif opcao == 5:
        # Ver o histórico de roupas
        Funções.verhistorico()

    elif opcao == 6:
        Funções.temporario()

    else:
        # Usuário não digitou um valor válido
        print('\033[0;31m -> Digite um valor válido <- \033[m')

print('Fim do programa')
