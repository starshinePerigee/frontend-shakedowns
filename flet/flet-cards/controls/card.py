from math import pi

import flet as ft

from game import value_to_face


FACE_CARDS = {1: "A", 11: "J", 12: "Q", 13: "K"}


def value_to_face(value: int):
    return FACE_CARDS.get(value, value)


class PCard(ft.Card):
    def __init__(self, value: int):
        super().__init__()
        container = ft.Container()
        self.content = container

        container.width = 100
        container.height = 150
        container.padding = 10

        column = ft.Column()
        container.content = column

        column.alignment = ft.MainAxisAlignment.SPACE_BETWEEN

        face = value_to_face(value)

        top = ft.Row()
        column.controls.append(top)
        top_text = ft.Text(face)
        top.controls = [top_text]

        middle = ft.Row()
        column.controls.append(middle)
        middle_text = ft.Text(face)
        middle.controls = [middle_text]
        middle.alignment = ft.MainAxisAlignment.CENTER
        middle_text.size = 42
        middle_text.weight = ft.FontWeight.W_600
        middle_text.text_align = ft.TextAlign.CENTER

        bottom = ft.Row()
        column.controls.append(bottom)
        bottom_text = ft.Text(face)
        bottom.controls = [bottom_text]
        bottom.alignment = ft.MainAxisAlignment.END
        bottom_text.rotate = pi
