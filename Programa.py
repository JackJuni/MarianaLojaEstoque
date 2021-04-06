import Funções

while True:

    opcao = int(input('[0] Cadastrar novas roupas\n'
                      '[1] Retirar peças de roupas\n'
                      '[2] Parar o programa\n'
                      '[3] Ver a lista de roupas\n'
                      'Digite uma opção: '))

    if opcao == 0:
        # Cadastrar novas roupas

        nome = str(input('Digite um nome de roupa: '))
        codigo = str(input('Digite o código de barras: '))
        preco = float(input('Digite o preço: R$'))
        q_p = int(input('Digite a quantidade para tamanhos P: (0 Se não nenhum) '))
        q_m = int(input('Digite a quantidade para tamanhos M: (0 Se não nenhum) '))
        q_g = int(input('Digite a quantidade para tamanhos G: (0 Se não nenhum) '))
        q_gg = int(input('Digite a quantidade para tamanhos GG: (0 Se não nenhum) '))

        roupa = Funções.Roupa(nome, preco, codigo, (q_p + q_m + q_g + q_gg), q_p, q_m, q_g, q_gg)
        roupa.cadastrar()
        print(f'Roupa {nome} cadastrada com sucesso!')

    elif opcao == 1:
        # Retirar peças de roupas

        # Validação de código de barras
        while True:
            # Lista de roupas
            Funções.verlista()

            codigo_de_barra = int(input('Digite o código de barras: '))
            barra_roupa = Funções.validacao_cdb(codigo_de_barra)
            if barra_roupa:
                break
            else:
                print('\033[0;31m -> Código de barras inválido. Digite um código de barras válido. <- \033[m')

        # Troca dos tamanhos para os valores em que estão ocupados na lista
        tam = str(input('Qual o tamanho que você está retirando? (P, M, G, GG) ')).strip().upper()[0]
        if tam == 'P':
            tam = 4
        elif tam == 'M':
            tam = 5
        elif tam == 'G':
            tam = 6
        elif tam == 'GG':
            tam = 7

        quant = int(input('Qual a quantidade de peças que deseja retirar? '))

    elif opcao == 2:
        # Parar o programa
        break

    elif opcao == 3:
        # Ver lista de roupas

        Funções.verlista()

    else:
        # Usuário não digitou um valor válido
        print('\033[0;31m -> Digite um valor válido <- \033[m')

print('Fim do programa')
