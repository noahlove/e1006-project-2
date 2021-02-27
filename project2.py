def select_meal():
    more_food = True
    total_order = []
    # ask the user repeatedly to add an item until the user types "done"
    while more_food:
        pizza_or_salad = input("Hello, would you like pizza or salad?\n")

        # Pizza order
        if pizza_or_salad == "pizza" or pizza_or_salad == "Pizza":
            pizza_statement = pizza()
            if not total_order:
                total_order = "You ordered a " + pizza_statement + "!"
                print(total_order)
            else:
                total_order = total_order + " You also ordered a " + pizza_statement + "."
                print(total_order)

        # Salad Order
        elif pizza_or_salad == "salad" or pizza_or_salad == "Salad":
            salad_statement = salad()
            if not total_order:
                total_order = "You ordered a " + salad_statement + "!"
                print(total_order)
            else:
                total_order = total_order + " You also ordered a " + salad_statement + "."
                print(total_order)

        # Done exit
        elif pizza_or_salad == "done" or pizza_or_salad == "done":
            more_food = False

        # Don't pick pizza or salad?
        else:
            print("You didn't pick one of the two options")

        print("Place another order or say 'done'.")


def pizza():
    pizza_size = input("Small, medium, or large?\n")
    complete_pizza_order = toppings(pizza_size)
    return complete_pizza_order


def toppings(pizza_size):
    # ask for toppings repeatedly until the user types "done"
    more_toppings = True
    toppings_list = []

    while more_toppings:
        topping = input("Add a topping: pepperoni, mushrooms, spinach, or say 'done'\n")
        if topping == "done":
            more_toppings = False
        else:
            toppings_list.append(topping)
    # Add the and between last 2 toppings
    toppings_list = " and ".join([", ".join(toppings_list[:-1]), toppings_list[-1]] if len(toppings_list) > 2 else
                                 toppings_list)

    pizza_order = pizza_size + " pizza with " + toppings_list
    return pizza_order


def salad():
    salad_choice = input("Would you like a garden salad or greek salad?\n")
    salad_order_full = dressing(salad_choice)
    return salad_order_full


def dressing(salad_choice):
    salad_dressing = input("Please choose a dressing: vinaigrette, ranch, blue cheese, lemon\n")
    salad_order = salad_choice + " salad with " + salad_dressing + " dressing"
    return salad_order


select_meal()
print("Your order has been placed. Goodbye")
