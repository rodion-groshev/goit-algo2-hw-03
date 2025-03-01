from timeit import timeit
from BTrees.OOBTree import OOBTree
import csv

tree = OOBTree()
dict_store = {}


def add_item_to_tree(item):
    tree.update(item)


def add_item_to_dict(item):
    dict_store.update(item)


with open("generated_items_data.csv") as file:
    data = csv.DictReader(file)
    for item in data:
        item_data = {
            item["ID"]: {
                "Name": item["Name"],
                "Category": item["Category"],
                "Price": float(item["Price"]),
            }
        }
        add_item_to_tree(item_data)
        add_item_to_dict(item_data)


def range_query_tree(tree, min_price, max_price):
    return [
        item for key, item in tree.items() if min_price <= item["Price"] <= max_price
    ]


def range_query_dict(items, min_price, max_price):
    return [item for item in items.values() if min_price <= item["Price"] <= max_price]


min_price = 0
max_price = 50

time_tree = timeit(lambda: range_query_tree(tree, min_price, max_price), number=100)
time_dict = timeit(
    lambda: range_query_dict(dict_store, min_price, max_price), number=100
)

avg_time_tree = time_tree / 100
avg_time_dict = time_dict / 100

print(f"Total range_query time for OOBTree {time_tree:.6f} seconds")
print(f"Average range_query time for OOBTree {avg_time_tree:.6f} seconds\n")

print(f"Total range_query time for Dict: {time_dict:.6f} seconds")
print(f"Average range_query time for Dict: {avg_time_dict:.6f} seconds")
