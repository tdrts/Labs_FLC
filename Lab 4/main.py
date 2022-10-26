import re

class SymTable:
    def __init__(self):
        self.__dimension = 101
        self.__table = [[] for _ in range(101)]

    def find_hash(self, value):
        sum_ = 0
        for c in value:
            sum_ += ord(c)
        return sum_ % self.__dimension

    def find_pos_in_chain(self, value):
        hash_position = self.find_hash(value)

        return self.__table[hash_position].index(value)

    def add(self, variable):
        hash_position = self.find_hash(variable)

        if variable not in self.__table[hash_position]:
            self.__table[hash_position].append(variable)

    def remove(self, variable):
        hash_position = self.find_hash(variable)
        if variable in self.__table[hash_position]:
            self.__table[hash_position].remove(variable)

    def display_sym_table(self):
        for i in range(self.__dimension):
            for j in self.__table[i]:
                print(j)


def read_tokens():
    f = open("token.in", mode='r', encoding='utf-8-sig')
    line = f.readline()
    tokens = []

    while line:
        tokens.append(line.split()[0])
        line = f.readline()

    return tokens


def scan_p1(tokens):
    f = open("p1.txt", mode='r', encoding='utf-8-sig')
    line = f.readline()

    pif = []
    sti = SymTable()
    stc = SymTable()

    s = ""
    for x in tokens:
        s = s + x + ' '

    s = s + '\n'
    print(s)
    for i in re.split(s,line):
        print(i)



    while line:



        for x in line.split():
            if x in tokens:
                pif.append([x,-1])
            else:
                if x.isnumeric():
                    stc.add(x)
                    #function to find code in pif
                    pif.append([x, stc.find_pos_in_chain(x)])
                else:
                    sti.add(x)
                    pif.append([x, sti.find_pos_in_chain(x)])
                    #print(x)

        line = f.readline()

    write_in_file(pif, "PIF.out")
    return tokens


def write_in_file(data, file_name):
    f = open(file_name, "w")
    for tpl in data:
        to_write = tpl[0] + "\t" + str(tpl[1]) + "\n"
        f.write(to_write)
    f.close()


def main():
    tokens = read_tokens()
    scan_p1(tokens)


main()