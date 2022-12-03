import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',  \
'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',  \
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def sol():
    sacks = []
    with open('data.txt') as f:
        for line in f.readlines():
            li = list(line.strip('\n'))
            sacks += [li]

    sol1val = 0
    for li in sacks:
        mid = len(li)//2
        first, second = li[:mid], li[mid:]
        common = list(set(first) & set(second))
        sol1val += lettersvalue(common)

    sol2val = 0
    for i in range(0,len(sacks),3):
        common = list(set(sacks[i]) & set(sacks[i+1]) & \
                                          set(sacks[i+2]))
        sol2val += lettersvalue(common)

    print('sol1', sol1val)
    print('sol2', sol2val)

def lettersvalue(common):
    return sum(((letters.index(letter)+1) for letter in common))
