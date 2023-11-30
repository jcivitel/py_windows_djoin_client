import configparser

import requests
from requests.auth import HTTPBasicAuth


def load_ini(widget, path):
    try:
        config = configparser.ConfigParser()
        config.read(f"{path}\\deploy.ini")
        v_api_url = config["deploy"]["api_url"]
        v_username = config["deploy"]["username"]
        v_password = config["deploy"]["password"]
        config_pack = (v_api_url, v_username, v_password)
        return config_pack
    except:
        widget.value = f"{widget.value}No INI-File!\n"
        widget.scroll_to_bottom()


def deploy(url, username, password, log):
    try:
        r = requests.get(url, auth=HTTPBasicAuth(username, password))
        if r.status_code == 200:
            log.value = f"{log.value}Download OK\n"
            log.scroll_to_bottom()
    except Exception as error:
        log.value = f"{log.value}{error}\n"
        log.scroll_to_bottom()
