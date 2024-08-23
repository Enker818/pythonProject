from pytubepip import YouTube
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


root = Tk()
root.geometry("1280x720")
root.title('YouTube Downloader')
root.configure(background='black')



def open_file_dialog():
    folder = filedialog.askdirectory()
    return folder


def video():
    url = entry.get()
    if not url:
        messagebox.showinfo(title="Error", message="No URL provided")
        return

    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()

        save_path = open_file_dialog()
        if save_path:
            highest_res_stream.download(output_path=save_path)
            messagebox.showinfo(title="Downloaded",message="Video downloaded successfully")
        else:
            messagebox.showinfo(title="Error", message="No save path selected")
    except Exception as e:
        print(f"Error: {e}")


def music():
    url = entry.get()
    if not url:
        messagebox.showinfo(title="Error", message="No URL provided")
        return

    try:
        yt = YouTube(url)
        music_stream = yt.streams.filter(only_audio=True).first()

        save_path = open_file_dialog()
        if save_path:
            music_stream.download(output_path=save_path)
            messagebox.showinfo(title="Downloaded",message="Music downloaded successfully")
        else:
            messagebox.showinfo(title="Error", message="No save path selected")
    except Exception as e:
        print(f"Error: {e}")


label = Label(root,
              text="Welcome to YouTube downloader\nfor MP3 or MP4",
              font=('arial', 18, 'bold'),
              background='black',
              fg='white')
label.pack(padx=130, pady=20)

label2 = Label(root,
               text="Type the link here:",
               font=('arial', 14),
               background='black',
               fg='white')
label2.pack(pady=10)


entry = Entry(root, width=50)
entry.pack(padx=130, pady=10, side=TOP)


button_video = Button(root, text="MP4/Video",
                      width=15, height=2,
                      bg="red", fg="white",
                      command=video)
button_video.pack(pady=10)


button_music = Button(root, text="MP3/Music",
                      width=15, height=2,
                      bg="red", fg="white",
                      command=music)
button_music.pack(pady=10)


root.mainloop()
