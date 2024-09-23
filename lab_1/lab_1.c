#include <stdio.h>

int main()
{
float x, y, z;
printf("введи x -> ");
scanf("%f", &x);
printf("введи y -> ");
scanf("%f", &y);
printf("введи z -> ");
scanf("%f", &z);

if (!x && !y && !z)
  return 0;

if (x>y>z)
  printf("x: %f\n", x);
else if (y>x+z)
  printf("y: %f\n", y);
else if (z>x+y)
  printf("z: %f\n", z);
else if (x>y && x>z)
  printf("%f\n", x-(y+z));
else if (y>x && y>z)
  printf("%f\n", y-(x+z));
else if (z>x && z>y)
  printf("%f\n", z-(x+y));
return 0;
}
