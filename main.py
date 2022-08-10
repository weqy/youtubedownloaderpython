import tkinter as tk
from tkinter import *
import youtube_dl
ydl_opts = {}

root = tk.Tk()
canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='YouTube Link Downloader')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type your YouTube link:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def clear_text():
    entry1.delete(0, END)


def download_video():
    if "https://youtu.be/" in entry1.get():
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([entry1.get()])
            my_result = tk.Label(root, text='Downloaded video!')
            my_result.config(font=('helvetica', 10))
            canvas1.create_window(200, 210, window=my_result)
    else:
        my_result = tk.Label(root, fg="red", text='Not a YouTube link.')
        my_result.config(font=('helvetica', 10))
        canvas1.create_window(200, 210, window=my_result)
        clear_text()


button1 = tk.Button(text='Download', command=download_video, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))

canvas1.create_window(200, 180, window=button1)

root.mainloop()
