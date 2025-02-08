from model import RecipeModel
from controller import RecipeController
from view import RecipeView

if __name__ == '__main__':
    recipe_model = RecipeModel('Борщ',"RussianFood","Первое","Национальное украинское блюдо,суп","Говядина,Свёкла,Картофель,Капуста белокочанная,Морковь,Лук репчатый,Томатная паста,Масло растительное,Уксус,Лавровый лист,Перец чёрный горошком,Соль,Вода,Зелень,Сметана","Украинская","https://www.russianfood.com/recipes/recipe.php?rid=107392")
    recipe_control = RecipeController(recipe_model)
    recipe_view = RecipeView(recipe_control)

    recipe_view.display_default_action()
    print(recipe_view.display_shoe_inform_auth('user'))
    recipe_view.display_name_recipe()
    recipe_view.display_author_recipe()
    recipe_view.display_type_recipe()
    recipe_view.display_brief_recipe()
    recipe_view.display_ingredient()
    recipe_view.display_kitchen()
    recipe_view.display_link_recipe()
    print(recipe_view.display_recipe_inform())
    print()

    recipe_model = RecipeModel("Паста Карбонара","Олег Михненков","Второе","Итальянское блюдо из макарон и бекона","Спагетти,Оливковое масло,Чеснок,Ветчина,Яичный желток,Тертый сыр пармезан,Сливки 10%-ные,Соль,Молотый черный перец","Итальянская","https://eda.ru/recepty/pasta-picca/pasta-karbonara-pasta-alla-carbonara-50865")
    recipe_control = RecipeController(recipe_model)
    recipe_view = RecipeView(recipe_control)

    recipe_view.display_default_action()
    print(recipe_view.display_shoe_inform_auth('user'))
    recipe_view.display_name_recipe()
    recipe_view.display_author_recipe()
    recipe_view.display_type_recipe()
    recipe_view.display_brief_recipe()
    recipe_view.display_ingredient()
    recipe_view.display_kitchen()
    recipe_view.display_link_recipe()
    print(recipe_view.display_recipe_inform())
    print()