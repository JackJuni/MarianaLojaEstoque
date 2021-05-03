import Funções
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIntValidator
import uic2
# from Funções import *  -> Opção <-

# while True:
#
#     opcao = int(input('[0] Cadastrar novas roupas\n'
#                       '[1] Compras (Retirar peças de roupas)\n'
#                       '[2] Parar o programa\n'
#                       '[3] Ver o estoque\n'
#                       '[4] Adicionar peças de roupas\n'
#                       '[5] Ver o histórico de remoção de roupas\n'
#                       'Digite uma opção: '))
#
#     if opcao == 0:
#         # Cadastrar novas roupas
#
#         nome = str(input('Digite um nome de roupa: '))
#         cdb = str(input('Digite o código de barras: '))
#         valor = float(input('Digite o preço: R$'))
#
#         # As bermudas/shorts tem uma forma diferente de tamanhos
#         op = int(input('Digite 1 se a peça é uma bermuda/shorts, se não for digite 0: '))
#
#         if op == 0:
#
#             q_u = int(input('Digite a quantidade para tamanhos Únicos(U): (0 Se nenhum) '))
#             q_p = int(input('Digite a quantidade para tamanhos P: (0 Se nenhum) '))
#             q_m = int(input('Digite a quantidade para tamanhos M: (0 Se nenhum) '))
#             q_g = int(input('Digite a quantidade para tamanhos G: (0 Se nenhum) '))
#             q_gg = int(input('Digite a quantidade para tamanhos GG: (0 Se nenhum) '))
#             Funções.adicionarhistorico(cdb, nome,
#                                        f'{q_u} Tamanhos U,{q_p} Tamanhos P, {q_m} Tamanhos M, {q_g} Tamanhos G, '
#                                        f'{q_gg} Tamanhos GG', 'Novo Cadastro', 0)
#             Funções.cadastrar(cdb, nome, valor, (q_u + q_p + q_m + q_g + q_gg), q_u, q_p, q_m, q_g, q_gg, op)
#
#         else:
#             q_36 = int(input('Digite a quantidade para tamanhos 36: (0 Se nenhum) '))
#             q_38 = int(input('Digite a quantidade para tamanhos 38: (0 Se nenhum) '))
#             q_40 = int(input('Digite a quantidade para tamanhos 40: (0 Se nenhum) '))
#             q_42 = int(input('Digite a quantidade para tamanhos 42: (0 Se nenhum) '))
#             q_44 = int(input('Digite a quantidade para tamanhos 44: (0 Se nenhum) '))
#             q_46 = int(input('Digite a quantidade para tamanhos 46: (0 Se nenhum) '))
#             Funções.adicionarhistorico(cdb, nome, f'{q_36} Tamanhos 36,{q_38} Tamanhos 38, {q_40} Tamanhos 40,'
#                                                   f' {q_42} Tamanhos 42, {q_44} Tamanhos 44, {q_46} Tamanhos 46',
#                                        'Novo Cadastro', 0)
#             Funções.cadastrar(cdb, nome, valor, (q_36 + q_38 + q_40 + q_42 + q_44 + q_46), q_36, q_38, q_40, q_42,
#             q_44, op, q_46)
#
#         print(f'\033[0;32mRoupa {nome} cadastrada com sucesso!\033[m')
#
#     elif opcao == 1:
#         # Retirar peças de roupas
#
#         # Validação de código de barras
#         while True:
#             # Lista de roupas
#             Funções.verlista()
#
#             cdb = int(input('Digite o código de barras: '))
#             barra_roupa = Funções.validacao_cdb(cdb)
#             if barra_roupa:
#                 break
#             else:
#                 print('\033[0;31m -> Código de barras inválido. Digite um código de barras válido. <- \033[m')
#
#         # Troca dos tamanhos para os valores em que estão ocupados na lista para a validação
#         # As variaveis de tam2 recebem a posição da lista
#
#         # Para saber se a tal peça é Short/Bermuda
#         op = Funções.pegarvalor(cdb, op=1)
#
#         if op[0] == 0:
#
#             while True:
#                 tam = str(input('Qual o tamanho que você está retirando? (U, P, M, G, GG) ')).strip().upper()
#
#                 tam2 = tam
#
#                 qt = int(input('Qual a quantidade de peças que deseja retirar? '))
#
#                 x = Funções.pegarvalor(cdb, nome=1, valor=1)
#
#                 tam = Funções.transformatam(tam)
#
#                 val = Funções.validacao_tr(cdb, tam, qt)
#
#                 # Se os dados inseridos puderem ser executados ele vai dar break
#                 if val:
#                     break
#                 else:
#                     print('\033[0;31m -> Os valores inseridos estão incorretos. Por favor verifique os dados'
#                           ' inseridos <-\033[m')
#                     Funções.verlista()
#
#         else:
#             while True:
#                 tam = int(input('Qual o tamanho que você está retirando? (36, 38, 40, 42, 44, 46) '))
#
#                 tam2 = tam
#
#                 qt = int(input('Qual a quantidade de peças que deseja retirar? '))
#
#                 x = Funções.pegarvalor(cdb, nome=1, valor=1)
#
#                 tam = Funções.transformatam(tam, op)
#
#                 val = Funções.validacao_tr(cdb, tam, qt)
#
#                 # Se os dados inseridos puderem ser executados ele vai dar break
#                 if val:
#                     break
#                 else:
#                     print('\033[0;31m -> Os valores inseridos estão incorretos. Por favor verifique os dados'
#                           ' inseridos <-\033[m')
#                     Funções.verlista()
#
#         Funções.adicionarhistorico(cdb, x[0], f'{qt} Tamanhos {tam2}', 'Comprado', valor=x[1] * qt)
#
#         q_t = Funções.pegarvalor(cdb, q_t=1)
#
#         Funções.remocaoeadicao(cdb, tam, val-qt, q_t[0]-qt)
#         print('Peça de roupa retirado com sucesso')
#
#     elif opcao == 2:
#         # Parar o programa
#         break
#
#     elif opcao == 4:
#         # Adicionar peças de roupas
#
#         # Validação de código de barras (Para ver se o código de barras digitado existe)
#         while True:
#             Funções.verlista()
#             cdb = int(input('Digite o código de barra da roupa: '))
#             val = Funções.validacao_cdb(cdb)
#             # Se o val for True quer dizer que já existe um código de barras desse sendo usado
#             if val:
#                 break
#             else:
#                 print('\033[0;31m -> Este código de barras não existe. Por favor digite um código de barras'
#                       ' válido <-\033[m')
#
#         op = Funções.pegarvalor(cdb, op=1)
#
#         if op[0] == 0:
#             tam = str(input('Qual o tamanho que você está adicionando? (U, P, M, G, GG) ')).strip().upper()
#         else:
#             tam = int(input('Qual o tamanho que você está adicionando? (36, 38, 40, 42, 44, 46) '))
#
#         tam2 = tam
#
#         qt = int(input('Deseja adicionar quantas unidades? '))
#
#         x = Funções.pegarvalor(cdb, nome=1)
#
#         tam = Funções.transformatam(tam, op)
#
#         #  A validação vai servir para puxar quantas roupas do tamanho x tem, para assim eu poder atualizar no banco -
#         # de dadosqt
#         # qt -> quantidade
#         qt2 = Funções.validacao_tr(cdb, tam, op=2)
#
#         # q_t é a quantidade total
#         q_t = Funções.pegarvalor(cdb, q_t=1)
#
#         Funções.remocaoeadicao(cdb, tam, qt+qt2, q_t[0]+qt)
#
#         Funções.adicionarhistorico(cdb, x[0], f'{qt} Tamanhos {tam2}', 'Adicionada')
#
#         print('Peças de roupas adicionado com sucesso')
#
#     elif opcao == 6:
#         Funções.criatabela()
#
#     else:
#         # Usuário não digitou um valor válido
#         print('\033[0;31m -> Digite um valor válido <- \033[m')
#
# print('Fim do programa')


