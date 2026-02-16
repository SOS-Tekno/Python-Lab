import flet as ft
def main(page: ft.Page):
    page.title = "Python Labs | Learning Python"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.Text("Olá mundo Python, com o Flet!"),
    )
ft.run(main)