def place_order(menu):
  """
  Displays a restaurant menu, asks customers for their order, then returns
  their receipt and total price.

  Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices.

  Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    order_total (float): The total price of the order.
  """
  order = []
  order_total = 0.0
  menu_items = get_menu_items_dict(menu)

  print("Welcome to the Generic Take Out Restaurant.")

  while True:
    print_menu_heading()

    i = 1
    for category, items in menu.items():
      print(f"{category}:")
      for meal, price in items.items():
        print(f"  {i}. {meal}: ${price:.2f}")
        i += 1

    customer_choice = input("Enter your choice by the number (or 'n' to quit): ")

    if customer_choice.lower() == 'n':
      break

    order = update_order(order, customer_choice, menu_items)

    if order:
      order_total = sum([item['Price'] * item['Quantity'] for item in order])

  return order, order_total

def update_order(order, menu_selection, menu_items):
  """
  Checks if the customer menu selection is valid, then updates the order.

  Parameters:
    order (list): A list of dictionaries containing the menu item name, price, 
                 and quantity ordered.
    menu_selection (str): The customer's menu selection.
    menu_items (dictionary): A dictionary containing the menu items and their 
                             prices.

  Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                 and quantity ordered (updated as needed).
  """
  try:
    menu_selection = int(menu_selection) 
  except ValueError:
    print("Invalid input. Please enter a valid menu number or 'n' to quit.")
    return order

  if menu_selection in menu_items:
    item_name = menu_items[menu_selection]["Item name"]
    item_price = menu_items[menu_selection]["Price"]
    try:
      quantity = int(input(f"Enter quantity for {item_name}: "))
    except ValueError:
      print("Invalid input. Please enter a valid quantity (integer).")
      quantity = 1 
    order.append({"Item Name": item_name, "Price": item_price, "Quantity": quantity})
  else:
    print(f"Invalid menu selection: {menu_selection}")

  return order

def print_itemized_receipt(receipt):
  """
  Creates a dictionary of menu items and their prices mapped to their menu 
  number.

  Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices.

  Returns:
    menu_items (dictionary): A dictionary containing the menu items and their 
                             prices.
  """
  print("\nYour Order Receipt:")
  print("------------------------")
  for item in receipt:
    item_name = item["Item Name"]
    price = item["Price"]
    quantity = item["Quantity"]
    print_receipt_line(item_name, price, quantity)
  print("------------------------")

##################################################
#  STARTER CODE
#  Do not modify any of the code below this line:
##################################################

def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
    item_name (str): The name of the meal item.
    price (float): The price of the meal item.
    quantity (int): The quantity of the meal item.
    """
    # Calculate the number of spaces for formatted printing
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))

    # Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")

def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")

def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
    total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")

def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")

def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    # Print the menu item number, food category, meal, and price
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")

def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu 
    number.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their
                        prices.

    Returns:
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.
    """
    # Create an empty dictionary to store the menu items
    menu_items = {}

    # Create a variable for the menu item number
    i = 1

    # Loop through the menu dictionary
    for food_category, options in menu.items():
        # Loop through the options for each food category
        for meal, price in options.items():
            # Store the menu item number, item name and price in the menu_items
            menu_items[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1

    return menu_items

def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.

    Returns:
    meals (dictionary): A nested dictionary containing the menu items and their
                        prices in the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }
    """
    # Create a meal menu dictionary
    #"""
    meals = {
        "Burrito": {
            "Chicken": 4.49,
            "Beef": 5.49,
            "Vegetarian": 3.99
        },
        "Rice Bowl": {
            "Teriyaki Chicken": 9.99,
            "Sweet and Sour Pork": 8.99
        },
        "Sushi": {
            "California Roll": 7.49,
            "Spicy Tuna Roll": 8.49
        },
        "Noodles": {
            "Pad Thai": 6.99,
            "Lo Mein": 7.99,
            "Mee Goreng": 8.99
        },
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    }
    """
    # This menu is just for testing purposes
    meals = {
        "Cake": {
            "Kuih Lapis": 3.49,
            "Strawberry Cheesecake": 6.49,
            "Chocolate Crepe Cake": 6.99
        },
        "Pie": {
            "Apple": 4.99,
            "Lemon Meringue": 5.49
        },
        "Ice-cream": {
            "2-Scoop Vanilla Cone": 3.49,
            "Banana Split": 8.49,
            "Chocolate Sundae": 6.99
        }
    }
    """
    return meals

# Run the program
if __name__ == "__main__":
    # Get the menu dictionary
    meals = get_menu_dictionary()

    receipt, total_price = place_order(meals)

    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Print the receipt heading
    print_receipt_heading()

    # Print the customer's itemized receipt
    print_itemized_receipt(receipt)

    # Print the receipt footer with the total price
    print_receipt_footer(total_price)

