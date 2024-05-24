def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply (a,b):
    return a * b
def divide(a,b):
    if b==0:
      return "Error!!!! Division by zero"
    return a /b 
def calculator():
    print("Welcome to the calclator")
    while True:
        num1= float(input("Enter your first number plesase:"))
        num2= float(input("Enter your second number plesase:"))
        opreation= input ("Enter the opreation you want(+, -, *, /, ):")
        if opreation == '+':
            result = add (num1, num2)
        elif opreation == '-':
            result = subtract(num1, num2)
        elif opreation == '*':
            result = multiply(num1, num2)
        elif opreation == '/':
            result = divide(num1, num2)
        else:
            print("Error!!! Invalid opreation")
            continue
        print(f"The result is : {result}")
        
        another_calculation = input("Do you want to perform another calculation? (y/n): ")
        if another_calculation.lower() != 'y':
            break

    print("Thank you for using the Calculator App. Goodbye!")

if __name__ == "__main__":
    calculator()


                    
