""" Objects models file.

    Edit the class definitions to make the tests pass.
"""


class Dessert(object):
    """Makes a new dessert"""
    def __init__(self, price, calories=None):
        if calories is None:
            self.calories = None
        self.price = price
        self.calories = calories
        # Edit me!
        # You need to be able to initialize a Dessert object with arguments:
        # price - required
        # calories - optional

        # This should set the object's price and calories, accessible by
        # .price and .calories respectively.
        # pass

    # Add a calories_per_dollar method that returns the calories per dollar
    # for the dessert.

    def calories_per_dollar(self):
        if self.calories is None:
            return None
        return self.calories/self.price

    # Define a method is_a_cake on Dessert that returns False

    def is_a_cake(self):
        return False

# new_dessert = Dessert(10)


class Cake(Dessert):

    def __init__(self, kind):
        self.kind = kind
        # Edit me!
        # Cakes all cost the same amount and have the same calories, so their
        # price and calories can be set at the class-level, not during init.
        # However, we need to be able to tell cakes apart. Accept argument:
        # kind - required

        # pass
    price = 5
    calories = 200
    # Define a method is_a_cake on Cake that returns True
    # (This will override the one on Dessert)

    def is_a_cake(self):
        return True


class Menu(object):

    def __init__(self, items):
        self.items = items

    def desserts(self):
        # Return only the items in self.items which are desserts
        desserts = []
        for item in self.items:
            if isinstance(item, Dessert):
                desserts.append(item)
        return desserts

    def cakes(self):
        cakes = []
        for item in self.items:
            if isinstance(item, Cake):
                cakes.append(item)
        return cakes


# dessert1 = Dessert(price=10, calories=5)
# print dessert1.calories

# cake = Cake(kind="chocolate")
# print cake.kind

# my_desserts = [dessert1, cake]

# my_menu = Menu(my_desserts)

# cakes = my_menu.cakes()
