import Funções
from datetime import date

# Data atual DD-MM-YY
data = date.today().strftime('%d/%m/%y')

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
        codigo = str(input('Digite o código de barras: '))
        preco = float(input('Digite o preço: R$'))
        q_p = int(input('Digite a quantidade para tamanhos P: (0 Se não nenhum) '))
        q_m = int(input('Digite a quantidade para tamanhos M: (0 Se não nenhum) '))
        q_g = int(input('Digite a quantidade para tamanhos G: (0 Se não nenhum) '))
        q_gg = int(input('Digite a quantidade para tamanhos GG: (0 Se não nenhum) '))

        Funções.adicionarhistorico(data, codigo, nome, f'{q_p} Tamanhos P, {q_m} Tamanhos M, {q_g} Tamanhos G,'
                                                       f'{q_gg} Tamanhos GG', 'Novo Cadastro', preco)

        roupa = Funções.Roupa(nome, preco, codigo, (q_p + q_m + q_g + q_gg), q_p, q_m, q_g, q_gg)
        roupa.cadastrar()
        print(f'\033[0;32mRoupa {nome} cadastrada com sucesso!\033[m')

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

        # Troca dos tamanhos para os valores em que estão ocupados na lista para a validação
        # As variaveis de tam2 recebem a posição da lista
        # Isso faz algum sentido e eu não faço a menor ideia do pq faz sentido
        while True:
            tam = str(input('Qual o tamanho que você está retirando? (P, M, G, GG) ')).strip().upper()

            quant = int(input('Qual a quantidade de peças que deseja retirar? '))

            x = Funções.pegarvalor(codigo_de_barra, nome=1, valor=1)

            Funções.adicionarhistorico(data, codigo_de_barra, x[0], f'{quant} Tamanhos {tam}', 'Comprado',
                                       valor=x[1]*quant)

            if tam == 'P':
                tam = 4
            elif tam == 'M':
                tam = 5
            elif 'G' in tam:
                if tam.count('G') == 1:
                    tam = 6
                else:
                    tam = 7

            val = Funções.validacao_tr(codigo_de_barra, tam, quant)

            # Se os dados inseridos puderem ser executados ele vai dar break
            if val:
                break
            else:
                print('\033[0;31m -> Os valores inseridos estão incorretos. Por favor verifique os dados inseridos <-'
                      '\033[m')
                Funções.verlista()

        q_t = Funções.pegarvalor(codigo_de_barra, q_t=1)

        Funções.remocaoeadicao(codigo_de_barra, tam, val-quant, q_t[0]-quant)
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
            codigo_de_barra = int(input('Digite o código de barra da roupa: '))
            val = Funções.validacao_cdb(codigo_de_barra)
            # Se o val for True quer dizer que já existe um código de barras desse sendo usado
            if val:
                break
            else:
                print('\033[0;31m -> Este código de barras não existe. Por favor digite um código de barras'
                      ' válido <-\033[m')

        tam = str(input('Qual o tamanho que você está adicionando? (P, M, G, GG) ')).strip().upper()
        qt1 = int(input('Deseja adicionar quantas unidades? '))
        if tam == 'P':
            tam = 4
        elif tam == 'M':
            tam = 5
        elif 'G' in tam:
            if tam.count('G') == 1:
                tam = 6
            else:
                tam = 7
        #  A validação vai servir para puxar quantas roupas do tamanho x tem, para assim eu poder atualizar no banco -
        # de dados
        # qt -> quantidade
        qt2 = Funções.validacao_tr(codigo_de_barra, tam, op=2)

        # x é a quantidade total
        q_t = Funções.pegarvalor(codigo_de_barra, q_t=1)

        Funções.remocaoeadicao(codigo_de_barra, tam, qt1+qt2, q_t[0]+qt1)
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
