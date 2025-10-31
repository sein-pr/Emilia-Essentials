import reflex as rx
from app.states.auth_state import AuthState


def login_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Admin Login",
                class_name="text-center text-3xl font-bold text-[#EEEEEE]",
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.label(
                        "Username", class_name="text-sm font-medium text-[#EEEEEE]"
                    ),
                    rx.el.input(
                        placeholder="Enter your username",
                        name="username",
                        class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
                    ),
                    class_name="space-y-2",
                ),
                rx.el.div(
                    rx.el.label(
                        "Password", class_name="text-sm font-medium text-[#EEEEEE]"
                    ),
                    rx.el.input(
                        placeholder="Enter your password",
                        type="password",
                        name="password",
                        class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
                    ),
                    class_name="space-y-2",
                ),
                rx.cond(
                    AuthState.error_message != "",
                    rx.el.div(
                        AuthState.error_message, class_name="text-red-500 text-sm mt-2"
                    ),
                    None,
                ),
                rx.el.button(
                    "Log In",
                    type="submit",
                    class_name="w-full bg-[#00ADB5] text-white px-6 py-3 rounded-lg hover:bg-teal-600 transition-transform duration-300 hover:scale-105 mt-6",
                ),
                on_submit=AuthState.login,
                class_name="space-y-6",
            ),
            class_name="w-full max-w-md space-y-8 rounded-xl bg-[#393E46] p-8 shadow-lg",
        ),
        class_name="flex min-h-screen items-center justify-center bg-[#222831] p-4",
    )