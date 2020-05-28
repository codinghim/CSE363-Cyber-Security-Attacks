#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]) {

  unsigned int i;
  char buf[256];

  for (i=0; i<strlen(argv[1]); i++) {
    if (((unsigned int)argv[1][i] >= 0x68) && ((unsigned int)argv[1][i] <= 0x6e)) {
      argv[1][i] = 'x';
    }
  }

  strcpy(buf, argv[1]);

  printf("Input: %s\n", buf);
  return 0;
}
