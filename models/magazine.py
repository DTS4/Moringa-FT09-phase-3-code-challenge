from database.connection import get_db_connection
from models.author import Author

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert into database if not already there
        cursor.execute('INSERT OR IGNORE INTO magazines (id, name, category) VALUES (?, ?, ?)', (id, name, category))
        conn.commit()
        conn.close()

    def __repr__(self):
        return f'<Magazine {self.name} ({self.category})>'

    @property
    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE magazine_id = ?', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return [article(article['id'], article['title'], article['content'], article['author_id'], article['magazine_id']) for article in articles]

    @property
    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            '''
            SELECT DISTINCT a.* FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
            ''',
            (self.id,)
        )
        contributors = cursor.fetchall()
        conn.close()
        return [Author(contributor['id'], contributor['name']) for contributor in contributors]
