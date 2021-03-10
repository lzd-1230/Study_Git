#include<unistd.h>
#include<fcntl.h>
#include<stdio.h>

#if 1
int main(int argc,char* argv[])
{
  char buf[64];  //缓冲区
  int fds,fdd,n=0,total=0;

  /* 判断参数个数是否正确 */
  if(argc != 3)
  {
    printf("请输入源和目标文件地址\n");
    return -1;
  }

  /* 打开源文件 */
  if((fds = (open(argv[1],O_RDONLY))) < 0)  //这里赋值语句的括号一定不能少
  {
    perror("opens"); 
    return -1;
  }
  /* 打开目标文件*/
  if((fdd = (open(argv[2],O_WRONLY|O_CREAT|O_TRUNC,0666))) < 0)  //这里赋值语句的括号一定不能少
  {
    perror("opend"); 
    return -1;
  }
  
  /* 读取字节并且统计大小 */
  while((n=read(fds,buf,64)) > 0)  //n读多少写多少
  {
    write(fdd,buf,n);
  }
  printf("----文件复制完成-----\n");
  close(fds);
  close(fdd);
  return 0;
}
#endif

