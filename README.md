# Sales Tax Application

## Overview
A Python application that calculates sales tax and generates receipts for shopping baskets. The application follows object-oriented design principles and includes comprehensive testing.

## Business Rules
- **Basic sales tax**: 10% on all goods except books, food, and medical products (which are exempt)
- **Import duty**: Additional 5% on all imported goods (no exemptions)
- **Tax rounding**: All taxes are rounded up to the nearest 0.05
- **Receipt format**: Shows item name, final price (including tax), total sales taxes, and total cost

## Architecture

### Classes
- **`Product`**: Represents individual items with properties (name, price, category, import status, quantity)
- **`ProductCategory`**: Enum defining product categories that affect tax exemption
- **`TaxCalculator`**: Handles all tax calculations with proper rounding rules
- **`ShoppingCart`**: Manages collections of products and calculates totals
- **`Receipt`**: Handles receipt generation and formatting
- **`SalesTaxApplication`**: Main application class that demonstrates the solution

### Design Principles
- Single Responsibility Principle: Each class has a clear, focused responsibility
- Open/Closed Principle: Easy to extend with new product categories or tax rules
- Dependency Inversion: Uses abstractions and interfaces where appropriate
- Proper encapsulation with clear public interfaces

## Files
- `product.py` - Product and ProductCategory definitions
- `tax_calculator.py` - Tax calculation logic
- `shopping_cart.py` - Shopping cart management
- `receipt.py` - Receipt generation
- `sales_tax_app.py` - Main application with test cases
- `test_sales_tax.py` - Comprehensive unit and integration tests
- `requirements.txt` - Dependencies (uses only Python standard library)

## Running the Application

### Run Test Cases
```bash
python sales_tax_app.py
```

### Run Unit Tests
```bash
python test_sales_tax.py
```

## Test Cases Covered

### Input 1:
- 1 book at 12.49 (tax exempt, not imported)
- 1 music CD at 14.99 (taxable, not imported)
- 1 chocolate bar at 0.85 (tax exempt food, not imported)

**Expected Output:**
```
1 book: 12.49
1 music CD: 16.49
1 chocolate bar: 0.85
Sales Taxes: 1.50
Total: 29.83
```

### Input 2:
- 1 imported box of chocolates at 10.00 (tax exempt food, imported)
- 1 imported bottle of perfume at 47.50 (taxable, imported)

**Expected Output:**
```
1 imported box of chocolates: 10.50
1 imported bottle of perfume: 54.65
Sales Taxes: 7.65
Total: 65.15
```

### Input 3:
- 1 imported bottle of perfume at 27.99 (taxable, imported)
- 1 bottle of perfume at 18.99 (taxable, not imported)
- 1 packet of headache pills at 9.75 (tax exempt medical, not imported)
- 1 box of imported chocolates at 11.25 (tax exempt food, imported)

**Expected Output:**
```
1 imported bottle of perfume: 32.19
1 bottle of perfume: 20.89
1 packet of headache pills: 9.75
1 imported box of chocolates: 11.85
Sales Taxes: 6.70
Total: 74.68
```

## Requirements
- Python 3.7 or higher
- No external dependencies (uses only Python standard library)

## Testing
The application includes comprehensive unit tests covering:
- Product creation and validation
- Tax calculations with various scenarios
- Rounding rules verification
- Shopping cart operations
- Integration tests for all test cases
- Receipt generation

All tests pass and verify the correct implementation of the business rules.

## Production Quality Features
- Comprehensive error handling and validation
- Type hints for better code documentation
- Detailed docstrings for all classes and methods
- Unit tests with high coverage
- Clean separation of concerns
- Extensible design for future enhancements 