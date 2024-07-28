import reflex as rx
from portfolio.components.media import media
from portfolio.data import Media
from portfolio.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.text("Paul Devey, 2023"),
        media(data),
        spacing=Size.SMALL.value
    )
