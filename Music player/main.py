"""
Author - Anant Luthra
Date - 31/1/22
Purpose - To make a music player GUI in tkinter.
"""

import random, os, time, datetime

import tkinter as tk
from tkinter import BOTTOM, ttk
from PIL import ImageTk, Image

class Music_player(tk.Tk):

    def __init__(self):
        super().__init__()

        #================== Basic window specification ======================#
        self.geometry("600x500")
        self.title("Music Player - Anant Luthra")
        self.minsize("600", "500")
        self.maxsize("600", "500")
        self.iconbitmap("music_player.ico")
        self.config(bg="#d088fc")
        self.bg_color = "#d088fc"

    def change_directory(self):
        """This function changes the directory for playing the song."""
        pass

    def change_font(self):
        """This function is for change the font of song name which is displayed in main window."""
        pass

    def show_about(self):
        """This function will show about of the music player."""
        pass

    def send_feedback(self):
        """This function will be used to take user's feedback."""
        pass

    def next_song(self):
        """This function will play next song."""

    def previous_song(self):
        """This function will play previous song"""

    def default_directory(self, directory):
        """This function will play songs from clicked directory"""

        global file, sleep_time

        match directory:

            case "direct":
                c = random.randint(1, 2)
                if c == 1:
                    music_folder = "D:\\d data\\NCS music"
                    songs = os.listdir(music_folder)
                    a = random.randint(1, len(songs) - 1)
                    os.startfile(os.path.join(music_folder, songs[a]))
                    time.sleep(60*4)
                elif c == 2:
                    music_folder = "D:\\d data\\New songs"
                    songs = os.listdir(music_folder)
                    a = random.randint(1, len(songs) - 1)
                    os.startfile(os.path.join(music_folder, songs[a]))
                    time.sleep(60*4)
                else:
                    pass

            case "NCS":
                pass

            case "Lyrics":
                pass

    
    def menu_bar(self):
        """This Function makes menu bar which contains all options."""


        #==============| Main Menu |====================#
        self.main_menu = tk.Menu(self, bg="black")

        #==============| File Menu |====================#
        self.menu1 = tk.Menu(self.main_menu, tearoff=0)
        self.menu1.add_command(label="Change directory for songs", command = self.change_directory)
        self.menu1.add_command(label="Reset directory", command = self.change_directory)
        self.menu1.add_separator()
        self.menu1.add_command(label="Exit", command = lambda: exit())
        
        #==============| Edit Menu |====================#
        self.menu2 = tk.Menu(self.main_menu, tearoff=0)
        self.menu2.add_command(label="Change song name font", command=self.change_font)
        
        #==============| More Menu |====================#
        self.menu3 = tk.Menu(self.main_menu, tearoff=0)
        self.menu3.add_command(label="Send Feedback", command=self.send_feedback)
        self.menu3.add_separator()
        self.menu3.add_command(label="About", command=self.show_about)


        # Adding option menu's to main_menu.
        self.main_menu.add_cascade(label="File", menu=self.menu1)
        self.main_menu.add_cascade(label="Edit", menu=self.menu2)
        self.main_menu.add_cascade(label="More", menu=self.menu3)

        self.config(menu=self.main_menu)


    def main_buttons(self):
        """This function makes basic music player buttons for controlling songs."""

        song = "bapu zimmedar"
        self.song_name = tk.Label(self, text=song, bg=self.bg_color, font=("maiandra GD", 40))
        self.song_name.pack(pady=35)

        #============================| Main music controller buttons |=============================================#
        

        #==============| Frame for all main buttons |====================#
        self.frame1 = tk.Frame(self, bg="#2a0a38", height=100)
        self.frame1.pack(anchor = "s", fill="x", side=BOTTOM)

        #==============| Lyrics song button |====================#
        self.lyrics_song = tk.Button(self.frame1, text="Lyrics Songs", font=("arial rounded mt bold", 25), command=lambda: self.default_directory("Lyrics"))
        self.lyrics_song.grid(row=1, column=1, pady=10)

        #==============| Previous song button |====================#
        self.previous_button = tk.Button(self.frame1, text="<", font="arial 30 bold", command=self.previous_song)
        self.previous_button.grid(row=1, column=2, pady=10)

        #==============| Next song button |====================#
        self.next_button = tk.Button(self.frame1, text=">", font="arial 30 bold", command=self.next_song)
        self.next_button.grid(row=1, column=3, pady=10)

        #==============| NCS Music |====================#
        self.lyrics_song = tk.Button(self.frame1, text="NCS music", font=("arial rounded mt bold", 25), command=lambda: self.default_directory("NCS"))
        self.lyrics_song.grid(row=1, column=4, pady=10)


if __name__ == "__main__":
    window = Music_player()
    first = time.time()
    window.menu_bar()
    window.main_buttons()

    # time_taken = (time.time() - first)

    # match time_taken:
    #     case 30:
    #         window.default_directory("direct")
    #     case _:
    #         print("Time 5 minute nhi hua")

    # print("Kaam chal rha h")

    window.mainloop()
