#include<unistd.h>
#include<dirent.h>
#include<fcntl.h>
#include<stdio.h>

#if 1
int main(int argc,char* argv[])
{
  char buf[64];  //缓冲区
  int fds,fdd,n=0,total=0;

  /* 判断参数个数是否正确 */
  if(argc != 2)
  {
    printf("请输入目录地址\n");
    return -1;
  }

  DIR* dirp;

  if((dirp = opendir(argv[1])) == NULL)
  {
    perror("diropen");
  }
  struct dirent* dp;
  while(dp = readdir(dirp))
  {
    printf("%s\n",dp->d_name);
  }
  return 0;
}
#endif

