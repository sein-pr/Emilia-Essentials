import reflex as rx
from app.states.theme_state import ThemeState


def nav_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name="hover:text-[#00ADB5] transition-colors duration-300",
    )


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a("Emilia Essentials", href="/", class_name="text-2xl font-bold"),
            rx.el.div(
                rx.el.nav(
                    nav_link("Portfolio", "/portfolio"),
                    nav_link("Blog", "/blog"),
                    nav_link("Contact", "/contact"),
                    class_name="hidden md:flex items-center gap-8",
                ),
                rx.el.button(
                    rx.cond(
                        ThemeState.is_dark_mode,
                        rx.icon("sun", class_name="w-5 h-5"),
                        rx.icon("moon", class_name="w-5 h-5"),
                    ),
                    on_click=ThemeState.toggle_theme,
                    class_name="p-2 rounded-full hover:bg-black/10 dark:hover:bg-white/10 transition-colors",
                ),
                class_name="flex items-center gap-4",
            ),
            class_name="container mx-auto flex items-center justify-between p-4",
        ),
        class_name="backdrop-blur-sm sticky top-0 z-50 transition-colors",
        style={
            "background_color": rx.cond(
                ThemeState.is_dark_mode, "#222831/80", "#FFFFFF/80"
            ),
            "color": ThemeState.text_color,
        },
    )