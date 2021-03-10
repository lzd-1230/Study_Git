#include<stdio.h>

int main()
{
  FILE *fp=0;
  
  if((fp = fopen("test.txt","w")) == 0)
  {
    perror("fopen");
    return -1;
  }

  fputc('a',fp);
  fflush(fp);
  while(1);

  return 0;
}
