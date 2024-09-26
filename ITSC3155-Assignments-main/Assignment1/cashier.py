#cashier

class Cashier:

    def __init__(self):
        self.total_money = 0  # Example attribute


    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        # float int(input())) * value
        print("Please insert coins.")

        large_dollar = int(input("How many large dollars?: ")) * 1.00
        half_dollar = int(input("How many half dollars?: ")) * 0.50
        quarters = int(input("How many quarters?: ")) * 0.25
        nickels = int(input("How many nickels?: ")) * 0.05

        # calculates value from  total sum of inserted coins
        cost = large_dollar + half_dollar + quarters + nickels
        return cost  # returns the total amount inserted

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        # coins = self.process_coins()
        #checks if amount of inserted coins is >= to sandwich cost
        if coins >= cost:

            #calculates change amount
            amount = round(coins - cost, 2)

            #if amount is greater than 0 then print amount
            if amount > 0:
                print(f"Here is ${amount} in change.")
            return True

        else:
            #if amount is insufficient refund money
            print("Sorry that's not enough money. Money refunded")
            return False