def editarquant():
    print('a')
#     pro.cdb.setText()


def mudoucombobox():
    op = pro.tipotamanho.currentIndex()
    # Tamanho bermuda o index é 1 e o tamanho normal é 0
    # tamanho1 -> tamanho6 label // xtamanho1 -> xtamanho6 spinbox
    if op == 0:
        pro.tamanho6.hide()
        pro.xtamanho6.hide()
        pro.tamanho1.setText('Tamanho U')
        pro.tamanho2.setText('Tamanho P')
        pro.tamanho3.setText('Tamanho M')
        pro.tamanho4.setText('Tamanho G')
        pro.tamanho5.setText('Tamanho GG')
    else:
        pro.tamanho1.setText('Tamanho 36')
        pro.tamanho2.setText('Tamanho 38')
        pro.tamanho3.setText('Tamanho 40')
        pro.tamanho4.setText('Tamanho 42')
        pro.tamanho5.setText('Tamanho 44')
        pro.tamanho6.show()
        pro.xtamanho6.show()


def pesquisar():
    cdb = int(pro.cdb_add.text())
    print('->', cdb)
    if cdb == '':
        cdb = 0000
    validacao = Funções.validacao_cdb(cdb)
    dados = 0
    if validacao:
        dados = Funções.pegarvalor(cdb, todos=1)
        dados.insert(0, cdb)

        for y in range(0, 16):
            pro.verestoquetabela_2.setItem(0, y, QtWidgets.QTableWidgetItem(str(dados[y])))

        # Limpa todos os dados passados antes
        pro.cdb.clear()
        pro.descricao.clear()
        pro.valor.clear()
        pro.tipotamanho.setCurrentIndex(0)
        mudoucombobox()

        # Inserindo os dados na janela
        pro.cdb.insert(str(dados[0]))
        # pro.cdb.readOnly(True)
        pro.descricao.insert(dados[1])
        # pro.descricao.setReadOnly()
        pro.valor.insert('R$'+str(dados[2]+0))
        # pro.valor.readOnly()
        pro.tipotamanho.setCurrentIndex(dados[15])
        # pro.valor

        # mudoucombobox()
        if dados[15] == 1:
            pro.xtamanho1.setValue(dados[9])
            pro.xtamanho2.setValue(dados[10])
            pro.xtamanho3.setValue(dados[11])
            pro.xtamanho4.setValue(dados[12])
            pro.xtamanho5.setValue(dados[13])
            pro.xtamanho6.setValue(dados[14])
        else:
            pro.xtamanho1.setValue(dados[4])
            pro.xtamanho2.setValue(dados[5])
            pro.xtamanho3.setValue(dados[6])
            pro.xtamanho4.setValue(dados[7])
            pro.xtamanho5.setValue(dados[8])


    else:
        QtWidgets.QMessageBox.about(pro, 'Dados inválidos', 'Os dados inseridos estão incorretos')
    # print(cdb)
    # print(dados)


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


