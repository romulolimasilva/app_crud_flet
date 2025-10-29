import flet as ft
from home import HomeView
from form_cadastro import FormCadastroView
from cadastros import CadastrosView
from editar_cadastros import EditarCadastrosView
from deletar_cadastros import DeletarCadastrosView

def main(page: ft.Page):
    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(HomeView(page))
        elif page.route == "/cadastro":
            page.views.append(FormCadastroView(page))
        elif page.route == "/cadastros":
            page.views.append(CadastrosView(page))
        elif page.route == "/editar_cadastros":
            page.views.append(EditarCadastrosView(page))
        elif page.route == "/deletar_cadastros":
            page.views.append(DeletarCadastrosView(page))
        page.update()

    page.on_route_change = route_change
    page.go(page.route)


ft.app(target=main, view=ft.WEB_BROWSER)