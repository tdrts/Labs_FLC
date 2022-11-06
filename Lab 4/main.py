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

    def get_sym_table_data(self):
        data = []
        for i in range(self.__dimension):
            for j in self.__table[i]:
                data.append(j)

        return data


class Scanner:
    def __init__(self):
        self.id_sym_table = SymTable()
        self.const_sym_table = SymTable()
        self.pif = []
        self.separators = []
        self.operators = []
        self.res_words = []

    def classify_tokens(self):
        line_number = 0
        f = open("token.in", mode='r', encoding='utf-8-sig')
        line = f.readline()

        while line:
            line = line.replace('\n', '')
            if line_number < 9:
                self.separators.append(line)
            elif line_number < 22:
                self.operators.append(line)
            else:
                self.res_words.append(line)
            line_number += 1

            line = f.readline()

        if " " not in self.separators:
            self.separators.append(" ")

    def print_tokens(self):
        print(self.separators)
        print(self.operators)
        print(self.res_words)
        print()

    def tokenize(self, line):
        index = 0
        tokens = []
        token = ''

        line = line.replace("\t", "")
        line = line.replace("\n", "")

        while index < len(line):
            #getting operators with 1 or 2 chars
            if line[index] in self.operators:
                if token:
                    tokens.append(token)
                if index + 1 < len(line) and line[index:index + 2] in self.operators:
                    tokens.append(line[index:index + 2])
                    index += 2
                else:
                    tokens.append(line[index])
                    index += 1
                token = ''
            #getting strings
            elif line[index] == '\"':
                if token:
                    tokens.append(token)
                new_str = ""
                end = 0
                index += 1
                while index < len(line) and end == 0:
                    if line[index] == "\"":
                        end = index
                    else:
                        new_str += line[index]
                    index += 1

                if end != 0:
                    new_str = "\"" + new_str + "\""
                else:
                    new_str = "\"" + new_str

                tokens.append(new_str)
                token = ''
            #getting separators
            elif line[index] in self.separators or line == 'begin' or line == 'end':
                if token:
                    tokens.append(token)
                    token = ''
                if line == "begin":
                    tokens.append("begin")
                    index += 5
                elif line == "end":
                    tokens.append("end")
                    index += 3
                else:
                    tokens.append(line[index])
                    token = ''
                    index += 1
            else:
                token += line[index]
                index += 1

        if token:
            tokens.append(token)

        tokens = list(filter(" ".__ne__, tokens))
        return tokens

    def scan_file(self, filename):
        f = open(filename, mode='r', encoding='utf-8-sig')
        line = f.readline()
        line_number = 1
        ok = 0
        while line:
            tokens = self.tokenize(line)
            if len(tokens) > 0:
                for token in tokens:
                    if token in self.separators or token in self.operators or token in self.res_words:
                        self.pif.append([token, -1])
                    else:
                        #print(token)
                        if re.match(r"^0|[+-]?[1-9][0-9]*\.?[0-9]*$", token) or (token[0] == "\"" and token[-1] == "\""):
                            self.const_sym_table.add(token)
                            self.pif.append(["const", self.const_sym_table.find_pos_in_chain(token)])
                        elif re.search(r"^[a-zA-Z]([a-zA-Z]|[0-9])*$", token):
                            self.id_sym_table.add(token)
                            self.pif.append(["id", self.id_sym_table.find_pos_in_chain(token)])
                        else:
                            print("lexical error on line "+str(line_number) + " at token " + token)
                            ok = 1
            line_number += 1
            line = f.readline()

        if ok == 0:
            print("lexically correct")
        write_pif_in_file(self.pif)
        write_sym_table_in_file(self.const_sym_table.get_sym_table_data(), self.id_sym_table.get_sym_table_data())


def write_sym_table_in_file(consts, ids):
    f = open("sym_table_const.out", "w")
    for x in consts:
        f.write(x+"\n")
    f.close()

    g = open("sym_table_ids.out", "w")
    for x in ids:
        g.write(x+"\n")
    g.close()


def write_pif_in_file(data):
    f = open("pif.out", "w")
    for tpl in data:
        to_write = tpl[0] + "\t\t\t" + str(tpl[1]) + "\n"
        f.write(to_write)
    f.close()


def main():
    my_scanner = Scanner()
    my_scanner.classify_tokens()
    my_scanner.print_tokens()
    my_scanner.scan_file("p1.txt")


main()
