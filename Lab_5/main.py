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
        self.final = []
        self.transitions = []

    def read_elements(self, filename):
        f = open(filename, mode='r', encoding='utf-8-sig')
        line = f.readline()
        # get states
        states_line = line.split()
        for x in states_line:
            self.states.append(x)

        # get alphabet
        line = f.readline()
        alphabet_line = line.split()
        for x in alphabet_line:
            self.alphabet.append(x)

        # get initial
        self.initial = f.readline().strip()

        # get final states
        line = f.readline()
        final_line = line.split()
        for x in final_line:
            self.final.append(x)

        # get transitions
        line = f.readline()
        while line:
            transition_elms = line.strip().split(',')
            self.transitions.append(Transitions(transition_elms[0], transition_elms[1], transition_elms[2]))
            line = f.readline()
        f.close()

    def print_menu(self):
        print("What do you want to see?\na) set of states\nb) alphabet\nc) initial state\nd) final states\ne) set of "
              "transitions\nf) test sequence\nx) exit\n")
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
            if opt == 'f':
                print(self.check_sequence(input("seq=")))
            opt = input(">")

    def check_if_dfa(self):
        list_counters = []
        for x in self.transitions:
            counter = -1
            for y in self.transitions:
                if x.first == y.first and x.value == y.value:
                    counter += 1
            list_counters.append(counter)

        ok = True
        for x in list_counters:
            if x > 0:
                ok = False

        return ok

    def check_sequence(self, sequence):
        if self.check_if_dfa():
            current = self.initial
            for one in sequence:
                ok = True
                for x in self.transitions:
                    if x.first == current and x.value == one:
                        current = x.second
                        ok = False
                        break
                if ok:
                    return False
            if current in self.final:
                return True
            else:
                return False
        else:
            return False


fa = FA()
fa.read_elements("FA.in")
# print(fa.check_sequence("001")) #true
# print(fa.check_sequence("01")) #false, doesn't exist
fa.print_menu()

