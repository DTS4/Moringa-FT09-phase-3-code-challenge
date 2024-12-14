## Magazine Article CRUD
This project is a Python-based CRUD application for managing authors, magazines, and articles. It utilizes SQLite for database management and object-oriented Python to handle the logic.

## Features
Create authors, magazines, and articles with validations.
Establish relationships between authors, magazines, and articles.
Query articles, magazines, and authors using SQL joins.
Includes validation for author name, magazine name, category, and article title.

## Setup
Clone this repository:

bash
Copy code
git clone <repo_url>
cd <repo_name>
Install dependencies using Pipenv:

bash
Copy code
pipenv install
pipenv shell
Run the application:

bash
Copy code
python3 app.py
The application will create the necessary database tables if they don’t exist.

## Folder Structure
/app.py: Main application file to interact with the database.
/database/setup.py: Setup file to create database tables.
/models: Contains the classes Article.py, Author.py, and Magazine.py for CRUD operations.
/tests: Contains some basic tests.

## Validations
Author name: Must be a non-empty string.
Magazine name: Between 2 and 16 characters.
Magazine category: Must be a non-empty string.
Article title: Between 5 and 50 characters.
