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


def remocaoeadicao(cdb, tam, qt, q_t):
    """ Função para remover peças de roupa
    :param cdb: Código de barras
    :param q_t: Quantidade total
    :param qt: quantidade a ser retirada/adicionada
    :param tam: tamanho da roupa a ser retirada/adicionada
    """

    con = sqlite3.connect("dados.db")
    c = con.cursor()

    if tam == 4:
        c.execute("UPDATE produtos SET q_u = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))
    elif tam == 5:
        c.execute("UPDATE produtos SET q_p = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))
    elif tam == 6:
        c.execute("UPDATE produtos SET q_m = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))
    elif tam == 7:
        c.execute("UPDATE produtos SET q_g = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))
    elif tam == 8:
        c.execute("UPDATE produtos SET q_gg = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))
    elif tam == 9:
        c.execute("UPDATE produtos SET q_36 = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))
    elif tam == 10:
        c.execute("UPDATE produtos SET q_38 = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))
    elif tam == 11:
        c.execute("UPDATE produtos SET q_40 = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))
    elif tam == 12:
        c.execute("UPDATE produtos SET q_42 = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))
    elif tam == 13:
        c.execute("UPDATE produtos SET q_44 = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))
    elif tam == 14:
        c.execute("UPDATE produtos SET q_46 = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))

    con.commit()
    con.close()


def verlista():
    """ Função para ver a lista de produtos
    """
    con = sqlite3.connect("dados.db")
    c = con.cursor()

    print('-'*144)
    print(f'|{"Código de barra":^17}|{"Nome da roupa":^20}|{"Valor":^7}|{"Quantidade Total":^18}|{"T U":^5}|'
          f'{"T P":^5}|{"T M":^5}|{"T G":^5}|{"T GG":^6}|{"Op":^3}|{"T 36":^6}|{"T 38":^6}|{"T 40":^6}|{"T 42":^6}|'
          f'{"T 44":^6}|{"T 46":^6}|')
    print('-'*144)

    for lista in c.execute('SELECT * FROM produtos'):
        print(f'|{lista[0]:^17}|{lista[1]:^20}|{lista[2]:^7.2f}|{lista[3]:^18}|{lista[4]:^5}|{lista[5]:^5}|'
              f'{lista[6]:^5}|{lista[7]:^5}|{lista[8]:^6}|{lista[15]:^3}|{lista[9]:^6}|{lista[10]:^6}|{lista[11]:^6}|'
              f'{lista[12]:^6}|{lista[13]:^6}|{lista[14]:^6}|')

    print('-'*144)

    con.close()


def verhistorico():
    """ Função para ver o histórico
    """
    con = sqlite3.connect('dados.db')
    c = con.cursor()
    print('-'*154)

    print(f'|{"Data":^17}|{"Código de barra":^15}|{"Nome da roupa":^20}|{"Valor total":^11}'
          f'|{"Tamanhos":^87}|{"Situação":^13}')

    print('-'*154)
    for linha in c.execute('SELECT * FROM historico'):
        print(f'|{linha[0]:^17}|{linha[1]:^15}|{linha[2]:^20}|{linha[3]:^11}|{linha[4]:^87}|{linha[5]:^13}')

    print('-'*154)


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


def pegarvalor(cd, nome=0, valor=0, q_t=0, q_u=0, q_p=0, q_m=0, q_g=0, q_gg=0, q_36=0, q_38=0, q_40=0, q_42=0,
               q_44=0, q_46=0, op=0):
    """ Função para pegar um valor x. Para pegar um valor desejado é só especificar
    :param cd: Código de barras
    :param nome: Nome da roupa
    :param valor: Valor da roupa
    :param q_t: Quantidade total
    :param q_u: Quantidade de Tamanhos único
    :param q_p: Quantidade de Tamanhos P
    :param q_m: Quantidade de Tamanhos M
    :param q_g: Quantidade de Tamanhos G
    :param q_gg: Quantidade de Tamanhos GG
    :param q_36: Quantidade de Tamanhos 36
    :param q_38: Quantidade de Tamanhos 38
    :param q_40: Quantidade de Tamanhos 40
    :param q_42: Quantidade de Tamanhos 42
    :param q_44: Quantidade de Tamanhos 44
    :param q_46: Quantidade de Tamanhos 46
    :param op: Para diferenciar de shorts/bermudas. 1 Short/bermudas, 0 Peças de roupas normais
    :return:  Os valores desejados em uma lista. Para pegar o valor no return é só dá um: lista[0]
    """

    con = sqlite3.connect("dados.db")
    c = con.cursor()

    dados = []
    for linha in c.execute("SELECT * FROM produtos"):
        if cd == linha[0]:
            if nome == 1:
                dados.append(linha[1])
            if valor == 1:
                dados.append(linha[2])
            if q_t == 1:
                dados.append(linha[3])
            if q_u == 1:
                dados.append(linha[4])
            if q_p == 1:
                dados.append(linha[5])
            if q_m == 1:
                dados.append(linha[6])
            if q_g == 1:
                dados.append(linha[7])
            if q_gg == 1:
                dados.append(linha[8])
            if q_36 == 1:
                dados.append(linha[9])
            if q_38 == 1:
                dados.append(linha[10])
            if q_40 == 1:
                dados.append(linha[11])
            if q_42 == 1:
                dados.append(linha[12])
            if q_44 == 1:
                dados.append(linha[13])
            if q_46 == 1:
                dados.append(linha[14])
            if op == 1:
                dados.append(linha[15])
    return dados


def criatabela():
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
