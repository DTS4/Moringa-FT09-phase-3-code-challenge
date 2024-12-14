from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            print("Article title must be a string between 5 and 50 characters.")
            return
        
        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id

        # Insert into database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)', 
                       (title, content, author_id, magazine_id))
        conn.commit()
        self._id = cursor.lastrowid
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors WHERE id = ?', (self._author_id,))
        author = cursor.fetchone()
        conn.close()
        return author(author["id"], author["name"])

    @property
    def magazine(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines WHERE id = ?', (self._magazine_id,))
        magazine = cursor.fetchone()
        conn.close()
        return magazine(magazine["id"], magazine["name"], magazine["category"])

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles')
        articles = cursor.fetchall()
        conn.close()
        return [cls(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]) for article in articles]

    def __repr__(self):
        return f"Article(id={self.id}, title={self.title}, author_id={self._author_id}, magazine_id={self._magazine_id})"
