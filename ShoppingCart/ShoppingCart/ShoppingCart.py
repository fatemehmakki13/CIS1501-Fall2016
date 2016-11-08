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

cart = ShoppingCart("Eric", "11/8/2016")
item1 = ItemToPurchase()
item1.item_name = 'Cookies'
item1.item_price = 3
item1.item_quantity = 1
item1.item_description = 'Chips Ahoy!'
cart.add_item(item1)

cart.remove_item("bananas")
cart.remove_item("Cookies")
