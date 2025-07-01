import math
from product import Product


class TaxCalculator:
    """Handles tax calculations for products with proper rounding rules."""
    
    # these values can be driven either by the env or 
    # we can make it configurable throught adding the getters and setters       
    BASIC_TAX_RATE = 0.10
    IMPORT_DUTY_RATE = 0.05
    ROUNDING_PRECISION = 0.05
    
    _TAX_EXEMPT_CATEGORIES = {"book", "food", "medical"}

    @classmethod
    def set_exempt_categories(cls, categories: set[str]):
        """Set the collection of tax-exempt product categories."""
        cls._TAX_EXEMPT_CATEGORIES = {cat.lower() for cat in categories}

    @classmethod
    def add_exempt_category(cls, category: str):
        """Add a category to the set of tax-exempt categories."""
        cls._TAX_EXEMPT_CATEGORIES.add(category.lower())

    @classmethod
    def remove_exempt_category(cls, category: str):
        """Remove a category from the set of tax-exempt categories."""
        cls._TAX_EXEMPT_CATEGORIES.discard(category.lower())

    @classmethod
    def is_tax_exempt(cls, product: Product) -> bool:
        """Check if a product's category is tax-exempt."""
        return product.category.lower() in cls._TAX_EXEMPT_CATEGORIES
    
    @classmethod
    def calculate_basic_tax(cls, product: Product) -> float:
        """
        Calculate basic sales tax for a product.
        
        Args:
            product: The product to calculate tax for
            
        Returns:
            Basic tax amount (rounded up to nearest 0.05)
        """
        if cls.is_tax_exempt(product):
            return 0.0
        
        tax_amount = product.price * cls.BASIC_TAX_RATE
        return cls._round_up_to_nearest_nickel(tax_amount)
    
    @classmethod
    def calculate_import_duty(cls, product: Product) -> float:
        """
        Calculate import duty for a product.
        
        Args:
            product: The product to calculate import duty for
            
        Returns:
            Import duty amount (rounded up to nearest 0.05)
        """
        if not product.is_imported:
            return 0.0
        
        duty_amount = product.price * cls.IMPORT_DUTY_RATE
        return cls._round_up_to_nearest_nickel(duty_amount)
    
    @classmethod
    def calculate_total_tax(cls, product: Product) -> float:
        """
        Calculate total tax (basic tax + import duty) for a product.
        
        Args:
            product: The product to calculate total tax for
            
        Returns:
            Total tax amount
        """
        basic_tax = cls.calculate_basic_tax(product)
        import_duty = cls.calculate_import_duty(product)
        return basic_tax + import_duty
    
    @classmethod
    def calculate_final_price(cls, product: Product) -> float:
        """
        Calculate final price including all taxes for a product.
        
        Args:
            product: The product to calculate final price for
            
        Returns:
            Final price including taxes
        """
        return product.price + cls.calculate_total_tax(product)
    
    @classmethod
    def _round_up_to_nearest_nickel(cls, amount: float) -> float:
        """
        Round up to the nearest 0.05 .  
        
        Args:
            amount: Amount to round
            
        Returns:
            Amount rounded up to nearest 0.05
        """
        return math.ceil(amount / cls.ROUNDING_PRECISION) * cls.ROUNDING_PRECISION 