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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_enough(order_ingredient):
    """4. Returns True when orders can be made, reject if order is sufficient"""
    is_enough = True
    for item in order_ingredient:
       if order_ingredient[item] >= resources[item]:
        print(f"Sorry there is not enough {item}")
        is_enough = False
    return is_enough

def process_coin():
    """ 5. Returns the total calculated from the coins inserted"""
    print("Please insert coins: ")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """ 6. Return True when the payment is accepted, or False if money is not enough"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit 
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money refund")
        return False
def make_coffee(drink_name, order_ingredients):
    """ 7. Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕, Enjoy!!")

is_on = True
while is_on:
    # 1. Prompt user to pick which drink they want
    user_prompt = input("What would you like today? (espresso/latte/cappuccino): ")
    
    # 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_prompt == "off":
        is_on = False
    elif user_prompt == "report":
        # 3. Print Report
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: $ {profit}")
    elif user_prompt == 'espresso' or user_prompt == 'latte' or  user_prompt == 'cappuccino':
        drink = MENU[user_prompt]
        if is_resource_enough(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_prompt, drink["ingredients"])
    else:
        print("Error!")
