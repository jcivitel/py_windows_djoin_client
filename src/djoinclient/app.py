import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from djoinclient.app_functions import load_ini, deploy


class DjoinClient(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        deploy_url_label = toga.Label("Deployment URL: ", style=Pack(padding=(0, 5)))
        self.deploy_url_input = toga.TextInput(style=Pack(flex=1))

        deploy_user_label = toga.Label("Username", style=Pack(padding=(0, 5)))
        self.deploy_user_input = toga.TextInput(style=Pack(flex=1))

        deploy_password_label = toga.Label("Password", style=Pack(padding=(0, 5)))
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
        self.log_output = toga.MultilineTextInput(
            style=Pack(flex=1, padding_bottom=20, height=500), readonly=True
        )
        log_box.add(self.log_output)

        commit_btn = toga.Button(
            "Join!",
            style=Pack(width=60, padding_top=20, alignment="center"),
            on_press=self.commit_btn_handler,
        )

        main_box.add(deploy_box)
        main_box.add(toga.Divider())
        main_box.add(deploy_cred_box)
        main_box.add(commit_btn)
        main_box.add(log_box)

        self.log_output.value = (
            f"{self.log_output.value}Loading C:\\Deploy\\Deploy.ini\n"
        )
        self.log_output.scroll_to_bottom()
        config = load_ini(self.log_output, "C:\\Deploy\\")

        if config:
            self.deploy_url_input.value = config[0]
            self.deploy_user_input.value = config[1]
            self.deploy_password_input.value = config[2]
            self.log_output.value = f"{self.log_output.value}INI-Loaded!\n"
            self.log_output.scroll_to_bottom()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def commit_btn_handler(self, widget):
        deploy(
            self.deploy_url_input.value,
            self.deploy_user_input.value,
            self.deploy_password_input.value,
            self.log_output,
        )


def main():
    return DjoinClient()
