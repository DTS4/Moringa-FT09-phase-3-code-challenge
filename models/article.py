from database.connection import get_db_connection
from models.author import Author
from models.magazine import Magazine

class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            print("Author must be an instance of Author")
            return
        if not isinstance(magazine, Magazine):
            print("Magazine must be an instance of Magazine")
            return
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            print("Title must be a string between 5 and 50 characters")
            return

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
            (title, '', author.id, magazine.id)
        )
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

        self.author = author
        self.magazine = magazine
        self.title = title

    def __repr__(self):
        return f'<Article {self.title}>'

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @property
    def title(self):
        return self._title
