#include <stdlib.h>

struct Node
{
  int i;
  struct Node* next;
};

typedef struct Node* List;

void use_list(List list)
{
  // Do nothing, set breakpoint here
}

struct Node* create_list(int length)
{
  struct Node* head = NULL;
  struct Node* tail = NULL;
  for (int i = 0; i < length; ++i) {
    if (!head) {
      head = malloc(sizeof(struct Node));
      head->i = i;
      head->next = NULL;
      tail = head;
    } else {
      struct Node* new = malloc(sizeof(struct Node));
      new->i = i;
      new->next = NULL;
      tail->next = new;
      tail = new;
    }
  }
  return head;
}

void free_list(List list)
{
  while (list) {
    List tail = list->next;
    free(list);
    list = tail;
  }
}

int main(void)
{
  List list = create_list(10);
  use_list(list);
  free_list(list);
  return 0;
}
