from Database import Database


class Interpreter(object):
    def __init__(self):
        pass

    def interpret(self, args):
        entry = None
        execute = False
        copy = False

        db = Database()

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
        return entry, execute, copy
