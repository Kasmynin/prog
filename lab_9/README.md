# Лабораторная работа 9
## Задания 
Решите задачу своего варианта.
Оформите отчёт в README.md.
### Вариант 2
Генератор для построчного чтения файла. Если длина строки превышает заданный предел - возвращает подстроку допустимого размера.
## Решение
```py
def line_generator(filename, max_length):
    try:
        with open(filename, 'r') as f:
            for line in f:
                yield line[:max_length]
    except FileNotFoundError:
        yield "Файл не найден"

for line in line_generator("my_file.txt", 20):
    print(line)
```
