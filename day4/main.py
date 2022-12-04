import string

def sol():
    with open("data.txt", "r") as f:
        data = [line.strip('\n') for line in f.readlines()]
    fulloverlap = 0
    anyoverlap = 0
    for line in data:
        l = line.split(',')
        f1, f2 = int(l[0].split('-')[0]),int(l[0].split('-')[1])
        s1, s2 = int(l[1].split('-')[0]),int(l[1].split('-')[1])
        first, second = list(range(f1,f2+1)), list(range(s1,s2+1))
        common = sorted(list((set(first) & set(second))))
        if((common == first) or (common == second)):
            fulloverlap += 1
            anyoverlap += 1
        elif(common != []): anyoverlap += 1
    print(fulloverlap)
    print(anyoverlap)

if __name__ == "__main__":
    sol()
