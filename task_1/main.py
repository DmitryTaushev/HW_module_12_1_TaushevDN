from model import ShoeModel
from controller import ShoeController
from view import ShoeView

if __name__ == '__main__':
    shoe_model = ShoeModel('Мужские',"Кросовки","Белый","10000","Adidas","45")
    shoe_control = ShoeController(shoe_model)
    shoe_view = ShoeView(shoe_control)

    shoe_view.display_default_action()
    print(shoe_view.display_shoe_inform_auth('user'))
    shoe_view.display_shoe_type()
    shoe_view.display_shoe_kind()
    shoe_view.display_color()
    shoe_view.display_price()
    shoe_view.display_manufacture()
    shoe_view.display_size()
    print(shoe_view.display_shoe_inform())
    print()

    shoe_model = ShoeModel("Женские","Туфли","Красный","15000","Gucci","36")
    shoe_control = ShoeController(shoe_model)
    shoe_view = ShoeView(shoe_control)

    shoe_view.display_default_action()
    print(shoe_view.display_shoe_inform_auth('user'))
    shoe_view.display_shoe_type()
    shoe_view.display_shoe_kind()
    shoe_view.display_color()
    shoe_view.display_price()
    shoe_view.display_manufacture()
    shoe_view.display_size()
    print(shoe_view.display_shoe_inform())
    print()