class Roupa:

    def __init__(self, nome, preco, codigo_de_barra, quantidade):
        self.nome = nome
        self.preco = preco
        self.barra = codigo_de_barra
        self.quantidade = quantidade

    def cadastrar(self):
        import json
        with open('documentos.json', 'a') as arquivo:
            json.dump(f'{self.nome};{self.preco};{self.barra}\n', arquivo)
            print(f'Roupa {self.nome} adicionada com sucesso')
            arquivo.close()
