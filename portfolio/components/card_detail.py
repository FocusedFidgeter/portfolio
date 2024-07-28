import reflex as rx
from portfolio.data import Extra

from portfolio.styles.styles import IMAGE_HEIGHT, Size


def card_detail(extra: Extra) -> rx.Component:
    return rx.card(
        rx.link(
            rx.inset(
                rx.image(
                    src=extra.image,
                    height=IMAGE_HEIGHT,
                    width="100%",
                    object_fit="cover"
                ),
                pb=Size.DEFAULT.value
            ),
            rx.text.strong(extra.title),
            rx.text(
                rx.markdown(extra.description),
                size=Size.SMALL.value,
                color_scheme="gold"
            )
        ),
        width="100%",
        href=extra.url,
        is_external=True
    )
