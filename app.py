from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Initialize objects and validate them before inserting
    author = Author(id=None, name=author_name)
    magazine = Magazine(id=None, name=magazine_name, category=magazine_category)
    article = Article(id=None, title=article_title, content=article_content, author_id=None, magazine_id=None)

    # Perform validation and only proceed if valid
    if author.name is not None and magazine.name is not None and article.title is not None:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert records into the database if they are valid
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (author.name,))
        author_id = cursor.lastrowid

        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (magazine.name, magazine.category))
        magazine_id = cursor.lastrowid

        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)', 
                       (article.title, article.content, author_id, magazine_id))

        conn.commit()
        conn.close()

        print("\nData successfully added to the database.")
    else:
        print("\nInvalid input, data was not added to the database.")

    # Query and display results using model methods
    magazines = Magazine.get_all()
    authors = Author.get_all()
    articles = Article.get_all()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        print(magazine)

    print("\nAuthors:")
    for author in authors:
        print(author)

    print("\nArticles:")
    for article in articles:
        print(article)

if __name__ == "__main__":
    main()
