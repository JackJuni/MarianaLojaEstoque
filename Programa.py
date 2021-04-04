
while True:

    opcao = int(input('[0] Cadastrar novas roupas\n'
                      '[1] Retirar peças de roupas\n'
                      '[2] Parar o programa\n'
                      '[3] Ver roupas\n'
                      'Digite uma opção: '))

    if opcao == 0:
        # Cadastrar novas roupas
        from Funções import Roupa

        nome = str(input('Digite um nome de roupa: '))
        codigo = str(input('Digite o código de barras: '))
        preco = float(input('Digite o preço: R$'))
        quantidade = int(input('Digite a quantidade: '))

        roupa = Roupa(nome, preco, codigo, quantidade)
        roupa.cadastrar()
        print(f'Roupa {nome} cadastrada com sucesso!')

    elif opcao == 1:
        barra_roupa = int(input('Qual o código de barras da roupa você gostaria de retirar? '))
        quant = int(input('Qual a quantidade? '))

    elif opcao == 2:
        break

    elif opcao == 3:
        from Funções import verlista
        verlista()

print('Fim do programa')
