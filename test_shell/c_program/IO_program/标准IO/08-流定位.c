#include<stdio.h>

int main()
{
  FILE *fp = 0;
  fp = fopen("test.txt","r+");
  fseek(fp,0,SEEK_END);
  fputc('t',fp);
  printf("--添加成功--");
  return 0;
}
