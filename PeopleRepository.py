from collections import deque


class PeopleRepository:
    def __init__(self, load):
        self.people = deque()
        if load:
            self.load_from_file()

    def get_all(self):
        return self.people

    def add_person(self, person):
        self.people.append(person)

    def load_from_file(self):
        with open("People.txt", "r") as f:
            for person in f.read().splitlines():
                data = person.split(",")
                self.people.append(Person(id = data[0], name = data[1], \
                                          vaccination = False if data[2] == "False" else True,\
                                          sick = False if data[3] == "False" else True))

    def save_repository(self):
        """"writes repo to disk"""
        with open("People.txt", "w") as f:
            for person in self.people:
                f.write("{},{},{},{}\n".format(person.getID(), person.getName(), person.getImmunization(), person.getSick()))
