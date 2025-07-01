import unittest
from product import Product
from tax_calculator import TaxCalculator
from shopping_cart import ShoppingCart



class TestProduct(unittest.TestCase):
    """Test cases for the Product class."""
    
    def test_product_creation(self):
        """Test basic product creation."""
        product = Product("test item", 10.00, "other", False, 1)
        self.assertEqual(product.name, "test item")
        self.assertEqual(product.price, 10.00)
        self.assertEqual(product.category, "other")
        self.assertFalse(product.is_imported)
    
    def test_invalid_product_values(self):
        """Test validation of product values."""
        with self.assertRaises(ValueError):
            Product("item", -1.0, "other")  # Negative price
        
        with self.assertRaises(ValueError):
            Product("item", 10.0, "other", quantity=0)  # Zero quantity


class TestTaxCalculator(unittest.TestCase):
    """Test cases for the TaxCalculator class."""

    def test_tax_exempt_products(self):
        """Test tax exemption for books, food, and medical products."""
        book = Product("book", 10.00, "book")
        food = Product("food", 10.00, "food")
        medical = Product("pills", 10.00, "medical")
        other = Product("other", 10.00, "other")
        
        self.assertTrue(TaxCalculator.is_tax_exempt(book))
        self.assertTrue(TaxCalculator.is_tax_exempt(food))
        self.assertTrue(TaxCalculator.is_tax_exempt(medical))
        self.assertFalse(TaxCalculator.is_tax_exempt(other))
    
    def test_basic_tax_calculation(self):
        """Test basic tax calculation."""
        product = Product("item", 14.99, "other")
        tax = TaxCalculator.calculate_basic_tax(product)
        self.assertEqual(tax, 1.50)
        
        book = Product("book", 12.49, "book")
        tax = TaxCalculator.calculate_basic_tax(book)
        self.assertEqual(tax, 0.0)
    
    def test_import_duty_calculation(self):
        """Test import duty calculation."""
        imported_item = Product("item", 10.00, "other", is_imported=True)
        duty = TaxCalculator.calculate_import_duty(imported_item)
        self.assertEqual(duty, 0.50)
        
        local_item = Product("item", 10.00, "other", is_imported=False)
        duty = TaxCalculator.calculate_import_duty(local_item)
        self.assertEqual(duty, 0.0)
    
    def test_rounding_up_to_nearest_nickel(self):
        """Test rounding up to nearest 0.05."""
        test_cases = [
            (1.499, 1.50),
            (0.50, 0.50),
            (0.51, 0.55),
            (2.375, 2.40),
            (0.5625, 0.60),
            (1.3995, 1.40)
        ]
        
        for input_val, expected in test_cases:
            result = TaxCalculator._round_up_to_nearest_nickel(input_val)
            self.assertAlmostEqual(result, expected, places=2, msg=f"Failed for input {input_val}")
    
    def test_final_price_calculation(self):
        """Test final price calculation including all taxes."""
        music_cd = Product("music CD", 14.99, "other")
        final_price = TaxCalculator.calculate_final_price(music_cd)
        self.assertAlmostEqual(final_price, 16.49, places=2)
        
        imported_perfume = Product("perfume", 47.50, "other", is_imported=True)
        final_price = TaxCalculator.calculate_final_price(imported_perfume)
        self.assertAlmostEqual(final_price, 54.65, places=2)


class TestShoppingCart(unittest.TestCase):
    """Test cases for the ShoppingCart class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.cart = ShoppingCart()
        self.book = Product("book", 12.49, "book")
        self.music_cd = Product("music CD", 14.99, "other")
    
    def test_empty_cart(self):
        """Test empty cart functionality."""
        self.assertTrue(self.cart.is_empty())
        self.assertEqual(len(self.cart), 0)
    
    def test_add_products(self):
        """Test adding products to cart."""
        self.cart.add_product(self.book)
        self.cart.add_product(self.music_cd)
        
        self.assertFalse(self.cart.is_empty())
        self.assertEqual(len(self.cart), 2)
    
    def test_total_calculations(self):
        """Test total cost and tax calculations."""
        book = Product("book", 12.49, "book")
        music_cd = Product("music CD", 14.99, "other")
        chocolate_bar = Product("chocolate bar", 0.85, "food")
        
        self.cart.add_product(book)
        self.cart.add_product(music_cd)
        self.cart.add_product(chocolate_bar)
        
        total_taxes = self.cart.calculate_total_taxes()
        total_cost = self.cart.calculate_total_cost()
        
        self.assertAlmostEqual(total_taxes, 1.50, places=2)
        self.assertAlmostEqual(total_cost, 29.83, places=2)


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete system."""
    
    def test_case_1_integration(self):
        """Test complete integration for test case 1."""
        cart = ShoppingCart()
        
        book = Product("book", 12.49, "book")
        music_cd = Product("music CD", 14.99, "other")
        chocolate_bar = Product("chocolate bar", 0.85, "food")
        
        cart.add_product(book)
        cart.add_product(music_cd)
        cart.add_product(chocolate_bar)
        
        self.assertAlmostEqual(cart.calculate_total_taxes(), 1.50, places=2)
        self.assertAlmostEqual(cart.calculate_total_cost(), 29.83, places=2)
        
        item_details = cart.calculate_item_details()
        self.assertAlmostEqual(item_details[0][1], 12.49, places=2)
        self.assertAlmostEqual(item_details[1][1], 16.49, places=2)
        self.assertAlmostEqual(item_details[2][1], 0.85, places=2)
    
    def test_case_2_integration(self):
        """Test complete integration for test case 2."""
        cart = ShoppingCart()
        
        imported_chocolates = Product("box of chocolates", 10.00, "food", is_imported=True)
        imported_perfume = Product("bottle of perfume", 47.50, "other", is_imported=True)
        
        cart.add_product(imported_chocolates)
        cart.add_product(imported_perfume)
        
        self.assertAlmostEqual(cart.calculate_total_taxes(), 7.65, places=2)
        self.assertAlmostEqual(cart.calculate_total_cost(), 65.15, places=2)
    
    def test_case_3_integration(self):
        """Test complete integration for test case 3."""
        cart = ShoppingCart()
        
        imported_perfume = Product("bottle of perfume", 27.99, "other", is_imported=True)
        perfume = Product("bottle of perfume", 18.99, "other")
        headache_pills = Product("packet of headache pills", 9.75, "medical")
        imported_chocolates = Product("box of chocolates", 11.25, "food", is_imported=True)
        
        cart.add_product(imported_perfume)
        cart.add_product(perfume)
        cart.add_product(headache_pills)
        cart.add_product(imported_chocolates)
        
        self.assertAlmostEqual(cart.calculate_total_taxes(), 6.70, places=2)
        self.assertAlmostEqual(cart.calculate_total_cost(), 74.68, places=2)


if __name__ == "__main__":
    unittest.main() 