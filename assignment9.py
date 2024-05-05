#NAME = ABEER LABEB ALI AHMED
#NIM = 20230040299
print("Welcome! In this program, you can store items in a list, update them anytime and you can come check it out.")
items = []
while True:
 #Menu
  print("Select Menu: ")
  print("1. Input item: ")
  print("2. Delete item: ")
  print("3. Print items: ")
  print("4. Update item:")
  print("5. Exit program!")
  selected_menu = input("Select Menu: ")
#Insert Items
  if(selected_menu == "1"):
    new_item = input("Input your item: ")
    items.append(new_item)
    print("Your new Item has been added successfully")
#Delete Items
  if selected_menu == "2":
    delete_item = input("What item do you want to remove? ")
    if delete_item in items:
      items.remove(delete_item)
      print("The item is successfully deleted. Confirm")
    else:
      print("Item not found!")
#Display the items
  if selected_menu == "3":
    print("The items in your list are: ", items)
#Update the Items
  if selected_menu == "4":
    update_item = input("What item do you want to update? ")
    if update_item in items:
      updated_item = input("What do you want to update it to? ")
      items.remove(update_item)
      items.append(updated_item)
      print("The item you wish to update has been updated successfully")
    else:
      print("Item not found!")
  if selected_menu == "5":
    print("Thank you for using the program. You can come back anytime!")
    break
  