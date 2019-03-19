#Роботишин mykola robotyshyn
#Квочкин kvochkin vlad
class Pizza:
    def getIngredients(self):
        return self.ingredients
    def getExtraIngredients(self):
        return self.extra_ingredients
    def getTotalCost(self):
        return self.cost
    def __str__(self):
        return 'Ingredients: ' + str(self.getIngredients()) + \
               '\n'+ 'Extra Ingredients: ' + \
               str(self.getExtraIngredients()) + '\n' + \
               'Cost: ' + str(self.getTotalCost())

class Decorator(Pizza):
    def __init__(self, pizza_component):
        self.component = pizza_component

    def getIngredients(self):
        return self.component.getIngredients()

    def getExtraIngredients(self):
        return self.component.getExtraIngredients() + Pizza.getExtraIngredients(self)

    def getTotalCost(self):
        return self.component.getTotalCost() + Pizza.getTotalCost(self)

class Pepper(Decorator):
    cost = 10
    extra_ingredients = ['pepper']
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class Pineapple(Decorator):
    cost = 13
    extra_ingredients = ['pineapple']
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class Beef(Decorator):
    cost = 16
    extra_ingredients = ['beef']
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class Cheese1(Decorator):
    cost = 9
    extra_ingredients = ['cheese1']
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class Cheese2(Decorator):
    cost = 16
    extra_ingredients = ['cheese2']
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class standart(Pizza):
    ingredients = ['tomatoes in juice', 'olive oil', 'basil leaves', 'mozzarella']
    extra_ingredients = []
    cost = 35.0

somepizza = Cheese1(Cheese2(standart()))
print(somepizza)