#!/usr/bin/env python3

board = {
        'a1':'wlR','b1':'wlK','c1':'wlB','d1':'wQ','e1':'wP','f1':'wrB','g1':'wrK','h1':'wrR',
        'a2':'.','b2':'.','c2':'.','d2':'.','e2':'.','f2':'.','g2':'.','h2':'.',
        'a3':'.','b3':'.','c3':'.','d3':'.','e3':'.','f3':'.','g3':'.','h3':'.',
        'a4':'.','b4':'.','c4':'.','d4':'.','e4':'.','f4':'.','g4':'.','h4':'.',
        'a5':'.','b5':'.','c5':'.','d5':'.','e5':'.','f5':'.','g5':'.','h5':'.',
        'a6':'.','b6':'.','c6':'.','d6':'.','e6':'.','f6':'.','g6':'.','h6':'.',
        'a7':'.','b7':'.','c7':'.','d7':'.','e7':'.','f7':'.','g7':'.','h7':'.',
        'a8':'blR','b8':'blK','c8':'blB','d8':'bQ','e8':'bP','f8':'brB','g8':'brK','h8':'brR'
        }

    #sample move: 

def move(move):
    piece = move.split()[0]
    place = move.split()[1]
    for places in board:
        if board[places] == piece:
            board[places] = '.'
    board[place] = piece

def color(count):
    if count % 2 == 0:
        return 'w'
    else:
        return 'b'

def boardUI():
    print('  ---------------')
    i = 1
    while i < 9:
        collumn = '| '
        j = 'a'
        while j < 'i':
            #print(j + str(i))
            if board[j + str(i)] == '.':
                collumn += '+ '

            elif board[j + str(i)][-1] == 'P':
                collumn += 'K '

            elif board[j + str(i)][-1] == 'R':
                collumn += 'R '

            elif board[j + str(i)][-1] == 'B':
                collumn += 'B '

            elif board[j + str(i)][-1] == 'K':
                collumn += 'k '

            elif board[j + str(i)][-1] == 'Q':
                collumn += 'Q '
 
            else:
                collumn += '  '
            j = chr(ord(j) + 1)
        print(collumn + '|')
        i += 1
    print('  ---------------')
counter = 0
running = True
boardUI()
while running:
    mv = input()
    if mv != 'q':
        move(mv)
        print(board)
        counter += 1
        boardUI()
    else:
        running = False
