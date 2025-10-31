import reflex as rx
from app.states.contact_state import ContactState
from app.components.layout.header import header
from app.components.layout.footer import footer


def contact_page() -> rx.Component:
    return rx.el.div(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "Get in Touch",
                    class_name="text-5xl font-bold text-white mb-4 text-center",
                ),
                rx.el.p(
                    "Have a project in mind or just want to say hi? I'd love to hear from you.",
                    class_name="text-lg text-[#EEEEEE]/80 text-center max-w-2xl mx-auto",
                ),
                class_name="container mx-auto py-16 px-4",
            ),
            class_name="bg-[#222831]",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.form(
                        rx.el.div(
                            rx.el.label(
                                "Name", class_name="text-sm font-medium text-[#EEEEEE]"
                            ),
                            rx.el.input(
                                placeholder="Your Name",
                                name="name",
                                class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
                                required=True,
                            ),
                            class_name="space-y-2",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Email", class_name="text-sm font-medium text-[#EEEEEE]"
                            ),
                            rx.el.input(
                                placeholder="Your Email",
                                type="email",
                                name="email",
                                class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
                                required=True,
                            ),
                            class_name="space-y-2",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Message",
                                class_name="text-sm font-medium text-[#EEEEEE]",
                            ),
                            rx.el.textarea(
                                placeholder="Your Message",
                                name="message",
                                class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
                                rows=5,
                                required=True,
                            ),
                            class_name="space-y-2",
                        ),
                        rx.el.button(
                            "Send Message",
                            type="submit",
                            class_name="w-full bg-[#00ADB5] text-white px-6 py-3 rounded-lg hover:bg-teal-600 transition-transform duration-300 hover:scale-105 mt-6",
                        ),
                        on_submit=ContactState.submit_contact_form,
                        reset_on_submit=True,
                        class_name="space-y-6",
                    ),
                    class_name="max-w-xl mx-auto",
                ),
                class_name="container mx-auto px-4 py-12",
            ),
            class_name="bg-[#393E46]",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Schedule a Meeting",
                    class_name="text-3xl font-bold text-white mb-4 text-center",
                ),
                rx.el.p(
                    "Use the calendar below to book a time that works for you.",
                    class_name="text-lg text-[#EEEEEE]/80 text-center max-w-2xl mx-auto mb-8",
                ),
                rx.el.div(
                    rx.el.iframe(
                        src="https://calendly.com/d/C2j-3kS-L6j-k9R/emilia-essentials-meeting",
                        class_name="w-full h-[700px] border-0 rounded-lg",
                    ),
                    class_name="max-w-4xl mx-auto bg-[#222831] p-2 rounded-lg",
                ),
                class_name="container mx-auto px-4 py-16",
            ),
            class_name="bg-[#222831]",
        ),
        footer(),
        class_name="font-['Montserrat'] bg-[#393E46] min-h-screen",
    )