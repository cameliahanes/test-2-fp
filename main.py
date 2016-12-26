import atexit

import sys

from src.controller.Controller import Controller


class Main():
    def __init__(self):
        self.control = Controller()
        atexit.register(self.control.save)
        self.run()

    def run(self):
        s = ["1 - add persom", "2 - simulate day", "3 - print all", "4 - vaccinate", "x - exit"]
        functioncalls = [lambda: sys.exit(), self.add_new_person, self.tick, self.list, self.vaccinate]
        while True:
            for e in s:
                print(e)
            opt = input("> ")
            if isInt(opt):
                opt = int(opt)
                if opt in range(0, 5):
                    try:
                        functioncalls[opt]()
                    except Exception as e:
                        print(e)
                    input("Press any key to continue.")
                else:
                    print("Unknown option!")

    def add_new_person(self):
        name = input("Name: ")
        self.control.addPerson(name)

    def tick(self):
        print("Day {}".format(self.control.tick()))

    def vaccinate(self):
        index = input("Index: ")
        self.control.vaccinate(int(index))

    def list(self):
        print(self.control.print_all())

def isInt(v):
    try:
        int(v)
        return True
    except ValueError:
        return False

Main().run()