def abrirestoque():
    pro.framecompras.close()
    pro.frameverhistorico.close()
    pro.frameadicionarpecas.close()
    pro.frameclientes.close()
    pro.frameverestoque.show()


def abrirhistorico():
    pro.framecompras.close()
    pro.frameadicionarpecas.close()
    pro.frameclientes.close()
    pro.frameverestoque.close()
    pro.frameverhistorico.show()


def abriradicionarpecas():
    pro.framecompras.close()
    pro.frameclientes.close()
    pro.frameverestoque.close()
    pro.frameverhistorico.close()
    pro.frameadicionarpecas.show()


def abrirclientes():
    pro.framecompras.close()
    pro.frameverestoque.close()
    pro.frameverhistorico.close()
    pro.frameadicionarpecas.close()
    pro.frameclientes.show()

def abrircompras():
    pro.frameverestoque.close()
    pro.frameverhistorico.close()
    pro.frameadicionarpecas.close()
    pro.frameclientes.close()
    pro.framecompras.show()


app = QtWidgets.QApplication([])
pro = uic2.loadUi('app.ui')

# Isso são valores padrões
pro.cdb_add.setValidator(QIntValidator())
pro.tipotamanho.currentIndexChanged.connect(mudoucombobox)
pro.tamanho6.hide()
pro.xtamanho6.hide()
# pro.comboBox.setCurrentIndex(1)

# Botões
pro.atualizarestoque.clicked.connect(atualizarestoque)
pro.atualizarhistorico.clicked.connect(atualizarhistorico)
pro.pesquisar.clicked.connect(pesquisar)
pro.editarquantidade.clicked.connect(editarquant)

# Icones
pro.pesquisar.setIcon(QtGui.QIcon('icons/dsds.png'))
pro.abahistorico.setIcon(QtGui.QIcon('icons/history.png'))
pro.abaadicionar.setIcon(QtGui.QIcon('icons/add.png'))
pro.abaestoque.setIcon(QtGui.QIcon('icons/stock.png'))
pro.abaclientes.setIcon(QtGui.QIcon('icons/user.png'))
pro.abacompras.setIcon(QtGui.QIcon('icons/cart.png'))

# Abas
pro.abaestoque.clicked.connect(abrirestoque)
pro.abahistorico.clicked.connect(abrirhistorico)
pro.abaadicionar.clicked.connect(abriradicionarpecas)
pro.abaclientes.clicked.connect(abrirclientes)
pro.abacompras.clicked.connect(abrircompras)

pro.show()
app.exec()
