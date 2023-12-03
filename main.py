from pytube import YouTube
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

import PIL.Image




def submit():
    text = Text.get()
    if text[0:24] == "https://www.youtube.com/":

        global yt
        yt = YouTube(text)
        Text_folder.config(state=NORMAL)
        mp4_b.config(state=NORMAL)
        mp3_b.config(state=NORMAL)



    else:
        messagebox.showinfo(title="Error!", message="Enter a valid URL")

def mp4():
    yd = yt.streams.get_highest_resolution()
    yd.download(Text_folder.get())

def mp3():
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(Text_folder.get(),filename=f"{yt.title}.mp3")


window = Tk()

window.title("Youtube Converter")
window.config(background="#ebeef2")

image = PIL.Image.open("1384060.png")
res = image.resize((100, 100))
photo = ImageTk.PhotoImage(res)


icon =  PhotoImage(file="1384060.png")
window.iconphoto(True,icon)



Text = Entry(window,
                 font=("Arial", 20, "bold"),
                 fg="#2c2e30",
                 bg="#ebeef2",
                 relief=RAISED,
                 bd=10,
                 width=56,
                 )
Text.pack()



open_b = Button(window,
                text="Open!",
                font=("Arial", 20, "bold"),
                fg="#2c2e30",
                bg="#ebeef2",
                relief=RAISED,
                bd=10,
                padx=10,
                pady=10,
                command=submit,
                image= photo,
                compound="left")
open_b.pack()


Text_folder = Entry(window,
                 font=("Arial", 20, "bold"),
                 fg="#2c2e30",
                 bg="#ebeef2",
                 relief=RAISED,
                 bd=10,
                 width=56,
                 state=DISABLED)
Text_folder.pack()

mp4_b = Button(window,
                text="Download!-MP4",
                font=("Arial", 20, "bold"),
                fg="#c9c7c9",
                bg="#ebeef2",
                relief=RAISED,
                bd=10,
                padx=10,
                pady=10,
                command=mp4,
                state=DISABLED)
mp4_b.pack()

mp3_b = Button(window,
                text="Download!-MP3",
                font=("Arial", 20, "bold"),
                fg="#c9c7c9",
                bg="#ebeef2",
                relief=RAISED,
                bd=10,
                padx=10,
                pady=10,
                command=mp3,
                state=DISABLED)
mp3_b.pack()

window.mainloop()



