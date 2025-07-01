from typing import List, Tuple
from product import Product
from tax_calculator import TaxCalculator


class ShoppingCart:
    """Shopping cart class for managing the list of products that were added to the cart."""
    
    def __init__(self):
        self.products: List[Product] = []
    
    def add_product(self, product: Product) -> None:
        """
        Add a product to the cart.
        
        Args:
            product: Product to add to the cart
        """
        self.products.append(product)
    
    def get_products(self) -> List[Product]:
        """
        Get all products in the cart.
        
        Returns:
            List of products in the cart
        """
        return self.products
    
    def calculate_item_details(self) -> List[Tuple[Product, float, float]]:
        """
        Calculate details for each item in the cart.
        
        Returns:
            List of tuples containing (product, final_price, tax_amount)
        """
        item_details = []
        for product in self.products:
            final_price = TaxCalculator.calculate_final_price(product)
            tax_amount = TaxCalculator.calculate_total_tax(product)
            item_details.append((product, final_price, tax_amount))
        return item_details
    
    def calculate_total_taxes(self) -> float:
        """
        Calculate total taxes for all items in the cart.
        
        Returns:
            Total tax amount for all items
        """
        total_taxes = 0.0
        for product in self.products:
            total_taxes += TaxCalculator.calculate_total_tax(product)
        return total_taxes
    
    def calculate_total_cost(self) -> float:
        """
        Calculate total cost (including taxes) for all items in the cart.
        
        Returns:
            Total cost for all items
        """
        total_cost = 0.0
        for product in self.products:
            total_cost += TaxCalculator.calculate_final_price(product)
        return total_cost
    
    def is_empty(self) -> bool:
        """
        Check if the cart is empty.
        
        Returns:
            True if cart is empty, False otherwise
        """
        return len(self.products) == 0
    
    def __len__(self) -> int:
        """Return the number of products in the cart."""
        return len(self.products)
