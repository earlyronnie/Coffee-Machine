MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


def check_resources(coffee):
    """Checks the machine's resources and the needed resources to make a specific type of coffee"""
    # convert each coin into its dollar equivalent
    final_water = (total_water - needed_water)
    final_milk = (total_milk - needed_milk)
    final_coffee = (total_coffee - needed_coffee)
    resources["water"] = final_water
    resources["milk"] = final_milk
    resources["coffee"] = final_coffee


def calculate_cost(coffee, quarters, dimes, nickels, pennies):
    """Adds each coins, and checks if it's more than or equal to the cost of the coffee.
    The user's total money and change gets evaluated."""
    coffee_cost = MENU[coffee]["cost"]
    quarters *= .25
    dimes *= .1
    nickels *= .05
    pennies *= .01
    user_money = (quarters + dimes + nickels + pennies)
    print(f"Your money: ${user_money}")

    change = float(user_money - coffee_cost)
    if user_money < coffee_cost:
        restocked_water = resources["water"] + needed_water
        resources["water"] = restocked_water

        restocked_milk = resources["milk"] + needed_milk
        resources["milk"] = restocked_milk

        restocked_coffee = resources["coffee"] + needed_coffee
        resources["coffee"] = restocked_coffee
        print(f"Not enough money. The coffee was {coffee_cost}")
        refund = user_money
        print(f"Money refunded: ${refund}")

    else:
        format_change = round(change, 2)
        global money
        money += coffee_cost
        print(f"Your change: ${format_change}")
        print(f"Here's your {coffee}!")


money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

end_of_order = False
while not end_of_order:
    user_order = input("Which coffee would you like? (espresso/latte/cappuccino): ").lower()
    if user_order == "off":
        end_of_order = True
        print("Goodbye")
    elif user_order == "report":
        # for keys in resources:
        #     print(f"{keys.title()}: {resources[keys]}")
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f"Money: ${money}")
    elif user_order == "espresso" or "latte" or "cappuccino":
        total_water = resources["water"]
        total_milk = resources["milk"]
        total_coffee = resources["coffee"]
        needed_water = MENU[user_order]["ingredients"]["water"]
        needed_milk = MENU[user_order]["ingredients"]["milk"]
        needed_coffee = MENU[user_order]["ingredients"]["coffee"]

        if total_water < needed_water:
            print(f"The machine has insufficient amount of water.")
        elif total_milk < needed_milk:
            print(f"The machine has insufficient amount of milk.")
        elif total_coffee < needed_coffee:
            print(f"The machine has insufficient amount of coffee.")
        else:
            check_resources(user_order)
            print("Please insert coins")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickel = int(input("How many nickels?: "))
            penny = int(input("How many pennies?: "))
            calculate_cost(user_order, quarter, dime, nickel, penny)
