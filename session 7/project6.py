def classify_temperture(temperature):
    if temperature < 0 :
        return "Freezing"
    elif temperature >=0 and temperature < 10:
        return"Very Cold"
    elif temperature >=10 and temperature <20:
        return "Cold"
    elif temperature >=20 and temperature < 30:
        return "Moderate"
    elif temperature >=30 and temperature < 40:
        return "Hot"
    else:
        return "Very Hot"
#INPUT
temperature= float(input( "Enter the temperture in Celsius"))
#OUTPUT
temperature_category = classify_temperture(temperature)
print("Temperature category: ", temperature_category)

