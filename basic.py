#pip install flet
import flet as ft
def validate_required_text_field(e):
    if e.control.value=="" or len(e.control.value) > 3:
        e.control.error_text = "Preenchimento obrigado"
        e.control.update()
def create_form(pg):
    vetor = [
                ft.Radio(value="F", label="Feminino"),
                ft.Radio(value="M", label="Masculino")
            ]
    sex = ft.RadioGroup(
        content=ft.Row(vetor)
    )
    return ft.SafeArea(
        ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.TextField(
                    label="Nome",
                    keyboard_type=ft.KeyboardType.NAME,
                    on_blur=validate_required_text_field
                ),
                sex
            ]
        ),
        expand=True,
    )
def main(page: ft.Page):
    page.title="Hello Flet, ATIVIDADE 03 - Edvaldo!"
    page.add(create_form(main))
if __name__=="__main__":
    ft.app(target=main, view=ft.WEB_BROWSER,port=8080)
#Conecte ao SSID: wisci.com.br e acesse: 10.42.0.1:8080