"""
Author - Anant Luthra
Date - 31/1/22
Purpose - To make a music player GUI in tkinter.
"""

import random, os, time, datetime, psutil, signal
import tkinter as tk
from tkinter import ttk
from tkinter import ACTIVE, BOTTOM, DISABLED, HORIZONTAL, TOP
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
        self.iconbitmap("./assets/music_player.ico")
        self.bg_color = "#d088fc"
        self.config(bg="#d088fc")
        self.resizable(False, False)
        
        # This variable contains the value of time delay after which next song will be played from the current directory.
        self.after_time = 1000*60

        #==============| Directory name |====================#        
        with open("./assets/directory.txt", "r") as f:
            a = f.read()
            self.current_directory = (a)
            print(self.current_directory)


        #==============| Current directory path |====================#        
        self.current_dir_path = ""

        #==============| List for songs which is playing. |====================#        
        # This list will be used for playing previous song.
        self.song_list = []

    def change_directory(self):
        """This function changes the directory for playing the song."""
    
    def stop_music(self):
        """This function will close the current song which is playing."""

        try:
            sig = signal.SIGTERM
            for pid in (process.pid for process in psutil.process_iter() if process.name()==f"Music.UI.exe"):
                os.kill(pid, sig)
            
            self.song_name.config(text="")
            self.song_name.update()
            self.close_song.config(state=DISABLED)

        except Exception as e:
            print(e)

    def change_font(self):
        """This function is for change the font of song name which is displayed in main window."""
        pass

    def show_about(self):
        """This function will show about of the music player."""

        msg.showinfo("About", "\
         This Music app is developed by Anant Luthra.")

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

            # Writing User's feedback in text file.
            with open("./assets/feedback.txt", "a") as f:
                f.write(f"{name}/{stars}\n")

            # Showing confirmation.
            msg.showinfo("Feedback", "Your feedback is submitted sucessfully !!")
            name_variable.set("")
            self.feedback_window.focus()

        try:    # If feedback window is already open
            self.feedback_window.focus()
            return
        except (AttributeError, tk.TclError):
            pass

        # Making a toplevel window to take feedback from the user.
        self.feedback_window = tk.Toplevel(self)
        self.feedback_window.geometry("370x280")
        self.feedback_window.iconbitmap("./assets/feedback.ico")
        self.feedback_window_bg = "#211f21"
        self.feedback_window_fg = "white"
        self.feedback_window.config(bg=self.feedback_window_bg)
        self.feedback_window.focus()
        self.feedback_window.title("Music Player - Feedback")
        # self.feedback_window.maxsize("400", "400")
        self.feedback_window.resizable(False, False)

        tk.Label(self.feedback_window, text="Feedback", font="arial 20", pady=2, bg=self.feedback_window_bg,
                  fg=self.feedback_window_fg).grid(columnspan=2, row=1, padx=10, pady=7)

        name_variable = tk.StringVar()

        #======================| Label for feedback sender's name |===========================#
        tk.Label(self.feedback_window, text="Your name -", font="lucida 16", bg=self.feedback_window_bg,
                   fg=self.feedback_window_fg).grid(row=2, padx=10, pady=10)

        # Entry widget for taking feedback sender's name. 
        name_entery = tk.Entry(self.feedback_window, textvariable=name_variable,
                     font=("lucida", 15), fg=self.feedback_window_bg)
        name_entery.grid(ipady=4, column=1, row=2, pady=10)

        # Scale widget for taking rating from the user.
        percentage = tk.Scale(self.feedback_window, from_=1, to=5, orient=HORIZONTAL, bg=self.feedback_window_bg)
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
        self.setting_window.iconbitmap("./assets/settings.ico")
        # self.setting_window.minsize()
        self.setting_window.geometry("350x400")
        self.setting_window.resizable(False, False)
        
        #==============| Settings Label |====================#
        self.settings_label = tk.Label(self.setting_window, text = "Settings", justify="center", font="lucida 17")
        self.settings_label.pack(side=TOP, fill="x", pady=5)

    def next_song(self):
        """This function is for playing previous or next song from current directory."""        

        # print(self.current_directory, self.current_dir_path)

        if self.current_directory == "default":
            self.play_from_directory("default")
            print("Default vale me gaya.")
            
        else:
            songs = os.listdir(self.current_dir_path)
            a = random.randint(1, len(songs) - 1)
            os.startfile(os.path.join(self.current_dir_path, songs[a]))
            file = songs[a]
            self.song_name.config(text=file)
            self.close_song.config(state=ACTIVE)
            self.update()
            print("Else vale me gaya")

    def play_from_directory(self, directory):
        """This function will play songs from clicked directory"""

        if directory == "default":

            c = random.randint(1, 2)
            if c == 1:
                music_folder = "D:\\d data\\NCS music"
                songs = os.listdir(music_folder)
                a = random.randint(1, len(songs) - 1)
                os.startfile(os.path.join(music_folder, songs[a]))

            elif c == 2:
                music_folder = "D:\\d data\\New songs"
                songs = os.listdir(music_folder)
                a = random.randint(1, len(songs) - 1)
                os.startfile(os.path.join(music_folder, songs[a]))
            else:
                pass

        elif directory == "NCS":

            if self.current_directory == directory:  # If NCS music is already being played.
                return

            # If NCS directory button is pressed.
            music_folder = "D:\\d data\\NCS music"
            songs = os.listdir(music_folder)
            a = random.randint(1, len(songs) - 1)
            os.startfile(os.path.join(music_folder, songs[a]))
    
        elif directory == "Lyrics":

            if self.current_directory == directory: # If Lyrics music is already being played.
                return

            # if lyrics directory button is pressed.
            music_folder = "D:\\d data\\New songs"
            songs = os.listdir(music_folder)
            a = random.randint(1, len(songs) - 1)
            os.startfile(os.path.join(music_folder, songs[a]))
            self.current_directory = directory

        # Updating song name and changing stop button state.
        file = songs[a]
        self.song_name.config(text=file)
        self.current_dir_path = music_folder
        self.close_song.config(state=ACTIVE)
        self.update()

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
        self.song_name = tk.Label(self, text="", bg=self.bg_color, font=("maiandra GD", 37), wraplength=620)
        self.song_name.pack(pady=35)

        #============================| Main music controller buttons |=============================================#
        

        #==============| Frame for all main buttons |====================#
        self.frame1 = tk.Frame(self, bg="#2a0a38", height=100)
        self.frame1.pack(anchor = "s", fill="x", side=BOTTOM)

        #==============| Lyrics song button |====================#
        self.lyrics_song = tk.Button(self.frame1, text="Lyrics Songs", font=("arial rounded mt bold", 25),
                                      command=lambda: self.play_from_directory("Lyrics"))
        self.lyrics_song.grid(row=1, column=1, pady=10)

        #==============| Previous song button |====================#
        self.previous_button = tk.Button(self.frame1, text="<", font="arial 25 bold", command=self.next_song)
        self.previous_button.grid(row=1, column=2, pady=10)
        
        # self.previous_button.bind("<Enter>", lambda e: self.previous_button.configure(fg="red"))
        # self.previous_button.bind("<Leave>", lambda e: self.previous_button.configure(fg="black"))

        # #==============| Previous song button |====================#
        self.close_song = tk.Button(self.frame1, text="Stop", font="arial 20 bold", command=self.stop_music)
        self.close_song.grid(column=3, row=1, pady=10)

        #==============| Next song button |====================#
        self.next_button = tk.Button(self.frame1, text=">", font="arial 25 bold", command=self.next_song)
        self.next_button.grid(row=1, column=4, pady=10)

        #==============| NCS Music |====================#
        self.lyrics_song = tk.Button(self.frame1, text="NCS music", font=("arial rounded mt bold", 25),
                                       command=lambda: self.play_from_directory("NCS"))
        self.lyrics_song.grid(row=1, column=5, pady=10)

        # Playing next song after 4 minutes.
        self.after(self.after_time, self.next_song)

        # Playing song from default directory at the startup of this app.
        self.play_from_directory(self.current_directory)

        
if __name__ == "__main__":
    window = Music_player()
    window.menu_bar()
    window.main_buttons()
    window.mainloop()
