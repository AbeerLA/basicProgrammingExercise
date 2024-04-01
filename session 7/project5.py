def print_month_name(month_number):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if month_number >=1 and month_number <=12:
        print("Month name:" , months [month_number ])
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")

#Input the month
month_number= int(input("Enter the month number"))

#Output the month name
print_month_name(month_number)


