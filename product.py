from enum import Enum, auto


class Product:
    """Product class to represent a product with its name, price, category, and import status."""

    def __init__(self, name: str, price: float, category: str,
                 is_imported: bool = False, quantity: int = 1):
        """
        Args:
            name: Product name
            price: Unit price of the product
            category: Product category (affects tax exemption)
            is_imported: Whether the product is imported
            quantity: Quantity of the product
        """
        if price < 0:
            raise ValueError("Price must be greater than 0")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
            
        self.name = name
        self.price = price
        self.category = category
        self.is_imported = is_imported
        self.quantity = quantity
    
    def __str__(self) -> str:
        """String representation of the product for receipt."""
        prefix = "imported " if self.is_imported else ""
        return f"{self.quantity} {prefix}{self.name}"
    
    def __repr__(self) -> str:
        """Detailed string representation for debugging."""
        return (f"Product(name='{self.name}', price={self.price}, "
                f"category='{self.category}', is_imported={self.is_imported}, "
                f"quantity={self.quantity})") 