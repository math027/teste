# teste
teste

tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
jogador_atual = 'X'

def exibir_tabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

def realizar_jogada(linha, coluna):
    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador_atual
        exibir_tabuleiro()
        verificar_vitoria()
        trocar_jogador()
    else:
        print("Essa posição já está ocupada. Escolha outra.")

def verificar_vitoria():
    # Lógica para verificar se algum jogador venceu o jogo
    # Implemente sua própria lógica de verificação de vitória aqui

def trocar_jogador():
    global jogador_atual
    jogador_atual = 'O' if jogador_atual == 'X' else 'X'

exibir_tabuleiro()

while True:
    print("Jogador", jogador_atual)
    linha = int(input("Digite o número da linha (0-2): "))
    coluna = int(input("Digite o número da coluna (0-2): "))
    realizar_jogada(linha, coluna)
