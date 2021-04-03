
while True:

    opcao = int(input('[0] Cadastrar novas roupas\n'
                      '[1] Retirar peças de roupas\n'
                      '[2] Parar o programa\n'
                      '[3] Ver roupas'
                      'Digite uma opção: '))

    if opcao == 0:
        from Funções import Roupa
        nome = str(input('Digite um nome de roupa: '))
        codigo = str(input('Digite o códgio de barras: '))
        preco = float(input('Digite o preço: '))
        quantidade = int(input('Digite a quantidade: '))
        roupa = Roupa(nome, preco, codigo, quantidade)
        roupa.cadastrar()

    elif opcao == 2:
        break

print('Fim do programa')
