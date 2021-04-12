import sqlite3


def cadastrar(cdb, nome, valor, q_t, q_u, q_p, q_m, q_g, q_gg):
    """ Função para cadastrar roupas no banco de dados
    :param cdb: Código de barras
    :param nome: Nome da peça de roupa
    :param valor: Valor da roupa em R$
    :param q_t: Quantidade total de tamanhos
    :param q_u: Tamanhos únicos
    :param q_p: Tamanhos P
    :param q_m: Tamanhos M
    :param q_g: Tamanhos G
    :param q_gg: Tamanhos GG
    :return:
    """
    con = sqlite3.connect("dados.db")
    c = con.cursor()

    c.execute("INSERT INTO produtos VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (cdb, nome, valor, q_t, q_u, q_p, q_m, q_g, q_gg, 0, 0, 0, 0, 0, 0))

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
        c.execute(f"UPDATE produtos SET q_u = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))
    elif tam == 5:
        c.execute(f"UPDATE produtos SET q_p = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))
    elif tam == 6:
        c.execute(f"UPDATE produtos SET q_m = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))
    elif tam == 7:
        c.execute(f"UPDATE produtoqts SET q_g = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))
    else:
        c.execute(f"UPDATE produtos SET q_gg = ?, q_t = ? WHERE cdb = ?",
                  (qt, q_t, cdb))

    con.commit()
    con.close()


def verlista():
    """ Função para ver a lista de produtos
    """
    con = sqlite3.connect("dados.db")
    c = con.cursor()

    print('-'*125)
    print(f'|{"Código de barra":^16}|{"Nome da roupa":^20}|{"Valor":^7}|{"Quantidade Total":^17}|{"Tamanhos U":^11}|'
          f'{"Tamanhos P":^11}|{"Tamanhos M":^11}|{"Tamanhos G":^11}|{"Tamanhos GG":^11}|')
    print('-'*125)

    for lista in c.execute('SELECT * FROM produtos'):
        print(f'|{lista[0]:^16}|{lista[1]:^20}|{lista[2]:^7.2f}|{lista[3]:^17}|{lista[4]:^11}|{lista[5]:^11}|'
              f'{lista[6]:^11}|{lista[7]:^11}|{lista[8]:^11}|')

    print('-'*125)

    con.close()


def verhistorico():
    """ Função para ver o histórico
    """
    con = sqlite3.connect('dados.db')
    c = con.cursor()
    print('-'*154)

    print(f'|{"Data":^17}|{"Código de barra":^17}|{"Nome da roupa":^20}|{"Valor total":^13}'
          f'|{"Tamanhos":^70}|{"Situação":^13}')

    print('-'*154)
    for linha in c.execute('SELECT * FROM historico'):
        print(f'|{linha[0]:^17}|{linha[1]:^17}|{linha[2]:^20}|{linha[3]:^13}|{linha[4]:^70}|{linha[5]:^13}')

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


def pegarvalor(cd, nome=0, valor=0, q_t=0, q_u=0, q_p=0, q_m=0, q_g=0, q_gg=0):
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
    :return: Os valores desejados em uma lista. Para pegar o valor no return é só dá um: lista[0]
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
    return dados


def temporario():
    con = sqlite3.connect('dados.db')
    c = con.cursor()

    c.execute('')

    con.commit()
    c.close()


def adicionarhistorico(cdb, nome, tam, sit, valor=0):
    """ Função para adicionar ao histórico as mudanças feita no estoque
    :param cdb: Código de barras
    :param nome: Nome da peça de roupa
    :param tam: Os tamanhos retirados/adicionados
    :param sit: A situação se foi: Novo cadastro, Adicionada e Comprada
    :param valor: Valor da roupa Retirado
    """
    from datetime import date
    import time

    # Data atual DD-MM-YY e hora HH:MM:SS para adicionar na tabela e não dar erro
    data = date.today().strftime('%d/%m/%y') + time.strftime(' %H:%M:%S')

    con = sqlite3.connect('dados.db')
    c = con.cursor()

    c.execute("INSERT OR IGNORE INTO historico VALUES (?, ?, ?, ?, ?, ?)", (data, cdb, nome, valor, tam, sit))

    con.commit()
    con.close()
