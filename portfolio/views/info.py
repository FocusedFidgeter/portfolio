import reflex as rx

from portfolio.components.heading import heading
from portfolio.components.info_detail import info_detail
from portfolio.data import Info
from portfolio.styles.styles import Size


def info(title: str, info: list[Info]) -> rx.Component:
    return rx.vstack(
        heading(title),
        rx.vstack(
            *[
                info_detail(item)
                for item in info
            ],
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
