from Cellphone import Cellphone
from inventory_manager import InventoryManager
import json
import csv
import pickle


def add_new_phone(manager):
    """Function to add a new phone to inventory"""
    print("\n=== Add New Phone ===")

    brand = input("Enter brand: ")
    model = input("Enter model: ")
    import_date = input("Enter import date (YYYY-MM-DD): ")
    supplier = input("Enter supplier: ")
    purchase_price = float(input("Enter purchase price: "))
    retail_price = float(input("Enter retail price: "))
    stock_quantity = int(input("Enter stock quantity: "))
    condition = input("Enter condition (New/Used/Refurbished): ")
    warranty_months = int(input("Enter warranty months: "))

    # Specifications
    print("\nEnter Specifications:")
    cpu = input("  CPU: ")
    ram = input("  RAM: ")
    storage = input("  Storage: ")
    battery = input("  Battery: ")

    specifications = {
        "cpu": cpu,
        "ram": ram,
        "storage": storage,
        "battery": battery
    }

    # Features
    features_input = input("\nEnter features (comma-separated, e.g., 5G,NFC,Wireless Charging): ")
    features = [f.strip() for f in features_input.split(",") if f.strip()]

    # Marketing tags
    tags_input = input("Enter marketing tags (comma-separated, e.g., Flagship,Premium): ")
    marketing_tags = [t.strip() for t in tags_input.split(",") if t.strip()]

    notes = input("Enter notes: ")

    # Create and add the phone
    new_phone = Cellphone(
        brand=brand,
        model=model,
        import_date=import_date,
        supplier=supplier,
        purchase_price=purchase_price,
        retail_price=retail_price,
        stock_quantity=stock_quantity,
        condition=condition,
        specifications=specifications,
        warranty_months=warranty_months,
        features=features,
        marketing_tags=marketing_tags,
        notes=notes
    )

    manager.add_phone(new_phone)
    print(f"\n✓ Phone '{model}' added successfully!")


def remove_phone(manager):
    """Remove a phone from inventory"""
    model_input = input("\nEnter model number to remove: ")
    phone = manager.search_by_model(model_input)

    if phone:
        print(f"\nFound: {phone.brand} {phone.model} (Stock: {phone.stock_quantity})")
        confirm = input("Are you sure you want to remove this phone? (yes/no): ")

        if confirm.lower() in ['yes', 'y']:
            manager.remove_phone(model_input)
            print(f"\n✓ Phone '{model_input}' removed successfully!")
        else:
            print("\n✗ Removal cancelled")
    else:
        print(f"\n✗ Phone model '{model_input}' not found in inventory")


def update_phone(manager):
    """Update phone attributes"""
    model_input = input("\nEnter model number to update: ")
    phone = manager.search_by_model(model_input)

    if not phone:
        print(f"\n✗ Phone model '{model_input}' not found in inventory")
        return

    print(f"\nFound: {phone.brand} {phone.model}")
    print("\n" + "=" * 40)
    print("What would you like to update?")
    print("=" * 40)
    print("1. Purchase Price")
    print("2. Retail Price")
    print("3. Stock Quantity")
    print("4. Condition")
    print("5. Warranty Months")
    print("6. All of the above")
    print("7. Cancel")
    print("=" * 40)

    update_choice = input("\nEnter your choice (1-7): ")

    if update_choice == "1":
        new_price = float(input(f"Current Purchase Price: {phone.purchase_price}\nEnter new purchase price: "))
        phone.purchase_price = new_price
        print("\n✓ Purchase price updated successfully!")

    elif update_choice == "2":
        new_price = float(input(f"Current Retail Price: {phone.retail_price}\nEnter new retail price: "))
        phone.retail_price = new_price
        print("\n✓ Retail price updated successfully!")

    elif update_choice == "3":
        new_qty = int(input(f"Current Stock Quantity: {phone.stock_quantity}\nEnter new stock quantity: "))
        phone.stock_quantity = new_qty
        print("\n✓ Stock quantity updated successfully!")

    elif update_choice == "4":
        new_condition = input(f"Current Condition: {phone.condition}\nEnter new condition (New/Used/Refurbished): ")
        phone.condition = new_condition
        print("\n✓ Condition updated successfully!")

    elif update_choice == "5":
        new_warranty = int(input(f"Current Warranty: {phone.warranty_months} months\nEnter new warranty months: "))
        phone.warranty_months = new_warranty
        print("\n✓ Warranty updated successfully!")

    elif update_choice == "6":
        print("\nUpdating all attributes...")
        phone.purchase_price = float(
            input(f"Current Purchase Price: {phone.purchase_price}\nEnter new purchase price: "))
        phone.retail_price = float(input(f"Current Retail Price: {phone.retail_price}\nEnter new retail price: "))
        phone.stock_quantity = int(input(f"Current Stock Quantity: {phone.stock_quantity}\nEnter new stock quantity: "))
        phone.condition = input(f"Current Condition: {phone.condition}\nEnter new condition (New/Used/Refurbished): ")
        phone.warranty_months = int(
            input(f"Current Warranty: {phone.warranty_months} months\nEnter new warranty months: "))
        print("\n✓ All attributes updated successfully!")

    elif update_choice == "7":
        print("\n✗ Update cancelled")
    else:
        print("\n✗ Invalid choice")


