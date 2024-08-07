import flet as ft
import json
from textwrap import wrap

current_page    = 1
global_offset   = 10

class ThemeIcon(ft.IconButton):
    def __init__(self, page: ft.Page, icon):
        super().__init__(icon)
        self.on_click = self.change_theme
        self.icon = icon
        self.page = page
    
    def change_theme(self, e):
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_400))
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.BLUE_400))
        self.page.update()


def load_data():
    with open("data.json", encoding="utf-8", mode="r") as f:
        q = json.loads(f.read())
        tovars = q["yml_catalog"]["shop"]["offers"]["offer"]
        return tovars


def change_page(e, paging: ft.CupertinoSlidingSegmentedButton, page: ft.Page, shop, cards):
    global current_page
    if e.data == "2":
        current_page += 1
    elif e.data == "0":
        current_page = max(1, current_page - 1)
    paging.controls[1] = ft.Text(str(current_page))
    paging.selected_index = 1
    set_page(page, shop, cards, global_offset, current_page)
    page.update()

def set_page(page: ft.Page, shop: list, cards: ft.Row, offset: int = 10, index: int = 1):
    cards.controls.clear()
    for i in shop[(index-1)*offset:index*offset]:
        title = i["description"][:33] if i["description"] else i["fullname"][:33] + "..."
        title = "\n".join(wrap(title, 15))
        cards.controls.append(
            ft.Container(
                content=ft.Column([

                    ft.Row(
                        [
                            ft.Image(src=i["picture"], width=150, border_radius=ft.BorderRadius(20, 20, 20, 20)),
                            ft.Column([
                                ft.ListTile(
                                    title=ft.Text(title, no_wrap=False),
                                    subtitle=ft.Text("Подробнее")
                                ),
                                ft.Row(
                                    [ft.Text("Цена: ", size=20), ft.Text(i["price"]+" руб", size=20)],
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                ),
                            ]),
                        ]
                    ),
                    ft.Divider(),
                    ft.Row(
                        [
                            ft.ElevatedButton("Заказать сейчас", ft.Icon(ft.icons.MONEY)),
                            ft.OutlinedButton("В корзину", ft.Icon(ft.icons.SHOPPING_BASKET)),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ]),
                adaptive=True,
                padding=10,
                width=530,
                border=ft.Border(*[ft.BorderSide(1, "grey")]*4),
                border_radius=ft.BorderRadius(*[10]*4),
                on_click=lambda e: print(e.target),
            )
        )
    page.update()


def market(page: ft.page):
    global current_page
    shop = load_data()
    page.title = "VoltMarket"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()

    drawer = ft.NavigationDrawer(
        on_change=lambda e: print(dir(e)),
        on_dismiss=lambda e: print(type(e)),
        controls=[
            ft.NavigationDrawerDestination("Главная", icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME),
            ft.NavigationDrawerDestination("Контакты", icon=ft.icons.PHONE_OUTLINED, selected_icon=ft.icons.PHONE),
            ft.NavigationDrawerDestination("О нас", icon=ft.icons.INFO_OUTLINE, selected_icon=ft.icons.INFO)
        ]
    )


    # ----------------------- Market ---------------------------------

    cards = ft.Row(
        wrap=True,
        expand=True,
        scroll="always",
        alignment=ft.MainAxisAlignment.CENTER,
        width=4000
    )
    set_page(page, shop, cards, global_offset)
    page.add(cards)

    pagination = ft.CupertinoSlidingSegmentedButton(
            selected_index=1,
            thumb_color=ft.colors.ORANGE_400,
            on_change=lambda e: change_page(e, pagination, page, shop, cards),
            padding=ft.padding.symmetric(0, 10),
            controls=[
                ft.Icon(ft.icons.ARROW_LEFT),
                ft.Text(str(current_page)),
                ft.Icon(ft.icons.ARROW_RIGHT),
            ],
        )


    page.add(
        ft.Row([pagination], alignment=ft.MainAxisAlignment.CENTER)
    )