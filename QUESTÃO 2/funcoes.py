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