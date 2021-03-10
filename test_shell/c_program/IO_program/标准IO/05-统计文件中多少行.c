#include<stdio.h>
#include<string.h>
#define N 20

int main(int argc,char* argv[])
{
  int count = 0;
  char buf[N];
  if(argc != 2)
  {
    printf("请输入目标文件路径\n");
    return -1;
  }

  FILE *fp = 0;

  if((fp = fopen(argv[1],"r")) == 0)
  {
    perror("fopen");
    return -1;
  }
  //这里的strlen要-1才是\n最后一个字符的下标
  while(fgets(buf,N,fp))
  {
    printf("%ld",strlen(buf));
    if(buf[strlen(buf)-1] == '\n')
      count++;
  }

  printf("%d\n",count);
  fclose(fp);
  return 0;
}
