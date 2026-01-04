class Cellphone:
    def __init__(self, brand, model, import_date, supplier,
                 purchase_price, retail_price, stock_quantity,
                 condition, specifications, warranty_months,
                 features, marketing_tags, notes):

        self.brand = brand
        self.model = model
        self.import_date = import_date
        self.supplier = supplier
        self.purchase_price = purchase_price
        self.retail_price = retail_price
        self.stock_quantity = stock_quantity
        self.condition = condition
        self.specifications = specifications
        self.warranty_months = warranty_months
        self.features = features
        self.marketing_tags = marketing_tags
        self.notes = notes

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f"{self.brand} {self.model} | Qty: {self.stock_quantity}"
