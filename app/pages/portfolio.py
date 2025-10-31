import reflex as rx
from app.states.portfolio_state import PortfolioState
from app.components.project_card import project_card
from app.components.layout.header import header
from app.components.layout.footer import footer


def tool_filter_badge(tool: str) -> rx.Component:
    return rx.el.button(
        tool,
        on_click=lambda: PortfolioState.set_tool_filter(tool),
        class_name=rx.cond(
            PortfolioState.tool_filter == tool,
            "bg-[#00ADB5] text-white px-4 py-1 rounded-full text-sm",
            "bg-[#393E46] text-[#EEEEEE] hover:bg-[#00ADB5] hover:text-white px-4 py-1 rounded-full text-sm transition-colors",
        ),
    )


def portfolio_page() -> rx.Component:
    return rx.el.div(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "My Work",
                    class_name="text-5xl font-bold text-white mb-4 text-center",
                ),
                rx.el.p(
                    "A selection of my projects in data analysis, statistics, and machine learning.",
                    class_name="text-lg text-[#EEEEEE]/80 text-center max-w-2xl mx-auto",
                ),
                class_name="container mx-auto py-16 px-4",
            ),
            class_name="bg-[#222831]",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.input(
                            placeholder="Search projects...",
                            on_change=PortfolioState.set_search_query,
                            class_name="w-full bg-[#222831] border border-[#393E46] rounded-full px-4 py-2 text-white focus:ring-[#00ADB5] focus:border-[#00ADB5]",
                            default_value=PortfolioState.search_query,
                        ),
                        class_name="w-full md:w-1/3",
                    ),
                    rx.el.div(
                        rx.foreach(PortfolioState.all_tools, tool_filter_badge),
                        class_name="flex flex-wrap gap-2 justify-center",
                    ),
                    class_name="flex flex-col md:flex-row justify-between items-center gap-4 mb-12",
                ),
                rx.el.div(
                    rx.foreach(PortfolioState.filtered_projects, project_card),
                    class_name="grid md:grid-cols-2 lg:grid-cols-3 gap-8",
                ),
                rx.cond(
                    PortfolioState.filtered_projects.length() == 0,
                    rx.el.div(
                        rx.el.p(
                            "No projects found matching your criteria.",
                            class_name="text-center text-[#EEEEEE]/70 col-span-full",
                        )
                    ),
                    None,
                ),
                class_name="container mx-auto px-4 py-12",
            ),
            class_name="bg-[#393E46]",
        ),
        footer(),
        class_name="font-['Montserrat'] bg-[#393E46] min-h-screen",
    )