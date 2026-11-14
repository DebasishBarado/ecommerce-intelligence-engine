
import csv
from pathlib import Path

def load_orders():
    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / "raw" / "orders.csv"

    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        orders = list(reader)
    for order in orders:
        order["Quantity"] = int(order["Quantity"])
        order["Unit_Price"] = float(order["Unit_Price"])
        order["Cost_Price"] = float(order["Cost_Price"])
        order["Discount_Rate"] = float(order["Discount_Rate"])

    return orders
