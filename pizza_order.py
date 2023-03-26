# Program to calculate the price of the Pizza order

# the variable holds dictionary's key and values
price_for_pizza_size = {'S':15, 'M':20, 'L':25, 'pepperoni_for_small_pizza':2, 'pepperoni_for_medium/large_pizza':3, 'Extra_cheese_for_any_pizza':1}

# Taking inputs and while loop runs until user provides valid answers
while True:
    size = str(input('Select the size of pizza (S/M/L): ')).upper()
    if size != "S" and size != "M" and size != "L":
        print("Enter valid input")
        continue
    else:
        break

while True:
    add_pepperoni = str(input('Add Pepproni? (Y/N): ')).upper()
    if add_pepperoni != "Y" and add_pepperoni != "N":
        print("Enter valid input")
        continue
    else:
        break

while True:
    extra_cheese = str(input('Add Extra Cheese? (Y/N): ')).upper()
    if extra_cheese != "Y" and extra_cheese != "N":
        print("Enter valid input")
        continue
    else:
        break

# Definig function to calculate the price for small pizzas with pepperoni and/or extra cheese.
def add_pepperoni_extra_cheese_for_small_pizza():
    if add_pepperoni =="Y":
        if extra_cheese == "Y":
            price = price_for_pizza_size[size] + price_for_pizza_size['pepperoni_for_small_pizza'] + price_for_pizza_size['Extra_cheese_for_any_pizza']
        else:
            price = price_for_pizza_size[size] + price_for_pizza_size['pepperoni_for_small_pizza']
    else:
        price = price_for_pizza_size[size]
    return price

# Definig function to calculate the price for pizzas that are medium or large and have pepperoni and/or extra cheese added.
def add_pepperoni_extra_cheese_for_medium_large_pizza():
    if add_pepperoni =="Y":
        if extra_cheese == "Y":
            price = price_for_pizza_size[size] + price_for_pizza_size['pepperoni_for_medium/large_pizza'] + price_for_pizza_size['Extra_cheese_for_any_pizza']
        else:
            price = price_for_pizza_size[size] + price_for_pizza_size['pepperoni_for_medium/large_pizza']
    else:
        price = price_for_pizza_size[size]
    return price

#A series of 'if' statements are used to determine which function to use for the given size of pizza.
if size == "S":
    price = add_pepperoni_extra_cheese_for_small_pizza()

elif size == "M":
    price = add_pepperoni_extra_cheese_for_medium_large_pizza()

else:
    price = add_pepperoni_extra_cheese_for_medium_large_pizza()


# The final calculated price is then printed using string formatting.
txt = "The price of your pizza is: ${amount}"
print(txt.format(amount=price))


