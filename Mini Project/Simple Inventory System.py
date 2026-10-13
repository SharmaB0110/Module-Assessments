class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(
            f"{self.name} | Price: ${self.price:.2f} | "
            f"Available quantity: {self.quantity}"
        )

    def update_quantity(self, change):
        # Use a positive number to restock and a negative number for a sale.
        if self.quantity + change < 0:
            print("Not enough stock for that sale.")
            return False

        self.quantity += change
        return True

    def inventory_value(self):
        return self.price * self.quantity


def find_product(products, name):
    for product in products:
        if product.name.casefold() == name.casefold():
            return product
    return None


def main():
    products = []

    while True:
        print("\n1. Add product")
        print("2. View inventory")
        print("3. Update quantity")
        print("4. Show total inventory value")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Product name: ").strip()

            try:
                price = float(input("Price: $"))
                quantity = int(input("Starting quantity: "))
                if price < 0 or quantity < 0:
                    print("Price and quantity cannot be negative.")
                    continue
            except ValueError:
                print("Enter a valid price and whole-number quantity.")
                continue

            products.append(Product(name, price, quantity))
            print(f"Added {name}.")

        elif choice == "2":
            if products:
                for product in products:
                    product.display_info()
            else:
                print("The inventory is empty.")

        elif choice == "3":
            name = input("Product name: ").strip()
            product = find_product(products, name)

            if product is None:
                print("Product not found.")
                continue

            try:
                change = int(
                    input("Quantity change (positive to restock, negative for a sale): ")
                )
            except ValueError:
                print("Enter a whole number.")
                continue

            if product.update_quantity(change):
                print(f"Updated quantity: {product.quantity}")

        elif choice == "4":
            total = sum(product.inventory_value() for product in products)
            print(f"Total inventory value: ${total:.2f}")

        elif choice == "5":
            break

        else:
            print("Choose an option from 1 to 5.")


if __name__ == "__main__":
    main()