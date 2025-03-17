
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "The car drives on the road."

class Bicycle(Vehicle):
    def move(self):
        return "The bicycle is pedaled on a bike lane."

class Boat(Vehicle):
    def move(self):
        return "The boat sails on water."

class Authenticator(ABC):
    @abstractmethod
    def login(self):
        pass

class EmailAuth(Authenticator):
    def login(self):
        return "Logging in with email and password."

class GoogleAuth(Authenticator):
    def login(self):
        return "Logging in with Google account."

class FingerprintAuth(Authenticator):
    def login(self):
        return "Logging in using fingerprint authentication."

vehicles = [Car(), Bicycle(), Boat()]
for v in vehicles:
    print(v.move())

print("-" * 40)

auth_methods = [EmailAuth(), GoogleAuth(), FingerprintAuth()]
for auth in auth_methods:
    print(auth.login())
