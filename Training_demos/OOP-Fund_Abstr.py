from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def age(self):
        pass

    @abstractmethod
    def hairColor(self):
        pass

class Music(ABC):
    @abstractmethod
    def style(self):
        pass


class Ivan(Person, Music):
    def age(self):
        print("Age 23")
    def hairColor(self):
        print("Brown")
    def style(self):
        print("Heavy Metal!!!!!!!!!!!!")

class Peter(Person, Music):
    def age(self):
        print("Age 40")
    def hairColor(self):
        print("Red")
    def style(self):
        print("House!!!!!!!!!!!!")


#person = Person()

peter = Peter()
peter.age()
peter.hairColor()
peter.style()

ivan = Ivan()
ivan.age()
ivan.hairColor()
ivan.style()
