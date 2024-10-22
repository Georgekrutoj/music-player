import flet as ft


class MusicRow(ft.Row):
    def __init__(
            self,
            music_name: str,
            author: str
    ) -> None:
        super().__init__()

        self.controls.extend(
            [
                ft.Text(music_name),
                ft.Text(author)
            ]
        )
