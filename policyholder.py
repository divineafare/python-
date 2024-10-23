class Policyholder:
    def __init__(self, name: str, email: str):
        """Initialize a new policyholder with name and email."""
        self.name = name
        self.email = email
        self.is_active = True
        self.products = []

    def register(self) -> None:
        """Register the policyholder."""
        print(f"{self.name} has been registered.")

    def suspend(self) -> None:
        """Suspend the policyholder's policy."""
        self.is_active = False
        print(f"{self.name}'s policy has been suspended.")

    def reactivate(self) -> None:
        """Reactivate the policyholder's policy."""
        self.is_active = True
        print(f"{self.name}'s policy has been reactivated.")

    def add_product(self, product) -> None:
        """Add a product to the policyholder's account."""
        self.products.append(product)
        print(f"{product.name} added to {self.name}'s account.")

    def display_account_details(self) -> dict:
        """Display the account details of the policyholder."""
        status = "Active" if self.is_active else "Suspended"
        return {
            "Name": self.name,
            "Email": self.email,
            "Status": status,
            "Products": [product.name for product in self.products]
        }
