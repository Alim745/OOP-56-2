import sqlite3


connect = sqlite3.connect("books.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE  IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXY NOT NULL,
        author TEXT NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES user_id
    )
''')



def add_user(name):
    cursor.execute(
        'INSERT INTO users(name) VALUES(?)',
        (name,)
    )
    connect.commit()
    print(f"{name} добавлен!")


def add_book(title, author, user_id):
    cursor.execute(
        'INSERT INTO books(title, author, user_id) VALUES(?,?,?)',
        (title, author, user_id)
    )
    connect.commit()
    print(f"{title} добавлен!")


def get_all_books():
    cursor.execute('''
        SELECT books.title, books.author, users.name
        FROM books LEFT JOIN users ON books.user_id = users.id
    ''')

    books = cursor.fetchall()
    for book in books:
        print(f"Книга: {book[0]}, Автор: {book[1]}, Читатель: {book[2]}")


def update_book_title(book_id, new_title):
    cursor.execute(
        "UPDATE books SET title = ? WHERE id = ?",
        (new_title, book_id)
    )
    connect.commit()
    print("Книга обнавлена!")

def delete_book(book_id):
    cursor.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,)
    )
    connect.commit()
    print("Книга удалена!")



add_user("Alim")
add_user("Kairat")

add_book("Гарри Поттер", "Дж. Роулинг", 1)
add_book("Капитанская дочка", "А.С.Пушкин", 1)
add_book("Отцы и дети", "И.С.Тургенев", 2)
add_book("Чудесный доктор", "А.И.Куприн", 2)
add_book("1984", "Дж. Оруэлл", 2)

get_all_books()

update_book_title(1, "Гарри Поттер и философский камень")

delete_book(5)