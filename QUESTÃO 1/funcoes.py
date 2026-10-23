def define_posicoes(linha,coluna,orientacao,tamanho):
    l_posicoes=[]
    if orientacao=='vertical':
        for i in range(tamanho):
            l_posicoes.append([linha+i,coluna])
    elif orientacao=='horizontal':
        for i in range(tamanho):
            l_posicoes.append([linha,coluna+i])
    return l_posicoes