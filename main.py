from Cellphone import Cellphone
from inventory_manager import InventoryManager

manager = InventoryManager()

phone1 = Cellphone(
    brand="Samsung",
    model="S23",
    import_date="2025-01-01",
    supplier="ABC Imports",
    purchase_price=600,
    retail_price=850,
    stock_quantity=10,
    condition="New",
    specifications={
        "cpu": "Snapdragon",
        "ram": "8GB",
        "storage": "256GB",
        "battery": "3900mAh"
    },
    warranty_months=24,
    features=["5G", "NFC"],
    marketing_tags=["Flagship", "Premium"],
    notes="No issues"
)
phone2 = Cellphone(
    brand="iphone",
    model="i17",
    import_date="2025-12-01",
    supplier="ABC Imports",
    purchase_price=227500,
    retail_price=276250,
    stock_quantity=8,
    condition="New",
    specifications={
        "cpu": "Snapdragon",
        "ram": "8GB",
        "storage": "256GB",
        "battery": "3900mAh"
    },
    warranty_months=24,
    features=["5G", "NFC"],
    marketing_tags=["Flagship", "Premium"],
    notes="No issues"
)

manager.add_phone(phone1)
manager.add_phone(phone2)

model_input = input("\nEnter model number to view details: ")

phone = manager.search_by_model(model_input)

if phone:
    print("\nPhone Details")
    print("-------------")
    print("Brand:", phone.brand)
    print("Model:", phone.model)
    print("Retail Price:", phone.retail_price)
    print("Stock Quantity:", phone.stock_quantity)
    print("Condition:", phone.condition)
    print("Specifications:", phone.specifications)
    print("Warranty (months):", phone.warranty_months)
else:
    print("Phone not found")