def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 40)
    print("CELL PHONE INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add new phone")
    print("2. Search phone by model")
    print("3. View all phones")
    print("4. Remove phone by model")
    print("5. Update phone attributes")
    print("6. Aggregate queries & reports")
    print("7. Export/Import data")
    print("8. Exit")
    print("=" * 40)


def search_phone(manager):
    """Search for a phone by model"""
    model_input = input("\nEnter model number to view details: ")
    phone = manager.search_by_model(model_input)

    if phone:
        print("\n" + "=" * 40)
        print("PHONE DETAILS")
        print("=" * 40)
        print(f"Brand: {phone.brand}")
        print(f"Model: {phone.model}")
        print(f"Import Date: {phone.import_date}")
        print(f"Supplier: {phone.supplier}")
        print(f"Purchase Price: {phone.purchase_price}")
        print(f"Retail Price: {phone.retail_price}")
        print(f"Stock Quantity: {phone.stock_quantity}")
        print(f"Condition: {phone.condition}")
        print(f"Specifications: {phone.specifications}")
        print(f"Warranty (months): {phone.warranty_months}")
        print(f"Features: {', '.join(phone.features)}")
        print(f"Marketing Tags: {', '.join(phone.marketing_tags)}")
        print(f"Notes: {phone.notes}")
        print("=" * 40)
    else:
        print("\n✗ Phone not found")


def view_all_phones(manager):
    """Display all phones in inventory"""
    if not manager.phones:
        print("\n✗ No phones in inventory")
        return

    print("\n" + "=" * 40)
    print("ALL PHONES IN INVENTORY")
    print("=" * 40)
    for model, phone in manager.phones.items():
        print(f"• {phone.brand} {phone.model} | Stock: {phone.stock_quantity} | Price: {phone.retail_price}")
    print("=" * 40)


def aggregate_queries_menu(manager):
    """Display aggregate queries submenu"""
    print("\n" + "=" * 40)
    print("AGGREGATE QUERIES")
    print("=" * 40)
    print("1. Total stock value")
    print("2. Count by brand")
    print("3. Average retail price")
    print("4. Total units in stock")
    print("5. Phones by condition")
    print("6. Low stock alert (quantity < 5)")
    print("7. Price range analysis")
    print("8. Back to main menu")
    print("=" * 40)

    choice = input("\nEnter your choice (1-8): ")

    if choice == "1":
        total = manager.total_stock_value()
        print(f"\n💰 Total Stock Value: {total:,.2f}")

    elif choice == "2":
        brand_count = manager.count_by_brand()
        print("\n" + "=" * 40)
        print("PHONES BY BRAND")
        print("=" * 40)
        for brand, count in brand_count.items():
            print(f"• {brand}: {count} units")
        print("=" * 40)

    elif choice == "3":
        if manager.phones:
            avg_price = sum(phone.retail_price for phone in manager.phones.values()) / len(manager.phones)
            print(f"\n📊 Average Retail Price: {avg_price:,.2f}")
        else:
            print("\n✗ No phones in inventory")

    elif choice == "4":
        total_units = sum(phone.stock_quantity for phone in manager.phones.values())
        print(f"\n📦 Total Units in Stock: {total_units}")

    elif choice == "5":
        condition_count = {}
        for phone in manager.phones.values():
            condition_count[phone.condition] = condition_count.get(phone.condition, 0) + phone.stock_quantity
        print("\n" + "=" * 40)
        print("PHONES BY CONDITION")
        print("=" * 40)
        for condition, count in condition_count.items():
            print(f"• {condition}: {count} units")
        print("=" * 40)

    elif choice == "6":
        low_stock = [phone for phone in manager.phones.values() if phone.stock_quantity < 5]
        if low_stock:
            print("\n" + "=" * 40)
            print("⚠️  LOW STOCK ALERT")
            print("=" * 40)
            for phone in low_stock:
                print(f"• {phone.brand} {phone.model} - Only {phone.stock_quantity} units left!")
            print("=" * 40)
        else:
            print("\n✓ All phones have sufficient stock")

    elif choice == "7":
        if manager.phones:
            prices = [phone.retail_price for phone in manager.phones.values()]
            print("\n" + "=" * 40)
            print("PRICE RANGE ANALYSIS")
            print("=" * 40)
            print(f"• Minimum Price: {min(prices):,.2f}")
            print(f"• Maximum Price: {max(prices):,.2f}")
            print(f"• Average Price: {sum(prices) / len(prices):,.2f}")
            print("=" * 40)
        else:
            print("\n✗ No phones in inventory")

    elif choice == "8":
        return
    else:
        print("\n✗ Invalid choice")


