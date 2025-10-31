import reflex as rx
from app.states.state import State
from app.states.admin_state import AdminState
from app.pages.dashboard import dashboard_layout


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


def documents_dashboard_page() -> rx.Component:
    return dashboard_layout(
        rx.el.div(
            rx.el.h2(
                "Manage Documents", class_name="text-xl font-bold text-white mb-6"
            ),
            rx.el.div(
                file_upload_component(
                    "CV (PDF/DOCX)",
                    State.cv_file,
                    AdminState.handle_cv_upload,
                    "cv-upload",
                ),
                file_upload_component(
                    "Cover Letter (PDF/DOCX)",
                    State.cover_letter_file,
                    AdminState.handle_cover_letter_upload,
                    "cover-letter-upload",
                ),
                class_name="grid md:grid-cols-2 lg:grid-cols-3 gap-6",
            ),
        )
    )