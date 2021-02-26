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
    pizza_size = input("small, medium, or large?")
    toppings()


def toppings():
    # ask for toppings repeatedly until the user types "done"
    print("Add a topping...")


def salad():
    print("Would you like a garden salad or greek salad?")


def dressing():
    print("Please choose a dressing...")


select_meal()

