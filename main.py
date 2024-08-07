import flet as ft
import json
from random import choice

class ThemeIcon(ft.IconButton):
    def __init__(self, page: ft.Page, icon):
        super().__init__(icon)
        self.on_click = self.change_theme
        self.icon = icon
        self.page = page
    
    def change_theme(self, e):
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.update()

def load_data():
    with open("data.json", encoding="utf-8", mode="r") as f:
        q = json.loads(f.read())
        tovar = q["yml_catalog"]["shop"]["offers"]["offer"]

srcs = [
    "http://ext.uniel.shop/p/6c123300-7a8b-11e6-8129-0cc47aa9a551.jpg",
    "http://ext.uniel.shop/p/3673b289-27f1-11e6-80f5-0cc47aa9a551.jpg",
    "http://ext.uniel.shop/p/b30f0b5b-abcb-11e6-813f-0cc47aa9a551.jpg"
]

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

    # ----------------------- Market ---------------------------------
    cards = ft.GridView(
        expand=1,
        runs_count=2,
        max_extent=400,
        child_aspect_ratio=0.6,
        spacing=5,
        run_spacing=5,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS_WITH_SAVE_LAYER
    )
    for i in range(10):
        cards.controls.append(
            ft.Container(
            content=ft.Column(
                [
                    ft.Image(src=choice(srcs), width=400, height=300),
                    ft.ListTile(
                        title=ft.Text("TLD-536 White/LED/250Lm/5500K/Dimmer Светильник настольный с ночником RGB и календарем, 4W. Встроенный аккумулятор 1200mAh. Сенсорный выключатель. Белый. TM Uniel"[:33] + "..."),
                        subtitle=ft.Text("Подробнее...")
                    ),
                    ft.Divider(),
                    ft.Row(
                        [
                            ft.ElevatedButton("Заказать сейчас", ft.Icon(ft.icons.MONEY)),
                            ft.OutlinedButton("В корзину", ft.Icon(ft.icons.SHOPPING_BASKET)),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ]
            ),
            padding=10,
            width=400,
            border=ft.Border(*[ft.BorderSide(1, "grey")]*4),
            border_radius=ft.BorderRadius(*[10]*4),
            on_click=lambda e: print("test")
        )
        )
    page.add(
        cards
    )



ft.app(main)