# Função da questão 1 para ser utilizada na questão 6
def define_posicoes(linha,coluna,orientacao,tamanho):
    l_posicoes=[]
    if orientacao=='vertical':
        for i in range(tamanho):
            l_posicoes.append([linha+i,coluna])
    elif orientacao=='horizontal':
        for i in range(tamanho):
            l_posicoes.append([linha,coluna+i])
    return l_posicoes

# Questão 6
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