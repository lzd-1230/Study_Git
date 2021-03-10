#include<stdio.h>

int main()
{
  int cnt = 0;
  while(1)
  {
    FILE *fp = 0;
    cnt++;
    // 异常处理
    if((fp = fopen("test.txt","r+")) == NULL)
    {
      printf("%d\n",cnt); // 调试信息一定要加回车
      perror("fopen");
      return -1;
    }
  }
  return 0;
}
