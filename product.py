class Product:
    def __init__(self, name: str, premium: float):
        """Initialize a new product with name and premium."""
        self.name = name
        self.premium = premium

    def update(self, new_premium: float) -> None:
        """Update the product's premium."""
        self.premium = new_premium
        print(f"{self.name} premium updated to {self.premium}.")

    def suspend(self) -> None:
        """Suspend the product."""
        print(f"{self.name} has been suspended.")
