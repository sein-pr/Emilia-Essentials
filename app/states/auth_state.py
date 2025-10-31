import reflex as rx
import os


class AuthState(rx.State):
    """State for handling authentication."""

    username: str = ""
    password: str = ""
    error_message: str = ""
    is_authenticated: bool = rx.LocalStorage(False, name="is_authenticated")

    @rx.event
    def login(self, form_data: dict[str, str]):
        """Handle user login."""
        self.username = form_data.get("username", "")
        self.password = form_data.get("password", "")
        valid_username = os.environ.get("ADMIN_USERNAME", "emilia")
        valid_password = os.environ.get("ADMIN_PASSWORD", "password123")
        if self.username == valid_username and self.password == valid_password:
            self.is_authenticated = True
            self.error_message = ""
            return rx.redirect("/dashboard")
        else:
            self.error_message = "Invalid username or password."
            self.is_authenticated = False

    @rx.event
    def logout(self):
        """Handle user logout."""
        self.is_authenticated = False
        self.username = ""
        self.password = ""
        return rx.redirect("/")

    @rx.event
    def on_load(self):
        """Check authentication status on page load."""
        if not self.is_authenticated and self.router.page.path not in ["/login"]:
            return rx.redirect("/login")
        if self.is_authenticated and self.router.page.path == "/login":
            return rx.redirect("/dashboard")