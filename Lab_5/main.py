from typing import List, Union, Any


class Transitions:
    def __init__(self, first, second, value):
        self.first = first
        self.second = second
        self.value = value

    def __str__(self) -> str:
        return self.first + "," + self.second + "=" + self.value


class FA:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.initial = ""
        self.final = ""
        self.transitions = []

    def read_elements(self, filename):
        f = open(filename, mode='r', encoding='utf-8-sig')
        line = f.readline()
        #get states
        states_line = line.split()
        for x in states_line:
            self.states.append(x)

        # get alphabet
        line = f.readline()
        alphabet_line = line.split()
        for x in alphabet_line:
            self.alphabet.append(x)

        self.initial = f.readline().strip()
        self.final = f.readline().strip()

        line = f.readline()
        while line:
            transition_elems = line.strip().split(',')
            self.transitions.append(Transitions(transition_elems[0],transition_elems[1],transition_elems[2]))
            line = f.readline()

    def print_menu(self):
        print("What do you want to see?\na) set of states\nb) alphabet\nc) initial state\nd) final states\ne) set of transitions\nx) exit\n")
        opt = input(">")
        while opt != 'x':
            if opt == 'a':
                print(self.states)
            if opt == 'b':
                print(self.alphabet)
            if opt == 'c':
                print(self.initial)
            if opt == 'd':
                print(self.final)
            if opt == 'e':
                for one in self.transitions:
                    print(one)
            opt = input(">")


fa = FA()
fa.read_elements("FA.in")
fa.print_menu()


