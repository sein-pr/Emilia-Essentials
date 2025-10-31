import reflex as rx
from app.states.blog_state import BlogState, BlogPost
from app.components.layout.header import header
from app.components.layout.footer import footer
import datetime


def category_filter_badge(category: str) -> rx.Component:
    return rx.el.button(
        category,
        on_click=lambda: BlogState.set_category_filter(category),
        class_name=rx.cond(
            BlogState.category_filter == category,
            "bg-[#00ADB5] text-white px-4 py-1 rounded-full text-sm font-semibold",
            "bg-[#393E46] text-[#EEEEEE] hover:bg-[#00ADB5] hover:text-white px-4 py-1 rounded-full text-sm font-semibold transition-colors",
        ),
    )


def tag_filter_badge(tag: str) -> rx.Component:
    return rx.el.button(
        f"#{tag}",
        on_click=lambda: BlogState.set_tag_filter(tag),
        class_name=rx.cond(
            BlogState.tag_filter == tag,
            "text-[#00ADB5] font-bold",
            "text-[#EEEEEE]/70 hover:text-[#00ADB5] transition-colors",
        ),
        variant="ghost",
    )


def post_card(post: BlogPost) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.image(
                src=post["image_url"],
                class_name="rounded-t-lg h-48 w-full object-cover",
            ),
            rx.el.div(
                rx.el.span(
                    post["category"],
                    class_name="text-xs font-semibold uppercase text-[#00ADB5]",
                ),
                rx.el.h4(post["title"], class_name="text-xl font-bold text-white my-2"),
                rx.el.p(
                    post["content"].to_string()[:100] + "...",
                    class_name="text-[#EEEEEE]/80 text-sm mb-4 h-16 overflow-hidden",
                ),
                rx.el.div(
                    rx.el.p(f"By {post['author']}", class_name="text-sm text-white"),
                    rx.el.p(
                        str(rx.el.span(post["created_at"])).split("T")[0],
                        class_name="text-sm text-gray-400",
                    ),
                    class_name="flex items-center justify-between pt-4 border-t border-[#393E46]",
                ),
                class_name="p-6",
            ),
            class_name="bg-[#222831] rounded-lg shadow-lg overflow-hidden transform hover:-translate-y-2 transition-transform duration-300 h-full flex flex-col justify-between",
        ),
        href=f"/blog/{post['id']}",
    )


def blog_page() -> rx.Component:
    return rx.el.div(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "Insights & Articles",
                    class_name="text-5xl font-bold text-white mb-4 text-center",
                ),
                rx.el.p(
                    "Exploring the world of data, one post at a time.",
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
                            placeholder="Search articles...",
                            on_change=BlogState.set_search_query,
                            class_name="w-full bg-[#222831] border border-[#393E46] rounded-full px-4 py-2 text-white focus:ring-[#00ADB5] focus:border-[#00ADB5]",
                        ),
                        class_name="w-full md:w-1/3",
                    ),
                    rx.el.div(
                        rx.foreach(BlogState.all_categories, category_filter_badge),
                        class_name="flex flex-wrap gap-2 justify-center",
                    ),
                    class_name="flex flex-col md:flex-row justify-between items-center gap-4 mb-8",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.foreach(BlogState.all_tags, tag_filter_badge),
                        class_name="flex flex-wrap gap-4 justify-center mb-12",
                    )
                ),
                rx.el.div(
                    rx.foreach(BlogState.filtered_posts, post_card),
                    class_name="grid md:grid-cols-2 lg:grid-cols-3 gap-8",
                ),
                rx.cond(
                    BlogState.filtered_posts.length() == 0,
                    rx.el.div(
                        rx.el.p(
                            "No posts found matching your criteria.",
                            class_name="text-center text-[#EEEEEE]/70 col-span-full py-12",
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