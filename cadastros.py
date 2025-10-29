import flet as ft
from db import obter_cadastros

def CadastrosView(page: ft.Page):
    # Obter os cadastros do banco
    cadastros = obter_cadastros()

    # Montar lista de cadastros
    if cadastros:
        lista_cadastros = [
            ft.Card(
                content=ft.Container(
                    padding=10,
                    content=ft.Column(
                        [
                            ft.Text(f"🆔 ID: {cadastro[0]}", size=12, color="gray"),
                            ft.Text(f"👤 Nome: {cadastro[1]}", size=16, weight="bold"),
                            ft.Text(f"📧 Email: {cadastro[2]}", size=14),
                        ],
                        spacing=3,
                    ),
                ),
            )
            for cadastro in cadastros
        ]
    else:
        lista_cadastros = [ft.Text("Nenhum cadastro encontrado.", color="gray")]

    # Tela principal
    return ft.View(
        "/cadastros",
        [
            ft.AppBar(title=ft.Text("Cadastro de Usuário"), bgcolor="yellow"),
            ft.Container(
                expand=True,
                padding=20,
                content=ft.Column(
                    [
                        ft.Text("Lista de Cadastros", size=22, weight="bold", color="red"),
                        ft.Column(lista_cadastros, scroll=ft.ScrollMode.ALWAYS),
                        ft.ElevatedButton(
                            text="Voltar para Home",
                            icon=ft.Icons.HOME,
                            bgcolor="blue",
                            color="white",
                            on_click=lambda e: page.go("/"),
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15,
                ),
            ),
        ],
    )
