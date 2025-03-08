# Base class for all vehicles
class Vehicle:
    def __init__(self, brand, model, rental_rate):
        self.brand = brand
        self.model = model
        self.rental_rate = rental_rate  # Cost per day

    def calculate_rental(self, days):
        """Calculates the rental cost for a given number of days."""
        return self.rental_rate * days

# Car class inherits from Vehicle
class Car(Vehicle):
    def open_trunk(self):
        """Simulates opening the trunk."""
        return f"{self.brand} {self.model}'s trunk is now open."

# Bike class inherits from Vehicle
class Bike(Vehicle):
    def kickstart(self):
        """Simulates kickstarting the bike."""
        return f"{self.brand} {self.model} has been kickstarted."

# Separate class for luxury features
class LuxuryFeatures:
    def enable_gps(self):
        """Activates GPS in a luxury car."""
        return "GPS is now enabled."

    def enable_heated_seats(self):
        """Activates heated seats in a luxury car."""
        return "Heated seats are now enabled."

# LuxuryCar inherits from both Car and LuxuryFeatures (Multiple Inheritance)
class LuxuryCar(Car, LuxuryFeatures):
    def __init__(self, brand, model, rental_rate, luxury_fee):
        # Call Car's constructor (which calls Vehicle's constructor)
        super().__init__(brand, model, rental_rate)
        self.luxury_fee = luxury_fee  # Extra charge for luxury features

    def calculate_rental(self, days):
        """Overrides calculate_rental() to include luxury fees."""
        base_cost = super().calculate_rental(days)  # Call parent method
        return base_cost + (self.luxury_fee * days)  # Add luxury fee per day

# Creating objects
car = Car("Toyota", "Corolla", 50)
bike = Bike("Yamaha", "R15", 30)
luxury_car = LuxuryCar("BMW", "7 Series", 200, 50)  # Base rate $200 + $50 luxury fee

# Testing rentals
print(f"Car Rental for 3 days: ${car.calculate_rental(3)}")  # $150
print(f"Bike Rental for 3 days: ${bike.calculate_rental(3)}")  # $90
print(f"Luxury Car Rental for 3 days: ${luxury_car.calculate_rental(3)}")  # $750

# Testing features
print(car.open_trunk())  # Car-specific method
print(bike.kickstart())  # Bike-specific method
print(luxury_car.enable_gps())  # Inherited from LuxuryFeatures
print(luxury_car.enable_heated_seats())  # Inherited from LuxuryFeatures
