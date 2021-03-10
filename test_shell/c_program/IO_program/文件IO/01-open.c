#include<unistd.h>
#include<fcntl.h>
#include<stdio.h>

#if 0
int main()
{
  if((fd = open("test_1.txt",O_WRONLY|O_CREAT|O_TRUNC,0666)) < 0)
  {
    perror("open");
    return -1;
  }

}
#endif

#if 1
int main()
{
  if(fd = (open("test_2.txt",O_RDWR|O_CREAT|O_EXCL,0666)) < 0)
  {
    if(errno == EEXIST)
      perror("file exist error");
    
    else
      perror("other error");
  }
  return 0;
}
#endif

