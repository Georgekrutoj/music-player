import flet as ft

from objects.musicrow import MusicRow

from constants import TITLE
from constants import THEME


def main(page: ft.Page) -> None:
    page.title = TITLE
    page.theme_mode = THEME
    page.add(ft.Row(
            [
                MusicRow("Du Hast", "RAMMSTEIN"),
                MusicRow("Нон Стоп", "Пошлая Молли")
            ]
        )
    )

    page.add(ft.Text("Hello"))

    page.update()


ft.app(main)
