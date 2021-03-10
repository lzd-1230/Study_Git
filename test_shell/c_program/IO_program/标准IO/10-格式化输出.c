#include<stdio.h>

int main()
{
  FILE *fp = 0;
  char buff[20];

  fp = fopen("test.txt","w");
  /* 将年月日写入文件 */
  fprintf(fp,"%d-0%d-0%d\n",2021,3,3);
  /* 写入缓冲区*/
  sprintf(buff,"%d-0%d-0%d",2021,3,3);
  printf("%s\n",buff);
  return 0;
}
