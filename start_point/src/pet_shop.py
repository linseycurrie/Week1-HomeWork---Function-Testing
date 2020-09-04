# WRITE YOUR FUNCTIONS HERE
import pdb

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] = (get_total_cash(pet_shop) + amount)


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, amount):
    pet_shop["admin"]["pets_sold"] = (get_pets_sold(pet_shop) + amount)


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])
    
    # stock = []
    # for pets in pet_shop["pets"]:
    #     stock.append(pets)
    # return len(stock)

def get_pets_by_breed(pet_shop, breed):
    desired_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            desired_pets.append(pet)
    return desired_pets

def find_pet_by_name(pet_shop, pet_name):
    index_count = 0
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet_shop["pets"][index_count]
        else:
            index_count += 1


def remove_pet_by_name(pet_shop, pet_name):
    index_count = 0
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            del pet_shop["pets"][index_count]
        else:
            index_count += 1
    if(index_counter > len(pet_shop["pets"])):
        return None

def add_pet_to_stock(pet_shop, new_pet):
    name = input("What is your pets name ? ")
    pet_type = input("What type of pet do you want to add ? ")
    breed = input("what breed is your pet ? ")
    price = input("How much does this pet cost ? ")
    new_pet = {
        "name": name, 
        "pet_type": pet_type, 
        "breed": breed, 
        "price": price
        }
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] = (get_customer_cash(customer) - amount)


def get_customer_pet_count(customer):
    return len(customer["pets"])
    
    
    # pet_count = []
    # for pet in customer["pets"]:
    #     pet_count.append(pet)
    # return len(pet_count)


def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)
    
def customer_can_afford_pet(customer, pet_list):
        if (get_customer_cash(customer) >= pet_list["price"]):
            return True
        else:
            return False

def sell_pet_to_customer(pet_shop, pet_name, customer):
    customer_has_enough_money = customer_can_afford_pet(customer, pet_to_sell)

    if((pet_to_sell = find_pet_by_name(pet_shop, pet_name))== None):
        print("Sorry that pet is not available")
    elif(pet_to_sell != None and customer_has_enough_money == True):
        remove_pet_by_name(pet_shop, pet_to_sell)
        add_pet_to_customer(customer, pet_to_sell)
        remove_customer_cash(customer, int(pet_to_sell["price"]))
        increase_pets_sold(pet_shop, 1)
        add_or_remove_cash(pet_shop, pet_to_sell["price"])
