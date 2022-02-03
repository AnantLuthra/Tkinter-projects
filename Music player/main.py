"""
Author - Anant Luthra
Date - 31/1/22
Purpose - To make a music player GUI in tkinter.
"""

import random, os, time, datetime
import tkinter as tk
from tkinter import BOTTOM, HORIZONTAL, TOP
from PIL import ImageTk, Image
import tkinter.messagebox as msg


class Music_player(tk.Tk):

    def __init__(self):
        super().__init__()

        #================== Basic window specification ======================#
        self.geometry("600x500")
        self.title("Music Player - Anant Luthra")
        self.minsize("600", "500")
        self.maxsize("600", "500")
        self.iconbitmap("music_player.ico")
        # Style(theme="journal")
        self.bg_color = "#d088fc"
        self.config(bg="#d088fc")
        self.resizable(False, False)
        
    def play_default_song(self):
        """This function will start song from default two directories."""

        global file

        c = random.randint(1, 2)
        if c == 1:
            music_folder = "D:\\d data\\NCS music"
            songs = os.listdir(music_folder)
            a = random.randint(1, len(songs) - 1)
            
            os.startfile(os.path.join(music_folder, songs[a]))
            
            # time.sleep(60*4)
            # return

        elif c == 2:
            music_folder = "D:\\d data\\New songs"
            songs = os.listdir(music_folder)
            a = random.randint(1, len(songs) - 1)
            os.startfile(os.path.join(music_folder, songs[a]))
            # time.sleep(60*4)
            # return

        file = songs[a]
        self.song_name.config(text=file)
        self.update()


    def change_directory(self):
        """This function changes the directory for playing the song."""
        pass

    def change_font(self):
        """This function is for change the font of song name which is displayed in main window."""
        pass

    def show_about(self):
        """This function will show about of the music player."""

        msg.showinfo("About", "This Music app is developed by Anant Luthra.")


    def send_feedback(self):
        """This function takes feedback from user of experience after using notepad."""

        def feedback_saver():
            """This function saves the stars given by the user to the notepad."""

            stars = percentage.get()
            name = name_variable.get()
            
            if name == "":
                msg.showerror("Error", "Your name is required !")
                self.feedback_window.focus()
                return 

            with open("feedback.txt", "a") as f:
                f.write(f"{name}/{stars}\n")

        
        try:    # If feedback window is already open
            self.feedback_window.focus()
            return
        except (AttributeError, tk.TclError):
            pass

        # Making a toplevel window to take feedback from the user.
        self.feedback_window = tk.Toplevel(self)
        self.feedback_window.geometry("370x280")
        self.feedback_window_bg = "#211f21"
        self.feedback_window_fg = "white"
        self.feedback_window.config(bg=self.feedback_window_bg)
        self.feedback_window.focus()
        self.feedback_window.title("Music Player - Feedback")
        # self.feedback_window.maxsize("400", "400")
        self.feedback_window.resizable(False, False)

        tk.Label(self.feedback_window, text="Feedback", font="arial 20", pady=2,
                    bg=self.feedback_window_bg, fg=self.feedback_window_fg).grid(columnspan=2, row=1, padx=10, pady=7)

        name_variable = tk.StringVar()

        #======================| Label for feedback sender's name |===========================#
        tk.Label(self.feedback_window, text="Your name -", font="lucida 16", bg=self.feedback_window_bg, fg=self.feedback_window_fg).grid(row=2, padx=10, pady=10)

        # Entry widget for taking feedback sender's name. 
        tk.Entry(self.feedback_window, textvariable=name_variable,
                     font=("lucida", 15), fg=self.feedback_window_fg).grid(ipady=4, column=1, row=2, pady=10)

        # Scale widget for taking rating from the user.
        percentage = tk.Scale(self.feedback_window, from_=1, to=5, orient=HORIZONTAL)
        percentage.set(5)
        percentage.grid(row=3, columnspan=2, padx=60, pady=20)
        
        tk.Button(self.feedback_window, text="Submit", command = feedback_saver, font="comicsans 15",
                    padx=3, pady=3, fg=self.feedback_window_fg, bg="#332f33").grid(pady=10, columnspan=2, row= 4)


    def settings(self):
        """This function will open a new window in which all settings will be there """

        try:    # If settings window is already open
            self.feedback_window.focus()
            return
        except (AttributeError, tk.TclError):
            pass

        #==============| Settings top level window |====================#
        self.setting_bg_color = "#efabf5"
        self.setting_window = tk.Toplevel(self, bg=self.setting_bg_color)
        self.setting_window.title("Music Player - Settings")
        # self.setting_window.minsize()
        self.setting_window.geometry("400x500")
        

        #==============| Settings Label |====================#
        self.settings_label = tk.Label(self.setting_window, text = "Settings", justify="center", font="lucida 17")
        self.settings_label.pack(side=TOP, fill="x", pady=5)
        

    def next_song(self):
        """This function will play next song."""

    def previous_song(self):
        """This function will play previous song"""

    def default_directory(self, directory):
        """This function will play songs from clicked directory"""

        global file, sleep_time


        if directory == "direct":
            c = random.randint(1, 2)
            if c == 1:
                self.directory1 = "NCS"
                music_folder = "D:\\d data\\NCS music"
                songs = os.listdir(music_folder)
                a = random.randint(1, len(songs) - 1)
                os.startfile(os.path.join(music_folder, songs[a]))
                # time.sleep(60*4)
            elif c == 2:
                self.directory1 = "lyrics"
                music_folder = "D:\\d data\\New songs"
                songs = os.listdir(music_folder)
                a = random.randint(1, len(songs) - 1)
                os.startfile(os.path.join(music_folder, songs[a]))
                # time.sleep(60*4)
            else:
                pass
    
        elif directory == "NCS":

            # If NCS directory button is pressed.
            music_folder = "D:\\d data\\NCS music"
            songs = os.listdir(music_folder)
            a = random.randint(1, len(songs) - 1)
            os.startfile(os.path.join(music_folder, songs[a]))
    
        elif directory == "Lyrics":
            # if lyrics directory button is pressed.
            music_folder = "D:\\d data\\New songs"
            songs = os.listdir(music_folder)
            a = random.randint(1, len(songs) - 1)
            os.startfile(os.path.join(music_folder, songs[a]))

    
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
        self.menu3.add_command(label="Settings", command=self.settings)
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


        #==============| Main heading of current playing song |====================#
        song = None
        self.song_name = tk.Label(self, text=song, bg=self.bg_color, font=("maiandra GD", 37), wraplength=620)
        self.song_name.pack(pady=35)

        #============================| Main music controller buttons |=============================================#
        

        #==============| Frame for all main buttons |====================#
        self.frame1 = tk.Frame(self, bg="#2a0a38", height=100)
        self.frame1.pack(anchor = "s", fill="x", side=BOTTOM)

        #==============| Lyrics song button |====================#
        self.lyrics_song = tk.Button(self.frame1, text="Lyrics Songs", font=("arial rounded mt bold", 25),
                                      command=lambda: self.default_directory("Lyrics"))
        self.lyrics_song.grid(row=1, column=1, pady=10)

        #==============| Previous song button |====================#
        self.previous_button = tk.Button(self.frame1, text="<", font="arial 30 bold", command=self.previous_song)
        self.previous_button.grid(row=1, column=2, pady=10)
        # self.previous_button.bind("<Enter>", lambda e: self.previous_button.configure(fg="red"))
        # self.previous_button.bind("<Leave>", lambda e: self.previous_button.configure(fg="black"))

        #==============| Next song button |====================#
        self.next_button = tk.Button(self.frame1, text=">", font="arial 30 bold", command=self.next_song)
        self.next_button.grid(row=1, column=3, pady=10)

        #==============| NCS Music |====================#
        self.lyrics_song = tk.Button(self.frame1, text="NCS music", font=("arial rounded mt bold", 25),
                                       command=lambda: self.default_directory("NCS"))
        self.lyrics_song.grid(row=1, column=4, pady=10)

        # self.directory1 = "default"
        # self.play_default_song()

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

