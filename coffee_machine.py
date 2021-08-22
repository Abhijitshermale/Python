


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredient):
    is_enough=True
    for item in order_ingredient:
        if order_ingredient[item]>=resources[item]:
            print(f"sorry there is no enough{item}")
            is_enough=False
    return is_enough

def process_coin():
    print("please insert coin:")
    total=int(input("how many 10 coin : "))*10
    total+=int(input("How many 5 coin : "))*5
    total+=int(input("How Many 2 Coin : "))*2
    total+=int(input("How many 1 coin : "))*1
    return total 

def is_transaction_succesfull(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is {change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("There is no enough Money.Money Refunded")
        return False

def make_coffee(drink_name,order_ingredient):
    for item in order_ingredient:
        resources[item]-=order_ingredient[item]
    print(f"Here is your {drink_name}")



is_on=True
while is_on:
    choice=input("What would you like(espresso, latte, cappuccino) : ") 
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}gm")
        print(f"money: {profit}")
    else:
        drink=MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment=process_coin()
            if is_transaction_succesfull(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])

