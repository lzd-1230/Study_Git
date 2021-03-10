#include<stdio.h>

int main()
{
  FILE *fp = 0;
  // 异常处理
  if((fp = fopen("testt.txt","r+")) == NULL)
  {
    perror("fopen");
    return -1;
  }
  fclose(fp);
  return 0;
}
