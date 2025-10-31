import reflex as rx
import logging


class NewsletterState(rx.State):
    email: str = ""
    subscribers: list[str] = []

    @rx.event
    def subscribe(self, form_data: dict):
        self.email = form_data.get("email", "")
        if not self.email:
            return rx.toast.error("Email is required.")
        if self.email in self.subscribers:
            return rx.toast.warning("You are already subscribed.")
        self.subscribers.append(self.email)
        logging.info(f"New subscriber: {self.email}")
        self.email = ""
        return rx.toast.success("Thank you for subscribing!")