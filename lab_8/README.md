# Лабораторная работа 8
## Задания 
Решите обе задачи своего варианта.
Примените декоратор к замыканию.
Оформите отчёт в README.md.
## Решение
### Задача 1
Замыкание для получение текста ответа на запрос к API, например https://dogapi.dog/api/v2/facts.
```py
import requests

def create_api_caller(api_base_url):
    def api_caller(endpoint, params=None):
        url = f"{api_base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            try:
                return data['data'][0]['attributes']['body']
            except (KeyError, IndexError, TypeError) as e:
                print(f"Ошибка при парсинге ответа: {e}, ответ: {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса к API: {e}")
            return None

    return api_caller


def main():
    api_base_url = "https://dogapi.dog/api/v2"

    get_fact = create_api_caller(api_base_url)

    try:
        fact = get_fact("facts")

        if fact:
            print(f"Факт о собаке: {fact}")
        else:
            print("Не удалось получить факт о собаке.")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
```
### Задача 2
Декоратор, ограничивающий частоту вызовов функций
