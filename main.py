from policyholder import Policyholder
from product import Product
from payment import Payment

if __name__ == "__main__":
    # Create products
    health_insurance = Product("Health Insurance", 100.0)
    life_insurance = Product("Life Insurance", 150.0)

    # Create policyholders
    john_doe = Policyholder("John Doe", "john@example.com")
    jane_smith = Policyholder("Jane Smith", "jane@example.com")

    # Register policyholders
    john_doe.register()
    jane_smith.register()

    # Add products to policyholders
    john_doe.add_product(health_insurance)
    jane_smith.add_product(life_insurance)

    # Process payment for John Doe
    payment_for_john = Payment(health_insurance.premium)
    payment_for_john.process_payment()

    # Display account details
    print(john_doe.display_account_details())
    print(jane_smith.display_account_details())
