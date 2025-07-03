from models.drink import Drink

class NonCoffeeDrink(Drink):
    def __init__(self, name, category, sizes):
        super().__init__(name)
        self.category = category
        self.sizes = sizes

    def display(self):
        lines = [f"<strong>{self.name}</strong> - {self.category}"]
        for s in self.sizes:
            lines.append(f"&rarr; {s['size']} - ${s['price']:.2f}")
        return "<br>".join(lines)
