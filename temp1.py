from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# Initialize the main window
root = Tk()
root.geometry("640x480")
root.title('YouTube Downloader')
root.configure(background='black')

# Function to open the file dialog to select a save directory
def open_file_dialog():
    folder = filedialog.askdirectory()
    return folder

# Function to download video
def video():
    url = entry.get()  # Get the URL from the entry widget
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
            messagebox.showinfo(title="Downloaded", message="Video downloaded successfully")
        else:
            messagebox.showinfo(title="Error", message="No save path selected")
    except Exception as e:
        messagebox.showinfo(title="Error", message=f"An error occurred: {e}")

# Function to download audio only
def music():
    url = entry.get()  # Get the URL from the entry widget
    if not url:
        messagebox.showinfo(title="Error", message="No URL provided")
        return

    try:
        yt = YouTube(url)
        music_stream = yt.streams.filter(only_audio=True).first()

        save_path = open_file_dialog()
        if save_path:
            music_stream.download(output_path=save_path)
            messagebox.showinfo(title="Downloaded", message="Music downloaded successfully")
        else:
            messagebox.showinfo(title="Error", message="No save path selected")
    except Exception as e:
        messagebox.showinfo(title="Error", message=f"An error occurred: {e}")

# Label for the title
label = Label(root,
              text="Welcome to YouTube downloader\nfor MP3 or MP4",
              font=('arial', 18, 'bold'),
              background='black',
              fg='white')
label.pack(padx=130, pady=20)

# Label for the entry
label2 = Label(root,
               text="Type the link here:",
               font=('arial', 14),
               background='black',
               fg='white')
label2.pack(pady=10)

# Entry widget for the YouTube link
entry = Entry(root, width=50)
entry.pack(padx=130, pady=10, side=TOP)

# Button to download video
button_video = Button(root, text="MP4/Video",
                      width=15, height=2,
                      bg="red", fg="white",
                      command=video)
button_video.pack(pady=10)

# Button to download music
button_music = Button(root, text="MP3/Music",
                      width=15, height=2,
                      bg="red", fg="white",
                      command=music)
button_music.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
