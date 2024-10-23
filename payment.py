class Payment:
    def __init__(self, amount: float):
        """Initialize a payment with a specific amount."""
        self.amount = amount
        self.status = "Pending"

    def process_payment(self) -> None:
        """Process the payment."""
        self.status = "Completed"
        print(f"Payment of {self.amount} processed successfully.")

    def send_reminder(self) -> None:
        """Send a payment reminder."""
        print(f"Reminder: Payment of {self.amount} is due.")

    def apply_penalty(self) -> None:
        """Apply a penalty for late payment."""
        print("Penalty applied for late payment.")
