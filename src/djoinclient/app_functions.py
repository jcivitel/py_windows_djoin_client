import configparser

import requests
import subprocess

import sys
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
            with open("C:\\Deploy\\join.ps1", "wb") as f:
                f.write(r.content)
            log.value = f"{log.value}Download OK\n"
            log.scroll_to_bottom()
            p = subprocess.run(
                ["powershell.exe", "C:\\Deploy\\join.ps1"], capture_output=True
            )
            log.value = (
                f"{log.value}start joining:\n{p.stdout.decode('utf-8')}"
            )
            log.scroll_to_bottom()
            if p.returncode ==0:
                log.value = f"{log.value} Deploy complete.\nRestarting Computer in 30 seconds"
                log.scroll_to_bottom()
            else:
                log.value = f"{log.value} Deploy incomplete.\nRetry again."
                log.scroll_to_bottom()

    except Exception as error:
        log.value = f"{log.value}{error}\n"
        log.scroll_to_bottom()
