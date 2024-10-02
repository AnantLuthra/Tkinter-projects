"""
Author - Anant Luthra
Date - 16/1/22
Purpose - To make a calculator GUI through tkinter.
"""

from tkinter import *

class Calculator(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("355x447")
        self.minsize("355", "447")
        self.maxsize("355", "447")
        self.title("Calculator - By Anant Luthra")
        self.wm_iconbitmap("./assets/calculator.ico")
        self.config(bg="#13aaeb")

    def handle_backspace(self):
        current_text = self.value.get()
        if current_text:
            self.value.set(current_text[:-1])

    def give(self, digit):
        "This function is used to handle pressed button action. wheather it's a digit or a function button"

        if digit == "=":
            value = eval(self.value.get())
        elif digit == "C":
            value = "0"
        else:
            if self.value.get() == "0":
                value = digit
            else:
                value = self.value.get() + digit

        self.value.set(value)
        self.update()

    def entry(self):
        "This function is used to make entry widget for visible calculations."
        self.value = StringVar()
        self.value.set("0")
        self.entery = Entry(self, font=("Bahnschrift Light ", 25), textvariable=self.value, bg="#b7dbeb")
        self.entery.pack(fill=X, anchor="n", ipady=10, pady=7, padx=4)

    def all_buttons(self):
        
        self.frame1 = Frame(self, height=100, width=380, bg="", padx=3)
        
        # ====================================== sign C ==============================================================#
        self.button = Button(self.frame1, text="C", command=lambda: self.give("C"), font=("cambria", 20), bg="#49b7e6",
                               pady=10, padx=28, activebackground="#91cce6")
        self.button.grid(column=4, row=1)

        # sign /
        self.button = Button(self.frame1, text="/", command=lambda: self.give("/"), font=("cambria", 20), bg="#49b7e6",
                               pady=10, padx=26, activebackground="#91cce6")
        self.button.grid(column=3, row=1)

        # sign **
        self.button = Button(self.frame1, text="**", command=lambda: self.give("**"), font=("cambria", 20), bg="#49b7e6",
                               pady=10, padx=21, activebackground="#91cce6")
        self.button.grid(column=2, row=1)

        # sign *                                                                                                    
        self.button = Button(self.frame1, text="*", command=lambda: self.give("*"), font=("cambria", 20), bg="#49b7e6",
                               pady=10, padx=26, activebackground="#91cce6")
        self.button.grid(column=1, row=1)

        # button 9
        self.button = Button(self.frame1, text="7", command=lambda: self.give("7"), font=("cambria", 20),
                             bg="#75c4e6", activebackground="#91cce6", pady=10, padx=25)
        self.button.grid(column=1, row=2)

        # button 8
        self.button = Button(self.frame1, text="8", command=lambda: self.give("8"), font=("cambria", 20),
                             bg="#75c4e6", activebackground="#91cce6",  pady=10, padx=25)
        self.button.grid(column=2, row=2)

        # button 7
        self.button = Button(self.frame1, text="9", command=lambda: self.give("9"), font=("cambria", 20),
                             bg="#75c4e6", activebackground="#91cce6", pady=10, padx=25)
        self.button.grid(column=3, row=2)

        # sign %
        self.button = Button(self.frame1, text="%", command=lambda: self.give("%"), font=("cambria", 20), bg="#49b7e6",
                               pady=10, padx=23, activebackground="#91cce6")
        self.button.grid(column=4, row=2)

        # button 6
        self.button = Button(self.frame1, text="4", command=lambda: self.give("4"), font=("cambria", 20),
                             bg="#75c4e6", activebackground="#91cce6", pady=10, padx=25)
        self.button.grid(column=1, row=3)

        # button 5
        self.button = Button(self.frame1, text="5", command=lambda: self.give("5"), font=("cambria", 20),
                             bg="#75c4e6", activebackground="#91cce6", pady=10, padx=25)
        self.button.grid(column=2, row=3)

        # button 4
        self.button = Button(self.frame1, text="6", command=lambda: self.give("6"), font=("cambria", 20),
                             bg="#75c4e6", activebackground="#91cce6", pady=10, padx=25)
        self.button.grid(column=3, row=3)

        # sign -
        self.button = Button(self.frame1, text=" - ", command=lambda: self.give("-"), font=("cambria", 20), bg="#49b7e6",
                              pady=10, padx=25, activebackground="#91cce6")
        self.button.grid(column=4, row=3)

        # button 3
        self.button = Button(self.frame1, text="1", command=lambda: self.give("1"), font=("cambria", 20),
                             bg="#75c4e6", activebackground="#91cce6", pady=10, padx=25)
        self.button.grid(column=1, row=4)

        # button 2
        self.button = Button(self.frame1, text="2", command=lambda: self.give("2"), font=("cambria", 20),
                             bg="#75c4e6", activebackground="#91cce6", pady=10, padx=25)
        self.button.grid(column=2, row=4)

        # button 1
        self.button = Button(self.frame1, text="3", command=lambda: self.give("3"), font=("cambria", 20),
                             bg="#75c4e6", activebackground="#91cce6", pady=10, padx=25)
        self.button.grid(column=3, row=4)

        # sign +
        self.button = Button(self.frame1, text="+ ", command=lambda: self.give("+"), font=("cambria", 20), bg="#49b7e6",
                             pady=10, padx=25, activebackground="#91cce6")
        self.button.grid(column=4, row=4)

        # button 0
        self.button = Button(self.frame1, text="0", command=lambda: self.give("0"), font=("cambria", 20),
                             bg="#75c4e6", activebackground="#91cce6", pady=10, padx=25)
        self.button.grid(column=2, row=5)

        # sign .
        self.button = Button(self.frame1, text=" . ", command=lambda: self.give("."), font=("cambria", 20), bg="#49b7e6",
                             pady=10, padx=23, activebackground="#91cce6")
        self.button.grid(column=3, row=5)

        # sign =
        self.button = Button(self.frame1, text="= ", command=lambda: self.give("="), font=("cambria", 20), bg="#49b7e6",
                             pady=10, padx=25, activebackground="#91cce6")
        self.button.grid(column=4, row=5)

        # sign //
        self.button = Button(self.frame1, text="//", command=lambda: self.give("//"), font=("cambria", 19), bg="#49b7e6",
                               pady=12, padx=21, activebackground="#91cce6")
        self.button.grid(column=1, row=5)
        
        self.frame1.pack(fill=X, side=TOP)


        self.bind_all("1", lambda e: self.give("1"))
        self.bind_all("2", lambda e: self.give("2"))
        self.bind_all("3", lambda e: self.give("3"))
        self.bind_all("4", lambda e: self.give("4"))
        self.bind_all("5", lambda e: self.give("5"))
        self.bind_all("6", lambda e: self.give("6"))
        self.bind_all("7", lambda e: self.give("7"))
        self.bind_all("8", lambda e: self.give("8"))
        self.bind_all("9", lambda e: self.give("9"))
        self.bind_all("0", lambda e: self.give("0"))
        self.bind_all("=", lambda e: self.give("="))
        self.bind_all("-", lambda e: self.give("-"))
        self.bind_all("+", lambda e: self.give("+"))
        self.bind_all("*", lambda e: self.give("*"))
        self.bind_all("^", lambda e: self.give("^"))
        self.bind_all("/", lambda e: self.give("/"))
        self.bind_all(".", lambda e: self.give("."))
        self.bind_all("%", lambda e: self.give("%"))
        self.bind_all("<Return>", lambda e: self.give("="))
        self.bind_all("<BackSpace>", lambda e: self.handle_backspace())
        self.bind_all("C", lambda e: self.give("C"))
        self.bind_all("c", lambda e: self.give("C"))


if __name__ == "__main__":
    window = Calculator()

    window.entry()
    window.all_buttons()

    window.mainloop()
