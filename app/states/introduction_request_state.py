import reflex as rx
import uuid
import datetime
from typing import TypedDict
import logging


class IntroductionRequest(TypedDict):
    id: str
    project_id: str
    project_title: str
    name: str
    email: str
    company: str
    message: str
    timestamp: str


class IntroductionRequestState(rx.State):
    """State for managing introduction requests."""

    requests: list[IntroductionRequest] = []

    @rx.event
    def submit_request(self, form_data: dict):
        from app.states.portfolio_state import PortfolioState

        project_id = form_data.get("project_id", "")
        project_title = "Unknown Project"
        new_request = IntroductionRequest(
            id=str(uuid.uuid4()),
            project_id=project_id,
            project_title=form_data.get("project_title", ""),
            name=form_data.get("name", ""),
            email=form_data.get("email", ""),
            company=form_data.get("company", ""),
            message=form_data.get("message", ""),
            timestamp=datetime.datetime.now().isoformat(),
        )
        self.requests.append(new_request)
        logging.info(f"New introduction request: {new_request}")
        return rx.toast.success("Your request has been sent!")