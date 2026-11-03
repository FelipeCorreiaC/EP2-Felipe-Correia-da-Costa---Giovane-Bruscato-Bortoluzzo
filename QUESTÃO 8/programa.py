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

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    linhas=[]
    linhas.append('   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9')
    linhas.append('_______________________________      _______________________________')

    for linha in range(len(tabuleiro_jogador)):
        jogador_info=''
        oponente_info=''
        for coluna in range(len(tabuleiro_jogador[linha])):
            jogador_info+=f'{tabuleiro_jogador[linha][coluna]}'
            if tabuleiro_oponente[linha][coluna]=='X':
                oponente_info+='X'
            elif tabuleiro_oponente[linha][coluna]=='-':
                oponente_info+='-'
            else:
                oponente_info+='0'
            if coluna < len(tabuleiro_jogador[linha])-1:
                jogador_info+='  '
                oponente_info+='  '
        linhas.append(f'{linha}| {jogador_info}|     {linha}| {oponente_info}|')
    return linhas

frota={}
informacoes={"porta-aviões":[1, 4],"navio-tanque":[2, 3],"contratorpedeiro":[3, 2],"submarino":[4, 1]}
for nome_navio in informacoes:
    quantidade=informacoes[nome_navio][0]
    tamanho=informacoes[nome_navio][1]
    for i in range(quantidade):
        valida=False
        while not valida:
            print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}")
            linha=int(input("Linha: "))
            coluna=int(input("Coluna: "))
            if tamanho==1:
                orientacao="vertical"
            else:
                opcao=int(input("[1] Vertical [2] Horizontal >"))
                if opcao==1:
                    orientacao="vertical"
                else:
                    orientacao="horizontal"
            valida=posicao_valida(frota, linha, coluna, orientacao, tamanho)
            if not valida:
                print("Esta posição não está válida!")
        frota=preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente=posiciona_frota(frota_oponente)
tabuleiro_jogador=posiciona_frota(frota)
jogando=True

while jogando:
    linhas=monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    for linha_tabuleiro in linhas:
        print(linha_tabuleiro)
    print()
    valida=False
    while not valida:
        linha=int(input("Jogador, qual linha deseja atacar? "))
        while linha<0 or linha>9:
            print("Linha inválida!")
            linha=int(input("Jogador, qual linha deseja atacar? "))
        coluna=int(input("Jogador, qual coluna deseja atacar? "))
        while coluna<0 or coluna>9:
            print("Coluna inválida!")
            coluna=int(input("Jogador, qual coluna deseja atacar? "))
        if tabuleiro_oponente[linha][coluna]=='X' or tabuleiro_oponente[linha][coluna]=='-':
            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        else:
            valida=True
    tabuleiro_oponente=faz_jogada(tabuleiro_oponente,linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente)==10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando=False