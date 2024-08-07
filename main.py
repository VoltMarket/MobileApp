import flet as ft
from market import market, ThemeIcon

def navigations(page: ft.Page):
    # --------------------- AppBar -------------------------------

    page.appbar = ft.AppBar(
        title=ft.Text("VoltMarket"),
        center_title=False,
        leading=ft.IconButton(ft.icons.MENU, on_click=lambda e: page.open(drawer)), # ft.Image("/img/logo.jpg")
        bgcolor=ft.colors.ORANGE,
        actions=[
            ft.IconButton(ft.icons.SEARCH),
            ThemeIcon(page, ft.icons.SUNNY) # ft.IconButton(ft.icons.SUNNY, on_click=change_theme)
        ]
    )

    # ----------------------- NavigationBar -------------------------

    page.navigation_bar = ft.NavigationBar(destinations=[
        ft.NavigationBarDestination(icon=ft.icons.SHOP, label="Магазин"),
        ft.NavigationBarDestination(icon=ft.icons.LOGIN, label="Профиль")
    ], adaptive=True)


def main(page: ft.Page):
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.BLUE_400))

    navigations(page)
    market(page)
#

ft.app(main)