class ShoeModel:
    def __init__(self, shoe_type, shoe_kind, color, price, manufacture, size):
        self.shoe_type = shoe_type
        self.shoe_kind = shoe_kind
        self.color = color
        self.price = price
        self.manufacture = manufacture
        self.size = size

    def get_shoe_type(self):
        return self.shoe_type

    def get_shoe_kind(self):
        return self.shoe_kind

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def get_manufacturer(self):
        return self.manufacture

    def get_size(self):
        return self.size

    def data_shoe(self):
        data_shoe = {}
        data_shoe['Тип'] = self.shoe_type
        data_shoe['Вид'] = self.shoe_kind
        data_shoe['Цвет'] = self.color
        data_shoe['Цена'] = self.price
        data_shoe['Производитель'] = self.manufacture
        data_shoe['Размер'] = self.size
        return data_shoe

    def shoe_inform(self):
        return self.data_shoe()


