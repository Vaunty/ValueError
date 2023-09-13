chicken_Sandwich = 8.50
Salad = 4.50
pastrami_Sandwich = 9.50
Soup = 3.00
Toast = 1.00
menu = ["Chicken Sandwich", "Salad", "Pastrami Sandwich", "Soup", "Toast"]
print("Hello! Welcome to Matthew's Diner, would you like to see the menu? (Y/N)")

#: Conditionals, Prompts User for their Answer; If Y continues

my_input = input("Enter Only Y/N:")
print(my_input)
if my_input == "Y":
    print("Here's the Menu! From Left to Right each food item corresponds to a number, from 1-5! I Hope you "
"enjoy!\n", menu)
elif my_input == "y":
    print("Here's the Menu! From Left to Right each food item corresponds to a number, from 1-5! I Hope you "
"enjoy!\n", menu)
elif my_input == "N":
    print("Sorry, I hope you have a nice dinner elsewhere!")
else:
    print("Sorry, I hope you have a nice dinner elsewhere!")

#: Next Conditional Set, Prompts for Item and Tells Price

my_order = input("Enter Only One Number:")
while my_order in ["1", "2", "3", "4", "5"]:
    print(my_order + "")
    if my_order == "1":
        print("Here's the price of our Chicken Sandwich!:", format(chicken_Sandwich, '.2f'))
    elif my_order == "2":
        print("Here's the price of our Salad!:", format(Salad, '.2f'))
    elif my_order == "3":
        print("Here's the price of our Pastrami Sandwich", format(pastrami_Sandwich, '.2f'))
    elif my_order == "4":
        print("Here's the price of our Soup", format(Soup, '.2f'))
    elif my_order == "5":
        print("Here's the price of our Toast", format(Toast, '.2f'))
    else:
        print("Sorry, we dont have that on the menu!")
    my_order = input("Enter Only One Number or \"stop\" to stop:")

item_input = input("Enter Your Item Number until satisfied with your order [Type stop to end]: ")
inputs = []
while item_input != "stop":
    inputs.append(item_input)
    item_input = input("Enter another item number or \"stop\" to stop: ")

# After "stop" was entered

total = 0.00

for item in inputs:
    if item == "1":
        total += chicken_Sandwich
    elif item == "2":
        total += Salad
    elif item == "3":
        total += pastrami_Sandwich
    elif item == "4":
        total += Soup
    elif item == "5":
        total += Toast
print("Total:", format(total, '.2f'))

#: Defining Taxes and Tips and adding to acquired total


def salestax(total):
    sales_tax = 0.07
    return format(total * sales_tax, '.2f')


def tip(total):
    tips = 0.18
    return format(total * tips, '.2f')

#: What user sees, after STOP and


def displayresult(total):
    print("Here is the Original Price Of Everything", format(total, '.2f'))
    sales_tax = salestax(total)
    print("Here's with sales tax included", format(float(total) + float(sales_tax), '.2f'), format(sales_tax, '.2f'))
    tips = tip(total)
    print("Tip:", format(tips, '.2f'))
    print('Total', format(float(total) + float(sales_tax) + float(tips), '.2f'))


def main():
    total = input("Enter the price of the purchase: ")
    displayresult(total)


main()
