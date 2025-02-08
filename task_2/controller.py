class RecipeController:

    def __init__(self,recipe_model):
        self.recipe_model = recipe_model

    def get_default_action(self):
        return "Добро пожаловать на главную страницу!"

    def get_recipe_inform_auth(self, user_role='user'):
        if user_role in ['admin', 'user']:
            if self.recipe_model.recipe_inform():
                return self.recipe_model.recipe_inform()
            return None
        return 'Forbidden!'

    def get_name_recipe(self):
        data = self.recipe_model.recipe_inform()
        if data:
            for key in data:
                if key == 'Название рецепта':
                    print(data['Название рецепта'])

    def get_author_recipe(self):
        data = self.recipe_model.recipe_inform()
        if data:
            for key in data:
                if key == 'Автор рецепта':
                    print(data['Автор рецепта'])

    def get_type_recipe(self):
        data = self.recipe_model.recipe_inform()
        if data:
            for key in data:
                if key == 'Тип рецепта':
                    print(data['Тип рецепта'])

    def get_brief_recipe(self):
        data = self.recipe_model.recipe_inform()
        if data:
            for key in data:
                if key == 'Краткое описание':
                    print(data['Краткое описание'])

    def get_ingredient(self):
        data = self.recipe_model.recipe_inform()
        if data:
            for key in data:
                if key == 'Ингредиенты':
                    print(data['Ингредиенты'])

    def get_kitchen(self):
        data = self.recipe_model.recipe_inform()
        if data:
            for key in data:
                if key == 'Кухня':
                    print(data['Кухня'])

    def get_link_recipe(self):
        data = self.recipe_model.recipe_inform()
        if data:
            for key in data:
                if key == 'Ссылка':
                    print(data['Ссылка'])

    def get_recipe_inform(self):
        return self.recipe_model.recipe_inform()


