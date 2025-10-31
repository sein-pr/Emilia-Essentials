import reflex as rx
from app.states.state import State, Skill, Stat
from app.components.layout.header import header
from app.components.layout.footer import footer


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Emilia Essentials",
                    class_name="text-5xl md:text-7xl font-bold text-[#EEEEEE]",
                ),
                rx.el.h2(
                    "Turning Numbers into Narratives",
                    class_name="text-2xl md:text-3xl text-[#00ADB5] mt-4",
                ),
                rx.el.p(
                    "Statistics student at UNAM | Data Analyst in the making | Passionate about turning data into insights.",
                    class_name="mt-6 text-lg text-[#EEEEEE]/80 max-w-xl",
                ),
                rx.el.div(
                    rx.el.button(
                        "View Portfolio",
                        class_name="bg-[#00ADB5] text-white px-6 py-3 rounded-lg hover:bg-teal-600 transition-transform duration-300 hover:scale-105",
                    ),
                    rx.el.button(
                        "Hire Me",
                        variant="outline",
                        class_name="border-[#00ADB5] text-[#00ADB5] px-6 py-3 rounded-lg hover:bg-[#00ADB5] hover:text-white transition-colors duration-300",
                    ),
                    rx.el.button(
                        "Download Profile Package",
                        on_click=State.download_profile_package,
                        class_name="bg-[#393E46] text-white px-6 py-3 rounded-lg hover:bg-gray-600 transition-transform duration-300 hover:scale-105",
                    ),
                    class_name="flex items-center gap-4 mt-8",
                ),
                class_name="flex flex-col items-start",
            ),
            rx.el.div(
                rx.image(
                    src="/placeholder.svg",
                    class_name="rounded-full border-8 border-[#00ADB5]/50 object-cover w-64 h-64 md:w-80 md:h-80 shadow-2xl shadow-[#00ADB5]/20",
                ),
                class_name="hidden md:flex items-center justify-center",
            ),
            class_name="container mx-auto grid md:grid-cols-2 gap-12 items-center min-h-[calc(100vh-80px)] px-4 py-16 text-center md:text-left",
        ),
        class_name="bg-[#222831] relative overflow-hidden",
    )


def skill_bar(skill: Skill) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(skill["name"], class_name="font-semibold text-sm text-[#EEEEEE]"),
            rx.el.p(f"{skill['level']}%", class_name="text-xs text-[#00ADB5]"),
            class_name="flex justify-between mb-1",
        ),
        rx.el.div(
            rx.el.div(
                class_name="bg-[#00ADB5] h-2 rounded-full",
                style={"width": f"{skill['level']}%"},
            ),
            class_name="w-full bg-[#393E46] rounded-full h-2",
        ),
        class_name="w-full",
    )


def skills_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h3(
                "Key Skills",
                class_name="text-3xl font-bold text-center text-[#EEEEEE] mb-12",
            ),
            rx.el.div(
                rx.foreach(State.skills, skill_bar),
                class_name="grid grid-cols-2 md:grid-cols-3 gap-8 max-w-4xl mx-auto",
            ),
            class_name="container mx-auto px-4 py-24",
        ),
        class_name="bg-[#222831]",
    )


def stat_card(stat: Stat) -> rx.Component:
    return rx.el.div(
        rx.el.p(stat["value"], class_name="text-4xl font-bold text-[#00ADB5]"),
        rx.el.p(stat["label"], class_name="text-sm text-[#EEEEEE]/70"),
        class_name="bg-[#393E46] p-6 rounded-lg text-center transform hover:-translate-y-2 transition-transform duration-300",
    )


def stats_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.foreach(State.stats, stat_card),
                class_name="grid md:grid-cols-3 gap-8 text-center",
            ),
            class_name="container mx-auto px-4 py-16",
        ),
        class_name="bg-[#393E46]",
    )


def testimonial_card(testimonial: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=testimonial["image_url"],
                class_name="w-16 h-16 rounded-full object-cover border-4 border-[#393E46]",
            ),
            class_name="absolute -top-8 left-1/2 -translate-x-1/2",
        ),
        rx.el.p(
            testimonial["content"],
            class_name="text-center text-[#EEEEEE]/80 italic mt-8",
        ),
        rx.el.div(
            rx.el.p(
                testimonial["author"],
                class_name="font-bold text-white text-center mt-4",
            ),
            rx.el.p(
                testimonial["role"], class_name="text-xs text-[#00ADB5] text-center"
            ),
        ),
        class_name="bg-[#222831] p-8 rounded-lg shadow-lg relative",
    )


