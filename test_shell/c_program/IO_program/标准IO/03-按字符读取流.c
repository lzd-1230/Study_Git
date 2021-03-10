#include<stdio.h>

int main(int argc,char* argv[])
{
  /*  从命令行读取一个字符
  int ch;
  ch = fgetc(stdin);
  printf("%c\n",ch);
  */

  if(argc != 2)
  {
    printf("请输入一个文件路径\n");
    return -1;
  }

  FILE *fp = 0;
  int ch=0,count=0;
  
  if((fp = fopen(argv[1],"r")) == 0)
  {
    perror("fopen");
    return -1;
  }
  
  while((ch = getc(fp) != EOF))
  {
    count++;
  }
  printf("%d\n",count);
  return 0;
}
