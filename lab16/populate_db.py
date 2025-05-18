import sqlite3
from parser import get_all_books  # Импортируем функции парсера
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def populate_db(db_name, books_data):
    """Заполняет таблицы данными о книгах."""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Функция для получения или создания категории
        def get_or_create_category(category_name):
            cursor.execute("SELECT CategoryID FROM Категория WHERE Название = ?", (category_name,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                cursor.execute("INSERT INTO Категория (Название) VALUES (?)", (category_name,))
                conn.commit()
                return cursor.lastrowid

        # Заполнение таблицы Книга
        for book in books_data:
            # В данном примере все книги из одной категории (пока)
            category_name = "Books" # Или извлекайте категорию из URL, если это возможно
            category_id = get_or_create_category(category_name)

            sql = '''
                INSERT INTO Книга (Название, Цена, Рейтинг, Url, CategoryID)
                VALUES (:title, :price, :rating, :book_url, :category_id)
            '''
            data = {
                "title": book["title"],
                "price": book["price"],
                "rating": book["rating"],
                "book_url": book["book_url"],
                "category_id": category_id,
            }
            cursor.execute(sql, data) # Использование именованных плейсхолдеров

        conn.commit()
        print("База данных успешно заполнена.")

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    # Настройка Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
    driver = webdriver.Chrome(options=chrome_options)

    base_url = "https://books.toscrape.com"
    all_books = get_all_books(base_url, driver)
    driver.quit()

    if all_books:
        db_name = "books.db"
        populate_db(db_name, all_books)
    else:
        print("Не удалось получить данные о книгах.")