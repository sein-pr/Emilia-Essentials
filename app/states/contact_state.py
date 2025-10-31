import reflex as rx
import uuid
import logging
from typing import TypedDict
import datetime


class Message(TypedDict):
    id: str
    name: str
    email: str
    message: str
    timestamp: str


class ContactState(rx.State):
    messages: list[Message] = []

    @rx.event
    def submit_contact_form(self, form_data: dict):
        new_message = Message(
            id=str(uuid.uuid4()),
            name=form_data.get("name", ""),
            email=form_data.get("email", ""),
            message=form_data.get("message", ""),
            timestamp=datetime.datetime.now().isoformat(),
        )
        self.messages.append(new_message)
        logging.info(f"New contact form submission: {new_message}")
        return rx.toast.success(
            "Message sent successfully! I will get back to you soon."
        )

    @rx.event
    def delete_message(self, message_id: str):
        self.messages = [m for m in self.messages if m["id"] != message_id]