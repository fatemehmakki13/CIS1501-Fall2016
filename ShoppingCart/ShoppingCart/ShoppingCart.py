class ItemToPurchase:
    currencySymbol = "$"

    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = 'none'

    def print_item_cost(self):
        print('%s %d @ %s%.2f = %s%.2f' % ( self.item_name, self.item_quantity, self.currencySymbol, self.item_price, self.currencySymbol, ( self.item_price * self.item_quantity ) ) )

    def print_item_description(self):
        print('%s: %s' % ( self.item_name, self.item_description) )

    def __str__(self):
        return '%s %d @ %s%.2f = %s%.2f\n' % ( self.item_name, self.item_quantity, self.currencySymbol, self.item_price, self.currencySymbol, ( self.item_price * self.item_quantity ) )

class ShoppingCart:
    def __init__(self, name, date):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []

    def add_item( self, itemToPurchase ):
        '''itemToPurchase is an ItemToPurchase'''
        self.cart_items.append( itemToPurchase )

    def remove_item( self, item_name ):
        itemRemoved = False
        for item in self.cart_items[:]:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                itemRemoved = True

        if not itemRemoved:
            print('Item not found in cart. Nothing removed.')

    def modify_item( self, itemToModify ):
        itemModified = False
        for index in range( len(self.cart_items) ):
            if self.cart_items[index].item_name == itemToModify.item_name:
                if itemToModify.item_name != 'none' and itemToModify.item_price != 0 and itemToModify.item_quantity != 0 and itemToModify.item_description != 'none':
                    self.cart_items[index].item_name = itemToModify.item_name
                    self.cart_items[index].item_price = itemToModify.item_price
                    self.cart_items[index].item_quantity = itemToModify.item_quantity
                    self.cart_items[index].item_description = itemToModify.item_description
                    itemModified = True

        if not itemModified:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        numberOfItemsInCart = 0

        for item in self.cart_items:
            numberOfItemsInCart += item.item_quantity

        return numberOfItemsInCart

    def get_cost_of_cart(self):
        costOfCart = 0

        for item in self.cart_items:
            costOfCart += item.item_quantity * item.item_price

        return costOfCart

    def __str__(self):
        output = ""
        output += "%s's Shopping Cart - %s\n" % ( self.customer_name, self.current_date )
        if len(self.cart_items) == 0:
            output += "SHOPPING CART IS EMPTY\n"
        else:
            output += "Number of Items: %d\n" % len(self.cart_items)
            output += "\n"
            for item in self.cart_items:
                output += str(item)
            output += "\n"
            output += "Total: %s%.2f\n" % ( ItemToPurchase.currencySymbol, self.get_cost_of_cart() )

        return output

    def print_total(self):
        print(self)


def print_menu(shoppingCart):
    shoppingCart.get_num_items_in_cart()
    shoppingCart.print_total
    

ericsCart = ShoppingCart("Eric", "11/8/2016")
ericsCart.add_item("apples")
jasminesCart = ShoppingCart("Jasmine", "11/8/2016")
item1 = ItemToPurchase()
item1.item_name = 'Cookies'
item1.item_price = 3
item1.item_quantity = 1
item1.item_description = 'Chips Ahoy!'
ericsCart.add_item(item1)

for item in ericsCart.cart_items:
    item.print_item_cost()

ericsCart.remove_item("bananas")

item2 = ItemToPurchase()
item2.item_name = 'Cookies'
item2.item_price = 3
item2.item_quantity = 2
item2.item_description = 'Chips Ahoy!'

item3 = ItemToPurchase()
item3.item_name = 'Apples'
item3.item_price = 1
item3.item_quantity = 5
item3.item_description = 'Granny Smith'

item4 = ItemToPurchase()
item4.item_name = 'Yogurt'
item4.item_price = 1
item4.item_quantity = 8
item4.item_description = 'Greek'

ericsCart.modify_item( item2 )

jasminesCart.add_item( item3 )
ericsCart.add_item(item4)

for item in ericsCart.cart_items:
    item.print_item_cost()

for item in jasminesCart.cart_items:
    item.print_item_cost()

print( ericsCart.get_num_items_in_cart() )
print( jasminesCart.get_num_items_in_cart() )

print( "cost of eric's cart: %s%.2f" % ( ItemToPurchase.currencySymbol, ericsCart.get_cost_of_cart() ) )
print( "cost of jasmine's cart: %s%.2f" % ( ItemToPurchase.currencySymbol, jasminesCart.get_cost_of_cart() ) )
print()
print()
print()


print(ericsCart)
print(jasminesCart)