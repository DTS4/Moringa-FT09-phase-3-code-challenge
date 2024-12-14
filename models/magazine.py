from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self.name = name   
        self.category = category   

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            self._name = None
            print("Magazine name must be a string between 2 and 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            self._category = None
            print("Magazine category must be a non-empty string.")

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines")
        magazines = cursor.fetchall()
        conn.close()
        return [cls(magazine["id"], magazine["name"], magazine["category"]) for magazine in magazines]

    def __repr__(self):
        if self._name and self._category:
            return f"Magazine(id={self.id}, name={self.name}, category={self.category})"
        else:
            return f"Magazine(id={self.id}, INVALID ENTRY)"
