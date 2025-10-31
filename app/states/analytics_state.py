import reflex as rx
from typing import TypedDict
import datetime


class PageView(TypedDict):
    path: str
    count: int


class AnalyticsState(rx.State):
    """State for managing the analytics dashboard."""

    total_visitors: int = 1345
    total_page_views: int = 4567
    total_downloads: int = 234
    total_revenue: float = 125.0
    page_views_data: list[PageView] = [
        {"path": "/", "count": 1203},
        {"path": "/portfolio", "count": 876},
        {"path": "/blog", "count": 754},
        {"path": "/contact", "count": 432},
    ]
    revenue_over_time: list[dict[str, int | str]] = [
        {"date": "2024-07-01", "revenue": 0},
        {"date": "2024-07-02", "revenue": 25},
        {"date": "2024-07-03", "revenue": 15},
        {"date": "2024-07-04", "revenue": 0},
        {"date": "2024-07-05", "revenue": 50},
        {"date": "2024-07-06", "revenue": 0},
        {"date": "2024-07-07", "revenue": 35},
    ]
    most_viewed_projects: list[dict[str, str | int]] = [
        {"title": "Customer Churn Prediction", "views": 450},
        {"title": "Market Basket Analysis", "views": 320},
        {"title": "Sales Dashboard", "views": 210},
    ]
    most_viewed_posts: list[dict[str, str | int]] = [
        {"title": "The Art of Data Storytelling", "views": 580},
        {"title": "A Deep Dive into Statistical Significance", "views": 410},
        {"title": "My First Machine Learning Model", "views": 350},
    ]

    @rx.event
    def load_analytics_data(self):
        """Placeholder to load real analytics data."""
        pass