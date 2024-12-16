#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код

# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
```
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

zoo.insert(1, 'bear')
print(zoo)

birds = ['rooster', 'ostrich', 'lark', ]
zoo.extend(birds)
print(zoo)

zoo.remove('elephant')
print(zoo)

print('Лев сидит в клетке номер 1.')
print('Жаворонок сидит в клетке номер 7.')
```
