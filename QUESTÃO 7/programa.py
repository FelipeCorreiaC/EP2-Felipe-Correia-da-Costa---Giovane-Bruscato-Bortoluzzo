from funcoes import posicao_valida, preenche_frota

frota = {}

informacoes = {
    "porta-aviões": [1, 4],
    "navio-tanque": [2, 3],
    "contratorpedeiro": [3, 2],
    "submarino": [4, 1]
}

for nome_navio in informacoes:
    quantidade = informacoes[nome_navio][0]
    tamanho = informacoes[nome_navio][1]

    for i in range(quantidade):
        valida = False

        while not valida:
            print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}")

            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if tamanho == 1:
                orientacao = "vertical"
            else:
                opcao = int(input("[1] Vertical [2] Horizontal >"))

                if opcao == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

            valida = posicao_valida(
                frota, linha, coluna, orientacao, tamanho
            )

            if not valida:
                print("Esta posição não está válida!")

        frota = preenche_frota(
            frota, nome_navio, linha, coluna, orientacao, tamanho
        )

print(frota)