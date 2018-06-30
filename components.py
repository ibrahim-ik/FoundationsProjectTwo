# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name = name
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.products.append(product)


    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        for product in self.products:
            print ("%s\n" %(product))


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        # your code goes here!
        return "\nName: \t\t%s\nDescription: \t%s\nPrice:\t\t%s K.D" % (self.name, self.description, self.price)

class Cart():

    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.cart_list = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.cart_list = []
        self.cart_list.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total = 0
        for item in self.cart_list:
            print(item.price)
            total = total + item.price
        return total

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        for item in self.cart_list:
            print (item)
        print (" your total is: %s" % (self.get_total_price()))

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!

        #print_receipt()
        confirmation = input("please confirm your order by typing Yes/No\t")
        if confirmation.lower() == "yes":
            print("order is confirmed")
            self.print_receipt()
        elif confirmation.lower() == "no":
            print("order is cancelled")
        else: 
            print("Error")
