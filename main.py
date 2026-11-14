import numpy as np
from src.data_loader import load_orders

orders = load_orders()

quantities = np.array([order["Quantity"] for order in orders])
prices = np.array([order["Unit_Price"] for order in orders])

revenue = quantities * prices

discount_rates = np.array([
    order["Discount_Rate"] for order in orders
])

net_revenue = quantities * prices * (1 - discount_rates)
cost_prices = np.array([
    order["Cost_Price"] for order in orders
])

total_cost = quantities * cost_prices
profit = net_revenue - total_cost

profit_margin = (profit / net_revenue) * 100

overall_profit_margin = (
    np.sum(profit) / np.sum(net_revenue)
) * 100

best_order_index = np.argmax(profit)
best_order = orders[best_order_index]

product_names = np.array([
    order["Product_Name"] for order in orders
])

unique_products = np.unique(product_names)

product_total_profits = []

for product in unique_products:
    product_mask = product_names == product
    total = np.sum(profit[product_mask])

    product_total_profits.append(total)

product_total_profits = np.array(product_total_profits)

best_product_index = np.argmax(product_total_profits)

print("Most Profitable Product:",
      unique_products[best_product_index])

print("Total Product Profit:",
      product_total_profits[best_product_index])

print("Best Order ID:", best_order["Order_ID"])
print("Best Product:", best_order["Product_Name"])
print("Highest Profit:", profit[best_order_index])

print("Highest Profit:", np.max(profit))
print("Best Order Index:", best_order_index)

print("Overall Profit Margin:", overall_profit_margin)

print("Profit Margin:", profit_margin)
print("Average Profit Margin:", np.mean(profit_margin))

print("Total Cost:", np.sum(total_cost))
print("Profit:", profit)
print("Total Profit:", np.sum(profit))

print("Net Revenue:", net_revenue)
print("Total Net Revenue:", np.sum(net_revenue))

print("Quantities:", quantities)
print("Prices:", prices)
print("Revenue:", revenue)
print("Total revenue:", np.sum(revenue))