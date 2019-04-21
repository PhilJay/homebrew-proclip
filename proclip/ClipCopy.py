from tkinter import Tk


class ClipCopy(object):
    def __init__(self):
        self.r = Tk()

    def copy2clipboard(self, txt):
        self.r.withdraw()
        self.r.clipboard_clear()
        self.r.clipboard_append(txt)
        self.r.update()  # now it stays on the clipboard after the window is closed
        self.r.destroy()
