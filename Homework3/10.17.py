# George Tannous 1971969
# 10.17
class ItemToPurchase:
    def __init__(self):
        self.item_name="none"
        self.item_price=0
        self.item_quantity=0

    def print_item_cost(self):
        print(self.item_name,self.item_quantity,'@ $',end='')
        print(self.item_price,'= $',end='')

        cost=self.item_price*self.item_quantity
        print(cost)

if __name__=="__main__":
    item1=ItemToPurchase()
    item2=ItemToPurchase()
    print('Item 1')
    item1.item_name=input('Enter the item name:\n')
    item1.item_price=int(input('Enter the item price:\n'))
    item1.item_quantity=int(input('Enter the item quantity:\n'))

    print('\nItem 2')
    item2.item_name=input('Enter the item name:\n')
    item2.item_price=int(input('Enter the item price:\n'))
    item2.item_quantity=int(input('Enter the item quantity:\n'))

    print('\nTOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()

    print('\nTotal: $',end='')
    total_cost=item1.item_price*item1.item_quantity+item2.item_price*item2.item_quantity
    print(total_cost)
