import sqlite3


def cadastrar(cdb, nome, valor, q_t, q_1, q_2, q_3, q_4, q_5, op, q_6=0):
    """ Função para cadastrar roupas no banco de dados
    :param cdb: Código de barras
    :param nome: Nome da peça de roupa
    :param valor: Valor da roupa em R$
    :param q_t: Quantidade total de tamanhos
    :param q_1: Tamanhos únicos // Tamanhos 36
    :param q_2: Tamanhos P // Tamanhos 38
    :param q_3: Tamanhos M // Tamanhos 40
    :param q_4: Tamanhos G // Tamanhos 42
    :param q_5: Tamanhos GG // Tamanhos 44
    :param q_6: Tamanhos 46
    :param op: Opção se ele é bermuda/shorts ou peça de roupa normal. 1 Bermudas/Shorts, 0 Peças normais
    """

    con = sqlite3.connect("dados.db")
    c = con.cursor()

    if op == 0:
        c.execute("INSERT INTO produtos VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (cdb, nome, valor, q_t, q_1, q_2, q_3, q_4, q_5, 0, 0, 0, 0, 0, 0, op))
    else:
        c.execute("INSERT INTO produtos VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (cdb, nome, valor, q_t, 0, 0, 0, 0, 0, q_1, q_2, q_3, q_4, q_5, q_6, op))

    con.commit()
    con.close()


def remocaoeadicao(cdb, op, q_t, q_1, q_2, q_3, q_4, q_5, q_6, descricao, valor):
    """ Função para remover peças de roupa
    :param cdb: Código de barras
    :param q_t: Quantidade total
    :param op: Tipo de tamanho de roupa, 1 para tamanhos de bermudas
    :param q_1: Referente aos tamanhos U ou 36
    :param q_2: Referente aos tamanhos P ou 38
    :param q_3: Referente aos tamanhos M ou 40
    :param q_4: Referente aos tamanhos G ou 42
    :param q_5: Referente aos tamanhos GG ou 44
    :param q_6: Referente ao tamanho 46
    :param descricao: O nome/descrição do produto
    :param valor: Preço do produto
    """

    con = sqlite3.connect("dados.db")
    c = con.cursor()

    # if op == 4:
    # c.execute("UPDATE produtos SET q_u = ?, q_t = ? WHERE cdb = ?",
    # (qt, q_t, cdb))

    if op == 1:
        c.execute("UPDATE produtos SET q_t = ?, q_36 = ?, q_38 = ?, q_40 = ?, q_42 = ?, q_44 = ?, q_46 = ?, nome = ?,"
                  " valor = ? WHERE cdb = ?",
                  (q_t, q_1, q_2, q_3, q_4, q_5, q_6, descricao, valor, cdb))
    else:
        c.execute("UPDATE produtos SET nome = ?, valor = ?, q_t = ?, q_u = ?, q_p = ?, q_m = ?, q_g = ?, q_gg = ?"
                  " WHERE cdb = ?", (descricao, valor, q_t, q_1, q_2, q_3, q_4, q_5, cdb))

    con.commit()
    con.close()


def verlista():
    """ Função para ver a lista de produtos
    """
    con = sqlite3.connect("dados.db")
    c = con.cursor()

    # print('-'*144)
    # print(f'|{"Código de barra":^17}|{"Nome da roupa":^20}|{"Valor":^7}|{"Quantidade Total":^18}|{"T U":^5}|'
    #       f'{"T P":^5}|{"T M":^5}|{"T G":^5}|{"T GG":^6}|{"Op":^3}|{"T 36":^6}|{"T 38":^6}|{"T 40":^6}|{"T 42":^6}|'
    #       f'{"T 44":^6}|{"T 46":^6}|')
    # print('-'*144)
    # for lista in c.execute('SELECT * FROM produtos'):
    #     print(f'|{lista[0]:^17}|{lista[1]:^20}|{lista[2]:^7.2f}|{lista[3]:^18}|{lista[4]:^5}|{lista[5]:^5}|'
    #           f'{lista[6]:^5}|{lista[7]:^5}|{lista[8]:^6}|{lista[15]:^3}|{lista[9]:^6}|{lista[10]:^6}|{lista[11]:^6}|'
    #           f'{lista[12]:^6}|{lista[13]:^6}|{lista[14]:^6}|')
    # print('-'*144)

    c.execute("SELECT * FROM PRODUTOS")
    dados = c.fetchall()

    con.close()
    return dados


def verhistorico():
    """ Função para ver o histórico
    """
    con = sqlite3.connect('dados.db')
    c = con.cursor()

    # print('-'*154)
    #
    # print(f'|{"Data":^17}|{"Código de barra":^15}|{"Nome da roupa":^20}|{"Valor total":^11}'
    #       f'|{"Tamanhos":^87}|{"Situação":^13}')
    #
    # print('-'*154)
    # for linha in c.execute('SELECT * FROM historico'):
    #     print(f'|{linha[0]:^17}|{linha[1]:^15}|{linha[2]:^20}|{linha[3]:^11}|{linha[4]:^87}|{linha[5]:^13}')
    #
    # print('-'*154)
    c.execute("SELECT * FROM historico")
    dados = c.fetchall()

    con.close()
    return dados


def validacao_cdb(cdb):
    """ Função para Validação de código de barras e de quantidade
    :param cdb: Código de barras
    :return: Se achar o código de barras o valor retornado vai ser True
    Se não, o valor retornado vai ser False"""

    con = sqlite3.connect("dados.db")
    c = con.cursor()

    for linha in c.execute("SELECT * FROM produtos"):
        if cdb == linha[0]:
            con.close()
            return True
    con.close()
    return False


def validacao_tr(cdb, tam, qp=1, op=1):
    """ Validação da função: tirar roupa. Tem o próposito de validação da quantiade de roupas do tamanho x
    :param tam: Tamanho da roupa
    :param qp: Quantidade de roupas a ser retirado. Como foi adicionado a "op" coloquei o qp também como =1
    :param cdb: Código de barras
    :param op: Apenas uma forma que achei para incluir a função na funcionalidade: adicionar quantidade de roupa
    :return: Return True se possuir, False se não possuir.
    """

    con = sqlite3.connect("dados.db")
    c = con.cursor()

    for linha in c.execute("SELECT * FROM produtos"):
        if cdb == linha[0]:
            if op == 2:
                con.close()
                return linha[tam]
            if qp <= linha[tam]:
                con.close()
                return True and linha[tam]
    con.close()
    return False


def pegarvalor(cd, nome=0, valor=0, q_t=0, q_1=0, q_2=0, q_3=0, q_4=0, q_5=0, q_6=0, op=0, todos=0):
    """ Função para pegar um valor x. Para pegar um valor desejado é só especificar
    :param cd: Código de barras
    :param nome: Nome da roupa
    :param valor: Valor da roupa
    :param q_t: Quantidade total
    :param q_1: Quantidade de Tamanhos único / Tamanhos 36
    :param q_2: Quantidade de Tamanhos P / Tamanhos 38
    :param q_3: Quantidade de Tamanhos M / Tamanhos 40
    :param q_4: Quantidade de Tamanhos G / Tamanhos 42
    :param q_5: Quantidade de Tamanhos GG / Tamanhos 44
    :param q_6: Quantidade de Tamanhos 46
    :param op: Para diferenciar de shorts/bermudas. 1 Short/bermudas, 0 Peças de roupas normais
    :param todos: Para pegar todos os dados
    :return:  Os valores desejados em uma lista. Para pegar o valor no return é só dá um: lista[0]
    """

    con = sqlite3.connect("dados.db")
    c = con.cursor()

    dados = []

    if todos == 1:
        # nome = valor = q_t = q_1 = q_2 = q_3 = q_4 = q_5 = q_6 = op = 1
        for linha in c.execute("SELECT * FROM produtos"):
            if cd == linha[0]:
                dados.append(linha[1])
                dados.append(linha[2])
                dados.append(linha[3])
                dados.append(linha[4])
                dados.append(linha[5])
                dados.append(linha[6])
                dados.append(linha[7])
                dados.append(linha[8])
                dados.append(linha[9])
                dados.append(linha[10])
                dados.append(linha[11])
                dados.append(linha[12])
                dados.append(linha[13])
                dados.append(linha[14])
                dados.append(linha[15])

        return dados

    else:
        for linha in c.execute("SELECT * FROM produtos"):
            if cd == linha[0]:
                if nome == 1:
                    dados.append(linha[1])
                if valor == 1:
                    dados.append(linha[2])
                if q_t == 1:
                    dados.append(linha[3])
                if linha[15] == 1:
                    # q_36
                    if q_1 == 1:
                        dados.append(linha[9])
                    # q_38
                    if q_2 == 1:
                        dados.append(linha[10])
                    # q_40
                    if q_3 == 1:
                        dados.append(linha[11])
                    # q_42
                    if q_4 == 1:
                        dados.append(linha[12])
                    # q_44
                    if q_5 == 1:
                        dados.append(linha[13])
                    # q_44
                    if q_6 == 1:
                        dados.append(linha[14])
                else:
                    # q_u
                    if q_1 == 1:
                        dados.append(linha[4])
                    # q_p
                    if q_2 == 1:
                        dados.append(linha[5])
                    # q_m
                    if q_3 == 1:
                        dados.append(linha[6])
                    # q_g
                    if q_4 == 1:
                        dados.append(linha[7])
                    # q_gg
                    if q_5 == 1:
                        dados.append(linha[8])
                if op == 1:
                    dados.append(linha[15])
        return dados


def criatabelaprodutos():
    con = sqlite3.connect('dados.db')
    c = con.cursor()

    c.execute("""CREATE TABLE produtos(cdb INTEGER NOT NULL PRIMARY KEY,
                                       nome TEXT NOT NULL,
                                       valor REAL NOT NULL,
                                       q_t INTEGER NOT NULL,
                                       q_u INTEGER,
                                       q_p INTEGER,
                                       q_m INTEGER,
                                       q_g INTEGER,
                                       q_gg INTEGER,
                                       q_36 INTEGER,
                                       q_38 INTEGER,
                                       q_40 INTEGER,
                                       q_42 INTEGER,
                                       q_44 INTEGER,
                                       q_46 INTEGER,
                                       op INTEGER NOT NULL)""")

    con.commit()
    c.close()


def adicionarhistorico(cdb, nome, tam, sit, valor=0):
    """ Função para adicionar ao histórico as mudanças feita no estoque
    :param cdb: Código de barras
    :param nome: Nome da peça de roupa
    :param tam: Os tamanhos retirados/adicionados
    :param sit: A situação se foi: Novo cadastro, Adicionada e Comprada
    :param valor: Valor total da roupa Retirado
    """
    from datetime import date
    import time

    # Data atual DD-MM-YY e hora HH:MM:SS para adicionar na tabela e não dar erro
    data = date.today().strftime('%d/%m/%y') + time.strftime(' %H:%M:%S')

    con = sqlite3.connect('dados.db')
    c = con.cursor()

    c.execute("INSERT INTO historico VALUES (?, ?, ?, ?, ?, ?)", (data, cdb, nome, valor, tam, sit))

    con.commit()
    con.close()


def transformatam(ob, op=0):
    """ Função para transformar os tamanhos
    :param ob: O tamanho
    :param op: 0 Tamanhos normais, 1 Tamanhos de Shorts/Bermudas
    :return: Retorna a peça de roupa com o número na respectiva posição na tabela do banco de dados
    """
    if op == 0:
        if ob == 'U':
            return 4
        elif ob == 'P':
            return 5
        elif ob == 'M':
            return 6
        elif 'G' in ob:
            if ob.count('G') == 1:
                return 7
            else:
                return 8
    else:
        if ob == 36:
            return 9
        elif ob == 38:
            return 10
        elif ob == 40:
            return 11
        elif ob == 42:
            return 12
        elif ob == 44:
            return 13
        elif ob == 46:
            return 14
