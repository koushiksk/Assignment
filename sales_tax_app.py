from product import Product
from shopping_cart import ShoppingCart
from receipt import Receipt


class SalesTaxApplication:

    AVAILABLE_CATEGORIES = ["Book", "Food", "Medical", "Other"]

    def __init__(self):
        self.cart = ShoppingCart()

    def run(self):
        print("Welcome to the Sales Tax Application!")
        print("Enter the details for each product. Type 'done' at any prompt to finish.")
        print("-" * 60)

        while True:
            try:
                product_name = input("Product name: ").strip()
                if product_name.lower() == 'done':
                    break

                price_input = input("Price: ").strip()
                if price_input.lower() == 'done':
                    break
                product_price = float(price_input)

                print("Available categories:")
                categories = self.AVAILABLE_CATEGORIES
                for i, category in enumerate(categories):
                    print(f"  {i + 1}. {category}")

                category_number = input(f"Category (1-{len(categories)}): ").strip()
                if category_number.lower() == 'done':
                    break
                category_index = int(category_number) - 1
                if not (0 <= category_index < len(categories)):
                    print("Invalid category selection. Please try again.\n")
                    continue
                category_name = categories[category_index]

                is_imported_input = input("Is it imported? (yes/no): ").strip().lower()
                if is_imported_input == 'done':
                    break
                is_imported = is_imported_input.startswith('y')

                quantity_input = input("Quantity: ").strip()
                if quantity_input.lower() == 'done':
                    break
                quantity = int(quantity_input)

                product = Product(
                    name=product_name,
                    price=product_price,
                    category=category_name,
                    is_imported=is_imported,
                    quantity=quantity
                )
                self.cart.add_product(product)
                print(f"-> Added: {product}\n")

            except ValueError:
                print("\nInvalid number for price, category, or quantity. Please try again.\n")
                continue
            except IndexError:
                print("\nInvalid category selection. Please try again.\n")
                continue

        if not self.cart.is_empty():
            print("\n" + "=" * 40)
            print("             RECEIPT")
            print("=" * 40)
            Receipt.print_receipt(self.cart)
            print("=" * 40)
        else:
            print("\nNo items were added to the cart.")


def main():
    app = SalesTaxApplication()
    app.run()


if __name__ == "__main__":
    main() 