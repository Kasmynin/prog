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
<<<<<<< HEAD
  
  if (!x && !y && !z)
    return 0;

=======

  if (!x && !y && !z)
    return 0;

>>>>>>> 2483149 (m)
  float max = x;
  if (y > max)
    max = y;
  if (z > max)
    max = z;
  float sum = x + y + z - max;
  if (max > sum)
    printf("max = %f\n", max);
  else
    printf("sum - max = %f\n", sum - max);
  return 0;
}
