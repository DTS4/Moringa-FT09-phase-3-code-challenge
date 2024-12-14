from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self._id = id
        self.title = title   
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else:
            self._title = None
            print("Article title must be a string between 5 and 50 characters.")

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles")
        articles = cursor.fetchall()
        conn.close()
        return [
            cls(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"])
            for article in articles
        ]

    def __repr__(self):
        if self._title:
            return f"Article(id={self.id}, title={self.title}, author_id={self.author_id}, magazine_id={self.magazine_id})"
        else:
            return f"Article(id={self.id}, INVALID ENTRY)"
