#include <stdlib.h>
#include <stdio.h>

void fdump_arr(FILE* stream, int* arr, size_t len)
{
  for (int i = 0; i < len; ++i) {
    fprintf(stream, "%d: %d\n", i, arr[i]);
  }
}

void dump_arr(int* arr, size_t len)
{
  fdump_arr(stdout, arr, len);
}

void break_here(int* arr, size_t len)
{
  // Do nothing, set breakpoint here
}

int main(void)
{
  int* arr = calloc(10, sizeof(int));
  for (int i = 0; i < 10; ++i) {
    arr[i] = i;
  }
  break_here(arr, 10);
  free(arr);
  return 0;
}
