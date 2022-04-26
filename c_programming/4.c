#include <stdio.h>
#include <stdlib.h>


int main() {
  int c, n;
  for (c = 1; c <= 3; c++) {
    n = rand();
    printf("Random Number is %d\n", n);
  }

  return 0;
}