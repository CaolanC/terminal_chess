#!/usr/bin/env python3

def legalInfo(board, white):
    pieces = []
    if white:
        color = ''
    if not white:
        color = ''
        for i in board:
            if board[i][-1] == '+':
                pieces.append(i)
    elif not white:
        for i in board:
            if board[i][-1] == '-':
                pieces.append(i)
    returnee = {}
    for location in pieces:
        if board[location][0] == 'K':
            returnee['K' + location + color] = checkableK(location)

        elif board[location][0] == 'N':
            returnee['N' + location + color] = checkableN(location)

        elif board[location][0] == 'B':
            returnee['B' + location +color] = []
            for directions in checkableBQ(location):
                returnee['B' + location + color].extend(directions)

        elif board[location][0] == 'Q':
            returnee['Q' + location + color] = []
            for directions in checkableBQ(location):
                returnee['Q' + location + color].extend(directions)
            for directions in checkableRQ(location):
                returnee['Q' + location + color].extend(directions)

        elif board[location][0] == 'R':
            returnee['R' + location + color] = []
            for directions in checkableRQ(location):
                returnee['R' + location + color].extend(directions)

        elif ord(board[location][0]) in range(ord('a'), ord('i')):
            returnee[location + color] = checkableP(location)
    return [returnee]

def checkableK(to):
    l = to[0]
    n = int(to[1])
    places = []
    places.append(l + str(n + 1))
    places.append(l + str(n - 1))
    places.append(chr(ord(l) + 1) + str(n))
    places.append(chr(ord(l) - 1) + str(n))
    places.append(chr(ord(l) + 1) + str(n + 1))
    places.append(chr(ord(l) + 1) + str(n - 1))
    places.append(chr(ord(l) - 1) + str(n + 1))
    places.append(chr(ord(l) - 1) + str(n - 1))
    acplaces = []
    for i in places:
        if i[0] >= 'a' and i[0] <= 'h' and int(i[1]) >= 1 and int(i[1]) <= 8:
            acplaces.append(i)
    return acplaces

def checkableN(to):
    l = to[0]
    n = int(to[1])
    places = []
    i = 1
    for j in range(2):
        a = chr(ord(l) - (2 * i)) + str(n - 1)
        if ord(a[0]) in range(ord('a'),ord('i')) and int(a[1]) in range(1,9):
            places.append(a)
        i *= -1
    i = 1
    for j in range(2):
        a = chr(ord(l) - (2 * i)) + str(n + 1)
        if ord(a[0]) in range(ord('a'),ord('i')) and int(a[1]) in range(1,9):
            places.append(a)
        i *= -1
    i = 1
    for j in range(2):
        a = chr(ord(l) + 1) + str(n - (2 * i))
        if ord(a[0]) in range(ord('a'),ord('i')) and len(a) < 3 and int(a[1]) in range(1,9):
            places.append(a)
        i *= -1
    i = 1
    for j in range(2):
        a = chr(ord(l) - 1) + str(n - (2 * i))
        if ord(a[0]) in range(ord('a'),ord('i')) and len(a) < 3 and int(a[1]) in range(1,9):
            places.append(a)
        i *= -1

    return places

def checkableRQ(to):
    l = to[0]
    n = int(to[1])
    uplaces = []
    dplaces = []
    rplaces = []
    lplaces = []
    i = 1
    for i in range(n + 1, 9):
        uplaces.append(l + str(i))
    for i in range(1, n):
        dplaces.append(l + str(i))
    dplaces.reverse()

    for i in range(ord(l), ord('i')):
        rplaces.append(chr(i) + str(n))

    for i in range(ord('a'), ord(l)):
        lplaces.append(chr(i) + str(n))
    lplaces.reverse()
    return [uplaces, dplaces, rplaces, lplaces]

def checkableBQ(to):
    l = to[0]
    n = int(to[1])
    tr = []
    tl = []
    br = []
    bl = []
    j = 1
    for i in range(ord(l), ord('i')):
        if n + j <= 8 and chr(ord(l) + j) <= 'h':
            tr.append(chr(ord(l) + j) + str(n + j))
        j += 1

    j = 1
    for i in range(ord('a'), ord(l)):
        if n - j >= 1 and chr(ord(l) - j) >= 'a':
            tl.append(chr(ord(l) - j) + str(n - j))
        j += 1

    j = 1
    for i in range(ord(l), ord('i')):
        if n - j >= 1 and chr(ord(l) + j) <= 'h':
            br.append(chr(ord(l) + j) + str(n - j))
        j += 1

    j = 1
    for i in range(ord('a'), ord(l)):
        if n + j <= 8 and chr(ord(l) - j) >= 'a':
            bl.append(chr(ord(l) - j) + str(n + j))
        j += 1
    
    return tr, tl, br, bl

def checkableP(to):
    l =  to[0]
    n = int(to[1])
    places = {'wplaces':[],'bplaces':[]}
    if chr(ord(l) - 1) >= 'a' and n + 1 <= 8:
        places['wplaces'].append(chr(ord(l) - 1) + str(n + 1))
    if chr(ord(l) + 1) <= 'h' and n + 1 <= 8:
        places['wplaces'].append(chr(ord(l) + 1) + str(n + 1))
    if chr(ord(l)) >= 'a' and n + 1 <= 8:
        places['wplaces'].append(chr(ord(l)) + str(n + 1))
    if chr(ord(l)) <= 'h' and n + 2 <= 8:
        places['wplaces'].append(chr(ord(l)) + str(n + 2))
    if chr(ord(l) - 1) >= 'a' and n - 1 >= 1:
        places['bplaces'].append(chr(ord(l) - 1) + str(n - 1))
    if chr(ord(l) + 1) <= 'h' and n - 1 >= 1:
        places['bplaces'].append(chr(ord(l) + 1) + str(n - 1))
    return places


#print(checkableK(input()))
#print(checkableP(input()))
#print(checkableN(input()))
#print(checkableRQ(input()))
#print(checkableBQ(input()))
