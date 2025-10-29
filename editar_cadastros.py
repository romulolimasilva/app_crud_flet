import flet as ft
from db import obter_cadastros, editar_cadastro


def EditarCadastrosView(page: ft.Page):
    # Função chamada ao clicar no botão "Salvar"
    def salvar_edicao(e, id_cadastro, nome_field, email_field):
        novo_nome = nome_field.value.strip()
        novo_email = email_field.value.strip()

        if not novo_nome or not novo_email:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Preencha todos os campos!"), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return

        # Atualiza no banco
        editar_cadastro(id_cadastro, novo_nome, novo_email)

        # Exibe mensagem de sucesso
        page.snack_bar = ft.SnackBar(ft.Text("✅ Cadastro atualizado com sucesso!"), bgcolor="green")
        page.snack_bar.open = True
        page.update()

        # Limpa os campos
        nome_field.value = ""
        email_field.value = ""
        page.update()

        # Atualiza lista após um pequeno delay (para mostrar mensagem antes)
        page.timer = page.run_task(lambda: carregar_cadastros(), delay=1.5)

    # Função para carregar e montar os cadastros
    def carregar_cadastros():
        cadastros = obter_cadastros()
        lista_cadastros.controls.clear()

        if cadastros:
            for cadastro in cadastros:
                id_cadastro, nome, email = cadastro

                nome_field = ft.TextField(label="Nome", value=nome, width=250)
                email_field = ft.TextField(label="Email", value=email, width=250)

                lista_cadastros.controls.append(
                    ft.Card(
                        content=ft.Container(
                            padding=10,
                            content=ft.Column(
                                [
                                    ft.Text(f"🆔 ID: {id_cadastro}", size=12, color="yellow"),
                                    nome_field,
                                    email_field,
                                    ft.ElevatedButton(
                                        text="💾 Salvar Alterações",
                                        bgcolor="green",
                                        color="white",
                                        on_click=lambda e, id=id_cadastro, n=nome_field, em=email_field: salvar_edicao(e, id, n, em),
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

    # Lista inicial de cadastros
    lista_cadastros = ft.Column(scroll=ft.ScrollMode.ALWAYS)
    carregar_cadastros()

    # Layout principal
    return ft.View(
        "/editar_cadastros",
        [
            ft.AppBar(title=ft.Text("Editar Cadastro de Usuário"), bgcolor="yellow"),
            ft.Container(
                expand=True,
                padding=20,
                content=ft.Column(
                    [
                        ft.Text("Editar Cadastros", size=22, weight="bold", color="red"),
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
