import flet as ft


def main(page: ft.Page):

    def add_clicked(e):
        checkbox = ft.Checkbox(label=new_task.value)

        def checked(e):
            checkbox.disabled = True
            page.update()

        checkbox.on_change = checked
        page.add(checkbox)
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="What's needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))


ft.app(main)
