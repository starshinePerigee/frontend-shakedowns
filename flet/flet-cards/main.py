import flet as ft

from controls.card import PCard


async def main(page: ft.Page):
    page.add(PCard(1))


ft.app(main)
