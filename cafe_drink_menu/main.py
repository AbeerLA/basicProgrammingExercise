import json
from models.coffee import CoffeeDrink
from models.non_coffee import NonCoffeeDrink

def load_drinks():
    coffee = []
    non_coffee = []
    with open('data/drinks.json', 'r') as f:
        data = json.load(f)
        for item in data:
            if item['type'] == 'CoffeeDrink':
                drink = CoffeeDrink(item['name'], item['coffee_type'], item['sizes'])
                drink.image = item.get("image", "")
                coffee.append(drink)
            elif item['type'] == 'NonCoffeeDrink':
                drink = NonCoffeeDrink(item['name'], item['category'], item['sizes'])
                drink.image = item.get("image", "")
                non_coffee.append(drink)
    return coffee, non_coffee

def generate_html(coffee, non_coffee):
    def render_drink(drink, drink_type):
        return f'''
        <div class="drink-card {drink_type}">
            <img src="../static/images/{drink.image}" alt="{drink.name}">
            <p>{drink.display()}</p>
        </div>
        '''

    coffee_html = "".join([render_drink(drink, "coffee") for drink in coffee])
    non_coffee_html = "".join([render_drink(drink, "non-coffee") for drink in non_coffee])

    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Cafe Drink Menu</title>
    <link rel="stylesheet" type="text/css" href="../static/style.css">
</head>
<body>
    <h1>Our Cafe Drink Menu</h1>

    <div class="menu-container">
        <div class="menu-column">
            <h2>☕ Coffee</h2>
            {coffee_html}
        </div>
        <div class="menu-column">
            <h2>🥤 Non-Coffee</h2>
            {non_coffee_html}
        </div>
    </div>

</body>
</html>
""")

if __name__ == "__main__":
    coffee, non_coffee = load_drinks()
    generate_html(coffee, non_coffee)
    print(" 2-column menu with images generated! Open templates/index.html in your browser.")
