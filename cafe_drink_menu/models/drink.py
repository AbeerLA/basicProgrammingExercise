from abc import ABC, abstractmethod

class Drink(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self):
        pass
