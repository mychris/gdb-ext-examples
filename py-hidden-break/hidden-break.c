#include <stdio.h>

static const char* VERSION = "1.2.3";

void print_version(void)
{
  printf("%s\n", VERSION);
}

void break_here(void)
{
  // Do nothing, set breakpoint here
}

void init(void)
{
  // pretend to do some initialization
}

int main(void)
{
  init();
  break_here();
  return 0;
}
