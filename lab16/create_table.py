import sqlite3

def create_tables(db_name):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Категория (
                CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
                Название VARCHAR(255) UNIQUE
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Книга (
                BookID INTEGER PRIMARY KEY AUTOINCREMENT,
                Название VARCHAR(255),
                Цена DECIMAL(10,2),
                Рейтинг INT,
                Url VARCHAR(255),
                CategoryID INT,
                FOREIGN KEY (CategoryID) REFERENCES Категория(CategoryID)
            )
        ''')

        conn.commit()
        print("Таблицы успешно созданы.")

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    db_name = "books.db"
    create_tables(db_name)
