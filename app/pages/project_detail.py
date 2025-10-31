import reflex as rx
from app.states.portfolio_state import PortfolioState
from app.components.project_card import tool_badge
from app.components.layout.header import header
from app.components.layout.footer import footer


def payment_form() -> rx.Component:
    return rx.el.div(id="payment-element", class_name="mb-4")


def project_detail_page() -> rx.Component:
    return rx.el.div(
        header(),
        rx.cond(
            PortfolioState.current_project,
            rx.el.main(
                rx.el.div(
                    rx.el.div(
                        rx.el.h1(
                            PortfolioState.current_project["title"],
                            class_name="text-4xl md:text-6xl font-bold text-white mb-4",
                        ),
                        rx.el.div(
                            rx.foreach(
                                PortfolioState.current_project["tools"], tool_badge
                            ),
                            class_name="flex flex-wrap gap-2 my-4",
                        ),
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.h2(
                                "Project Overview",
                                class_name="text-2xl font-bold text-white mb-4",
                            ),
                            rx.el.p(
                                PortfolioState.current_project["full_description"],
                                class_name="text-[#EEEEEE]/80 leading-relaxed",
                            ),
                            introduction_request_form(),
                            class_name="md:col-span-2",
                        ),
                        rx.el.div(
                            rx.el.h3(
                                "Access Full Report",
                                class_name="text-xl font-bold text-white mb-4",
                            ),
                            rx.cond(
                                PortfolioState.current_project["is_premium"],
                                premium_access_card(),
                                free_access_card(),
                            ),
                            class_name="bg-[#222831] p-6 rounded-lg",
                        ),
                        class_name="grid md:grid-cols-3 gap-12 mt-12",
                    ),
                    class_name="container mx-auto px-4 py-16",
                )
            ),
            rx.el.div(
                rx.el.p("Loading project...", class_name="text-white text-center p-12")
            ),
        ),
        footer(),
        class_name="bg-[#393E46] min-h-screen",
        on_mount=PortfolioState.load_project_details(
            PortfolioState.router.page.params.get("project_id", "")
        ),
    )


def premium_access_card() -> rx.Component:
    return rx.el.div(
        rx.el.p(
            f"Purchase the full detailed report and dataset for ${PortfolioState.current_project['price_amount'].to(float) / 100}",
            class_name="text-white mb-4",
        ),
        rx.el.button(
            "Purchase Access",
            on_click=PortfolioState.create_payment_intent,
            class_name="w-full bg-[#00ADB5] text-white px-6 py-3 rounded-lg hover:bg-teal-600 transition-transform duration-300 hover:scale-105",
        ),
        rx.cond(PortfolioState.payment_status == "succeeded", payment_form(), None),
    )


def free_access_card() -> rx.Component:
    return rx.el.div(
        rx.el.p("This report is available for free.", class_name="text-white mb-4"),
        rx.el.a(
            "Download Report",
            href=PortfolioState.current_project["report_file_url"],
            download=True,
            class_name="w-full block text-center bg-[#00ADB5] text-white px-6 py-3 rounded-lg hover:bg-teal-600 transition-transform duration-300 hover:scale-105",
        ),
    )


from app.states.introduction_request_state import IntroductionRequestState


def introduction_request_form() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Request Personalized Introduction",
            class_name="text-xl font-bold text-white mb-4 pt-6 mt-6 border-t border-[#393E46]",
        ),
        rx.el.p(
            "Interested in how this project's approach could benefit you? Let's talk.",
            class_name="text-sm text-[#EEEEEE]/70 mb-4",
        ),
        rx.el.form(
            rx.el.input(
                name="project_id",
                type="hidden",
                default_value=PortfolioState.current_project["id"],
            ),
            rx.el.input(
                name="project_title",
                type="hidden",
                default_value=PortfolioState.current_project["title"],
            ),
            rx.el.div(
                rx.el.input(
                    placeholder="Your Name",
                    name="name",
                    required=True,
                    class_name="mb-2 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
                ),
                rx.el.input(
                    placeholder="Your Email",
                    name="email",
                    type="email",
                    required=True,
                    class_name="mb-2 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
                ),
                rx.el.input(
                    placeholder="Company/Organization",
                    name="company",
                    class_name="mb-2 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
                ),
                rx.el.textarea(
                    placeholder="Your Message",
                    name="message",
                    required=True,
                    class_name="mb-2 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
                    rows=3,
                ),
            ),
            rx.el.button(
                "Send Request",
                type="submit",
                class_name="w-full bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors",
            ),
            on_submit=IntroductionRequestState.submit_request,
            reset_on_submit=True,
        ),
        class_name="mt-6",
    )