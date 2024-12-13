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

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert records into the database
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid

    cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid

    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)', 
                   (article_title, article_content, author_id, magazine_id))

    conn.commit()

    # Query and display results using model methods
    magazines = Magazine.get_all()
    authors = Author.get_all()
    articles = Article.get_all()

    conn.close()

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
