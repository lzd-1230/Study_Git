#include<unistd.h>
#include<fcntl.h>
#include<stdio.h>

#if 1
int main(int argc,char* argv[])
{
  char buf[64];  //缓冲区
  int fd,n=0,total=0;

  /* 判断参数个数是否正确 */
  if(argc != 2)
  {
    printf("请输入1个目标文件地址\n");
    return -1;
  }

  /* 打开文件 */
  if((fd = (open(argv[1],O_RDONLY))) < 0)  //这里赋值语句的括号一定不能少
  {
    printf("打开我呢见失败");
    perror("open"); 
    return -1;
  }
  /* 读取字节并且统计大小 */
  while((n = read(fd,buf,64)) > 0)  //error:一直卡死在循环
  {
    total += n;
  }

  printf("总共%d个字节\n",total);
  return 0;
}
#endif

