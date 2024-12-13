from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('INSERT OR IGNORE INTO authors (id, name) VALUES (?, ?)', (id, name))
        conn.commit()
        conn.close()

    def __repr__(self):
        return f'<Author {self.name}>'

    @property
    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE author_id = ?', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return [article(article['id'], article['title'], article['content'], article['author_id'], article['magazine_id']) for article in articles]
