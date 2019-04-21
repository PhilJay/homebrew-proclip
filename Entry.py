class Entry(object):

    def __init__(self, db_object):
        self.identifier = db_object[0]
        self.name = db_object[1]
        self.content = db_object[2]

    def __repr__(self):
        return "{ id: %s, name: %s, content: %s }" % (self.identifier, self.name, self.content)
