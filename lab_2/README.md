# Лабораторная работа 2
## Вариант 2
$$
f(x)=
    \begin{cases}
        e^{sinx} \text{,} & 0 \leq x \leq \frac{1}{4} \text{;} \\
        e^x-\frac{1}{\sqrt{x}} \text{,} & \frac{1}{4} < x \leq \frac{1}{2} \text{.}
    \end{cases}
$$
## Задания
1. написать программу по вариант используя оператор цикла do while
2. написать программу используя оператор цикла for
3. построить график с использованием gnuplot
4. составить блок-схему
5. оформить отчет
## График
![график](gnuplot.pdf)
## Блок-схема

## Программа 
1. программа написана с помощью цикла do while 
``` c
#include <math.h>
#include <stdio.h>

float f(float x, float h) {
    float eps = h/2;
    if (x >= 0 && x <= 0.25)
        return exp(sin(x));
    else if (x > 0.25 && x <= 0.5)
        return exp(x) - pow(sqrt(x), -1);
}

int main()
{
    float x = 0;
    float h;
    printf("введите шаг h -> ");
    scanf("%f", &h);
    do {
        printf("%f", x); 
        printf("%f", f(x, h));
        x = x + h;
    } while (x <= 0.5);

    return o;
}
```
2. программа написана с помощью цикла for
``` c
#include <math.h>
#include <stdio.h>

float f(float x, float h) {
    float eps = h/2;
    if (x >= 0 && x <= 0.25)
        return exp(sin(x));
    else if (x > 0.25 && x <= 0.5)
        return exp(x) - pow(sqrt(x), -1);
}

int main() {
    float x = 0;
    float h;
    printf("введите шаг h -> ");
    scanf("%f", &h);
    for (x = 0; x <= 0.5; x += h) {
        printf("x = %f, f(x) = %f\n", x, f(x, h));
    }
    return 0;
}
```
