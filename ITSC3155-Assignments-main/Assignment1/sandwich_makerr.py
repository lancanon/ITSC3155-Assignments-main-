import Data

class SandwichMachine:


    def __init__(self, machine_resources):
        """Receives resources as input and binds it to self variable."""
        self.machine_resources = machine_resources


    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        order_made = True

        # search ingredients dictionary for item
        for item, quantity in ingredients.items():
            if self.machine_resources[item] < quantity:  # if item is insufficient then order can't be made
                order_made = False

        return order_made


    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        # gets recipe for the sandwich size
        recipe = Data.recipes[sandwich_size]
        item_ingredients = recipe["ingredients"]

        # checks if the required ingredients are available or not
        if not self.check_resources(item_ingredients):
            print(f"Sorry, there is not enough bread")
            return

        # deduct the required ingredients from the resources based on order_ingredients
        for item, quantity in order_ingredients.items():
            if item in self.machine_resources:
                self.machine_resources[item] -= quantity

        return f"{sandwich_size} sandwich is ready. Bon appetit!"