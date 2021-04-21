import Funções
from PyQt5 import QtWidgets
import uic2
# from Funções import *  -> Opção <-

while True:

    opcao = int(input('[0] Cadastrar novas roupas\n'
                      '[1] Compras\n'
                      '[2] Parar o programa\n'
                      '[3] Ver o estoque\n'
                      '[4] Adicionar peças de roupas\n'
                      '[5] Ver o histórico de remoção de roupas\n'
                      'Digite uma opção: '))

    if opcao == 0:
        # Cadastrar novas roupas

        nome = str(input('Digite um nome de roupa: '))
        cdb = str(input('Digite o código de barras: '))
        valor = float(input('Digite o preço: R$'))

        # As bermudas/shorts tem uma forma diferente de tamanhos
        op = int(input('Digite 1 se a peça é uma bermuda/shorts, se não for digite 0: '))

        if op == 0:

            q_u = int(input('Digite a quantidade para tamanhos Únicos(U): (0 Se nenhum) '))
            q_p = int(input('Digite a quantidade para tamanhos P: (0 Se nenhum) '))
            q_m = int(input('Digite a quantidade para tamanhos M: (0 Se nenhum) '))
            q_g = int(input('Digite a quantidade para tamanhos G: (0 Se nenhum) '))
            q_gg = int(input('Digite a quantidade para tamanhos GG: (0 Se nenhum) '))
            Funções.adicionarhistorico(cdb, nome,
                                       f'{q_u} Tamanhos U,{q_p} Tamanhos P, {q_m} Tamanhos M, {q_g} Tamanhos G, '
                                       f'{q_gg} Tamanhos GG', 'Novo Cadastro', 0)
            Funções.cadastrar(cdb, nome, valor, (q_u + q_p + q_m + q_g + q_gg), q_u, q_p, q_m, q_g, q_gg, op)

        else:
            q_36 = int(input('Digite a quantidade para tamanhos 36: (0 Se nenhum) '))
            q_38 = int(input('Digite a quantidade para tamanhos 38: (0 Se nenhum) '))
            q_40 = int(input('Digite a quantidade para tamanhos 40: (0 Se nenhum) '))
            q_42 = int(input('Digite a quantidade para tamanhos 42: (0 Se nenhum) '))
            q_44 = int(input('Digite a quantidade para tamanhos 44: (0 Se nenhum) '))
            q_46 = int(input('Digite a quantidade para tamanhos 46: (0 Se nenhum) '))
            Funções.adicionarhistorico(cdb, nome, f'{q_36} Tamanhos 36,{q_38} Tamanhos 38, {q_40} Tamanhos 40,'
                                                  f' {q_42} Tamanhos 42, {q_44} Tamanhos 44, {q_46} Tamanhos 46',
                                       'Novo Cadastro', 0)
            Funções.cadastrar(cdb, nome, valor, (q_36 + q_38 + q_40 + q_42 + q_44 + q_46), q_36, q_38, q_40, q_42, q_44,
                              op, q_46)

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

        # Para saber se a tal peça é Short/Bermuda
        op = Funções.pegarvalor(cdb, op=1)

        if op[0] == 0:

            while True:
                tam = str(input('Qual o tamanho que você está retirando? (U, P, M, G, GG) ')).strip().upper()

                tam2 = tam

                qt = int(input('Qual a quantidade de peças que deseja retirar? '))

                x = Funções.pegarvalor(cdb, nome=1, valor=1)

                tam = Funções.transformatam(tam)

                val = Funções.validacao_tr(cdb, tam, qt)

                # Se os dados inseridos puderem ser executados ele vai dar break
                if val:
                    break
                else:
                    print('\033[0;31m -> Os valores inseridos estão incorretos. Por favor verifique os dados'
                          ' inseridos <-\033[m')
                    Funções.verlista()

        else:
            while True:
                tam = int(input('Qual o tamanho que você está retirando? (36, 38, 40, 42, 44, 46) '))

                tam2 = tam

                qt = int(input('Qual a quantidade de peças que deseja retirar? '))

                x = Funções.pegarvalor(cdb, nome=1, valor=1)

                tam = Funções.transformatam(tam, op)

                val = Funções.validacao_tr(cdb, tam, qt)

                # Se os dados inseridos puderem ser executados ele vai dar break
                if val:
                    break
                else:
                    print('\033[0;31m -> Os valores inseridos estão incorretos. Por favor verifique os dados'
                          ' inseridos <-\033[m')
                    Funções.verlista()

        Funções.adicionarhistorico(cdb, x[0], f'{qt} Tamanhos {tam2}', 'Comprado', valor=x[1] * qt)

        q_t = Funções.pegarvalor(cdb, q_t=1)

        Funções.remocaoeadicao(cdb, tam, val-qt, q_t[0]-qt)
        print('Peça de roupa retirado com sucesso')

    elif opcao == 2:
        # Parar o programa
        break

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

        op = Funções.pegarvalor(cdb, op=1)

        if op[0] == 0:
            tam = str(input('Qual o tamanho que você está adicionando? (U, P, M, G, GG) ')).strip().upper()
        else:
            tam = int(input('Qual o tamanho que você está adicionando? (36, 38, 40, 42, 44, 46) '))

        tam2 = tam

        qt = int(input('Deseja adicionar quantas unidades? '))

        x = Funções.pegarvalor(cdb, nome=1)

        tam = Funções.transformatam(tam, op)

        #  A validação vai servir para puxar quantas roupas do tamanho x tem, para assim eu poder atualizar no banco -
        # de dadosqt
        # qt -> quantidade
        qt2 = Funções.validacao_tr(cdb, tam, op=2)

        # q_t é a quantidade total
        q_t = Funções.pegarvalor(cdb, q_t=1)

        Funções.remocaoeadicao(cdb, tam, qt+qt2, q_t[0]+qt)

        Funções.adicionarhistorico(cdb, x[0], f'{qt} Tamanhos {tam2}', 'Adicionada')

        print('Peças de roupas adicionado com sucesso')

    elif opcao == 6:
        Funções.criatabela()

    else:
        # Usuário não digitou um valor válido
        print('\033[0;31m -> Digite um valor válido <- \033[m')

print('Fim do programa')


def atualizarhistorico():
    # Lê os dados do historico e mostra na tela
    dados = Funções.verhistorico()
    pro.verhistoricotabela.setRowCount(len(dados))

    for m in range(0, len(dados)):
        for b in range(0, 6):
            pro.verhistoricotabela.setItem(m, b, QtWidgets.QTableWidgetItem(str(dados[m][b])))


def atualizarestoque():
    # Lê os dados do banco de dados e mostra no "Ver Estoque"
    dados = Funções.verlista()
    pro.verestoquetabela.setRowCount(len(dados))

    for m in range(0, len(dados)):
        for b in range(0, 16):
            pro.verestoquetabela.setItem(m, b, QtWidgets.QTableWidgetItem(str(dados[m][b])))


app = QtWidgets.QApplication([])
pro = uic2.loadUi('app.ui')

pro.atualizarestoque.clicked.connect(atualizarestoque)
pro.atualizarhistorico.clicked.connect(atualizarhistorico)


pro.show()
app.exec()
