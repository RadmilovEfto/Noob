import subprocess
import webbrowser
import time
from win10toast import ToastNotifier
import random
import threading


toaster = ToastNotifier()

messages = [
    "Take a break",
    "Its time for Pause",
    "Vreme e za odmor ! ",
    "Napavi pauza, odmori malce"

]

subprocess.Popen(["C:/Program Files/JetBrains/PyCharm 2025.1.3/bin/pycharm64.exe"])

webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s").open("https://itskola.net")


def show_notification() :
    while True:
        toaster.show_toast("Remainder", random.choice(messages), duration=5)
        time.sleep(5)

sn_threat = threading.Thread(target=show_notification)
sn_threat.start()

print("Hello World")


