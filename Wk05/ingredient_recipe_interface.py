class Ingredient(object):
    """The ingredient object that contains nutritional information"""

    def __init__(self, name, *args):
        self.name = name

        values = []
        nutrients = ['carbs', 'protein', 'fat', 'cholesterol']

        for arg in args:
            # if argument is a dict, assign it as instance attribute
            if isinstance(arg, dict):
                self.nutrition = arg
            # if argument isn't a dict, add argument to list
            else:
                values.append(arg)

        # if non-dict arguments were added to list, set them as instance attributes
        if len(values) > 0:
            self.nutrition = {}
            for nutrient, value in zip(nutrients, values):
                self.nutrition[nutrient] = value


    def __repr__(self):
        # if instance contains 'cholesterol' attribute, include it in str representation
        return 'Ingredient({0}, {1})'.format(self.name, self.nutrition)


    def get_nutrition(self):
        """Returns the nutritional information for the ingredient"""
        return (self.nutrition)
    

class Recipe(object):
    """The Recipe object containing the ingredients"""
    
    def __init__(self, name, ingredients,):
        self.name = name
        self.ingredients = ingredients
    

    def __repr__(self):
        return 'Recipe({0}, {1})'.format(self.name, self.ingredients)


    def get_nutrition(self):
        """Returns the nutritional information for the recipe"""
        nutrition = [0, 0, 0]
        carbs = 0
        protein = 0
        fat = 0
        cholesterol = 0
        nutrition_cholesterol = 0
        for amount, ingredient in self.ingredients:
            # if ingredient is a Recipe instance
            if isinstance(ingredient, Recipe):  
                ingredient = ingredient.ingredients  # update ingredient to recipe's ingredients
                for amt, ing in ingredient:
                    # print('ingredient within recipe: ', ing)
                    carbs += amt * ing.carbs
                    protein += amt * ing.protein
                    fat += amt * ing.fat
                    if hasattr(ing, 'cholesterol'):
                        cholesterol += amt * ing.cholesterol
                nutrition[0] += amount * carbs
                nutrition[1] += amount * protein
                nutrition[2] += amount * fat
                nutrition_cholesterol += amount * cholesterol
            # if ingredient is an Ingredient instance
            else:
                # print('ingredient: ', ingredient)
                nutrition[0] += amount * ingredient.carbs
                nutrition[1] += amount * ingredient.protein
                nutrition[2] += amount * ingredient.fat
                if hasattr(ingredient, 'cholesterol'):
                    nutrition_cholesterol += amount * ingredient.cholesterol

        # if cholesterol nutrition info has been supplied, append to list
        if nutrition_cholesterol > 0:  
            nutrition.append(nutrition_cholesterol)
        return nutrition


    @property  
    def nutrition(self):
        info = self.get_nutrition()
        nutrients = {}
        nutrients['carbs'] = info[0]
        nutrients['protein'] = info[1]
        nutrients['fat'] = info[2]
        # if info consists of more than carbs, protein, fat, add to nutrients dict
        if len(info) > 3:  
            nutrients['cholesterol'] = info[3]
        return nutrients



