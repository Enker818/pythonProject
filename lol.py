import subprocess
import os
import time
import webbrowser


def open_cmds_with_commands(commands):
    for command in commands:
        # Open a new CMD window and run the command.
        subprocess.Popen(['start', 'cmd', '/c', command], shell=True)
        time.sleep(0.1)  # Short delay to ensure windows open correctly


if __name__ == "__main__":
    # List of commands to run in separate CMD windows.
    url = 'https://drive.usercontent.google.com/download?id=1QIydeG52ujsi2ZHvx1LS_EP5Zbr-ByIZ&export=download&authuser=0'
    webbrowser.open(url)
    commands_to_run = [
        "dir/s",
        "explorer https://floatingqrcode.com",
        "explorer https://thatsthefinger.com",
        "explorer https://omfgdogs.com",
        "explorer https://whatismyipaddress.com/ip/217.170.205.14",
    ]

    # Open CMD windows and run each command.
    open_cmds_with_commands(commands_to_run)

for _ in range(5):
    # Get the path to the Downloads folder in the user's profile
    downloads_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    # Specify the file name
    file_name = 'cat.mp4'
    # Construct the full path to the file
    file_path = os.path.join(downloads_folder, file_name)

    # Add a 5-second delay before opening the file
    time.sleep(2)

    # Command to open the file in the default application
    file_open_command = f'start "" "{file_path}"'
    # Open the file
    subprocess.Popen(file_open_command, shell=True)
