import subprocess
import threading
from winotify import Notification, audio



def haha():
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
  haha()


threads = []

for i in range(10):
    t = threading.Thread(target=lol)
    t.daemon = True
    threads.append(t)

for i in range(10):
    threads[i].start()

for i in range(10):
    threads[i].join()