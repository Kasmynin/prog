# Лаборатоная работа 6
## Задания 
Напишите две функции для решения задач своего варианта - с использованием рекурсии и без.
Оформите отчёт в README.md.
## Решение
### Задание 1
Функция для расчёта суммы вложенных списков.
sum_nested([1, [2, [3, 4, [5]]]])
15

#### С рекурсией
```py
def sum_nested(nested_list):
    total = 0
    for item in nested_list:
        if isinstance(item, list):
            total += sum_nested(item)
        elif isinstance(item,(int,float)):
            total += item
        else:
            pass

    return total
print(sum_nested([1, [2, [3, 4, [5]]]]))
```
#### Без рекурсии 
```py
def sum_nested_iterative(nested_list):
    stack = [nested_list]
    total = 0
    while stack:
        current_list = stack.pop()
        for item in current_list:
            if isinstance(item, list):
                stack.append(item)
            elif isinstance(item,(int,float)):
                total += item
            else:
                pass

    return total

print(sum_nested_iterative([1, [2, [3, 4, [5]]]]))
```
### Задание 2
Функция для расчёта 
$a_k = \frac{1}{2} \left( \sqrt{b_(k-1)} + \frac{1}{2} \sqrt{a_(k-1)} \right)$