def export_import_menu(manager):
    """Display export/import submenu"""
    print("\n" + "=" * 40)
    print("EXPORT/IMPORT DATA")
    print("=" * 40)
    print("1. Export to JSON")
    print("2. Import from JSON")
    print("3. Export to CSV")
    print("4. Import from CSV")
    print("5. Export to Binary (Pickle)")
    print("6. Import from Binary (Pickle)")
    print("7. Back to main menu")
    print("=" * 40)

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        filename = input("Enter filename (e.g., phones.json): ")
        if not filename.endswith('.json'):
            filename += '.json'
        manager.export_json(filename)
        print(f"\n✓ Data exported to {filename}")

    elif choice == "2":
        filename = input("Enter filename to import (e.g., phones.json): ")
        try:
            manager.import_json(filename)
            print(f"\n✓ Data imported from {filename}")
        except FileNotFoundError:
            print(f"\n✗ File '{filename}' not found")
        except json.JSONDecodeError:
            print(f"\n✗ Invalid JSON file")

    elif choice == "3":
        filename = input("Enter filename (e.g., phones.csv): ")
        if not filename.endswith('.csv'):
            filename += '.csv'
        export_to_csv(manager, filename)
        print(f"\n✓ Data exported to {filename}")

    elif choice == "4":
        filename = input("Enter filename to import (e.g., phones.csv): ")
        try:
            import_from_csv(manager, filename)
            print(f"\n✓ Data imported from {filename}")
        except FileNotFoundError:
            print(f"\n✗ File '{filename}' not found")
        except Exception as e:
            print(f"\n✗ Error importing CSV: {e}")

    elif choice == "5":
        filename = input("Enter filename (e.g., phones.pkl): ")
        if not filename.endswith('.pkl'):
            filename += '.pkl'
        export_to_binary(manager, filename)
        print(f"\n✓ Data exported to {filename}")

    elif choice == "6":
        filename = input("Enter filename to import (e.g., phones.pkl): ")
        try:
            import_from_binary(manager, filename)
            print(f"\n✓ Data imported from {filename}")
        except FileNotFoundError:
            print(f"\n✗ File '{filename}' not found")
        except Exception as e:
            print(f"\n✗ Error importing binary file: {e}")

    elif choice == "7":
        return
    else:
        print("\n✗ Invalid choice")


def export_to_csv(manager, filename):
    """Export inventory to CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        if not manager.phones:
            return

        # Get all field names from first phone
        fieldnames = ['brand', 'model', 'import_date', 'supplier', 'purchase_price',
                      'retail_price', 'stock_quantity', 'condition', 'warranty_months',
                      'features', 'marketing_tags', 'notes', 'specifications']

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for phone in manager.phones.values():
            row = phone.to_dict()
            # Convert lists and dicts to strings for CSV
            row['features'] = ','.join(row['features']) if row['features'] else ''
            row['marketing_tags'] = ','.join(row['marketing_tags']) if row['marketing_tags'] else ''
            row['specifications'] = str(row['specifications'])
            writer.writerow(row)


def import_from_csv(manager, filename):
    """Import inventory from CSV file"""
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert string values back to appropriate types
            row['purchase_price'] = float(row['purchase_price'])
            row['retail_price'] = float(row['retail_price'])
            row['stock_quantity'] = int(row['stock_quantity'])
            row['warranty_months'] = int(row['warranty_months'])
            row['features'] = row['features'].split(',') if row['features'] else []
            row['marketing_tags'] = row['marketing_tags'].split(',') if row['marketing_tags'] else []
            row['specifications'] = eval(row['specifications'])  # Convert string back to dict

            phone = Cellphone(**row)
            manager.add_phone(phone)


def export_to_binary(manager, filename):
    """Export inventory to binary file using pickle"""
    with open(filename, 'wb') as f:
        pickle.dump(manager.phones, f)


def import_from_binary(manager, filename):
    """Import inventory from binary file using pickle"""
    with open(filename, 'rb') as f:
        manager.phones = pickle.load(f)


# Initialize manager with sample data
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

# Main program loop
while True:
    display_menu()
    choice = input("\nEnter your choice (1-8): ")

    if choice == "1":
        add_new_phone(manager)
    elif choice == "2":
        search_phone(manager)
    elif choice == "3":
        view_all_phones(manager)
    elif choice == "4":
        remove_phone(manager)
    elif choice == "5":
        update_phone(manager)
    elif choice == "6":
        aggregate_queries_menu(manager)
    elif choice == "7":
        export_import_menu(manager)
    elif choice == "8":
        print("\nThank you for using the system. Goodbye!")
        break
    else:
        print("\n✗ Invalid choice. Please try again.")