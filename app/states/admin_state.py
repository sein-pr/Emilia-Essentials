import reflex as rx
from typing import Optional
import os
from app.states.state import State


class AdminState(rx.State):
    """State for managing admin dashboard functionality."""

    upload_error: str = ""

    async def _handle_file_upload(self, file: rx.UploadFile, target_var: str):
        upload_data = await file.read()
        upload_dir = rx.get_upload_dir()
        upload_dir.mkdir(parents=True, exist_ok=True)
        file_path = upload_dir / file.name
        with file_path.open("wb") as f:
            f.write(upload_data)
        main_state = await self.get_state(State)
        setattr(main_state, target_var, file.name)

    @rx.event
    async def handle_profile_photo_upload(self, files: list[rx.UploadFile]):
        if not files:
            self.upload_error = "No file selected."
            return
        await self._handle_file_upload(files[0], "profile_photo")
        self.upload_error = ""
        return rx.toast.success("Profile photo updated.")

    @rx.event
    async def handle_cv_upload(self, files: list[rx.UploadFile]):
        if not files:
            self.upload_error = "No file selected."
            return
        await self._handle_file_upload(files[0], "cv_file")
        self.upload_error = ""
        return rx.toast.success("CV uploaded.")

    @rx.event
    async def handle_cover_letter_upload(self, files: list[rx.UploadFile]):
        if not files:
            self.upload_error = "No file selected."
            return
        await self._handle_file_upload(files[0], "cover_letter_file")
        self.upload_error = ""
        return rx.toast.success("Cover letter uploaded.")

    @rx.event
    async def save_profile_changes(self, form_data: dict):
        main_state = await self.get_state(State)
        main_state.name = form_data.get("name", main_state.name)
        main_state.tagline = form_data.get("tagline", main_state.tagline)
        main_state.bio = form_data.get("bio", main_state.bio)
        return rx.toast.success("Profile changes saved!")

    @rx.event
    async def save_education(self, form_data: dict):
        main_state = await self.get_state(State)
        main_state.education_university = form_data.get(
            "education_university", main_state.education_university
        )
        main_state.education_major = form_data.get(
            "education_major", main_state.education_major
        )
        main_state.education_year = form_data.get(
            "education_year", main_state.education_year
        )
        return rx.toast.success("Education details saved!")

    @rx.event
    async def save_social_links(self, form_data: dict):
        main_state = await self.get_state(State)
        main_state.social_linkedin = form_data.get(
            "social_linkedin", main_state.social_linkedin
        )
        main_state.social_github = form_data.get(
            "social_github", main_state.social_github
        )
        main_state.social_kaggle = form_data.get(
            "social_kaggle", main_state.social_kaggle
        )
        main_state.social_email = form_data.get("social_email", main_state.social_email)
        main_state.social_twitter = form_data.get(
            "social_twitter", main_state.social_twitter
        )
        return rx.toast.success("Social links updated!")

    @rx.event
    async def add_skill(self):
        main_state = await self.get_state(State)
        main_state.skills.append({"name": "New Skill", "level": 50})

    @rx.event
    async def remove_skill(self, index: int):
        main_state = await self.get_state(State)
        if 0 <= index < len(main_state.skills):
            main_state.skills.pop(index)

    @rx.event
    async def update_skill_name(self, index: int, name: str):
        main_state = await self.get_state(State)
        if 0 <= index < len(main_state.skills):
            main_state.skills[index]["name"] = name

    @rx.event
    async def update_skill_level(self, index: int, level: str):
        import logging

        main_state = await self.get_state(State)
        if 0 <= index < len(main_state.skills):
            try:
                main_state.skills[index]["level"] = int(level)
            except ValueError as e:
                logging.exception(f"Error updating skill level: {e}")