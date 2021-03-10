#include<stdio.h>
#include<math.h>

#define N 10
#define _DEBUGE_

int main()
{
  double m =615,n;
  m += N;
  n = sqrt(m);

  #ifdef _DEBUGE_
    printf("debug:m=%lf  n=%lf\n",m,n);
  #else
    printf("release:m=%lf  n=%lf\n",m,n);
  #endif 
    return 0;
}
