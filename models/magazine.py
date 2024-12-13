from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines')
        magazines = cursor.fetchall()
        conn.close()
        return [cls(magazine["id"], magazine["name"], magazine["category"]) for magazine in magazines]

    def __repr__(self):
        return f"Magazine(id={self.id}, name={self.name}, category={self.category})"
