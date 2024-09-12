import flet as ft
from components.product_list import ProductList
from components.output_text import OutputText
from widgets.start_button import StartButton

class TrialResetView:
    def __init__(self, controller):
        self.controller = controller
        self.text_output = None

    def main(self, page: ft.Page):
        page.title = "JetBrains IDE Trial Reset"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 20
        page.window.width = 800
        page.window.height = 660
        page.window.resizable = False
        page.window.center()

        product_list = ProductList(self.controller.products)
        self.text_output = OutputText()
        start_button = StartButton(self.on_start)

        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text("JetBrains IDE Trial Reset", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_400),
                    ft.Text("Selecciona los IDEs que deseas restablecer y haz clic en 'Iniciar'", size=14, color=ft.colors.GREY_400),
                    product_list,
                    self.text_output,
                    ft.Row([start_button], alignment=ft.MainAxisAlignment.END)
                ], spacing=20),
                padding=20,
                bgcolor=ft.colors.GREY_900,
                border_radius=10
            )
        )

    def on_start(self, e):
        self.text_output.clear()
        selected_products = [p["name"] for p in self.controller.products if p.get("selected", False)]
        if self.controller.os_name == "windows":
            output = self.controller.reset_product_windows()
        elif self.controller.os_name == "linux":
            output = self.controller.reset_product_linux(selected_products)
        elif self.controller.os_name == "darwin":
            output = "macOS no está disponible."
        else:
            output = "Sistema operativo no reconocido"
        self.text_output.show_text(output)
