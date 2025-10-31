import reflex as rx
from app.states.blog_state import BlogState
from app.components.layout.header import header
from app.components.layout.footer import footer


def blog_detail_page() -> rx.Component:
    return rx.el.div(
        header(),
        rx.cond(
            BlogState.current_post,
            rx.el.main(
                rx.el.div(
                    rx.el.div(
                        rx.el.img(
                            src=BlogState.current_post["image_url"],
                            class_name="w-full h-96 object-cover rounded-lg mb-8 shadow-lg",
                        ),
                        rx.el.h1(
                            BlogState.current_post["title"],
                            class_name="text-4xl md:text-6xl font-bold text-white mb-4",
                        ),
                        rx.el.div(
                            rx.el.p(
                                f"By {BlogState.current_post['author']}",
                                class_name="text-white",
                            ),
                            rx.el.p(
                                f"Published on {str(rx.el.span(BlogState.current_post['created_at'])).split('T')[0]}",
                                class_name="text-gray-400",
                            ),
                            class_name="flex items-center gap-4 mb-8",
                        ),
                        rx.el.div(
                            rx.foreach(
                                BlogState.current_post["tags"],
                                lambda tag: rx.el.span(
                                    f"#{tag}",
                                    class_name="bg-[#222831] text-xs text-[#00ADB5] font-semibold px-2.5 py-1 rounded-full",
                                ),
                            ),
                            class_name="flex flex-wrap gap-2 my-4",
                        ),
                        rx.el.div(
                            rx.markdown(
                                BlogState.current_post["content"],
                                component_map={
                                    "h1": lambda text: rx.el.h1(
                                        text,
                                        class_name="text-3xl font-bold text-white my-6",
                                    ),
                                    "h2": lambda text: rx.el.h2(
                                        text,
                                        class_name="text-2xl font-bold text-white my-5",
                                    ),
                                    "p": lambda text: rx.el.p(
                                        text,
                                        class_name="text-[#EEEEEE]/80 leading-relaxed my-4",
                                    ),
                                    "a": lambda text, **props: rx.el.a(
                                        text,
                                        **props,
                                        class_name="text-[#00ADB5] hover:underline",
                                    ),
                                    "code": lambda text: rx.el.code(
                                        text,
                                        class_name="bg-[#222831] text-white p-1 rounded-md text-sm",
                                    ),
                                    "codeblock": lambda text, **props: rx.code_block(
                                        text,
                                        **props,
                                        theme="tomorrow-night-bright",
                                        class_name="my-4 rounded-lg",
                                    ),
                                },
                                class_name="prose prose-invert max-w-none",
                            ),
                            class_name="mt-8",
                        ),
                    ),
                    class_name="container mx-auto px-4 py-16",
                )
            ),
            rx.el.div(
                rx.el.p("Loading post...", class_name="text-white text-center p-12")
            ),
        ),
        footer(),
        class_name="bg-[#393E46] min-h-screen",
        on_mount=BlogState.load_post_details(
            BlogState.router.page.params.get("post_id", "")
        ),
    )