# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    total_cash = get_total_cash(pet_shop)
    pet_shop["admin"]["total_cash"] = (total_cash + amount)
    return pet_shop["admin"]["total_cash"]

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, amount):
    sold_pets = get_pets_sold(pet_shop)
    pet_shop["admin"]["pets_sold"] = sold_pets + amount
    return pet_shop["admin"]["pets_sold"]

def get_stock_count(pet_shop):
    stock = []
    for pets in pet_shop["pets"]:
        stock.append(pets)
    return len(stock)

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
    for each_customer in customer["name"]:
        if customer["name"] == each_customer:
            new_amount = get_customer_cash(each_customer) - amount
            return each_customer["cash"] = new_amount


    

