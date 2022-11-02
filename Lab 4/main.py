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

        return [hash_position, self.__table[hash_position].index(value)]

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

    tokens_string = ""
    for x in tokens:
        tokens_string = tokens_string + x + ' '

    print(tokens_string)

    while line:
        for x in line.split():
            if x in tokens:
                pif.append([x, -1])
            else:
                if x.isnumeric():
                    stc.add(x)
                    pif.append([x, stc.find_pos_in_chain(x)])
                else:
                    if re.search(r"^[^\d\W]\w*\Z", x):
                        sti.add(x)
                        pif.append([x, sti.find_pos_in_chain(x)])
                    else:
                        print(x+"\t\tNOT id")

                    first_paranthesis = x.find('(')
                    second_paranthesis = x.find(')')

                    if first_paranthesis != -1:
                        pif.append([x[first_paranthesis], -1])
                        if second_paranthesis != -1:
                            new_token = x[first_paranthesis+1:second_paranthesis]
                            if re.search(r"^[^\d\W]\w*\Z", new_token):
                                sti.add(x)
                                pif.append([x, sti.find_pos_in_chain(x)])
                            for ch in range(len(new_token)):
                                #catch operators like == <= >= !=
                                if x[ch] == '!' or x[ch] == '<' or x[ch] == '>' or x[ch] == '=':
                                    if ch+1 < len(x):
                                        if x[ch+1] == '=':
                                            new_st = ""
                                            new_st += x[ch]
                                            new_st += x[ch+1]
                                            pif.append([new_st, -1])

                            pif.append([x[second_paranthesis],-1])

        line = f.readline()

    write_in_file(pif, "PIF.out")
    print("\nSym Table Const is ")
    stc.display_sym_table()
    print("\nSym Table Id is ")
    sti.display_sym_table()
    return tokens


def write_in_file(data, file_name):
    f = open(file_name, "w")
    for tpl in data:
        to_write = tpl[0] + "\t\t\t" + str(tpl[1]) + "\n"
        f.write(to_write)
    f.close()


def main():
    tokens = read_tokens()
    scan_p1(tokens)

main()