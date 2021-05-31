# Version 0.1
# Simple app to get a delay in milliseconds written in python using tkinter.
# By Kurtsley.

import tkinter as tk
import tkinter.font as tkFont
import time


class App:
    """Main window class."""

    def __init__(self, root):

        # setting title
        root.title("Kounter")

        # setting window size
        width = 320
        height = 120
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Start button
        btn_start = tk.Button(root)
        self.text = tk.StringVar()
        self.text.set("Start")
        btn_start["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        btn_start["font"] = ft
        btn_start["fg"] = "#000000"
        btn_start["justify"] = "center"
        btn_start["textvariable"] = self.text
        btn_start.place(x=110, y=60, width=105, height=50)
        btn_start["command"] = self.btn_click

        # Delay output label
        lbl_output = tk.Label(root)
        self.outtext = tk.StringVar()
        self.outtext.set("0")
        ft = tkFont.Font(family='Times', size=10)
        lbl_output["font"] = ft
        lbl_output["fg"] = "#333333"
        lbl_output["justify"] = "center"
        lbl_output["textvariable"] = self.outtext
        lbl_output.place(x=120, y=31, width=63, height=30)

        # Instruction label
        lbl_instr = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        lbl_instr["font"] = ft
        lbl_instr["fg"] = "#333333"
        lbl_instr["justify"] = "center"
        lbl_instr["text"] = 'Click the button twice to get the delay'
        lbl_instr.place(x=30, y=8, width=261, height=30)

        # Milliseconds label
        lbl_ms = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        lbl_ms["font"] = ft
        lbl_ms["fg"] = "#333333"
        lbl_ms["justify"] = "center"
        lbl_ms["text"] = "ms"
        lbl_ms.place(x=165, y=31, width=30, height=30)

        # Setting Clap button clicked flag.
        self.clap_clicked_once = False
        self.clap_clicked_twice = False

    def btn_click(self):
        """Function to control the button clicking logic."""
        if not self.clap_clicked_once and not self.clap_clicked_twice:
            self.first_click()

        elif self.clap_clicked_once and not self.clap_clicked_twice:
            self.second_click()

        else:
            self.reset()

    def time_convert(self):
        """Function to convert the elapsed time to ms."""
        time_lapsed = self.start_time - self.end_time
        self.num = abs(int(time_lapsed * 1000))

    def first_click(self):
        self.clap_clicked_once = True
        self.text.set("End")
        self.start_time = time.time()

    def second_click(self):
        self.clap_clicked_twice = True
        self.text.set("Reset")
        self.end_time = time.time()
        self.time_convert()
        self.outtext.set(self.num)

    def reset(self):
        """Resets all flags and labels."""
        self.clap_clicked_once = False
        self.clap_clicked_twice = False
        self.text.set("Start")
        self.outtext.set("0")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
