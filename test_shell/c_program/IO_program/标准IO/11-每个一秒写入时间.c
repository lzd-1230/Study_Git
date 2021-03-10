#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<time.h>
#define N 64 

/* 通过time()获取一个时间 
 * 通过ilocaltime()将时间转换成系统时间
 * sleep()实现程序的睡眠
 * */

int main(int argc,char* argv[])
{
  struct tm *tp;
  time_t t;
  int count = 0;
  char buff[N];

  if(argc != 2)
  {
    printf("请输入目标文件路径\n");
    return -1;
  }

  FILE *fp = 0;
  /* 错误处理 */
  if((fp = fopen(argv[1],"a+")) == 0)
  {
    perror("fopen");
    return -1;
  }

  //这里的strlen要-1才是\n最后一个字符的下标
  while(fgets(buff,64,fp) != 0)
  {
    if(buff[strlen(buff)-1] == '\n')
    {
      count++;
    }
  }
  /* 写入时间 */
  while(1)
  {
    time(&t);
    tp = localtime(&t);
    /* 利用count继续输出行号 */
    fprintf(fp,"%02d. %d-%02d-%02d %02d:%02d:%02d\n",++count,1900+tp->tm_year,
                                                    tp->tm_mon+1,tp->tm_mday,
                                                    tp->tm_hour,tp->tm_min,
                                                    tp->tm_sec);
    /* 因为普通打开的文件是全缓冲的,因此强制刷新缓冲区 */
    fflush(fp);
    sleep(1);  // 睡眠一秒

  }

//  printf("%d\n",count);
  fclose(fp);
  return 0;
}
