import reflex as rx
from app.states.state import State
from app.states.admin_state import AdminState
from app.pages.dashboard import dashboard_layout


def profile_form() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            rx.el.label("Full Name", class_name="text-sm font-medium text-[#EEEEEE]"),
            rx.el.input(
                name="name",
                default_value=State.name,
                class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
            ),
            class_name="space-y-2",
        ),
        rx.el.div(
            rx.el.label("Tagline", class_name="text-sm font-medium text-[#EEEEEE]"),
            rx.el.input(
                name="tagline",
                default_value=State.tagline,
                class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
            ),
            class_name="space-y-2",
        ),
        rx.el.div(
            rx.el.label("Bio", class_name="text-sm font-medium text-[#EEEEEE]"),
            rx.el.textarea(
                name="bio",
                default_value=State.bio,
                class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
                rows=4,
            ),
            class_name="space-y-2",
        ),
        rx.el.button(
            "Save Changes",
            type="submit",
            class_name="bg-[#00ADB5] text-white px-6 py-2 rounded-lg hover:bg-teal-600 transition-colors",
        ),
        on_submit=AdminState.save_profile_changes,
        class_name="space-y-6 bg-[#222831] p-6 rounded-lg",
    )


def file_upload_component(
    title: str, file_var: rx.Var, handler: rx.event.EventHandler, upload_id: str
) -> rx.Component:
    return rx.el.div(
        rx.el.h3(title, class_name="text-lg font-bold text-white mb-2"),
        rx.upload.root(
            rx.el.div(
                rx.icon(tag="cloud_upload", class_name="w-8 h-8 text-[#00ADB5]"),
                rx.el.p("Click or drag to select file"),
                class_name="flex flex-col items-center justify-center p-4 border-2 border-dashed border-[#393E46] rounded-lg cursor-pointer hover:bg-[#2a2f38]",
            ),
            id=upload_id,
            multiple=False,
            accept={
                "application/pdf": [".pdf"],
                "application/msword": [".doc"],
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document": [
                    ".docx"
                ],
                "image/png": [".png"],
                "image/jpeg": [".jpg", ".jpeg"],
            },
            class_name="w-full",
        ),
        rx.foreach(rx.selected_files(upload_id), lambda file: rx.el.div(rx.el.p(file))),
        rx.el.button(
            "Upload",
            on_click=handler(rx.upload_files(upload_id=upload_id)),
            class_name="mt-2 bg-[#00ADB5] text-white px-4 py-2 rounded-lg hover:bg-teal-600 text-sm",
        ),
        rx.cond(
            file_var != "",
            rx.el.div(
                rx.el.p("Current file:"),
                rx.el.a(
                    file_var,
                    href=rx.get_upload_url(file_var),
                    target="_blank",
                    class_name="text-[#00ADB5] hover:underline",
                ),
                class_name="text-sm mt-2 text-white",
            ),
            None,
        ),
        class_name="bg-[#222831] p-6 rounded-lg",
    )


def skills_editor() -> rx.Component:
    return rx.el.div(
        rx.el.h3("Skills Editor", class_name="text-lg font-bold text-white mb-4"),
        rx.el.div(
            rx.foreach(
                State.skills,
                lambda skill, index: rx.el.div(
                    rx.el.input(
                        on_change=lambda val: AdminState.update_skill_name(index, val),
                        placeholder="Skill Name",
                        class_name="w-1/3 px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
                        default_value=skill["name"],
                    ),
                    rx.el.input(
                        type="range",
                        default_value=skill["level"].to_string(),
                        on_change=lambda level: AdminState.update_skill_level(
                            index, level
                        ).throttle(50),
                        min=0,
                        max=100,
                        key=f"skill-level-{index}",
                        class_name="w-1/3 accent-[#00ADB5]",
                    ),
                    rx.el.p(
                        f"{skill['level']}%", class_name="text-white w-12 text-center"
                    ),
                    rx.el.button(
                        rx.icon("trash-2", class_name="w-4 h-4"),
                        on_click=lambda: AdminState.remove_skill(index),
                        class_name="text-red-400 hover:text-red-600",
                    ),
                    class_name="flex items-center gap-4 w-full",
                ),
            ),
            class_name="space-y-4",
        ),
        rx.el.button(
            "Add Skill",
            on_click=AdminState.add_skill,
            class_name="mt-4 bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 text-sm",
        ),
        class_name="bg-[#222831] p-6 rounded-lg",
    )


