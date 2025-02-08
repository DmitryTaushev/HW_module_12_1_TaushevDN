class ShoeView:
    def __init__(self, shoe_control):
        self.shoe_control = shoe_control


    def display_default_action(self):
        print(self.shoe_control.get_default_action())


    def display_shoe_inform_auth(self, user_role='user'):
        result = self.shoe_control.get_shoe_inform_auth(user_role)
        if result == 'Forbidden!':
            print(result)
        else:
            return self.shoe_control.get_shoe_inform()


    def display_shoe_type(self):
        return self.shoe_control.get_shoe_type()

    def display_shoe_kind(self):
        return self.shoe_control.get_shoe_kind()

    def display_color(self):
        return self.shoe_control.get_color()

    def display_price(self):
        return self.shoe_control.get_price()

    def display_manufacture(self):
        return self.shoe_control.get_manufacture()

    def display_size(self):
        return self.shoe_control.get_size()

    def display_shoe_inform(self):
        return self.shoe_control.get_shoe_inform()


