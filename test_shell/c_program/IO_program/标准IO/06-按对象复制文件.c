#include<stdio.h>

int main(int argc,char* argv[])
{
  /* 定义参数 */
  FILE *fps = 0,*fpd = 0;
  char buff[5];

  /* 检查参数 */
  if(argc != 3)
  {
    printf("请输入源和目标文件路径\n");
    return -1;
  }
  /* 文件打开异常判断 */
  if((fps = fopen(argv[1],"r")) == 0)
  {
    perror("fsopen");
    return -1;
  }
  if((fpd = fopen(argv[2],"w")) == 0)
  {
    perror("fdopen");
    return -1;
  }

  /* 按对象读取 */ 
  while(fread(buff,sizeof(char),sizeof(buff),fps) != 0)
  {
    fwrite(buff,sizeof(char),sizeof(buff),fpd);
  }

  fclose(fpd);
  fclose(fps);
  printf("--复制完成--\n");

  return 0;
}
