import json
from Cellphone import Cellphone


class InventoryManager:
    def __init__(self):
        self.phones = {}

    def add_phone(self, phone):
        self.phones[phone.model] = phone

    def remove_phone(self, model):
        if model in self.phones:
            del self.phones[model]

    def update_quantity(self, model, qty):
        if model in self.phones:
            self.phones[model].stock_quantity = qty

    def search_by_model(self, model):
        return self.phones.get(model)

    def total_stock_value(self):
        total = 0
        for phone in self.phones.values():
            total += phone.retail_price * phone.stock_quantity
        return total

    def count_by_brand(self):
        result = {}
        for phone in self.phones.values():
            result[phone.brand] = result.get(phone.brand, 0) + phone.stock_quantity
        return result

    def export_json(self, filename):
        with open(filename, "w") as f:
            json.dump(
                {model: phone.to_dict() for model, phone in self.phones.items()},
                f,
                indent=4
            )

    def import_json(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            for model, details in data.items():
                self.phones[model] = Cellphone(**details)
