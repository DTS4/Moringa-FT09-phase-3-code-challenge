from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self._id = id
        self.name = name  

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            self._name = None
            print("Author name must be a non-empty string.")

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        authors = cursor.fetchall()
        conn.close()
        return [cls(author["id"], author["name"]) for author in authors]

    def __repr__(self):
        if self._name:
            return f"Author(id={self.id}, name={self.name})"
        else:
            return f"Author(id={self.id}, INVALID ENTRY)"
