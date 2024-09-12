import flet as ft

class ProductList(ft.UserControl):
    def __init__(self, products):
        super().__init__()
        self.products = products

    def build(self):
        product_list = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=150,
            child_aspect_ratio=1.2,
            spacing=10,
            run_spacing=10
        )

        for product in self.products:
            checkbox = ft.Checkbox(
                value=product.get('selected', False),
                on_change=lambda e, p=product: self.update_product_selection(e, p)
            )
            product_list.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Container(
                            content=ft.Image(src=f"/icons/{product['icon']}", width=60, height=60),
                            alignment=ft.alignment.center
                        ),
                        ft.Row([
                            ft.Text(product['name'], size=12, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, expand=1),
                            checkbox
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                    ], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                    border=ft.border.all(1, ft.colors.GREY_400),
                    border_radius=10,
                    padding=10,
                    bgcolor=ft.colors.GREY_900,
                    ink=True,
                    tooltip=f"Restablecer {product['name']}"
                )
            )

        return product_list

    def update_product_selection(self, e, product):
        product['selected'] = e.control.value
        self.update()
