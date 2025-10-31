import reflex as rx
import os
import stripe
import logging


class DonationState(rx.State):
    """State for managing donations."""

    donation_amount: int = 500
    custom_amount: str = ""
    client_secret: str = ""
    payment_status: str = ""
    custom_amount_enabled: bool = False

    @rx.event
    def select_donation_amount(self, amount: int):
        self.donation_amount = amount
        self.custom_amount_enabled = False
        self.custom_amount = ""

    @rx.event
    def enable_custom_amount(self):
        self.custom_amount_enabled = True
        self.donation_amount = 0

    @rx.event
    def set_custom_amount(self, amount: str):
        if amount.isdigit():
            self.donation_amount = int(amount) * 100
        else:
            self.donation_amount = 0

    @rx.event
    async def create_donation_intent(self):
        if self.donation_amount < 100:
            return rx.toast.error("Donation amount must be at least $1.")
        stripe.api_key = os.getenv("STRIPE_API_KEY")
        if not stripe.api_key:
            self.payment_status = "error_config"
            logging.error("Stripe API key not configured.")
            return rx.toast.error("Payment system is not configured.")
        try:
            intent = stripe.PaymentIntent.create(
                amount=self.donation_amount,
                currency="usd",
                description="Buy Me a Coffee Donation",
            )
            self.client_secret = intent.client_secret
            self.payment_status = "succeeded"
            return rx.toast.info("Processing your donation...")
        except Exception as e:
            logging.exception(e)
            self.payment_status = "error_payment"
            return rx.toast.error("Failed to process payment.")