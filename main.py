# This dictionary includes the 3 coffee types ( Espresso, Latte, Cappuccino ) with the ingredients needed and costs
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# This is the resources at the beginning of the program
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def total_calculator(quarters, dimes, nickles, pennies):
    """Calculates the total money inserted in the machine"""
    return (quarters * 0.25) + (dimes * 0.1) + (nickles * .05) + (pennies * .01)


def coffee_actual_names(coffee_input):
    """Converts user inputs into coffee names"""
    if coffee_input.lower() == "e":
        coffee_input = "espresso"
    elif coffee_input.lower() == "l":
        coffee_input = "latte"
    elif coffee_input.lower() == "c":
        coffee_input = "cappuccino"
    return coffee_input


def resource_report():
    """Gives a report of current resources"""
    for resource in resources:
        if resource == "coffee":
            print(f"{resource} : {resources[resource]} g")
        else:
            print(f"{resource} : {resources[resource]} ml")
    print("\n")


def coffee_machine():
    """Does all the work"""
    if resources["coffee"] < 18 or resources["water"] < 50:
        print("Not enough resources for any coffee")
        exit()

    print("Welcome to your coffee machine!!")
    choice = input("What would you like ? \nType 'E' for Espresso, 'C' for Cappuccino, 'L' for Latte"
                   ", 'R' to see the current resources\n")

    if choice.lower() == "r":
        resource_report()
        coffee_machine()
    coffee_name = MENU[coffee_actual_names(choice)]
    for res in coffee_name["ingredients"]:
        if coffee_name["ingredients"][res] > resources[res]:
            print(f"Not Enough resources !!\nResources needed for {coffee_name}:")
            coffee_machine()

    print(f"The price of a cup of {coffee_actual_names(choice)} is ${coffee_name['cost']}"
          f", please insert coins:\n")
    quarters_inserted = int(input("How many quarters?: "))
    dimes_inserted = int(input("How many dimes?: "))
    nickles_inserted = int(input("How many nickles?: "))
    pennies_inserted = int(input("How many pennies?: "))

    total_paid = total_calculator(quarters_inserted, dimes_inserted, nickles_inserted, pennies_inserted)

    if coffee_name["cost"] > total_paid:
        print("Insufficient Money! Money refunded.\n")
        coffee_machine()
    else:
        for res in coffee_name["ingredients"]:
            resources[res] -= coffee_name["ingredients"][res]
        money_change = total_paid - coffee_name["cost"]

    if money_change == 0:
        print(f"Here is your {coffee_actual_names(choice)}. Enjoy it!\n")
        coffee_machine()
    else:
        print(f"Here is your {coffee_actual_names(choice)}. Your change is {round(money_change, 2)} \n")
        coffee_machine()


coffee_machine()
