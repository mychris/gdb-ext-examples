
void break_here(void)
{
  // Do nothing, set breakpoint here
}

void f3(void)
{
  break_here();
}

void f2(void)
{
  f3();
}

void f1(void)
{
  f2();
}

int main(void)
{
  f1();
  return 0;
}
