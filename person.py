import uuid


class SickException(Exception):
    pass


class Person(object):
    def __init__(self, name, vaccination = False, sick = False, id = None):
        if id is None:
            self.id = uuid.uuid1()
        else:
            self.id = id
            self.vaccination = vaccination
            self.sick = sick
            self.name = name
            self.sickDays = 0

    def vaccinate(self):
        if self.sick is True:
            raise SickException("Person is sick, can't vaccinate!")
        self.vaccination = True

    def getSick(self):
        return self.sick

    def getImmunization(self):
        return self.vaccination

    def makeSick(self):
        if self.vaccination == False:
            self.sick = True
        else:
            raise SickException("Person is vaccinated, can't get sick!")

    def getName(self):
        return self.name

    def getID(self):
        return self.id

    def tick(self):
        if self.sick is True:
            self.sickDays += 1
            if self.sickDays > 3:
                self.sick = False
                self.sickDays = 0