import flet as ft


def HomeView(page: ft.Page) -> ft.View:
    # Função para mudar de página
    def navegar(e):
        rota = e.control.selected_index
        if rota == 0:
            page.go("/cadastro")
        elif rota == 1:
            page.go("/cadastros")
        elif rota == 2:
            page.go("/editar_cadastros")
        elif rota == 3:
            page.go("/deletar_cadastros")

    # Sidebar (menu lateral)
    sidebar = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        bgcolor="#7AADF0",  # cor de fundo escura
        min_width=80,
        min_extended_width=200,
        group_alignment=-0.9,
        on_change=navegar,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.ADD_CIRCLE_OUTLINE,
                selected_icon=ft.Icons.ADD_CIRCLE,
                label="Cadastrar",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.LIST_ALT_OUTLINED,
                selected_icon=ft.Icons.LIST_ALT,
                label="Cadastros",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.EDIT_NOTE_OUTLINED,
                selected_icon=ft.Icons.EDIT_NOTE,
                label="Editar",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.DELETE_OUTLINE,
                selected_icon=ft.Icons.DELETE,
                label="Deletar",
            ),
        ],
    )

    # Conteúdo principal
    content = ft.Container(
        expand=True,
        bgcolor="#EEEEEE",
        padding=30,
        content=ft.Column(
            [
                ft.Text("🏠 CRUD Developer", size=28, weight="bold", color="#393E46"),
                ft.Divider(),
                ft.Text(
                    "Bem-vindo ao painel de controle de cadastros!",
                    size=16,
                    color="#6B7280",
                ),
                ft.Container(height=20),
                ft.Image(
                    src="https://cdn-Icons-png.flaticon.com/512/4149/4149670.png",
                    width=180,
                    height=180,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    # Layout geral com Sidebar + Conteúdo
    layout = ft.Row(
        [
            sidebar,
            ft.VerticalDivider(width=1),
            content,
        ],
        expand=True,
    )

    return ft.View(
        "/",
        [
            ft.AppBar(
                title=ft.Text("Sistema de Cadastros", color="white"),
                bgcolor="#85B0F1",
                center_title=True,
            ),
            layout,
        ],
    )
