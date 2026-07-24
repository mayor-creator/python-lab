from coffee_data import coffee

# default coffee machine values
WATER = 300
MILK = 200
COFFEE = 100
MONEY = 0.00

# coffee machine coin operated
PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25


# get coffee machine report
def get_report():
    print(f"Water: {WATER}ml")
    print(f"Milk: {MILK}ml")
    print(f"Coffee: {COFFEE}g")
    print(f"Money: ${MONEY}")


# checking if the coffee machine have enough resources
def check_resources(user_input):
    if coffee[user_input]["water"] > WATER:
        print("Sorry there is not enough water.")
        return False

    if coffee[user_input]["milk"] > MILK:
        print("Sorry there is not enough milk.")
        return False

    if coffee[user_input]["coffee"] > COFFEE:
        print("Sorry there is not enough coffee.")
        return False

    return True


# calculate the amount of water left
def calculate_water(default_water, user_input):
    water_left = default_water
    if user_input in coffee:
        water_left -= coffee[user_input]["water"]
    return water_left


# calculate the amount of milk left
def calculate_milk(default_milk, user_input):
    milk_left = default_milk
    if user_input in coffee:
        milk_left -= coffee[user_input]["milk"]
    return milk_left


# calculate the amount of coffee left
def calculate_coffee(default_coffee, user_input):
    coffee_left = default_coffee
    if user_input in coffee:
        coffee_left -= coffee[user_input]["coffee"]
    return coffee_left


# calculate penny amount
def calculate_pennies(user_amt):
    total = PENNY * user_amt
    return total


# calculate nickel amount
def calculate_nickels(user_amt):
    total = NICKEL * user_amt
    return total


# calculate dim amount
def calculate_dims(user_amt):
    total = DIME * user_amt
    return total


# calculate the quarter amount
def calculate_quarter(user_amt):
    total = QUARTER * user_amt
    return total


# calculate the total cost of drink
def coffee_cost():
    money = (
        calculate_pennies(pennies)
        + calculate_nickels(nickels)
        + calculate_dims(dimes)
        + calculate_quarter(quarters)
    )
    return money


# check the total cost against coffee price
def get_coffee_amounts(user_input):
    if coffee_cost() < coffee[user_input]["price"]:
        print("Sorry that's not enough money. Money refunded.")
        return False

    refund = coffee_cost() - coffee[user_input]["price"]

    print(f"Here's ${round(refund,2)} in charge.")
    return True


# update the coffee machine resources
def make_coffee_drink(user_input):
    global WATER, MILK, COFFEE, MONEY

    WATER = calculate_water(WATER, user_input)
    MILK = calculate_milk(MILK, user_input)
    COFFEE = calculate_coffee(COFFEE, user_input)
    MONEY += coffee[user_input]["price"]

    print(f"Here is your {user_input}. Enjoy!")


# start making coffee
drink = input("What would you like? (espresso/latte/cappuccino): ")

if drink == "report":
    get_report()

elif drink in coffee:
    if check_resources(drink):
        # insert coins
        print("Please insert coins: ")
        pennies = int(input("How many pennies: "))
        nickels = int(input("How many nickels: "))
        dimes = int(input("How many dimes: "))
        quarters = int(input("How many quarters: "))

        if get_coffee_amounts(drink):
            # make coffee
            make_coffee_drink(drink)

            # show updated resources
            get_report()
else:
    print("Invalid drink selection")
