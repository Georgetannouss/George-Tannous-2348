# George Tannous 1971969
# FinalProjectPart1

import csv  # Used to read and write CSV/Excel files
import datetime  # Used to get the current time


def conv_date(date: str):
    temp_date = [int(c) for c in date.split(sep='/')]

    return [temp_date[2], temp_date[0], temp_date[1]]

# Creating the class called Item


class Item:
    # The following class is being used to store an items information

    # defines the items
    def __init__(self, p_id=0, p_manufacturer='none', p_type='none', p_price=0, p_date='00-00-0000', p_damaged=''):
        self.id = p_id  # ItemID
        self.manufacturer = p_manufacturer  # Item Manufacturer
        self.type = p_type  # Item Type
        self.price = p_price  # Item Price
        self.date = p_date  # Item Service Date
        self.damaged = p_damaged  # Item Damaged

    def __str__(self):
        return f'{self.id}, {self.manufacturer}, {self.type}, {self.price}, {self.date}, {self.damaged}'


# Creating a class called Inventory
class Inventory:
    # This class is used to store the data

    def __init__(self):
        self.items = []  # This will list any Items in the Inventory

    # A - FullInventory
    def fullinventory(self):
        # Sorting the inventory by manufacturer
        def sort(i_sort: Item):
            return i_sort.manufacturer

        manufacturer_sorted_items = sorted(self.items, key=sort)

        # This will write to the fullinventory CSV file
        with open('FullInventory.csv', 'w', newline='') as fullinventory_file:
            fullinventory_writer = csv.writer(fullinventory_file)

            for manufacturer_item in manufacturer_sorted_items:
                fullinventory_writer.writerow((manufacturer_item.id, manufacturer_item.manufacturer,
                                               manufacturer_item.type, manufacturer_item.price, manufacturer_item.date, manufacturer_item.damaged))

    # B - LaptopInventory

    def inventorytype(self):
        types = []
        for i in self.items:
            if i.type not in types:
                types.append(i.type)

        # Sorting the inventory by ID
        def sort(id_sort: Item):
            return id_sort.id
        i_sorted_items = sorted(self.items, key=sort)

        # This will write each type into the LaptopInventory CSV file
        for ty in types:
            # Uses file name with the Type and ending 'Inventory.csv'
            with open(f'{ty.capitalize()}Inventory.csv', 'w', newline='') as type_file:
                type_writer = csv.writer(type_file)

                for i_item in i_sorted_items:
                    if i_item.type == ty:
                        type_writer.writerow((i_item.id, i_item.manufacturer, i_item.price,
                                              i_item.date, i_item.damaged))

    # C - PastServiceDateInventory
    def pastinventory(self):
        # This is to get the current date. Used import datetime in the beginning for this
        currentdate = [
            datetime.date.today().year,
            datetime.date.today().month,
            datetime.date.today().day
        ]

        # This is going to sort the inventory by dates
        def sort(date_sort: Item):
            return conv_date(date_sort.date)

        date_sorted_items = sorted(self.items, key=sort)

        # This will write to the PastServiceDateInventory CSV file
        with open('PastServiceDateInventory.csv', 'w', newline='') as past_file:
            past_writer = csv.writer(past_file)
            for date_item in date_sorted_items:
                # This will see if the date is past the due date by comparing the item date with the current date]
                if conv_date(date_item.date) < currentdate:
                    past_writer.writerow((date_item.id, date_item.manufacturer, date_item.type,
                                          date_item.price, date_item.date, date_item.damaged))

    # D - DamagedInventory
    def damagedinventory(self):
        # Pre-sort inventory items by price
        def sort(dmg_sort: Item):
            return dmg_sort.price
        price_sorted_items = sorted(self.items, key=sort, reverse=True)  # orders the list from highest to lowest

        # Write to the DamagedInventory CSV file
        with open('DamagedInventory.csv', 'w', newline='') as dmg_file:
            dmg_writer = csv.writer(dmg_file)

            for price_item in price_sorted_items:
                if price_item.damaged == 'damaged':  # if item is damaged then the item will be written in the CSV
                    dmg_writer.writerow((price_item.id, price_item.manufacturer, price_item.type,
                                        price_item.price, price_item.date))

    # Personal method for viewing the Inventory contents
    def viewinventory(self):
        for item in self.items:
            print(item)
        print()


inventory = Inventory()

with open('ManufacturerList.csv', 'r') as ml_file:
    ml_reader = csv.reader(ml_file)

    for row in ml_reader:
        inventory.items.append(Item(int(row[0]), row[1], row[2], p_damaged=row[3]))

# Read Price List
with open('PriceList.csv', 'r') as pl_file:
    pl_reader = csv.reader(pl_file)

    for row in pl_reader:
        # Look up Item by matching id
        for t_item in inventory.items:
            if int(row[0]) == t_item.id:
                t_item.price = int(row[1])
                break

# Read Service Dates List
with open('ServiceDatesList.csv', 'r') as sdl_file:
    sdl_reader = csv.reader(sdl_file)

    for row in sdl_reader:
        # Look up Item by matching id
        for t_item in inventory.items:
            if int(row[0]) == t_item.id:
                t_item.date = row[1]
                break

inventory.fullinventory()
inventory.inventorytype()
inventory.pastinventory()
inventory.damagedinventory()
