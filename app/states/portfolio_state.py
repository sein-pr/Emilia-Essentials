import reflex as rx
from typing import TypedDict
import uuid
import stripe
import os
import logging


class Project(TypedDict):
    id: str
    title: str
    image_url: str
    description: str
    full_description: str
    tools: list[str]
    project_url: str
    report_file_url: str
    price_amount: int
    is_premium: bool


class PortfolioState(rx.State):
    """State for managing portfolio projects."""

    projects: list[Project] = [
        {
            "id": str(uuid.uuid4()),
            "title": "Customer Churn Prediction",
            "image_url": "/placeholder.svg",
            "description": "Developed a model to predict customer churn for a telecom company, achieving 92% accuracy.",
            "full_description": "This project involved building a machine learning model to identify customers likely to churn. The model was trained on a large dataset of customer behavior and demographics, and it achieved an accuracy of 92% on the test set. Key technologies included Python, Scikit-learn, and Pandas for data manipulation and modeling.",
            "tools": ["Python", "Scikit-learn", "Pandas"],
            "project_url": "#",
            "report_file_url": "/sample_report.pdf",
            "price_amount": 2500,
            "is_premium": True,
        },
        {
            "id": str(uuid.uuid4()),
            "title": "Sales Dashboard",
            "image_url": "/placeholder.svg",
            "description": "Created an interactive sales dashboard in PowerBI to track KPIs and sales performance.",
            "full_description": "A comprehensive sales dashboard built with PowerBI to provide real-time insights into sales performance. It features multiple visualizations, including sales trends, regional performance, and top-selling products. The dashboard connects to a SQL database for live data updates.",
            "tools": ["PowerBI", "SQL", "Excel"],
            "project_url": "#",
            "report_file_url": "/sample_report.pdf",
            "price_amount": 0,
            "is_premium": False,
        },
        {
            "id": str(uuid.uuid4()),
            "title": "Market Basket Analysis",
            "image_url": "/placeholder.svg",
            "description": "An analysis of retail transaction data to identify frequently co-purchased products.",
            "full_description": "This analysis used association rule mining to discover interesting relationships between variables in a large retail dataset. The findings helped the client optimize product placement and marketing strategies. The project was primarily conducted using R.",
            "tools": ["R", "Excel", "Statistics"],
            "project_url": "#",
            "report_file_url": "/sample_report.pdf",
            "price_amount": 1500,
            "is_premium": True,
        },
        {
            "id": str(uuid.uuid4()),
            "title": "Sentiment Analysis of Social Media",
            "image_url": "/placeholder.svg",
            "description": "Performed sentiment analysis on Twitter data to gauge public opinion on a new product launch.",
            "full_description": "Using Python and the NLTK library, this project analyzed thousands of tweets to determine public sentiment towards a new product. The results were visualized using Matplotlib and provided valuable feedback to the marketing team.",
            "tools": ["Python", "NLTK", "Matplotlib"],
            "project_url": "#",
            "report_file_url": "/sample_report.pdf",
            "price_amount": 0,
            "is_premium": False,
        },
    ]
    search_query: str = ""
    tool_filter: str = ""
    current_project_id: str = ""
    client_secret: str = ""
    payment_status: str = ""

    @rx.var
    def filtered_projects(self) -> list[Project]:
        """Return a list of projects filtered by search query and tool."""
        projects = self.projects
        if self.search_query:
            projects = [
                p
                for p in projects
                if self.search_query.lower() in p["title"].lower()
                or self.search_query.lower() in p["description"].lower()
            ]
        if self.tool_filter:
            projects = [p for p in projects if self.tool_filter in p["tools"]]
        return projects

    @rx.var
    def all_tools(self) -> list[str]:
        """Return a list of all unique tools used in projects."""
        tools = set()
        for project in self.projects:
            tools.update(project["tools"])
        return sorted(list(tools))

    @rx.var
    def current_project(self) -> Project | None:
        if not self.current_project_id:
            return None
        for p in self.projects:
            if p["id"] == self.current_project_id:
                return p
        return None

    @rx.event
    def set_tool_filter(self, tool: str):
        if self.tool_filter == tool:
            self.tool_filter = ""
        else:
            self.tool_filter = tool

    @rx.event
    def load_project_details(self, project_id: str):
        self.current_project_id = project_id
        self.client_secret = ""
        self.payment_status = ""

    @rx.event
    async def create_payment_intent(self):
        if not self.current_project or not self.current_project["is_premium"]:
            return
        stripe.api_key = os.getenv("STRIPE_API_KEY")
        if not stripe.api_key:
            self.payment_status = "error_config"
            return
        try:
            intent = stripe.PaymentIntent.create(
                amount=self.current_project["price_amount"],
                currency="usd",
                metadata={"project_id": self.current_project_id},
            )
            self.client_secret = intent.client_secret
            self.payment_status = "succeeded"
        except Exception as e:
            logging.exception(e)
            self.payment_status = "error_payment"

    @rx.event
    def add_project(self, project_data: dict):
        project_data["id"] = str(uuid.uuid4())
        self.projects.insert(0, project_data)

    @rx.event
    def delete_project(self, project_id: str):
        self.projects = [p for p in self.projects if p["id"] != project_id]
        return rx.redirect("/dashboard/projects")