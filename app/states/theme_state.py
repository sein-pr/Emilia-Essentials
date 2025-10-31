import reflex as rx


class ThemeState(rx.State):
    """State for managing the theme of the app."""

    theme: str = rx.LocalStorage("dark", name="theme")

    @rx.var
    def is_dark_mode(self) -> bool:
        return self.theme == "dark"

    @rx.event
    def toggle_theme(self):
        self.theme = "light" if self.theme == "dark" else "dark"

    @rx.var
    def text_color(self) -> str:
        return "#EEEEEE" if self.is_dark_mode else "#333333"

    @rx.var
    def text_color_subtle(self) -> str:
        return "#EEEEEE/80" if self.is_dark_mode else "#333333/80"

    @rx.var
    def accent_color(self) -> str:
        return "#00ADB5"

    @rx.var
    def bg_color(self) -> str:
        return "#222831" if self.is_dark_mode else "#FFFFFF"

    @rx.var
    def card_bg_color(self) -> str:
        return "#393E46" if self.is_dark_mode else "#F5F5F5"