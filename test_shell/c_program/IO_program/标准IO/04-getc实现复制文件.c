#include<stdio.h>

int main(int argc,char* argv[])
{
  if(argc != 3)
  {
    printf("请输入源和目标文件路径\n");
    return -1;
  }

  FILE *fps = 0,*fpd = 0;
  
  if((fps = fopen(argv[1],"r")) == 0)
  {
    perror("fsopen");
    return -1;
  }
  /* 打开目标文件 */
  if((fpd = fopen(argv[2],"w")) == 0)
  {
    perror("fdopen");
    return -1;
  }

  char ch = 0; 
  while((ch = fgetc(fps)) != EOF)
  {
    fputc(ch,fpd);
  }

  fclose(fpd);
  fclose(fps);

  return 0;
}
