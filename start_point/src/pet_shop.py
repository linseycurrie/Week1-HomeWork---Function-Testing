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
    
    # Alternative method for stock count.
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
    index_counter = 0
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet_shop["pets"][index_counter]
        else:
            index_counter += 1


def remove_pet_by_name(pet_shop, pet_name):
    index_counter = 0
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            del pet_shop["pets"][index_counter]
        else:
            index_counter += 1


def add_pet_to_stock(pet_shop, new_pet):
    new_pet = {
        "name": input("\nWhat is your pets name ? "), 
        "pet_type": input("\nWhat type of pet do you want to add ? "), 
        "breed": input("\nwhat breed is your pet ? "), 
        "price": input("\nHow much does this pet cost ? ")
        }
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] = (get_customer_cash(customer) - amount)


def get_customer_pet_count(customer):
    return len(customer["pets"])
    
    # Different way to calculate the customer pet count. 
    # pet_count = []
    # for pet in customer["pets"]:
    #     pet_count.append(pet)
    # return len(pet_count)


def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)
    
def customer_can_afford_pet(customer, pet_list):
        if (pet_list == None):
            print("\nSorry no pet list available")
            # break
        elif (get_customer_cash(customer) >= pet_list["price"]):
            return True
        else:
            return False

def sell_pet_to_customer(pet_shop, pet, customer):
    if((customer_can_afford_pet(customer, pet) and pet)):
        remove_pet_by_name(pet_shop, pet)
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, int(pet["price"]))
        increase_pets_sold(pet_shop, 1)
        add_or_remove_cash(pet_shop, pet["price"])
    elif(pet == None):
        return "\n Sorry we do not have that pet."
    elif((customer_can_afford_pet(customer, pet) == False)):
        return "\n Sorry you do not have enough money."

