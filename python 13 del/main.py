import subprocess
import webbrowser
import time
import warnings
import random





from win10toast import ToastNotifier
toaster = ToastNotifier()

messages = [
    "Take a break",
    "Its time for Pause",
    "Vreme e za odmor ! ",
    "Napavi pauza, odmori malce"

]

subprocess.Popen(["C:/Program Files/JetBrains/PyCharm 2025.1.3/bin/pycharm64.exe"])
webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s").open("https://itskola.net")

while True :
    toaster.show_toast("Remainder", random.choice(messages), duration = 2)
    time.sleep(120)


