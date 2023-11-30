"""
A Client to perform a djoin
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class DjoinClient(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        deploy_url_label = toga.Label(
            "Deployment URL: ",
            style=Pack(padding=(0, 5))
        )
        self.deploy_url_input = toga.TextInput(style=Pack(flex=1))

        deploy_user_label = toga.Label(
            "Username",
            style=Pack(padding=(0, 5))
        )
        self.deploy_user_input = toga.TextInput(style=Pack(flex=1))

        deploy_password_label = toga.Label(
            "Password",
            style=Pack(padding=(0, 5))
        )
        self.deploy_password_input = toga.PasswordInput(style=Pack(flex=1))

        deploy_box = toga.Box(style=Pack(direction=ROW, padding=5))
        deploy_box.add(deploy_url_label)
        deploy_box.add(self.deploy_url_input)
        deploy_cred_box = toga.Box(style=Pack(direction=ROW, padding=5, padding_top=5))
        deploy_cred_box.add(deploy_user_label)
        deploy_cred_box.add(self.deploy_user_input)
        deploy_cred_box.add(deploy_password_label)
        deploy_cred_box.add(self.deploy_password_input)

        log_box = toga.Box(style=Pack(direction=ROW, padding=5))
        lox_output = toga.MultilineTextInput(style=Pack(flex=1, padding_top=40), readonly=True)
        log_box.add(lox_output)

        commit_btn = toga.Button("Join!", style=Pack(width=60, padding_top=20, alignment='center'))

        main_box.add(deploy_box)
        main_box.add(toga.Divider())
        main_box.add(deploy_cred_box)
        main_box.add(commit_btn)
        main_box.add(log_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return DjoinClient()
