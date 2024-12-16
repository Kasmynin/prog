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
        printf("%f ", x); 
        printf("%f\n", f(x, h));
        x = x + h;
    } while (x <= 0.5);

    return 0;
} 