def education_form() -> rx.Component:
    return rx.el.form(
        rx.el.h3("Education", class_name="text-lg font-bold text-white mb-4"),
        rx.el.div(
            rx.el.label("University", class_name="text-sm font-medium text-[#EEEEEE]"),
            rx.el.input(
                name="education_university",
                default_value=State.education_university,
                class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
            ),
            class_name="space-y-2",
        ),
        rx.el.div(
            rx.el.label("Major", class_name="text-sm font-medium text-[#EEEEEE]"),
            rx.el.input(
                name="education_major",
                default_value=State.education_major,
                class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
            ),
            class_name="space-y-2",
        ),
        rx.el.div(
            rx.el.label(
                "Graduation Year", class_name="text-sm font-medium text-[#EEEEEE]"
            ),
            rx.el.input(
                name="education_year",
                default_value=State.education_year,
                class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
            ),
            class_name="space-y-2",
        ),
        rx.el.button(
            "Save Education",
            type="submit",
            class_name="mt-4 bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 text-sm",
        ),
        on_submit=AdminState.save_education,
        class_name="space-y-4 bg-[#222831] p-6 rounded-lg",
    )


def social_links_form() -> rx.Component:
    return rx.el.form(
        rx.el.h3("Social Links", class_name="text-lg font-bold text-white mb-4"),
        rx.el.div(
            rx.el.label("LinkedIn", class_name="text-sm font-medium text-[#EEEEEE]"),
            rx.el.input(
                name="social_linkedin",
                default_value=State.social_linkedin,
                class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
            ),
        ),
        rx.el.div(
            rx.el.label("GitHub", class_name="text-sm font-medium text-[#EEEEEE]"),
            rx.el.input(
                name="social_github",
                default_value=State.social_github,
                class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
            ),
        ),
        rx.el.div(
            rx.el.label("Kaggle", class_name="text-sm font-medium text-[#EEEEEE]"),
            rx.el.input(
                name="social_kaggle",
                default_value=State.social_kaggle,
                class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
            ),
        ),
        rx.el.div(
            rx.el.label("Email", class_name="text-sm font-medium text-[#EEEEEE]"),
            rx.el.input(
                name="social_email",
                default_value=State.social_email,
                class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
            ),
        ),
        rx.el.div(
            rx.el.label("Twitter", class_name="text-sm font-medium text-[#EEEEEE]"),
            rx.el.input(
                name="social_twitter",
                default_value=State.social_twitter,
                class_name="mt-1 w-full px-3 py-2 rounded-lg border border-[#393E46] bg-[#222831] text-white focus:border-[#00ADB5] focus:ring-[#00ADB5]",
            ),
        ),
        rx.el.button(
            "Save Social Links",
            type="submit",
            class_name="mt-4 bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 text-sm",
        ),
        on_submit=AdminState.save_social_links,
        class_name="space-y-4 bg-[#222831] p-6 rounded-lg",
    )


def profile_dashboard_page() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.h2("Edit Profile", class_name="text-xl font-bold text-white mb-6"),
            rx.el.div(
                rx.el.div(
                    profile_form(),
                    skills_editor(),
                    education_form(),
                    class_name="space-y-6",
                ),
                rx.el.div(
                    file_upload_component(
                        "Profile Photo",
                        State.profile_photo,
                        AdminState.handle_profile_photo_upload,
                        "profile-photo-upload",
                    ),
                    social_links_form(),
                    class_name="space-y-6",
                ),
                class_name="grid md:grid-cols-2 gap-6",
            ),
        )
    )