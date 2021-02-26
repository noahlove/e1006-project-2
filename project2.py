#imports?

def select_meal():
    # ask the user repeatedly to add an item until the user types "done"
    pizza_or_salad = input("Hello, would you like pizza or salad?")
    if pizza_or_salad == "pizza" or pizza_or_salad == "Pizza":
        pizza()
    elif pizza_or_salad == "salad" or pizza_or_salad == "Salad":
        salad()
    else:
        print("You didn't pick one of the two options")


def pizza():
    pizza_size = input("Small, medium, or large?")
    toppings(pizza_size)


def toppings(passed_pizza):
    # ask for toppings repeatedly until the user types "done"
    more_toppings = True
    toppings_list = []

    while more_toppings == True:
        topping = input("Add a topping: pepperoni, mushrooms, spinach, or say 'done'")
        if topping == "done":
            more_toppings = False
        else:
            toppings_list.append(topping)
    # Add the and between last 2 toppings
    print("You ordered a", passed_pizza + " pizza with", ', '.join(toppings_list))
    pizza()


def salad():
    print("Would you like a garden salad or greek salad?")


def dressing():
    print("Please choose a dressing...")


select_meal()
