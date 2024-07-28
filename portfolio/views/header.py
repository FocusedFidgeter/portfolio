import reflex as rx
from portfolio.components.heading import heading
from portfolio.components.media import media
from portfolio.data import Data
from portfolio.styles.styles import Size


def header(data: Data) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src=data.avatar,
            size=Size.BIG.value
        ),
        rx.hstack(
            rx.vstack(
                heading(data.name, True),
                heading(data.skill),
                rx.hstack(
                    rx.icon("map-pin"),
                    data.location,
                    spacing=Size.SMALL.value,
                    display="inherit"
                ),
                media(data.media),
                spacing=Size.SMALL.value,
            ),
            
            spacing=Size.DEFAULT.value,
        ),
        spacing=Size.DEFAULT.value,
    )
