from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re

def parse_books(url, driver):
    """Парсит данные о книгах с сайта."""
    try:
        driver.get(url)
        books = []
        book_elements = driver.find_elements(By.CLASS_NAME, "product_pod")

        for book_element in book_elements:
            try:
                title_element = book_element.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a")
                title = title_element.get_attribute("title")
                book_url = title_element.get_attribute("href")

                price_element = book_element.find_element(By.CLASS_NAME, "price_color")
                # Используем регулярное выражение для извлечения цены
                price_text = price_element.text
                price_match = re.search(r'£(\d+\.\d+)', price_text)  # Ищем "£" и затем число
                if price_match:
                    price_str = price_match.group(1) # Извлекаем только числовую часть
                    price = float(price_str)
                else:
                    print(f"Не удалось извлечь цену из текста: {price_text}")
                    continue # Пропускаем книгу, если не удалось извлечь цену


                rating_element = book_element.find_element(By.CLASS_NAME, "star-rating")
                rating = rating_element.get_attribute("class").split(" ")[1]

                rating_dict = {
                    "One": 1,
                    "Two": 2,
                    "Three": 3,
                    "Four": 4,
                    "Five": 5,
                }
                rating_num = rating_dict.get(rating, 0)

                books.append({
                    "title": title,
                    "price": price,
                    "rating": rating_num,
                    "book_url": book_url,
                })
            except Exception as e:
                print(f"Ошибка при парсинге книги: {e}")
                continue

        return books

    except Exception as e:
        print(f"Ошибка при парсинге страницы: {e}")
        return []

def get_all_books(base_url, driver):
    """Собирает данные о всех книгах с нескольких страниц."""
    all_books = []
    page_num = 1
    while True:
        url = f"{base_url}/catalogue/page-{page_num}.html"
        print(f"Парсинг страницы: {url}")
        books = parse_books(url, driver)
        if not books:
            break  # Если нет книг, то закончили
        all_books.extend(books)
        page_num += 1
    return all_books

if __name__ == '__main__':
    # Настройка Selenium (только для проверки парсера)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
    driver = webdriver.Chrome(options=chrome_options)

    base_url = "https://books.toscrape.com"
    all_books = get_all_books(base_url, driver)
    driver.quit()

    if all_books:
        print(f"Всего найдено {len(all_books)} книг.")
    else:
        print("Не удалось получить данные о книгах.")