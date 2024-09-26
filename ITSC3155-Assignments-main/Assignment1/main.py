import Data
import sandwich_makerr
import cashier

### Complete functions ###

class SandwichMachine:

 """Create variables based on data dictionaries (resources and recipes). """
resources = Data.resources
recipes = Data.recipes

### Make an instance of SandwichMachine class and write the rest of the codes ###
sandwich = sandwich_makerr.SandwichMachine(resources) #passes resources to instance of sandwich maker
cashier = cashier.Cashier() #creates an instance of cashier class (handles transactions)



# script
def main():
    while True:
        # prompts user with choice
        choice = input("What would you like? (small/medium/large/off): ").lower()

        if choice == "off":
            print("Turning off.")
            break  # ends script

        elif choice in recipes:
            # gets the recipe and order_ingredients
            recipe = recipes[choice]
            order_ingredients = recipe["ingredients"]
            cost = recipe["cost"]

            # checks if ingredients are not available
            if not sandwich.check_resources(order_ingredients):
                print(f"Sorry, we are out of ingredients for {choice}")
                continue

            # process the coins and makes sure payment is successful
            coins = cashier.process_coins()  # Call the process_coins method from the cashier instance
            if cashier.transaction_result(coins, cost):  # Call the transaction_result method from the cashier instance
                # if payment is successful, make the sandwich
                sandwich.make_sandwich(choice, order_ingredients)  # Call make_sandwich from sandwich instance
                print(f"Here is your {choice} sandwich. Bon appetit!")

        else:
            print("Invalid choice. Please select a valid option.")

# Call the main function to run the program
if __name__ == "__main__":
    main()