from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            print("Magazine name must be a string between 2 and 16 characters.")
            return
        if not isinstance(category, str) or len(category) == 0:
            print("Magazine category must be a non-empty string.")
            return        
        self._id = id
        self._name = name
        self._category = category
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (name, category))
        conn.commit()
        self._id = cursor.lastrowid
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            print("Magazine name must be a string between 2 and 16 characters.")
            return
        self._name = value
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE magazines SET name = ? WHERE id = ?', (value, self.id))
        conn.commit()
        conn.close()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            print("Magazine category must be a non-empty string.")
            return
        self._category = value
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE magazines SET category = ? WHERE id = ?', (value, self.id))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines')
        magazines = cursor.fetchall()
        conn.close()
        return [cls(magazine["id"], magazine["name"], magazine["category"]) for magazine in magazines]

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE magazine_id = ?', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return [article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]) for article in articles]

    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT authors.*
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
        ''', (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return [Author(author["id"], author["name"]) for author in authors]

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT authors.*, COUNT(articles.id) as article_count
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING article_count > 2
        ''', (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return [author(author["id"], author["name"]) for author in authors]

    def __repr__(self):
        return f"Magazine(id={self.id}, name={self.name}, category={self.category})"
