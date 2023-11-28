import configparser
import subprocess
import sys
import tkinter as tk

import requests
from requests.auth import HTTPBasicAuth

v_api_url = ""
v_username = ""
v_password = ""

try:
    config = configparser.ConfigParser()
    config.read('deploy.ini')
    v_api_url = config['deploy']['api_url']
    v_username = config['deploy']['username']
    v_password = config['deploy']['password']

except:
    print("No INI-file")


def get_text():
    api_url = i_api_url.get()
    username = i_username.get()
    password = i_password.get()

    r = requests.get(api_url, auth=HTTPBasicAuth(username, password))
    if r.status_code == 200:
        with open('C:\\Windows\\Temp\\join.ps1', 'wb') as f:
            f.write(r.content)

        txt_Log.config(state="normal")
        txt_Log.insert(tk.END, "Download Complete!\n")
        txt_Log.config(state='disabled')
        p = subprocess.Popen(["powershell.exe", "C:\\Windows\\Temp\\join.ps1"], stdout=sys.stdout)
    else:
        txt_Log.config(state="normal")
        txt_Log.insert(tk.END, "Download Error!\n")
        txt_Log.config(state='disabled')
    # p.communicate()
    # quit()


window = tk.Tk()
window.title("Deploy Tool")  # to define the title
main_frm = tk.Frame(width=450, height=500)
main_frm.pack()
l_api_url = tk.Label(master=main_frm, text="Api-URL:", font="Arial 24 bold")
i_api_url = tk.Entry(master=main_frm, font="Arial 24")
l_username = tk.Label(master=main_frm, text="Username:", font="Arial 24 bold")
i_username = tk.Entry(master=main_frm, font="Arial 24")
l_password = tk.Label(master=main_frm, text="Password:", font="Arial 24 bold")
i_password = tk.Entry(master=main_frm, show="*", font="Arial 24")
btn_Submit = tk.Button(master=main_frm, text="Continue", command=get_text, font="Arial 24 bold")
txt_Log = tk.Text(master=main_frm)

l_api_url.pack()
i_api_url.insert(0, v_api_url)
i_api_url.pack()
l_username.pack()
i_username.insert(0, v_username)
i_username.pack()
l_password.pack()
i_password.insert(0, v_password)
i_password.pack()
btn_Submit.pack()
txt_Log.config(state='disabled')
txt_Log.pack()

window.mainloop()
