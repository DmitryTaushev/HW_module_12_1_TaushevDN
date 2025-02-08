class RecipeView:
    def __init__(self, recipe_control):
        self.recipe_control = recipe_control


    def display_default_action(self):
        print(self.recipe_control.get_default_action())


    def display_shoe_inform_auth(self, user_role='user'):
        result = self.recipe_control.get_recipe_inform_auth(user_role)
        if result == 'Forbidden!':
            print(result)
        else:
            return self.recipe_control.get_recipe_inform()


    def display_name_recipe(self):
        return self.recipe_control.get_name_recipe()

    def display_author_recipe(self):
        return self.recipe_control.get_author_recipe()

    def display_type_recipe(self):
        return self.recipe_control.get_type_recipe()

    def display_brief_recipe(self):
        return self.recipe_control.get_brief_recipe()

    def display_ingredient(self):
        return self.recipe_control.get_ingredient()

    def display_kitchen(self):
        return self.recipe_control.get_kitchen()

    def display_link_recipe(self):
        return self.recipe_control.get_link_recipe()

    def display_recipe_inform(self):
        return self.recipe_control.get_recipe_inform()


