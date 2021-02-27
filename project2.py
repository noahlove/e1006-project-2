#imports?

def select_meal():
    more_food = True
    pizza_statement = []
    salad_statement = []
    # ask the user repeatedly to add an item until the user types "done"
    while more_food == True:
        pizza_or_salad = input("Hello, would you like pizza or salad?\n")
        if pizza_or_salad == "pizza" or pizza_or_salad == "Pizza":
            pizza_statement = pizza()
        elif pizza_or_salad == "salad" or pizza_or_salad == "Salad":
            salad_statement = salad()
        elif pizza_or_salad == "done" or pizza_or_salad == "done":
            more_food = False
        else:
            print("You didn't pick one of the two options")
        print("you ordered a", pizza_statement, "and a", salad_statement)



def pizza():
    pizza_size = input("Small, medium, or large?\n")
    complete_pizza_order = toppings(pizza_size)
    return complete_pizza_order


def toppings(pizza_size):
    # ask for toppings repeatedly until the user types "done"
    more_toppings = True
    toppings_list = []

    while more_toppings == True:
        topping = input("Add a topping: pepperoni, mushrooms, spinach, or say 'done'\n")
        if topping == "done":
            more_toppings = False
        else:
            toppings_list.append(topping)
    # Add the and between last 2 toppings
    toppings_list = ",".join(toppings_list[:-1]) + " and " + toppings_list[-1]
    pizza_order = pizza_size + " pizza with " + toppings_list
    return pizza_order


def salad():
    salad_choise = input("Would you like a garden salad or greek salad?\n")
    salad_order_full = dressing(salad_choise)
    return salad_order_full


def dressing(salad_choice):
    salad_dressing = input("Please choose a dressing: vinaigrette, ranch, blue cheese, lemon\n")
    salad_order = salad_choice + " salad with " + salad_dressing + " dressing"
    return salad_order


select_meal()
print("Your order has been placed. Goodbye")
