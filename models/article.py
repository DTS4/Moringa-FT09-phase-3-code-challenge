from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles')
        articles = cursor.fetchall()
        conn.close()
        return [cls(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]) for article in articles]

    def __repr__(self):
        return f"Article(id={self.id}, title={self.title}, author_id={self.author_id}, magazine_id={self.magazine_id})"
