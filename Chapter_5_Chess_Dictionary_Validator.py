'''
Programa para testar aprendizagem de Dicionários
Autor: Douglas Silva
Data: 04/06/2023
'''

def isValidChessBoard(chessBoard):
    #Função para avaliar se o tabuleiro de xadrez é valido
    minimum = ['bking', 'wking'] #variável com as peças mínimas no tabuleiro
    qntPieces = {} #variável auxiliar para saber quantas peças de cada existem no tabuleiro
    pieces = {'white': ['wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wking'],
              'black': ['bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking']} #variável com todas as peças do jogo
    spaces = {'1': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], #variável com todas as casas do jogo
              '2': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
              '3': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
              '4': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
              '5': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
              '6': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
              '7': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
              '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']}
    maxPieces = {'wpawn': 8, 'wknight': 2, 'wbishop': 2, 'wrook': 2, 'wqueen': 1, 'wking': 1, #variável com a quantidade máxima de cada peça
                 'bpawn': 8, 'bknight': 2, 'bbishop': 2, 'brook': 2, 'bqueen': 1, 'bking': 1}
    
    #valida se há dois reis no tabuleiro e cria o dicionário das peças e suas quantidades
    for position, piece in chessBoard.items():
        if minimum[0] not in chessBoard.values():
            print('Está faltando o rei preto')
            return False
        elif minimum[1] not in chessBoard.values():
            print('Está faltando o rei branco')
            return False
        qntPieces.setdefault(piece,0)
        qntPieces[piece] += 1
        #valida se as casas existem
        if len(str(position)) != 2:
            print('Não existe a casa ' + position + ' no tabuleiro')
            return False            
        elif (str(position)[0] not in spaces.keys()):
            print('Não existe a casa ' + position + ' no tabuleiro')
            return False
        elif (str(position)[1] not in spaces[str(position)[0]]):
            print('Não existe a casa ' + position + ' no tabuleiro')
            return False
    
    #valida se as peças existem e sua quantidade
    for piece2, countPiece in qntPieces.items():
        if (piece2 not in pieces['white']) and (piece2 not in pieces ['black']):
            print('Erro. A peça ' + piece2 + ' não existe')
            return False
        #quantidade
        for maxPiece, maxPieceValue in maxPieces.items():
            if piece2 == maxPiece:
                if countPiece > maxPieceValue:
                    print('A peça ' + piece2 + ' tem ' + str(countPiece - maxPieceValue) + ' aparições a mais que o permitido')
                    return False    
    
    #caso não haja nada que invalide, retorna verdadeiro
    return True
    
chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
if isValidChessBoard(chessBoard):
    print('Este tabuleiro é válido')
else:
    print('Este tabuleiro é inválido')