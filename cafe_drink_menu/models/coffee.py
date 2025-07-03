from models.drink import Drink

class CoffeeDrink(Drink):
    def __init__(self, name, coffee_type, sizes):
        super().__init__(name)
        self.coffee_type = coffee_type
        self.sizes = sizes 

    def display(self):
        lines = [f"<strong>{self.name}</strong> - {self.coffee_type}"]
        for s in self.sizes:
            lines.append(f"&rarr; {s['size']} - ${s['price']:.2f}")
        return "<br>".join(lines)
