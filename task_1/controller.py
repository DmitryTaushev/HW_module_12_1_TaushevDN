class ShoeController:

    def __init__(self,shoe_model):
        self.shoe_model = shoe_model

    def get_default_action(self):
        return "Добро пожаловать на главную страницу!"

    def get_shoe_inform_auth(self, user_role='user'):
        if user_role in ['admin', 'user']:
            if self.shoe_model.shoe_inform():
                return self.shoe_model.shoe_inform()
            return None
        return 'Forbidden!'

    def get_shoe_type(self):
        data = self.shoe_model.shoe_inform()
        if data:
            for key in data:
                if key == 'Тип':
                    print(data['Тип'])

    def get_shoe_kind(self):
        data = self.shoe_model.shoe_inform()
        if data:
            for key in data:
                if key == 'Вид':
                    print(data['Вид'])

    def get_color(self):
        data = self.shoe_model.shoe_inform()
        if data:
            for key in data:
                if key == 'Цвет':
                    print(data['Цвет'])

    def get_price(self):
        data = self.shoe_model.shoe_inform()
        if data:
            for key in data:
                if key == 'Цена':
                    print(data['Цена'])

    def get_manufacture(self):
        data = self.shoe_model.shoe_inform()
        if data:
            for key in data:
                if key == 'Производитель':
                    print(data['Производитель'])

    def get_size(self):
        data = self.shoe_model.shoe_inform()
        if data:
            for key in data:
                if key == 'Размер':
                    print(data['Размер'])

    def get_shoe_inform(self):
        return self.shoe_model.shoe_inform()


