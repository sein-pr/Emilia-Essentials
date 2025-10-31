import reflex as rx
from app.states.portfolio_state import Project, PortfolioState


def tool_badge(tool: str) -> rx.Component:
    return rx.el.span(
        tool,
        class_name="bg-[#222831] text-xs text-[#00ADB5] font-semibold px-2.5 py-1 rounded-full",
    )


def project_card(project: Project) -> rx.Component:
    return rx.el.div(
        rx.el.a(
            rx.image(
                src=project["image_url"],
                class_name="rounded-t-lg h-48 w-full object-cover",
            ),
            href=f"/portfolio/{project['id']}",
        ),
        rx.el.div(
            rx.el.h4(project["title"], class_name="text-xl font-bold text-white mb-2"),
            rx.el.p(
                project["description"],
                class_name="text-[#EEEEEE]/80 text-sm mb-4 h-16 overflow-hidden",
            ),
            rx.el.div(
                rx.foreach(project["tools"], tool_badge),
                class_name="flex flex-wrap gap-2 mb-4",
            ),
            rx.el.a(
                "View More",
                href=f"/portfolio/{project['id']}",
                class_name="inline-block text-[#00ADB5] hover:underline",
            ),
            class_name="p-6",
        ),
        class_name="bg-[#222831] rounded-lg shadow-lg overflow-hidden transform hover:-translate-y-2 transition-transform duration-300",
    )