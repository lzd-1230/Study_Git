#include<stdio.h>

int main()
{
  long count =0;
  FILE *fp = 0;
  /* 可以用任意权限打开文件 */
  fp = fopen("test.txt","r");
  /* 将指针移到结尾 */
  fseek(fp,0,SEEK_END);
  count = ftell(fp);
  printf("--获取的文件长度为%ld--",count);
  return 0;
}
