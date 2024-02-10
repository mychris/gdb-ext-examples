#include <stdlib.h>

struct Array {
  int* base;
  size_t len;
};

struct Node {
  int val;
  struct Node* next;
};

typedef struct Array* Array;
typedef struct Node* List;

Array create_array(int length)
{
  Array result = malloc(sizeof(struct Array));
  result->base = malloc(sizeof(int) * length);
  result->len = length;
  for (int i = 0; i < length; ++i) {
    result->base[i] = i;
  }
  return result;
}

List create_list(int length)
{
  List head = NULL;
  List tail = NULL;
  for (int i = 0; i < length; ++i) {
    List new = malloc(sizeof(struct Node));
    new->val = i;
    new->next = NULL;
    if (!head) {
      head = tail = new;
    } else {
      tail->next = new;
      tail = new;
    }
  }
  return head;
}

void free_array(Array arr)
{
  free(arr->base);
  free(arr);
}

void free_list(List list)
{
  while (list) {
    List head = list;
    list = list->next;
    free(head);
  }
}

void break_here(Array array, List list)
{
  // Do nothing, set breakpoint here
}

int main(void)
{
  Array array = create_array(10);
  List list = create_list(10);
  break_here(array, list);
  free_array(array);
  free_list(list);
  return 0;
}
