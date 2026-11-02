def posiciona_frota(frota):
    tabuleiro = []

    for i in range(10):
        tabuleiro.append([0] * 10)

    for nome_navio in frota:

        for navio in frota[nome_navio]:

            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro