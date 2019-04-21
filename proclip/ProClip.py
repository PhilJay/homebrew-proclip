#!/usr/bin/env python

from proclip.Database import Database
from tkinter import Tk
import sys, argparse, os


def copy2clipboard(txt):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(txt)
    r.update()  # now it stays on the clipboard after the window is closed
    r.destroy()


if __name__ == '__main__':

    argv = sys.argv
    argv = argv[1:]  # first element of args is always the file name
    length = len(argv)
    db = Database()

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', nargs='*')
    parser.add_argument('-p', nargs='*')
    parser.add_argument('-r', nargs='*')
    parser.add_argument('-g', nargs='*')
    parser.add_argument('-c', nargs='*')
    parser.add_argument('-e', nargs='*')

    args = vars(parser.parse_args())
    args = dict((k, v) for k, v in args.items() if v is not None)
    # print(args)

    entry = None
    execute = False
    copy = False

    for opt, arg in args.items():
        if opt in ("p", "push"):
            if len(arg) == 2:
                identifier = db.push_with_name(arg[0], arg[1])
            else:
                identifier = db.push(arg[0])
            print("Stored: " + str(arg) + ", identifier: " + str(identifier))
        elif opt in ("l", "list"):
            print(db.list())
        elif opt in ("g", "get"):
            if len(arg) == 1:
                entry = db.get_id(arg[0])
                if entry is None:
                    entry = db.get_name(arg[0])
            else:
                entry = db.get_id(1)
            print("Getting... " + str(entry))
        elif opt in ("c", "copy"):
            copy = True
        elif opt in ("e", "execute"):
            execute = True
        elif opt in ("r", "remove"):
            if len(arg) == 1:
                db.delete_name(arg[0])
                print("Deleted " + arg[0])
            else:
                db.delete_all()
                print("Deleted all")

    db.close()

    if entry is not None:
        if execute:
            print("Executing...")
            os.system(entry.content)
        if copy:
            print("Copying to clipboard...")
            copy2clipboard(entry.content)
