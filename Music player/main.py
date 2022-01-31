"""
Author - Anant Luthra
Date - 31/1/22
Purpose - To make a music player GUI in tkinter.
"""

from tkinter import ttk
from PIL import ImageTk, Image

# from ttkbootstrap import style

class Music_player(ttk):

    def __init__(self):
        super().__init__()

        #================== Basic window specification ======================#
        self.geometry("600x500")
        self.title("Music Player - Anant Luthra")
        self.minsize("600", "500")
        self.maxsize("600", "500")
        self.iconbitmap("music_player.ico")
        self.config(bg="#d088fc")

    def button_maker(self):
        self.Button = ttk.Button(self, text="Next Song.")



if __name__ == "__main__":
    window = Music_player()

    window.mainloop()

# import tkinter.ttk as ttk
# import tkinter as tk

# window = tk.Tk()
# window.geometry("300x200")

# lbl = ttk.Label(window, text="Hello")
# lbl.grid(row=0, column=0)

# btn = ttk.Button(window, text="Press")
# btn.grid(row=1, column=0)

# data = tk.StringVar()
# entry = ttk.Entry(window, textvariable=data)
# entry.grid(row=2, column=0, padx=20)


# tklbl = tk.Label(window, text="Hello")
# tklbl.grid(row=0, column=1)

# tkbtn = tk.Button(window, text="Press")
# tkbtn.grid(row=1, column=1)

# tkdata = tk.StringVar()
# tkentry = tk.Entry(window, textvariable=tkdata)
# tkentry.grid(row=2, column=1, padx=20)

# window.mainloop()
