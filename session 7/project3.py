def classify_age(age):
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teenager"
    elif age <= 20:
        return "Adult"
    else:
        return "Invalid age"
# INPUT 
age = int(input("Enter your age :"))
    
age_group = classify_age(age)
print("Age group:", age_group)






