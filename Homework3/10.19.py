# George Tannous 1971969
# 10.19
class ItemToPurchase:
    def __init__(self, name="none", price=0, quantity=0, description="none"):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, total))

    def print_item_description(self):
        print('%s: %s' % (self.item_name, self.item_description))


class ShoppingCart:

    def __init__(self, cust_name="none", current_date='January 1, 2016'):
        self.customer_name = cust_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, ItemName):
        remove_item = False
        for item in self.cart_items:
            if item.item_name == ItemName:
                self.cart_items.remove(item)
                remove_item = True
                break
        if not remove_item:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, ItemToPurchase):
        modify_item = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == ItemToPurchase.item_name:
                modify_item = True
                if (ItemToPurchase.item_price == 0 and ItemToPurchase.item_quantity == 0 and ItemToPurchase.item_description == "none"):
                    break
                else:
                    if (ItemToPurchase.item_price != 0):
                        self.cart_items[i].item_price = ItemToPurchase.item_price
                    if (ItemToPurchase.item_quantity != 0):
                        self.cart_items[i].item_quantity = ItemToPurchase.item_quantity
                    if (ItemToPurchase.item_description != "none"):
                        self.cart_items[i].item_description = ItemToPurchase.item_description
                    break
        if not modify_item:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0
        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            total_cost += cost
        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if (total_cost == 0):
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: 0\n')
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: %d\n' % self.get_num_items_in_cart())
            for item in self.cart_items:
                item.print_item_cost()

        print('\nTotal: $%d' % (total_cost))

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('\nItem Descriptions')
            for item in self.cart_items:
                item.print_item_description()


def print_menu(Cart):
    global ItemPurchase, ItemToPurchase
    customer_Cart = Cart
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            "i - Output items' descriptions\n"
            'o - Output shopping cart\n'
            'q - Quit\n')

    command = ''
    while (command != 'q'):
        print(menu)
        command = input('Choose an option:\n')
        while (command != 'a' and command != 'o' and command != 'i' and command != 'q' and command != 'r' and command != 'c'):
            command = input('Choose an option:\n')
        if (command == 'a'):
            print("\nADD ITEM TO CART")
            item_name = input('Enter the item name:\n')
            item_description = input('Enter the item description:\n')
            item_price = int(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))
            ItemPurchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            customer_Cart.add_item(ItemPurchase)
        elif (command == 'o'):
            print('OUTPUT SHOPPING CART')
            customer_Cart.print_total()
        elif (command == 'i'):
            print('\nOUTPUT ITEMS\' DESCRIPTIONS')
            customer_Cart.print_descriptions()
        elif (command == 'r'):
            print('REMOVE ITEM FROM CART')
            ItemName = input('Enter name of item to remove:\n')
            customer_Cart.remove_item(ItemName)
        elif (command == 'c'):
            print('\nCHANGE ITEM QUANTITY')
            ItemName = input('Enter the item name:\n')
            qty = int(input('Enter the new quantity:\n'))
            ItemPurchase = ItemToPurchase(ItemName, 0, qty)
            customer_Cart.modify_item(ItemPurchase)


if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print("\nCustomer name: %s" % customer_name)
    print("Today's date: %s" % current_date)
    Cart = ShoppingCart(customer_name, current_date)
    print_menu(Cart)
