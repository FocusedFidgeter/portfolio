"""The main Chat app."""

import reflex as rx
from .components.chat_component import chat_window, action_bar
from .components.navbar import navbar

def chat_page() -> rx.Component:
    """The main app.""" 
    
    return rx.vstack(
        navbar(),
        chat_window(),
        action_bar(),
        background_color=rx.color("mauve", 1),
        color=rx.color("mauve", 12),
        height="100vh",
        align_items="stretch",
        spacing="0",
    )
