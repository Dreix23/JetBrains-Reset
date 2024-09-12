import flet as ft

class StartButton(ft.UserControl):
    def __init__(self, on_click):
        super().__init__()
        self.on_click = on_click

    def build(self):
        return ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Text("Iniciar", size=18, weight=ft.FontWeight.BOLD),
                    ft.ProgressRing(visible=False, width=16, height=16, stroke_width=2)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            style=ft.ButtonStyle(
                color={
                    ft.ControlState.HOVERED: ft.colors.WHITE,
                    ft.ControlState.DEFAULT: ft.colors.BLACK,
                },
                bgcolor={
                    ft.ControlState.HOVERED: ft.colors.GREEN_400,
                    ft.ControlState.DEFAULT: ft.colors.GREEN_600,
                },
                padding=15,
                animation_duration=300,
                side={
                    ft.ControlState.DEFAULT: ft.BorderSide(2, ft.colors.GREEN_200),
                    ft.ControlState.HOVERED: ft.BorderSide(3, ft.colors.GREEN_400),
                },
            ),
            on_click=self.on_click
        )
