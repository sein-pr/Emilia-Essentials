import reflex as rx
from app.pages.dashboard import dashboard_layout
from app.states.analytics_state import AnalyticsState


def stat_card(icon: str, title: str, value: rx.Var, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name=f"h-6 w-6 text-{color}-500"),
            class_name=f"p-3 rounded-full bg-{color}-100",
        ),
        rx.el.div(
            rx.el.p(title, class_name="text-sm text-gray-400"),
            rx.el.p(value, class_name="text-2xl font-bold text-white"),
        ),
        class_name="flex items-center gap-4 bg-[#222831] p-4 rounded-lg",
    )


def revenue_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Revenue Over Time", class_name="text-lg font-bold text-white mb-4"),
        rx.recharts.area_chart(
            rx.recharts.cartesian_grid(stroke_dasharray="3 3", stroke_opacity=0.2),
            rx.recharts.graphing_tooltip(
                content_style={"background": "#393E46", "border": "none"}
            ),
            rx.recharts.x_axis(data_key="date", stroke="#EEEEEE"),
            rx.recharts.y_axis(stroke="#EEEEEE"),
            rx.recharts.area(
                type_="monotone",
                data_key="revenue",
                stroke="#00ADB5",
                fill="#00ADB5",
                fill_opacity=0.3,
            ),
            data=AnalyticsState.revenue_over_time,
            height=300,
            margin={"top": 5, "right": 20, "left": -10, "bottom": 5},
        ),
        class_name="bg-[#222831] p-6 rounded-lg",
    )


def page_views_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Top Pages by Views", class_name="text-lg font-bold text-white mb-4"),
        rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(stroke_dasharray="3 3", stroke_opacity=0.2),
            rx.recharts.graphing_tooltip(
                content_style={"background": "#393E46", "border": "none"}
            ),
            rx.recharts.x_axis(data_key="path", stroke="#EEEEEE"),
            rx.recharts.y_axis(stroke="#EEEEEE"),
            rx.recharts.bar(data_key="count", fill="#00ADB5", bar_size=20),
            data=AnalyticsState.page_views_data,
            layout="vertical",
            height=300,
            margin={"top": 5, "right": 20, "left": 20, "bottom": 5},
        ),
        class_name="bg-[#222831] p-6 rounded-lg",
    )


def most_viewed_chart(title: str, data: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.h3(title, class_name="text-lg font-bold text-white mb-4"),
        rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(stroke_dasharray="3 3", stroke_opacity=0.2),
            rx.recharts.graphing_tooltip(
                content_style={"background": "#393E46", "border": "none"}
            ),
            rx.recharts.x_axis(data_key="title", hide=True),
            rx.recharts.y_axis(width=80),
            rx.recharts.bar(data_key="views", fill="#00ADB5", radius=[0, 5, 5, 0]),
            data=data,
            layout="vertical",
            height=300,
            margin={"top": 5, "right": 20, "left": -10, "bottom": 5},
        ),
        class_name="bg-[#222831] p-6 rounded-lg",
    )


def activity_feed_item(icon: str, text: str, time: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name=f"h-5 w-5 text-{color}-400"),
            class_name=f"p-2 rounded-full bg-{color}-500/10",
        ),
        rx.el.div(
            rx.el.p(text, class_name="text-sm text-white"),
            rx.el.p(time, class_name="text-xs text-gray-400"),
            class_name="flex-1",
        ),
        class_name="flex items-center gap-3",
    )


def recent_activity_feed() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Recent Activity", class_name="text-lg font-bold text-white mb-4"),
        rx.el.div(
            activity_feed_item(
                "user-plus", "New Subscriber: user@example.com", "5 minutes ago", "blue"
            ),
            activity_feed_item(
                "dollar-sign", "New Donation: $5.00", "1 hour ago", "green"
            ),
            activity_feed_item(
                "file-text",
                "Project Report Downloaded: Customer Churn",
                "3 hours ago",
                "yellow",
            ),
            activity_feed_item(
                "message-square", "New Contact Message", "1 day ago", "purple"
            ),
            class_name="space-y-4",
        ),
        class_name="bg-[#222831] p-6 rounded-lg",
    )


def analytics_dashboard_page() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.h2(
                "Analytics Overview", class_name="text-xl font-bold text-white mb-6"
            ),
            rx.el.div(
                stat_card(
                    "users",
                    "Total Visitors",
                    AnalyticsState.total_visitors.to_string(),
                    "blue",
                ),
                stat_card(
                    "eye",
                    "Page Views",
                    AnalyticsState.total_page_views.to_string(),
                    "teal",
                ),
                stat_card(
                    "download",
                    "Downloads",
                    AnalyticsState.total_downloads.to_string(),
                    "green",
                ),
                stat_card(
                    "dollar-sign",
                    "Total Revenue",
                    f"${AnalyticsState.total_revenue:.2f}",
                    "yellow",
                ),
                class_name="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6",
            ),
            rx.el.div(
                revenue_chart(),
                page_views_chart(),
                class_name="grid lg:grid-cols-2 gap-6 mb-6",
            ),
            rx.el.div(
                most_viewed_chart(
                    "Most Viewed Projects", AnalyticsState.most_viewed_projects
                ),
                most_viewed_chart(
                    "Most Viewed Posts", AnalyticsState.most_viewed_posts
                ),
                class_name="grid lg:grid-cols-2 gap-6 mb-6",
            ),
            recent_activity_feed(),
        )
    )