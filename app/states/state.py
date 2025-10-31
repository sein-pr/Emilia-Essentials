import reflex as rx
from typing import TypedDict


class Skill(TypedDict):
    name: str
    level: int


class Stat(TypedDict):
    value: str
    label: str


import reflex as rx
from typing import TypedDict, Optional
import zipfile
import os


class Skill(TypedDict):
    name: str
    level: int


class Stat(TypedDict):
    value: str
    label: str


class State(rx.State):
    """The main state for the app."""

    name: str = "Emilia Essentials"
    tagline: str = "Turning Numbers into Narratives"
    bio: str = "Statistics student at UNAM | Data Analyst in the making | Passionate about turning data into insights."
    profile_photo: str = "/placeholder.svg"
    cv_file: str = ""
    cover_letter_file: str = ""
    education_university: str = "UNAM"
    education_major: str = "Statistics"
    education_year: str = "2025"
    social_linkedin: str = "#"
    social_github: str = "#"
    social_kaggle: str = "#"
    social_email: str = "mailto:emilia@essentials.com"
    social_twitter: str = "#"
    skills: list[Skill] = [
        {"name": "Python", "level": 90},
        {"name": "R", "level": 85},
        {"name": "SQL", "level": 80},
        {"name": "Excel", "level": 95},
        {"name": "PowerBI", "level": 75},
        {"name": "Statistics", "level": 92},
    ]
    stats: list[Stat] = [
        {"value": "12+", "label": "Projects Completed"},
        {"value": "50+", "label": "Datasets Analyzed"},
        {"value": "100s", "label": "Insights Delivered"},
    ]

    @rx.event
    def download_profile_package(self) -> Optional[rx.event.EventSpec]:
        """Create and download a zip file of profile documents."""
        upload_dir = rx.get_upload_dir()
        zip_filename = "Emilia_Essentials_Profile_Package.zip"
        zip_filepath = upload_dir / zip_filename
        files_to_zip = []
        if self.cv_file and (upload_dir / self.cv_file).exists():
            files_to_zip.append(self.cv_file)
        if self.cover_letter_file and (upload_dir / self.cover_letter_file).exists():
            files_to_zip.append(self.cover_letter_file)
        if not files_to_zip:
            return rx.toast.error("No documents available to download.")
        with zipfile.ZipFile(zip_filepath, "w") as zipf:
            for file in files_to_zip:
                zipf.write(upload_dir / file, arcname=file)
        return rx.download(url=f"/{zip_filename}", filename=zip_filename)