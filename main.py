import flet as ft

def main(page: ft.Page):
    page.title = "from Laptop"
    page.add(ft.Text("test for Leonid"))

# test

ft.app(target=main)