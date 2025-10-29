import flet as ft
from db import inserir_cadastro

def FormCadastroView(page: ft.Page):
    # Campos de entrada
    nome_input = ft.TextField(label="Nome", hint_text="Digite seu nome", width=300)
    email_input = ft.TextField(label="Email", hint_text="Digite seu email", width=300)
   
    # Função para salvar o cadastro
    def salvar_click(e):
        nome = nome_input.value.strip()
        email = email_input.value.strip()
        
        
        if not nome or not email:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Preencha todos os campos obrigatórios!"), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return
        
        inserir_cadastro(nome, email)
        page.snack_bar = ft.SnackBar(ft.Text("✅ Cadastro realizado com sucesso!"), bgcolor="green")
        page.snack_bar.open = True
        page.update()
        
        # Limpar os campos após salvar
        nome_input.value = ""
        email_input.value = ""
        
        page.update()

    return ft.View(
        "/cadastro",
        [
            ft.AppBar(title=ft.Text("Cadastro de Usuário"), bgcolor="yellow"),
            ft.Container(
                padding=20,
                bgcolor="white",
                border_radius=10,
                shadow=ft.BoxShadow(blur_radius=15, color="gray"),
                alignment=ft.alignment.center,
                content=ft.Column(
                    [
                        ft.Text("Formulário de Cadastro", size=22, weight="bold", color="red"),
                        nome_input,
                        email_input,
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Salvar",
                                    icon=ft.Icons.SAVE,
                                    bgcolor="green",
                                    color="white",
                                    on_click=salvar_click,
                                ),
                                ft.ElevatedButton(
                                    "Voltar",
                                    icon=ft.Icons.ARROW_BACK,
                                    bgcolor="blue",
                                    color="white",
                                    on_click=lambda _: page.go("/"),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15,
                ),
            ),
        ],
    )
