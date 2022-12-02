def sol1():
    current, elves = 0, []
    with open('data.txt') as f:
        for line in f.readlines():
            if line.strip() == '':
                elves += [current]
                current = 0
                continue
            current += int(line.strip())
    sorted_elves = sorted(elves, reverse=True)
    print('Sol1: ', sorted_elves[0])
    print('Sol2: ', sum(sorted_elves[:3]))
