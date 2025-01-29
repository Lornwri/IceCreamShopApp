# Ice Cream Shop Application
# Date: 1/29/2025

# Store Ice Cream Shop menu items
flavors = ["vanilla", "chocolate", "cookie dough"]
toppings = ["sprinkles", "cookies", "banana"]
prices = {"scoop": 2.50, "topping": 0.50}

def display_menu():
    """Shows available flavors and toppings to the customer"""
    print("\n=== Welcome to the Ice Cream Shop!")
    print("\nAvailable flavors:")

    # Loop through the list of flavors and
    # Loop through the list of toppings

    for flavor in flavors:
        print(f" - {flavor}")

    print("\nAvailable Toppings:")
    for topping in toppings:
        print(f"- {topping}")

    # Show prices to users
    print("\nPrices")
    print(f"Scoops: ${prices['scoop']:.2f} each")
    print(f"Toppings: ${prices['topping']:.2f} each")

def get_flavors():
    """Gets Ice Cream flavor choices from customer"""
    chosen_flavors = []

    # Use While loop to keep taking orders until customer is done

    while True:
        try:
            # Prompt user to choose their scoops of ice cream
            num_scoops = int(input("\nHow many scoops would you like? (1-3):"))
            # Validate the input

            if 1 <= num_scoops <= 3:
                break
            print("Please choose between 1 and 3 scoops.")

        except ValueError:
            print("Please enter a number.")

    # Prompt user to enter the ice cream flavor
    print("\nFor each scoop, enter the flavor you'd like:")
    for i in range(num_scoops): # For loop prompts for each scoop of ice cream
        # Nested while loop handles the user's input and validation
        while True:
            flavor = input(f"Scoop {i+1}: ").lower()
            # Check to see if flavor is in shop's list
            if  flavor in flavors:
                chosen_flavors.append(flavor)
                break
            print("Sorry, that flavor isn't available.")

    # Return to calling function, the number of scoops the user wants
    # and the flavors they picked
    return num_scoops, chosen_flavors

def get_toppings(): 
    """Gets topping choices from the customer"""
    chosen_toppings = []

# Use a while loop to prompt the user for the toppings
# until they are done adding toppings
    while True:
        topping = input("\nEnter a topping (or 'done' if finished): ").lower()
        # Test if the user is done ordering toppings
        if topping == 'done':
            break
        # Test if the topping is in the list of toppings for the shop
        if topping in toppings:
            chosen_toppings.append(topping)
            print(f"Added {topping}!")
        else:
            print("Sorry, that topping isn't available.")

    # Return the list of toppings that the user chose
    return chosen_toppings

def calculate_total(num_scoops, num_toppings):
    """Calculates the total cost of the order"""
    scoop_cost = num_scoops * prices["scoop"]
    topping_cost = num_toppings * prices["topping"]
    return scoop_cost + topping_cost

def print_receipt(num_scoops, chosen_flavors, chosen_toppings):
    """Prints a receipt for the customer"""
    print("\n=== Your Ice Cream Order ===")
    for i in range(num_scoops):
        print(f"Scoop {i+1}: {chosen_flavors[i].title()}")

    if chosen_toppings:
        print("\nToppings:")

        # Loop through the list of toppings
        for topping in chosen_toppings:
            print(f" - {topping.title()}")

    # Print the total
    total = calculate_total(num_scoops, len(chosen_toppings))
    print(f"\nTotal: ${total:.2f}")

    # Save order to file
    with open("daily_orders.txt", "a") as file:
        file.write(f"\nOrder: {num_scoops} scoops - ${total:.2f}")


# Main function - updated test function

def main():
    display_menu()

    # Call get flavors function which returns the number of scoops
    # and the list of flavors

    num_scoops, chosen_flavors = get_flavors()

    #Call the get toppings function which returns the list of toppings
    chosen_toppings = get_toppings()

    #Display the receipts
    print_receipt(num_scoops, chosen_flavors, chosen_toppings)

# Automatically execute main function
if __name__ == "__main__":
    main()
