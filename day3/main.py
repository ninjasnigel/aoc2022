import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Might make good later but today we went a bit speedy

def sol1():
    liststore = []
    value = 0
    with open('data.txt') as f:
        for line in f.readlines():
            li = list(line.strip('\n'))
            liststore += [li]
            mid = len(li)//2
            first = li[:mid]
            second = li[mid:]
            common = list(set(first).intersection(second))
            for letter in common:
                value += (letters.index(letter)+1)
    newvalue = 0

    for i in range(0,len(liststore),3):
        common = list(set(liststore[i]) & set(liststore[i+1]) & set(liststore[i+2]))
        for letter in common:
            newvalue += (letters.index(letter)+1)

    print(value)
    print(newvalue)
