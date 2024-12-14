from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        if not isinstance(name, str) or len(name) == 0:
            print("Author name must be a non-empty string.")
            return        
        self._id = id
        self._name = name
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        conn.commit()
        self._id = cursor.lastrowid
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors')
        authors = cursor.fetchall()
        conn.close()
        return [cls(author["id"], author["name"]) for author in authors]

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE author_id = ?', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return [article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]) for article in articles]

    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT magazines.*
            FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.author_id = ?
        ''', (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return [magazine(magazine["id"], magazine["name"], magazine["category"]) for magazine in magazines]

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name})"
