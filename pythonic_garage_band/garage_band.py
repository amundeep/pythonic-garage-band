from abc import ABC, abstractmethod

class Band:
    """ Band Class """
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __repr__(self):
        """ Object Representation """
        return "{'name': " + self.name + ", 'members': [" + str(self.members) + "]}"

    def __str__(self):
        """ String representation """
        return f"Band({self.name}, {str(self.members)})"

    # play solos in the order they were added
    def play_solos(self):
        solos = ""
        for m in self.members:
            solos = solos + m.play_solo() + " "
        return solos.strip()

    @classmethod
    def to_list(cls):
        return cls.instances

    @staticmethod
    def create_from_data(data):
        # create from some data source
        pass

class Musician(ABC):
    """ Musician Abstract Class """
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __repr__(self):
        return "{'name': " + self.name + ", 'instrument': " + self.instrument + "}"

    def __str__(self):
        return f"Musician({self.name}, {self.instrument})"

    def get_instrument(self):
        return self.instrument

    @abstractmethod
    def play_solo(self):
        pass

""" Below are subclasses of Musician """
class Drummer(Musician):
    def __init__(self, name, solo="BADDUM TSS"):
        super().__init__(name, "Drumset")
        self.solo = solo

    def play_solo(self):
        return self.solo

class Guitarist(Musician):
    def __init__(self, name, solo="DI DI DOO DA"):
        super().__init__(name, "Guitar")
        self.solo = solo

    def play_solo(self):
        return self.solo

class Singer(Musician):
    def __init__(self, name, solo="LET IT GO"):
        super().__init__(name, "Voice")
        self.solo = solo

    def play_solo(self):
        return self.solo