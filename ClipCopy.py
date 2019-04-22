#  from tkinter import Tk
import os


class ClipCopy(object):
    def __init__(self):
        pass
        #  self.r = Tk()

    def copy2clipboard(self, txt):
        cmd = 'echo %s | tr -d "\n" | pbcopy' % txt
        os.system(cmd)
        #  self.r.withdraw()
        #  self.r.clipboard_clear()
        #  self.r.clipboard_append(txt)
        #  self.r.update()  # now it stays on the clipboard after the window is closed
        #  self.r.destroy()
