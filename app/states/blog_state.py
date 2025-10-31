import reflex as rx
import uuid
from typing import TypedDict
import datetime


class BlogPost(TypedDict):
    id: str
    title: str
    author: str
    content: str
    created_at: str
    image_url: str
    tags: list[str]
    category: str


class BlogState(rx.State):
    """State for managing the blog."""

    posts: list[BlogPost] = [
        {
            "id": str(uuid.uuid4()),
            "title": "The Art of Data Storytelling",
            "author": "Emilia",
            "content": "Data storytelling is the practice of building a narrative around a set-of-data and its accompanying visualizations to help convey the meaning of that data in a powerful and compelling fashion. This article explores the key elements of effective data storytelling...",
            "created_at": datetime.datetime(2024, 7, 15).isoformat(),
            "image_url": "/placeholder.svg",
            "tags": ["Data Visualization", "Communication"],
            "category": "Data Science",
        },
        {
            "id": str(uuid.uuid4()),
            "title": "A Deep Dive into Statistical Significance",
            "author": "Emilia",
            "content": "What does it really mean for a result to be statistically significant? We'll break down p-values, confidence intervals, and common misconceptions in hypothesis testing. A must-read for any aspiring analyst...",
            "created_at": datetime.datetime(2024, 6, 28).isoformat(),
            "image_url": "/placeholder.svg",
            "tags": ["Statistics", "Hypothesis Testing"],
            "category": "Statistics",
        },
        {
            "id": str(uuid.uuid4()),
            "title": "My First Machine Learning Model: A Beginner's Journey",
            "author": "Emilia",
            "content": "Follow along as I document the process of building my very first predictive model. From data cleaning and feature engineering to model selection and evaluation, I share my challenges, learnings, and results...",
            "created_at": datetime.datetime(2024, 5, 10).isoformat(),
            "image_url": "/placeholder.svg",
            "tags": ["Machine Learning", "Python", "Tutorial"],
            "category": "Machine Learning",
        },
    ]
    search_query: str = ""
    category_filter: str = ""
    tag_filter: str = ""
    current_post_id: str = ""

    @rx.var
    def sorted_posts(self) -> list[BlogPost]:
        """Return blog posts sorted by creation date."""
        return sorted(self.posts, key=lambda p: p["created_at"], reverse=True)

    @rx.var
    def filtered_posts(self) -> list[BlogPost]:
        """Return a list of posts filtered by search, category, and tag."""
        posts = self.sorted_posts
        if self.search_query:
            posts = [
                p
                for p in posts
                if self.search_query.lower() in p["title"].lower()
                or self.search_query.lower() in p["content"].lower()
            ]
        if self.category_filter:
            posts = [p for p in posts if p["category"] == self.category_filter]
        if self.tag_filter:
            posts = [p for p in posts if self.tag_filter in p["tags"]]
        return posts

    @rx.var
    def featured_posts(self) -> list[BlogPost]:
        """Return the 3 most recent blog posts."""
        return self.sorted_posts[:3]

    @rx.var
    def all_categories(self) -> list[str]:
        """Return a list of all unique categories."""
        return sorted(list(set((p["category"] for p in self.posts))))

    @rx.var
    def all_tags(self) -> list[str]:
        """Return a list of all unique tags."""
        tags = set()
        for post in self.posts:
            tags.update(post["tags"])
        return sorted(list(tags))

    @rx.var
    def current_post(self) -> BlogPost | None:
        if not self.current_post_id:
            return None
        for p in self.posts:
            if p["id"] == self.current_post_id:
                return p
        return None

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def set_category_filter(self, category: str):
        if self.category_filter == category:
            self.category_filter = ""
        else:
            self.category_filter = category

    @rx.event
    def set_tag_filter(self, tag: str):
        if self.tag_filter == tag:
            self.tag_filter = ""
        else:
            self.tag_filter = tag

    @rx.event
    def load_post_details(self, post_id: str):
        self.current_post_id = post_id

    @rx.event
    def add_post(self, post_data: dict):
        new_post = BlogPost(
            id=str(uuid.uuid4()),
            title=post_data.get("title", ""),
            author=post_data.get("author", "Emilia"),
            content=post_data.get("content", ""),
            created_at=datetime.datetime.now().isoformat(),
            image_url=post_data.get("image_url", "/placeholder.svg"),
            tags=post_data.get("tags", []),
            category=post_data.get("category", "General"),
        )
        self.posts.insert(0, new_post)

    @rx.event
    def update_post(self, post_data: dict):
        post_id = post_data.get("id")
        for i, post in enumerate(self.posts):
            if post["id"] == post_id:
                self.posts[i]["title"] = post_data.get("title", post["title"])
                self.posts[i]["content"] = post_data.get("content", post["content"])
                break

    @rx.event
    def delete_post(self, post_id: str):
        self.posts = [p for p in self.posts if p["id"] != post_id]