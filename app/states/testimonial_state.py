import reflex as rx
import uuid
from typing import TypedDict


class Testimonial(TypedDict):
    id: str
    author: str
    role: str
    content: str
    image_url: str


class TestimonialState(rx.State):
    testimonials: list[Testimonial] = [
        {
            "id": str(uuid.uuid4()),
            "author": "Dr. Jane Smith",
            "role": "Lead Data Scientist, TechCorp",
            "content": "Emilia has a rare combination of statistical rigor and a keen eye for business application. Her ability to translate complex data into actionable insights was invaluable to our project.",
            "image_url": "/placeholder.svg",
        },
        {
            "id": str(uuid.uuid4()),
            "author": "Prof. John Doe",
            "role": "Statistics Department, UNAM",
            "content": "As a student, Emilia consistently demonstrated a deep understanding of statistical concepts and a passion for applying them to real-world problems. She is a standout talent.",
            "image_url": "/placeholder.svg",
        },
    ]

    @rx.event
    def add_testimonial(self, testimonial_data: dict):
        testimonial_data["id"] = str(uuid.uuid4())
        self.testimonials.append(testimonial_data)

    @rx.event
    def delete_testimonial(self, testimonial_id: str):
        self.testimonials = [t for t in self.testimonials if t["id"] != testimonial_id]