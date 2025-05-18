import sqlite3
from pypika import Query, Table, Field
from pypika.functions import Avg, Count, Max, Min

def execute_pypika_queries(db_name):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        book = Table("Книга")
        category = Table("Категория")

        # 1. Запрос с JOIN: Вывести название книги и название её категории
        q1 = Query.from_(book).join(category).on(book.CategoryID == category.CategoryID).select(book.Название, category.Название).limit(5) #ограничение на 5 записей для примера
        cursor.execute(str(q1))
        results_q1 = cursor.fetchall()
        print("Название книги и название категории (JOIN):")
        for row in results_q1:
            print(f"  Книга: {row[0]}, Категория: {row[1]}")

        # 2. Запрос с JOIN: Вывести название книги и цену, отсортированные по названию категории
        q2 = Query.from_(book).join(category).on(book.CategoryID == category.CategoryID).select(book.Название, book.Цена, category.Название).orderby(category.Название).limit(5)
        cursor.execute(str(q2))
        results_q2 = cursor.fetchall()
        print("\nНазвание книги и цена, отсортированные по категории (JOIN):")
        for row in results_q2:
            print(f"  Книга: {row[0]}, Цена: {row[1]}, Категория: {row[2]}")

        # 3. Запрос с агрегирующей функцией: Средняя цена книг
        q3 = Query.from_(book).select(Avg(book.Цена)).as_("average_price")
        cursor.execute(str(q3))
        average_price = cursor.fetchone()[0]
        print(f"\nСредняя цена книг: {average_price}")

        # 4. Запрос с группировкой: Количество книг в каждой категории
        q4 = Query.from_(book).join(category).on(book.CategoryID == category.CategoryID).groupby(category.Название).select(category.Название, Count(book.BookID))
        cursor.execute(str(q4))
        results_q4 = cursor.fetchall()
        print("\nКоличество книг в каждой категории:")
        for row in results_q4:
            print(f"  Категория: {row[0]}, Количество: {row[1]}")

        # 5. Запрос с MIN/MAX: Самая дорогая и самая дешёвая книга
        q5_max = Query.from_(book).select(book.Название, Max(book.Цена)).limit(1)
        cursor.execute(str(q5_max))
        most_expensive = cursor.fetchone()

        q5_min = Query.from_(book).select(book.Название, Min(book.Цена)).limit(1)
        cursor.execute(str(q5_min))
        least_expensive = cursor.fetchone()

        print("\nСамая дорогая книга:")
        print(f"  Название: {most_expensive[0]}, Цена: {most_expensive[1]}")
        print("Самая дешёвая книга:")
        print(f"  Название: {least_expensive[0]}, Цена: {least_expensive[1]}")

    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    db_name = "books.db"
    execute_pypika_queries(db_name)
