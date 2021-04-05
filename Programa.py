import sqlite3
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
        q_p = int(input('Digite a quantidade para tamanhos P: (0 Se não nenhum)'))
        q_m = int(input('Digite a quantidade para tamanhos M: (0 Se não nenhum)'))
        q_g = int(input('Digite a quantidade para tamanhos G: (0 Se não nenhum)'))
        q_gg = int(input('Digite a quantidade para tamanhos GG: (0 Se não nenhum)'))

        roupa = Funções.Roupa(nome, preco, codigo, (q_p + q_m + q_g + q_gg), q_p, q_m, q_g, q_gg)
        roupa.cadastrar()
        print(f'Roupa {nome} cadastrada com sucesso!')

    elif opcao == 1:
        # Retirar peças de roupas

        # Lista de roupas
        Funções.verlista()

        barra_roupa = int(input('Qual o código de barras da roupa você gostaria de retirar? '))
        quant = int(input('Qual a quantidade? '))

    elif opcao == 2:
        # Parar o programa
        break

    elif opcao == 3:
        # Ver lista de roupas

        Funções.verlista()

    elif opcao == 4:
        Funções.temporario()

print('Fim do programa')
