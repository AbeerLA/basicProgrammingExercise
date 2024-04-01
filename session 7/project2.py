#The conditional
def calculator (num1, num2, opreator):
    if opreator == '+':
        return num1 + num2
    elif opreator == '-':
        return num1 - num2
    elif opreator == '*':
        return num1 * num2
    elif opreator == '/':
        return num1 / num2
        if num2 != 0:
          return num1 / num2
        else:
          print ("Error! The division by zero is not allowed.")
    else :
       print("Error! Invalid operator.")
   
 # INPUT VALUES
num1= float (input("Enter the first value"))
num2= float (input("Enter the second value"))
operator = input("Enter the operator (+, -, *, /): ")

#The opreation 
result = calculator(num1, num2, operator)
print("Result", result )
