class Folder:
    def __init__(self, name, parent):
        self.name       = name
        self.parent     = parent
        self.children   = []
        self.size       = 0
        self.sol1sum    = 0

    def __repr__(self):
        return self.name +' - ' +str(self.getsize())

    def getsize(self):
        tempsize = self.size
        for child in self.getchildren():
            tempsize += child.getsize()
        return tempsize

    def sol1(self):
        for child in self.getchildren():
            self.sol1sum += child.sol1()
        if(self.getsize() <= 100000): self.sol1sum += self.getsize()
        return self.sol1sum

    def sol2(self, min):
        elgible = []
        if self.getsize() >= min:
            elgible += [self]
        for child in self.getchildren():
            if(child.getsize() >= min):
                elgible += child.sol2(min)
        return elgible

    def addchild(self, child):
        self.children.append(child)

    def getchildren(self):
        return self.children

    def getparent(self):
        return self.parent

    def increasesize(self, size):
        self.size += int(size)

    def getname(self):
        return self.name


def sol():
    with open("data.txt", "r") as f:
        data = [line.strip('\n') for line in f.readlines()]

    mainf = Folder('main', [])
    currfolder = mainf

    for line in data:
        line = line.split(' ')
        match line[0]:
            case '$':
                if(line[1] == 'ls'):
                    continue
                elif(line[2]) == '..':
                    currfolder = currfolder.getparent()
                else:
                    for child in currfolder.getchildren():
                        if(child.getname() == line[2]):
                            currfolder = child
                            continue
            case 'dir':
                currfolder.addchild(Folder(line[1], currfolder))
            case _:
                currfolder.increasesize(line[0])

    print(mainf.sol1(), ' <------ sol1')
    print(min(folder.getsize() for folder in \
        mainf.sol2(41111105 + 30000000 - 70000000)), ' <------ sol2')



if __name__ == "__main__":
    sol()
