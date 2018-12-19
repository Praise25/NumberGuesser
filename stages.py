# import maingame

a = 0
b = 0
tries = 0
diff = " "

"""
If you want to run the game it's console/terminal form, un-comment every occurrence of 'maingame(a, b, tries, diff)'
and un-comment the 'import maingame' statement

If you want to run the game in it's GUI form, comment every occurrence of 'maingame(a, b, tries, diff)'
"""


def easy():
    global a
    global b
    global tries
    global diff

    # easy difficulty. Number of tries
    a = 1
    b = 20
    tries = 7
    diff = 'Very Easy'
    # select random number
    # maingame.maingame(a, b, tries, diff)


def casual():
    global a
    global b
    global tries
    global diff

    # Casual difficulty. Number of tries
    a = 1
    b = 30
    tries = 7
    diff = 'Casual'
    # select random number
    # maingame.maingame(a, b, tries, diff)


def hard():
    global a
    global b
    global tries
    global diff

    # hard difficulty. Number of tries
    a = 1
    b = 200
    tries = 7
    diff = 'Hard'
    # select random number
    # maingame.maingame(a, b, tries, diff)


def vhard():
    global a
    global b
    global tries
    global diff

    # Very Hard difficulty. Number of tries
    a = 1
    b = 250
    tries = 9
    diff = 'Very Hard'
    # select random number
    # maingame.maingame(a, b, tries, diff)


def impossible():
    global a
    global b
    global tries
    global diff

    # Impossible difficulty. Number of tries
    a = 1
    b = 500
    tries = 10
    diff = 'Impossible'
    # select random number
    # maingame.maingame(a, b, tries, diff)
