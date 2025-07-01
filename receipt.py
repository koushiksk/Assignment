from shopping_cart import ShoppingCart


class Receipt:
    """Handles receipt generation for the products purchased."""
    
    @staticmethod
    def generate_receipt(cart: ShoppingCart) -> str:
        """
        Generate a formatted receipt for the products purchased.
        
        Args:
        ShoppingCart containing the products purchased
        """
        if cart.is_empty():
            return "No items in cart."
        
        receipt_lines = []
        item_details = cart.calculate_item_details()
        
        for product, final_price, _ in item_details:
            item_line = f"{product}: {final_price:.2f}"
            receipt_lines.append(item_line)
        
        total_tax = cart.calculate_total_taxes()
        receipt_lines.append(f"Sales Taxes: {total_tax:.2f}")
        
        total_cost = cart.calculate_total_cost()
        receipt_lines.append(f"Total: {total_cost:.2f}")
        
        return "\n".join(receipt_lines)
    
    @staticmethod
    def print_receipt(cart: ShoppingCart) -> None:
        """
        Print a formatted receipt for the items purchased.
        
        Args:
            cart: ShoppingCart containing the products
        """
        receipt = Receipt.generate_receipt(cart)
        print(receipt)
