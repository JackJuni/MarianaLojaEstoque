import sqlite3


class Roupa:

    def __init__(self, nome, preco, codigo_de_barra, quantidade):
        self.nome = nome
        self.preco = preco
        self.barra = codigo_de_barra
        self.quantidade = quantidade

    def cadastrar(self):
        """ Cadastra Novas peças de roupas no banco de dados
        """
        con = sqlite3.connect("dados.db")
        c = con.cursor()

        c.execute("INSERT INTO produtos VALUES (?, ?, ?, ?)", (self.barra, self.nome, self.preco, self.quantidade))

        con.commit()
        con.close()


def remocao(barra, quantidade):
    """ Função para remover peças de roupa
    :param barra: Código de barras
    :param quantidade: quantidade a ser retirada
    """
    verlista()
    con = sqlite3.connect("dados.db")
    c = con.cursor()
    c.execute("UPDATE produtos SET quantidade = ? WHERE codigo_de_barra = ?", (quantidade, barra))


def verlista():
    con = sqlite3.connect("dados.db")
    c = con.cursor()

    for lista in c.execute('SELECT * FROM produtos'):
        print(lista)

    con.close()
