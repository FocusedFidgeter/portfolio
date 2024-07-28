import reflex as rx
from portfolio.components.heading import heading
from portfolio.data import Technology
from portfolio.styles.styles import EmSize, Size


def tech_stack(technologies: list[Technology]) -> rx.Component:
    return rx.vstack(
        heading("Technology"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        class_name=technology.icon,
                        font_size="24px"
                    ),
                    rx.text(technology.name),
                    color_scheme="violet",
                    size="2"
                )
                for technology in technologies
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )
