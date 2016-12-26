from src.repository.PeopleRepository import PeopleRepository


class Controller():
    def __init__(self, load = True):
        self.repo = PeopleRepository(load)
        self._ticks = 0

    def addPerson(self, name):
        self.repo.add_person(Person(name))

    def tick(self):
        """"
        :simulates a new day
        """
        self._ticks += 1
        cands = [person for person in self.repo.get_all() if not person.getSick() and not person.getImmunization()]
        sick = [person for person in self.repo.get_all() if person.getSick()]
        if len(sick) == 0 and len(cands) > 1:
            cands[0].makeSick()
            return self._ticks
        cands = cands[:len(sick)]
        for person in cands:
            try:
                person.makeSick()
            except Exception as e:
                pass
        for person in self.repo.get_all():
            person.tick()
        return self._ticks

    def print_all(self):
        """"
        :return a table with all data
        """
        str = ""
        str += ("-"*49) + "\n"
        str += ("|{: ^15}|{: ^15}|{: ^15}".format("Name", "Vaccination", "Status")) + "\n"
        str += ("-"*49) + "\n"
        for person in self.repo.get_all():
            str += ("|{: ^15}|{: ^15}|{: ^15}".format(person.getName(), person.getImmunization(), "{}|{}".format(person.getSick(), person.getSickDays()))) + '\n'
        str += ("-" * 49) + '\n'
        return str

    def vaccinate(self, ind):
        people = self.repo.get_all()
        if ind > len(people):
            raise ValueError("Index out of range!!!")
        people[ind].vaccinate()

    def save(self):
        self.repo.save_repository()

    def get_all(self):
        return self.repo.get_all()