def sol():
    with open("data.txt", "r") as f:
        data = [line.strip('\n') for line in f.readlines()][0]
    print(seqstarts(data, 4), seqstarts(data, 14)) # prob 1, prob 2

def seqstarts(list, seqlen):
    for i in range(seqlen,len(list)):
        sequence = list[(i-seqlen):i]
        if(len(sequence) == len(set(sequence))):
            return i

if __name__ == "__main__":
    sol()
