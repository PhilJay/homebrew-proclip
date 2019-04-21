import sqlite3
from proclip.Entry import Entry


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("proclip.db")
        self.c = self.conn.cursor()

        create = """CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY, 
        name TEXT,
        content TEXT not null,
        unique (name, content)
        )"""
        # Create table
        self.c.execute(create)

        # Save (commit) the changes
        self.conn.commit()

    def push(self, content):
        insert = "INSERT INTO entries (content) VALUES (?)"
        self.c.execute(insert, [content])
        self.conn.commit()
        return self.c.lastrowid

    def push_with_name(self, name, content):
        self.c.execute("INSERT INTO entries (name, content) VALUES (?, ?)", [name, content])
        self.conn.commit()
        return self.c.lastrowid

    def list(self):
        results = self.c.execute("SELECT * FROM entries").fetchall()
        entries = []

        for result in results:
            entries.append(Entry(result))

        return entries

    def get_id(self, identifier):
        result = self.c.execute("SELECT * FROM entries WHERE id=?", [identifier]).fetchone()
        if result is not None:
            return Entry(result)
        else:
            return None

    def get_name(self, name):
        result = self.c.execute("SELECT * FROM entries WHERE name=?", [name]).fetchone()
        if result is not None:
            return Entry(result)
        else:
            return None

    def pop(self):
        top = self.c.execute("SELECT * FROM entries ORDER BY id ASC LIMIT 1").fetchone()
        self.delete(0)
        return top

    def delete(self, offset):
        rows = self.c.execute("SELECT * FROM entries ORDER BY id ASC").fetchmany(offset + 1)
        length = len(rows)
        if length > offset:
            row = rows[offset]
            self.c.execute("DELETE FROM entries WHERE id=?", [row[0]])
        else:
            row = rows[length - 1]
            self.c.execute("DELETE FROM entries WHERE id=?", [row[0]])
        self.conn.commit()

    def delete_name(self, name):
        self.c.execute("DELETE FROM entries WHERE name=?", [name])
        self.conn.commit()
        return self.c.lastrowid

    def delete_id(self, id):
        self.c.execute("DELETE FROM entries WHERE id=?", [id])
        self.conn.commit()
        return self.c.lastrowid

    def delete_all(self):
        self.c.execute("DROP TABLE entries")
        self.conn.commit()

    def close(self):
        self.conn.close()
