import os
import re

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Read the input file
rules, orders = set(), []
use_example = False

rules_file = "20241205_rules_example.txt" if use_example else "20241205_rules.txt"
orders_file = "20241205_orders_example.txt" if use_example else "20241205_orders.txt"

with open(rules_file, "r") as file:
    for line in file:
        rules.add(tuple(line.strip().split("|")))

with open(orders_file, "r") as file:
    for line in file:
        orders.append(line.strip().split(","))

# print(rules)
# print(orders)

# 2. The rules are tuples of two string values. The first string is supposed to be in front of the second string in the order.
# The goal is to find the orders where the sequence of strings are consistent with the rules.
# We can sort each of the orders based upon all the rules we have and see if the order is not the same as the original order, if so, it is a invalid order and we return the sorted order.
# Use bubble sort to sort the orders based upon the rules.
def bubble_sort_validate(order, rules):
    order_str = ",".join(order)
    for i in range(len(order)):
        for j in range(i+1, len(order)):
            if (order[j], order[i]) in rules:
                order[i], order[j] = order[j], order[i]
    return order_str == ",".join(order), order

# 3. Validate all the orders based upon the rules
invalid_orders = []
for order in orders:
    is_valid, sorted_order = bubble_sort_validate(order, rules)
    if not is_valid:
        invalid_orders.append(sorted_order)

# print(invalid_orders)

# 4. Find the middle value of each of the valid orders, convert it to a number and return the sum of all the numbers in the valid orders
middle_values = [invalid_orders[len(invalid_orders) // 2] for invalid_orders in invalid_orders]
print(sum(map(int, middle_values)))
