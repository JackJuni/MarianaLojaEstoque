import sqlite3


class Roupa:

    def __init__(self, nome, preco, codigo_de_barra, q_t, q_p, q_m, q_g, q_gg):
        """
        :param nome: Nome da roupa
        :param preco: Preço da roupa
        :param codigo_de_barra: Código de barras
        :param q_t: Quantidade total
        :param q_p: Quantitade de Tamanhos P
        :param q_m: Quantitade de Tamanhos M
        :param q_g: Quantitade de Tamanhos G
        :param q_gg: Quantitade de Tamanhos GG
        """
        self.nome = nome
        self.preco = preco
        self.barra = codigo_de_barra
        self.q_t = q_t
        self.q_p = q_p
        self.q_m = q_m
        self.q_g = q_g
        self.q_gg = q_gg

    def cadastrar(self):
        """ Cadastra novas peças de roupas no banco de dados
        """
        con = sqlite3.connect("dados.db")
        c = con.cursor()

        c.execute("INSERT INTO produtos VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (self.barra, self.nome, self.preco, self.q_t, self.q_p, self.q_m, self.q_g, self.q_gg))

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
    """ Função para ver a lista de produtos
    """
    con = sqlite3.connect("dados.db")
    c = con.cursor()

    print('-'*71)
    print(f'|{"Código de barra":<16}|{"Nome da roupa":<20}|{"Valor":<15}|{"Quantidade":<15}|')
    print('-'*71)

    for lista in c.execute('SELECT * FROM produtos'):
        print(f'|{lista[0]:<16}|{lista[1]:<20}|{lista[2]:<15}|{lista[3]:<15}|')

    print('-'*71)

    con.close()


def temporario():
    """Função temporária"""
    con = sqlite3.connect("dados.db")
    c = con.cursor()

    c.execute("""CREATE TABLE produtos(codigo_de_barra INTEGER NOT NULL PRIMARY KEY,
                                       nome TEXT NOT NULL,
                                       valor REAL NOT NULL,
                                       quantidade_total INTEGER NOT NULL,
                                       quantidade_p INTEGER NOT NULL,
                                       quantidade_m INTEGER NOT NULL,
                                       quantidade_g INTEGER NOT NULL,
                                       quantidade_gg INTEGER NOT NULL)""")

    con.commit()
    con.close()