def testimonials_section() -> rx.Component:
    from app.states.testimonial_state import TestimonialState

    return rx.el.section(
        rx.el.div(
            rx.el.h3(
                "What People Are Saying",
                class_name="text-3xl font-bold text-center text-[#EEEEEE] mb-16",
            ),
            rx.el.div(
                rx.foreach(TestimonialState.testimonials, testimonial_card),
                class_name="grid md:grid-cols-2 gap-12 max-w-4xl mx-auto",
            ),
            class_name="container mx-auto px-4 py-24",
        ),
        class_name="bg-[#393E46]",
    )


def featured_blog_card(post: dict) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.image(
                src=post["image_url"],
                class_name="rounded-t-lg h-40 w-full object-cover",
            ),
            rx.el.div(
                rx.el.span(
                    post["category"],
                    class_name="text-xs font-semibold uppercase text-[#00ADB5]",
                ),
                rx.el.h4(post["title"], class_name="text-lg font-bold text-white my-1"),
                rx.el.p(
                    str(rx.el.span(post["created_at"])).split("T")[0],
                    class_name="text-xs text-gray-400 mb-2",
                ),
                rx.el.p(
                    post["content"].to_string()[:80] + "...",
                    class_name="text-[#EEEEEE]/70 text-sm h-12 overflow-hidden",
                ),
                class_name="p-4",
            ),
        ),
        href=f"/blog/{post['id']}",
        class_name="bg-[#222831] rounded-lg shadow-md overflow-hidden transform hover:-translate-y-1 transition-transform duration-300",
    )


def featured_blog_section() -> rx.Component:
    from app.states.blog_state import BlogState

    return rx.el.section(
        rx.el.div(
            rx.el.h3(
                "From the Blog",
                class_name="text-3xl font-bold text-center text-[#EEEEEE] mb-12",
            ),
            rx.el.div(
                rx.foreach(BlogState.featured_posts, featured_blog_card),
                class_name="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto",
            ),
            rx.el.div(
                rx.el.a(
                    "View All Posts",
                    href="/blog",
                    class_name="mt-12 inline-block bg-transparent border border-[#00ADB5] text-[#00ADB5] px-6 py-3 rounded-lg hover:bg-[#00ADB5] hover:text-white transition-colors duration-300",
                ),
                class_name="text-center",
            ),
            class_name="container mx-auto px-4 py-24",
        ),
        class_name="bg-[#393E46]",
    )


from app.states.theme_state import ThemeState


def index() -> rx.Component:
    return rx.el.main(
        header(),
        hero_section(),
        stats_section(),
        featured_blog_section(),
        skills_section(),
        testimonials_section(),
        footer(),
        class_name="font-['Montserrat'] transition-colors duration-300",
        style={"background_color": ThemeState.bg_color, "color": ThemeState.text_color},
    )


from app.pages.login import login_page
from app.pages.contact import contact_page
from app.pages.dashboard import dashboard_page, projects_dashboard_page
from app.pages.profile_dashboard import profile_dashboard_page
from app.pages.documents_dashboard import documents_dashboard_page
from app.pages.analytics_dashboard import analytics_dashboard_page
from app.pages.portfolio import portfolio_page
from app.pages.project_detail import project_detail_page
from app.pages.blog import blog_page
from app.pages.blog_detail import blog_detail_page
from app.states.auth_state import AuthState
from app.states.portfolio_state import PortfolioState
from app.states.blog_state import BlogState
from app.states.theme_state import ThemeState
from app.states.donation_state import DonationState

app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.meta(
            name="description",
            content="Emilia Essentials - Data Analyst Portfolio. Turning Numbers into Narratives.",
        ),
        rx.el.meta(
            name="keywords",
            content="Data Analyst, Portfolio, Statistics, UNAM, Python, R, SQL, PowerBI, Machine Learning",
        ),
        rx.el.meta(
            property="og:title", content="Emilia Essentials - Data Analyst Portfolio"
        ),
        rx.el.meta(
            property="og:description",
            content="Showcasing data analysis projects and insights by Emilia, a statistics student at UNAM.",
        ),
        rx.el.meta(property="og:image", content="/placeholder.svg"),
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
        rx.el.script(src="https://js.stripe.com/v3/"),
    ],
)
app.add_page(index)
app.add_page(login_page, route="/login")
app.add_page(contact_page, route="/contact")
app.add_page(portfolio_page, route="/portfolio")
app.add_page(project_detail_page, route="/portfolio/[project_id]")
app.add_page(blog_page, route="/blog")
app.add_page(blog_detail_page, route="/blog/[post_id]")
app.add_page(dashboard_page, route="/dashboard", on_load=AuthState.on_load)
app.add_page(
    projects_dashboard_page, route="/dashboard/projects", on_load=AuthState.on_load
)
app.add_page(
    profile_dashboard_page, route="/dashboard/profile", on_load=AuthState.on_load
)
app.add_page(
    documents_dashboard_page, route="/dashboard/documents", on_load=AuthState.on_load
)
app.add_page(
    analytics_dashboard_page, route="/dashboard/analytics", on_load=AuthState.on_load
)