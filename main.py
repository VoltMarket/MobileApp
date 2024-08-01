import flet as ft

class ThemeIcon(ft.IconButton):
    def __init__(self, page: ft.Page, icon):
        super().__init__(icon)
        self.on_click = self.change_theme
        self.icon = icon
        self.page = page
    
    def change_theme(self, e):
        print("hello test")
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.update()

def main(page: ft.Page):
    page.platform = ft.PagePlatform.IOS
    page.title = "VoltMarket"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()

    # def change_theme(e):
    #     if page.theme_mode == ft.ThemeMode.LIGHT:
    #         page.theme_mode = ft.ThemeMode.DARK
    #     else:
    #         page.theme_mode = ft.ThemeMode.LIGHT
    #     page.update()

    drawer = ft.NavigationDrawer(
        on_change=lambda e: print(dir(e)),
        on_dismiss=lambda e: print(type(e)),
        controls=[
            ft.NavigationDrawerDestination("Главная", icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME),
            ft.NavigationDrawerDestination("Контакты", icon=ft.icons.PHONE_OUTLINED, selected_icon=ft.icons.PHONE),
            ft.NavigationDrawerDestination("О нас", icon=ft.icons.INFO_OUTLINE, selected_icon=ft.icons.INFO)
        ]
    )

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
    page.add(ft.Text("test"))

ft.app(main)