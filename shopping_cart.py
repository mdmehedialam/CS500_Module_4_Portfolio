class ItemToPurchase:
    """
    A class to represent an item in a shopping cart.
    
    Attributes:
        item_name (str): The name of the item
        item_price (float): The price of the item
        item_quantity (int): The quantity of the item
    """
    
    def __init__(self):
        """
        Default constructor that initializes item's name = "none", 
        item's price = 0, item's quantity = 0
        """
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
    
    def print_item_cost(self):
        """
        Prints the item cost in the format: item_name quantity @ $price = $total
        Example: Bottled Water 10 @ $1 = $10
        """
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total_cost:.0f}")


def get_item_from_user(item_number):
    """
    Prompts the user for item details and returns an ItemToPurchase object.
    
    Args:
        item_number (int): The item number for display purposes
        
    Returns:
        ItemToPurchase: An object with the user's input data
    """
    item = ItemToPurchase()
    
    print(f"Item {item_number}")
    print("Enter the item name:")
    item.item_name = input().strip()
    
    print("Enter the item price:")
    item.item_price = float(input())
    
    print("Enter the item quantity:")
    item.item_quantity = int(input())
    print()  # Add a blank line for better formatting
    
    return item


def main():
    """
    Main function that creates two items and calculates the total cost.
    """
    print("Online Shopping Cart")
    print("=" * 50)
    
    # Get two items from the user
    item1 = get_item_from_user(1)
    item2 = get_item_from_user(2)
    
    # Calculate total cost
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    
    # Display the total cost
    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print(f"Total: ${total_cost:.0f}")


if __name__ == "__main__":
    main() 
