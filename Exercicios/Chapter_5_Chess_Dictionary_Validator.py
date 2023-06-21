'''
Programa para testar aprendizagem de Dicionários
Autor: Douglas Silva
Data: 04/06/2023
'''

def isValidChessBoard(chessBoard):
    '''Função que avalia se um tabuleiro de xadrez é válido.

    Avalia se há pelo menos um rei de cada lado, se as peças realmente existem, se as casas existem e se a quantidade de peças é permitida'''
    #Função para avaliar se o tabuleiro de xadrez é valido
    minPieces = ['bking', 'wking'] #variável com as peças mínimas no tabuleiro
    qntPieces = {} #variável auxiliar para saber quantas peças de cada existem no tabuleiro
    pieces = {'white': ['wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wking'],
              'black': ['bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking']} #variável com todas as peças do jogo
    boardSpaces = {'1': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], #variável com todas as casas do jogo
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
    for rank, piece in chessBoard.items():
        if minPieces[0] not in chessBoard.values():
            print('Está faltando o rei preto')
            return False
        elif minPieces[1] not in chessBoard.values():
            print('Está faltando o rei branco')
            return False
        qntPieces.setdefault(piece,0)
        qntPieces[piece] += 1
        #valida se as casas existem
        if len(str(rank)) != 2:
            print('Não existe a casa ' + rank + ' no tabuleiro')
            return False            
        elif (str(rank)[0] not in boardSpaces.keys()):
            print('Não existe a casa ' + rank + ' no tabuleiro')
            return False
        elif (str(rank)[1] not in boardSpaces[str(rank)[0]]):
            print('Não existe a casa ' + rank + ' no tabuleiro')
            return False
    
    #valida se as peças existem e sua quantidade
    for piece, countPiece in qntPieces.items():
        if (piece not in pieces['white']) and (piece not in pieces ['black']):
            print('Erro. A peça ' + piece + ' não existe')
            return False
        #quantidade
        for typePiece, maxPieceValue in maxPieces.items():
            if piece == typePiece:
                if countPiece > maxPieceValue:
                    print('A peça ' + piece + ' tem ' + str(countPiece - maxPieceValue) + ' aparições a mais que o permitido')
                    return False    
    
    #caso não haja nada que invalide, retorna verdadeiro
    return True
    
chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
if isValidChessBoard(chessBoard):
    print('Este tabuleiro é válido')
else:
    print('Este tabuleiro é inválido')