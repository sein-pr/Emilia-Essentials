import reflex as rx
from app.states.newsletter_state import NewsletterState
from app.states.donation_state import DonationState


def newsletter_form() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            rx.el.input(
                placeholder="Enter your email...",
                name="email",
                type="email",
                class_name="bg-[#393E46] border border-[#222831] rounded-l-lg px-4 py-2 text-white focus:ring-[#00ADB5] focus:border-[#00ADB5] flex-grow",
            ),
            rx.el.button(
                "Subscribe",
                type="submit",
                class_name="bg-[#00ADB5] text-white px-4 py-2 rounded-r-lg hover:bg-teal-600 transition-colors",
            ),
            class_name="flex",
        ),
        on_submit=NewsletterState.subscribe,
        reset_on_submit=True,
    )


def donation_component() -> rx.Component:
    return rx.el.div(
        rx.el.h4("Support My Work", class_name="font-bold text-white mb-2"),
        rx.el.p(
            "If you find my work valuable, consider buying me a coffee!",
            class_name="text-sm text-[#EEEEEE]/70 mb-4",
        ),
        rx.el.div(
            rx.foreach(
                [300, 500, 1000],
                lambda amount: rx.el.button(
                    f"${amount / 100:.0f}",
                    on_click=lambda: DonationState.select_donation_amount(amount),
                    class_name=rx.cond(
                        DonationState.donation_amount == amount,
                        "bg-[#00ADB5] text-white",
                        "bg-[#393E46] text-white",
                    ),
                    size="1",
                ),
            ),
            rx.el.button(
                "Custom", on_click=DonationState.enable_custom_amount, size="1"
            ),
            class_name="flex gap-2 mb-2",
        ),
        rx.cond(
            DonationState.custom_amount_enabled,
            rx.el.input(
                placeholder="Amount in USD",
                on_change=DonationState.set_custom_amount,
                class_name="bg-[#393E46] text-white rounded-lg px-2 py-1 w-full mb-2",
            ),
            None,
        ),
        rx.el.button(
            "Donate",
            on_click=DonationState.create_donation_intent,
            class_name="w-full bg-[#00ADB5] text-white px-4 py-2 rounded-lg hover:bg-teal-600 transition-colors",
        ),
        rx.cond(
            DonationState.payment_status == "succeeded",
            rx.el.p(
                "Thank you for your support!", class_name="text-green-400 text-sm mt-2"
            ),
            None,
        ),
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.h4("Stay Updated", class_name="font-bold text-white mb-2"),
                rx.el.p(
                    "Subscribe to my newsletter for the latest insights.",
                    class_name="text-sm text-[#EEEEEE]/70 mb-4",
                ),
                newsletter_form(),
                class_name="md:w-1/3",
            ),
            rx.el.div(donation_component(), class_name="md:w-1/3"),
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        rx.icon("linkedin"),
                        href="#",
                        class_name="text-[#EEEEEE] hover:text-[#00ADB5]",
                    ),
                    rx.el.a(
                        rx.icon("github"),
                        href="#",
                        class_name="text-[#EEEEEE] hover:text-[#00ADB5]",
                    ),
                    rx.el.a(
                        rx.icon("mail"),
                        href="mailto:emilia@essentials.com",
                        class_name="text-[#EEEEEE] hover:text-[#00ADB5]",
                    ),
                    class_name="flex gap-6 justify-center md:justify-start",
                ),
                rx.el.p(
                    "© 2024 Emilia Essentials. All Rights Reserved.",
                    class_name="text-sm text-[#EEEEEE]/50 mt-4 text-center md:text-left",
                ),
            ),
            class_name="container mx-auto grid md:grid-cols-3 items-start justify-between p-8 gap-8",
        ),
        class_name="bg-[#222831]",
    )