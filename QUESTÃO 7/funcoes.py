def define_posicoes(linha,coluna,orientacao,tamanho):
    l_posicoes=[]
    if orientacao=='vertical':
        for i in range(tamanho):
            l_posicoes.append([linha+i,coluna])
    elif orientacao=='horizontal':
        for i in range(tamanho):
            l_posicoes.append([linha,coluna+i])
    return l_posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio]=[]
    frota[nome_navio].append(posicoes)
    return frota

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna]==1:
        tabuleiro[linha][coluna]='X'
    elif tabuleiro[linha][coluna]==0:
        tabuleiro[linha][coluna]='-'
    return tabuleiro

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

def afundados(frota, tabuleiro):
    quantidade = 0

    for nome_navio in frota:
        for navio in frota[nome_navio]:
            atingidas = 0

            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]

                if tabuleiro[linha][coluna] == 'X':
                    atingidas += 1

            if atingidas == len(navio):
                quantidade += 1

    return quantidade

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in posicoes:
        linha_posicao = posicao[0]
        coluna_posicao = posicao[1]

        if linha_posicao < 0 or linha_posicao > 9:
            return False

        if coluna_posicao < 0 or coluna_posicao > 9:
            return False

    for nome_navio in frota:
        for navio in frota[nome_navio]:
            for posicao in posicoes:
                if posicao in navio:
                    return False

    return True