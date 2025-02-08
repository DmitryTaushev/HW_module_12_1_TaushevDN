class RecipeModel:
    def __init__(self, name_recipe, author_recipe, type_recipe, brief_recipe,ingredient, kitchen,link_recipe):
        self.name_recipe = name_recipe
        self.author_recipe = author_recipe
        self.type_recipe = type_recipe
        self.brief_recipe = brief_recipe
        self.ingredient = ingredient
        self.kitchen = kitchen
        self.link_recipe = link_recipe

    def get_name_recipe(self):
        return self.name_recipe

    def get_author_recipe(self):
        return self.author_recipe

    def get_type_recipe(self):
        return self.type_recipe

    def get_brief_recipe(self):
        return self.brief_recipe

    def get_ingredient(self):
        return self.ingredient

    def get_kitchen(self):
        return self.kitchen

    def get_link(self):
        return self.link_recipe

    def data_recipe(self):
        data_recipe = {}
        data_recipe['Название рецепта'] = self.name_recipe
        data_recipe['Автор рецепта'] = self.author_recipe
        data_recipe['Тип рецепта'] = self.type_recipe
        data_recipe['Краткое описание'] = self.brief_recipe
        data_recipe['Ингредиенты'] = self.ingredient
        data_recipe['Кухня'] = self.kitchen
        data_recipe['Ссылка'] = self.link_recipe
        return data_recipe

    def recipe_inform(self):
        return self.data_recipe()


