
# 4. Advanced Searching
# Feature: Support partial matching or filters (e.g., search by price range, quantity).
# Implementation Steps:
# Add parameters for filters (e.g., min_price, max_price).
# Apply these filters when searching the inventory.
# 5. Generate Reports
# Feature: Create summary reports, such as:
# Most expensive item.
# Total inventory value by category (if categories exist).
# Low-stock items (below a threshold).
# Implementation Steps:
# Add analysis methods to compute specific metrics.
# Optionally, export reports as a file.
import csv
import json
import re
class Item:
    def __init__(self, item, qty, price):
        self.item = item
        self.qty = qty
        self.price = price
    
    def remove_item(self, qty):
        self.qty -= qty

    def update_qty(self,qty):
            self.qty = qty
    
    def update_price(self, price):
            self.price = price
    
    def total_value(self):
        return self.qty * self.price
    
    def __str__(self):
        return (f"Item {self.item} QTY:{self.qty} PRICE: {self.price},"
        f"Total value of {self.item} is {self.qty * self.price}")
    
    def get_key_value_pair(self):
        return {
            "Item": self.item,
            "QTY": self.qty,
            "PRICE": self.price,
            "TOTAL": self.qty * self.price
        }
    

class Inventory:
    def __init__(self):
        self.inventory_list = {}
    
    def bulk_update_items(self, update_inventory_list):
        for i in update_inventory_list:
            self.update_items(*i)

    def update_items(self, item, qty,price):
        if item in self.inventory_list:
            self.inventory_list[item].update_qty(qty)
            self.inventory_list[item].update_price(price)
        else:
            self.inventory_list[item] = Item(item,qty,price)
    
    def bulk_remove_items(self, remove_inventory_list):
        for i in remove_inventory_list:
            self.remove_item(i[0], i[1])

    def remove_item(self, item, qty):
        if item in self.inventory_list and self.inventory_list[item].qty >= qty:
            self.inventory_list[item].remove_item(qty)
            if self.inventory_list[item].qty == 0:
                del self.inventory_list[item]
        else:
            print(f"Cannot remove {qty} units of {item}. Not enough stock or item not found.")
    
    def inventory_details(self):
        return [str(i) for i in self.inventory_list.values()]
    
    def inventory_json(self):
        return [ i.get_key_value_pair() for i in self.inventory_list.values()]
    
    def export_inventory_details_to_json(self):
        with open("inventory.json","w") as fh:
            fh.write(json.dumps(self.inventory_json()))

    def import_inventory_details_from_json(self):
        with open("inventory.json", "r") as fh:
            json_data = json.load(fh)
        self.bulk_update_items([list(i.values())[:3] for i in json_data])

    def export_inventory_details_to_csv(self):
        with open("inventory.csv", "w") as fh:
            csv_writer = csv.DictWriter(fh,["Item", "QTY", "PRICE", "TOTAL"] )
            csv_writer.writeheader()
            csv_writer.writerows(self.inventory_json())
    
    def import_inventory_details_from_csv(self):
        with open("inventory.csv", "r") as fh:
            csv_reader = csv.DictReader(fh)
            self.bulk_update_items([[i["Item"], int(i["QTY"]), int(i["PRICE"])] for i in csv_reader])
    
    def search_item(self, item):
        if item in self.inventory_list:
            return str(self.inventory_list[item])
        print(f"Item {item} not in inventory")
    
    def qty_filter(self):
        pass

    def min_price_filter(self):
        pass

    def max_price_filter(self):
        pass

    def partial_match_search(self,pat):
        match_data = []
        for i in self.inventory_details():
            if re.search(pat, i, flags=re.I):
                match_data.append(i)
        return match_data 

if __name__ == "__main__":
    # Create inventory
    inventory = Inventory()
    # Display inventory detaike
    # ls
    # print("\n--- Inventory Details ---")
    # for detail in inventory.inventory_details():
    #     print(detail)

    # # Search for an item
    # print("\n--- Search for Items ---")
    # print(inventory.search_item("Laptop"))
    # print(inventory.search_item("Monitor"))

    # # Remove items
    # print("\n--- Remove Items ---")
    # inventory.bulk_remove_items([["Mouse", 10], ["Keyboard", 10]])
    # print(inventory.search_item("Mouse"))
    # inventory.bulk_remove_items([["Mouse", 40]])  # Should remove Mouse completely

    # # Try removing an item not in inventory
    # inventory.remove_item("Monitor", 5)


    # # Display final inventory details
    # print("\n--- Final Inventory Details ---")
    # for detail in inventory.inventory_details():
    #     print(detail)

    
    # inventory.export_inventory_details_to_csv()
    inventory.import_inventory_details_from_json()

    print("\n--- Final Inventory Details ---")
    for detail in inventory.inventory_details():
        print(detail)
    
    inventory.export_inventory_details_to_json()
    inventory.import_inventory_details_from_csv()

    print("\n--- Final Inventory Details ---")
    for detail in inventory.inventory_details():
        print(detail)
        
    pat=input("\n--Enter item to search--\n")
    if inventory.partial_match_search(pat):
        for detail in inventory.partial_match_search(pat):
            print(detail)
    else:
        print("No matching resultZ")