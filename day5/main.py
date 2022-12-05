import copy
stacks = []


def sol():
    with open("data.txt", "r") as f:
        data = [line.strip('\n') for line in f.readlines()]
    stacks = []

    stacks += [list('wbgzrdcv')]
    stacks += [list('vtsbcfwg')]
    stacks += [list('wnsbc')]
    stacks += [list('pcvjnmgq')]
    stacks += [list('bhdflst')]
    stacks += [list('nmwtvj')]
    stacks += [list('gtsclfp')]
    stacks += [list('zdb')]
    stacks += [list('wznm')]

    stacks2 = copy.deepcopy(stacks)
    for line in data:
        try:
            if ((line[0] == '[' or line[0] == ' ')):
                continue
        except:
            continue
        ins = list(line.split(' '))
        stack1, stack2, times = int(ins[3])-1, int(ins[5])-1, int(ins[1])
        print(stack1, stack2, times)
        for i in range(times):
            stacks[stack2].insert(0, stacks[stack1].pop(0))

        newstack = stacks2[stack1][:times]
        stacks2[stack1] = stacks2[stack1][times:]
        stacks2[stack2] = newstack + stacks2[stack2]

    for i in range(9):
        print(stacks[i][0])

    print('----------')

    for i in range(9):
        print(stacks2[i][0])

if __name__ == "__main__":
    sol()
