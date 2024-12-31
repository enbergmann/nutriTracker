class Food:
    def __init__(self, name, ingredients = [], nutrients = {})
        self.name = name
        self.ingredients = ingredients
        if not nutrients and ingredients
            self.nutrients = get_nutrients(ingredients)
        elif nutrients
            self.nutrients = nutrients
        else
            # error, not a food possible without ingredients or nutrients

    @classmethod
    def loadFoods(cls, names) 
        # Get names of foods, load from the database (else set everything to 0
        # and warn about non-existing ones), and return list of the Food objects
        # for all list items
        processedNames = processNames(name)
        return cls(processedNames)

    @classmethod
    def createBaseFood(cls, name, nutrients)
        # TODO

    @classmethod
    def createFood(cls, name, ingredients)
        # TODO
        
