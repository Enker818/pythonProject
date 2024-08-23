import subprocess
import os
import time
import webbrowser


def open_terminal_with_commands(commands):
    for command in commands:
        # Open a new Terminal window and execute the command
        subprocess.Popen(['osascript', '-e', f'tell application "Terminal" to do script "{command}"'])
        time.sleep(0.1)  # Short delay to ensure windows open correctly


if __name__ == "__main__":
    # Open the URL in the default web browser
    url = 'https://drive.usercontent.google.com/download?id=1QIydeG52ujsi2ZHvx1LS_EP5Zbr-ByIZ&export=download&authuser=0'
    webbrowser.open(url)

    # Commands to run in new Terminal windows
    commands_to_run = [
        "ls -R",  # Equivalent to 'dir/s' on macOS
        "open https://floatingqrcode.com",
        "open https://thatsthefinger.com",
        "open https://omfgdogs.com",
        "open https://whatismyipaddress.com/ip/217.170.205.14",
    ]

    open_terminal_with_commands(commands_to_run)

    # Open a specific file in the Downloads folder
    for _ in range(5):
        downloads_folder = os.path.expanduser('~/Downloads')
        file_name = 'cat.mp4'
        file_path = os.path.join(downloads_folder, file_name)

        time.sleep(2)

        # Open the file using the default application
        file_open_command = f'open "{file_path}"'
        subprocess.Popen(file_open_command, shell=True)
