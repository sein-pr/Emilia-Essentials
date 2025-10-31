import reflex as rx
from app.states.auth_state import AuthState
from app.states.portfolio_state import PortfolioState
from app.components.project_card import project_card


def dashboard_link(text: str, href: str, active: bool) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name=rx.cond(
            active,
            "bg-[#393E46] text-white px-3 py-2 rounded-md text-sm font-medium",
            "text-gray-300 hover:bg-[#393E46] hover:text-white px-3 py-2 rounded-md text-sm font-medium",
        ),
    )


def dashboard_sidebar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            dashboard_link(
                "Overview", "/dashboard", "/dashboard" == AuthState.router.page.path
            ),
            dashboard_link(
                "Profile",
                "/dashboard/profile",
                "/dashboard/profile" == AuthState.router.page.path,
            ),
            dashboard_link(
                "Projects",
                "/dashboard/projects",
                "/dashboard/projects" == AuthState.router.page.path,
            ),
            dashboard_link(
                "Documents",
                "/dashboard/documents",
                "/dashboard/documents" == AuthState.router.page.path,
            ),
            dashboard_link(
                "Analytics",
                "/dashboard/analytics",
                "/dashboard/analytics" == AuthState.router.page.path,
            ),
            class_name="space-y-1",
        ),
        class_name="w-64 bg-[#222831] p-4 h-screen text-white",
    )


def dashboard_layout(content: rx.Component) -> rx.Component:
    return rx.el.div(
        dashboard_sidebar(),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Admin Dashboard", class_name="text-2xl font-bold text-[#EEEEEE]"
                ),
                rx.el.button(
                    "Log Out",
                    on_click=AuthState.logout,
                    class_name="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition-colors duration-300",
                ),
                class_name="flex items-center justify-between p-6 border-b border-[#393E46]",
            ),
            rx.el.main(content, class_name="p-6"),
            class_name="flex-1 bg-[#393E46]",
        ),
        class_name="flex min-h-screen",
    )


def dashboard_page() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.p(
                "Welcome, Emilia! Manage your portfolio from here.",
                class_name="text-[#EEEEEE]/80",
            )
        )
    )


def projects_dashboard_page() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.div(
                rx.el.h2("Manage Projects", class_name="text-xl font-bold text-white"),
                class_name="flex justify-between items-center mb-6",
            ),
            rx.el.div(
                rx.foreach(PortfolioState.projects, lambda p: admin_project_card(p)),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
            ),
        )
    )


def admin_project_card(project: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(project["title"], class_name="text-lg font-semibold text-white"),
            rx.el.p(
                rx.cond(project["is_premium"], "Premium", "Free"),
                class_name=rx.cond(
                    project["is_premium"], "text-green-400", "text-gray-400"
                ),
            ),
        ),
        rx.el.div(
            rx.el.button("Edit", class_name="text-sm text-blue-400 hover:underline"),
            rx.el.button(
                "Delete",
                class_name="text-sm text-red-400 hover:underline",
                on_click=lambda: PortfolioState.delete_project(project["id"]),
            ),
        ),
        class_name="bg-[#222831] p-4 rounded-lg flex justify-between items-center",
    )