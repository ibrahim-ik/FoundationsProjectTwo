# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.Ebraheem_store.com"  

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for item in stores:
        print (item.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """

    for store in stores:
        if store.name.lower() == store_name.lower():
            return store

    return False

    # your code goes here!
    # flag_store = False
    # while flag_store == False:
    #     for store in stores:
    #         if store_name.lower() == store.name.lower():
    #             flag_store = True
    #             return store
    #     print("COMPARING %s with %s" %(store_name.lower(), store.name.lower()))
    #     store_name = input("you entered an invaild name, please re enter the store you want to go to.\n")
    

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """

    while True:
        user_input = input("Pick a store: ")
        store = get_store(user_input)
        if store:
            # user entered a valid store name
            return store

        if user_input.lower() == "checkout":
            return "checkout"

        print("Invalid store name.")
    


    # your code goes here!
    # picked_store = input("please choose one of the stores you want to go to: ")
    # object_store = get_store(picked_store)
    # return object_store

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """

    while True:
        picked_store.print_products()
        user_input = input("Pick a product to add to your cart: ")
        if user_input.lower() == "back":
            break

        for product in picked_store.products:
            if product.name.lower() == user_input.lower():
                cart.add_to_cart(product)

    return user_input





    # your code goes here!
    # picked_store.print_products()
    # piked_product = input("Enter the wanted product,(back) to get back to sotre list,OR (checkout) to go out: \t")
    # product_found = False

    # while piked_product != "aaa":
    #     for item in picked_store.products:
    #         print("COMPARING \"%s\" WITH \"%s\"" % (piked_product.lower(), item.name.lower()))
    #         if piked_product.lower() == item.name.lower():
    #              print("you entered %s and the Comparing it with %s " % (piked_product.lower(),item.name.lower()))
    #              cart.add_to_cart(item.name)
    #              print("added to cart")
    #              print (cart.cart_list)
    #              product_found = True
        
    #     piked_product = input("and ?: \t")
    #     if piked_product == "checkout":
    #         cart.checkout()
    #     elif piked_product == "back":
    #         print_stores()
    #         pick_store()
    #         piked_product = input("you enterd in valid product, please re enter the product\t")







    

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    while True:
        print_stores()
        picked_store = pick_store()
        if picked_store == "checkout":
            break

        user_input = pick_products(cart,picked_store)

    cart.checkout()

    # your code goes here!

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
