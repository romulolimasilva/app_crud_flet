import flet as ft
from db import obter_cadastros, deletar_cadastro


def DeletarCadastrosView(page: ft.Page):
    # Função chamada ao clicar no botão "Deletar"
    def deletar_click(e, cadastro_id):
        deletar_cadastro(cadastro_id)
        page.snack_bar = ft.SnackBar(ft.Text("Cadastro deletado com sucesso!"), bgcolor="green")
        page.snack_bar.open = True
        page.update()
        carregar_cadastros()  # Atualiza a lista na tela

    # Função para carregar e montar os cadastros
    def carregar_cadastros():
        cadastros = obter_cadastros()
        lista_cadastros.controls.clear()

        if cadastros:
            for cadastro in cadastros:
                id_cadastro, nome, email = cadastro
                lista_cadastros.controls.append(
                    ft.Card(
                        content=ft.Container(
                            padding=10,
                            content=ft.Column(
                                [
                                    ft.Text(f"🆔 ID: {id_cadastro}", size=12, color="gray"),
                                    ft.Text(f"👤 Nome: {nome}", size=16, weight="bold"),
                                    ft.Text(f"📧 Email: {email}", size=14),
                                    ft.Row(
                                        [
                                            ft.ElevatedButton(
                                                text="🗑️ Deletar",
                                                bgcolor="red",
                                                color="white",
                                                on_click=lambda e, id=id_cadastro: deletar_click(e, id),
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.END,
                                    ),
                                ],
                                spacing=5,
                            ),
                        ),
                    )
                )
        else:
            lista_cadastros.controls.append(ft.Text("Nenhum cadastro encontrado.", color="gray"))

        page.update()

    # Layout principal
    lista_cadastros = ft.Column(scroll=ft.ScrollMode.ALWAYS)

    view = ft.View(
        "/deletar_cadastros",
        [
            ft.AppBar(title=ft.Text("Deletar Cadastros"), bgcolor="red"),
            ft.Container(
                expand=True,
                padding=20,
                content=ft.Column(
                    [
                        ft.Text("Remover Cadastros", size=22, weight="bold", color="red"),
                        lista_cadastros,
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

    carregar_cadastros()
    return view
