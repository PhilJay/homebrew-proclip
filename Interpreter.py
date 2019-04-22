from ClipCopy import ClipCopy
from Entry import Entry
import os


class Interpreter(object):

    def __init__(self, db, namespace, args):
        self.db = db
        self.namespace = namespace
        self.args = args

    def print_if(self, txt):  # only prints if verbosity is enabled
        if self.namespace.verbose:
            print(txt)

    def interpret(self):
        self.print_if("Arguments: " + str(self.args))

        for opt, arg in self.args.items():
            if opt in ("s", "store"):
                identifier = self.db.push_with_name(arg[0], arg[1])
                self.print_if("Stored: " + str(arg) + ", identifier: " + str(identifier))

            elif opt in ("e", "execute"):
                entry = self.db.get(arg[0])
                if entry is not None:
                    self.print_if("Executing: " + str(entry.content))
                    os.system(entry.content)
                else:
                    print("Cannot execute, entry not found")

            elif opt in ("c", "copy"):
                entry = self.db.get(arg[0])
                if entry is not None:
                    self.print_if("Copying to clipboard: " + str(entry.content))
                    copy = ClipCopy()
                    copy.copy2clipboard(entry.content)
                else:
                    print("Cannot copy to clipboard, entry not found")

            elif opt in ("r", "remove"):
                self.db.delete_name(arg[0])
                self.print_if("Deleted: " + arg[0])

        if self.namespace.list:
            entries = self.db.list()
            for e in entries:
                print(e)

        if self.namespace.removeAll:
            self.db.delete_all()
            self.print_if("Deleted all")
