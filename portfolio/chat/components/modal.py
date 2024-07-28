import reflex as rx
from ..state import ChatState


def modal() -> rx.Component:
    """A modal to create a new chat."""
    return rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.modal_header(
                    rx.hstack(
                        rx.text("Create new chat"),
                        rx.icon(
                            tag="close",
                            font_size="sm",
                            on_click=ChatState.toggle_modal,
                            color="#fff8",
                            _hover={"color": "#fff"},
                            cursor="pointer",
                        ),
                        align_items="center",
                        justify_content="space-between",
                    )
                ),
                rx.modal_body(
                    rx.input(
                        placeholder="Type something...",
                        on_blur=ChatState.set_new_chat_name,
                        bg="#222",
                        border_color="#fff3",
                        _placeholder={"color": "#fffa"},
                    ),
                ),
                rx.modal_footer(
                    rx.button(
                        "Create",
                        bg="#5535d4",
                        box_shadow="md",
                        px="4",
                        py="2",
                        h="auto",
                        _hover={"bg": "#4c2db3"},
                        on_click=ChatState.create_chat,
                    ),
                ),
                bg="#222",
                color="#fff",
            ),
        ),
        is_open=ChatState.modal_open,
    )