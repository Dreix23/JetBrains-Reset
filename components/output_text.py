import flet as ft

class OutputText(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.text_field = ft.TextField(
            multiline=True,
            read_only=True,
            text_size=12,
            min_lines=8,
            max_lines=8,
            color=ft.colors.GREEN_400,
            border_color=ft.colors.GREY_700,
            bgcolor=ft.colors.BLACK,
            height=130
        )

    def build(self):
        return self.text_field

    def show_text(self, text):
        self.text_field.value += text + "\n"
        self.text_field.update()

    def clear(self):
        self.text_field.value = ""
        self.text_field.update()
