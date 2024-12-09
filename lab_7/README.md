# Лабораторная работа 6
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
$a_k = \frac{1}{2} \left( \sqrt{b_{k-1}} + \frac{1}{2} \sqrt{a_{k-1}} \right)$
$a_1 = b_1 = 1$
#### С рекурсией 
```py
def calculate_a(k, a_prev, b_prev):
    if k == 1:
        return 1
    else:
        return (1/2) * ((b_prev**(1/2))+(1/2) * (a_prev**(1/2)))
print("Введите k")
k = int(input())
print("Введите a")
a_prev = int(input())
print("Введите b")
b_prev = int(input())

ak = calculate_a(k, a_prev, b_prev)
print(f"a{k} = {ak}")
```
я не до конца понимаю как это нужно реализовать, ведь функции b_k не имеется, я не знаю как менятеся b
#### Без рекурсии
```py
def calculate_a(k, a_prev, b_prev):
    if k == 1:
        return 1
    else:
        a = a_prev
        b = b_prev
        for i in range(2, k + 1):
            a_next = (1/2) * ((b**(1/2)) + (1/2) * (a**(1/2)))
            b = a
            a = a_next
        return a

print("Введите k")
k = int(input())
print("Введите a_1")  
a_prev = int(input())
print("Введите b_1") 
b_prev = int(input()) 


ak = calculate_a(k, a_prev, b_prev)
print(f"a{k} = {ak}")
```
я окончательно запутался в этом
