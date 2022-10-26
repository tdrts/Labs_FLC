class SymTable:
    def __init__(self):
        self.__dimension = 101
        self.__table = [[] for _ in range(101)]

    def find_hash(self, value):
        sum = 0
        for c in value:
            sum += ord(c)
        return sum % self.__dimension

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


def testSymTable(table):
    option = 0
    while option != 3:
        print("1.Add value\n2.Display symbol table\n3.Exit\n")
        option = int(input("option="))

        if option == 1:
            v = input("value=")
            table.add(v)
        elif option == 2:
            table.display_sym_table()


print("What sym table to test?\n1.Identifier\n2.Constants")
opt = int(input("option="))

if opt == 1:
    idSymTable = SymTable()
    testSymTable(idSymTable)
elif opt == 2:
    constSymTable = SymTable()
    testSymTable(constSymTable)