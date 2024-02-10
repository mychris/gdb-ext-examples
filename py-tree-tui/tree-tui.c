#include <stdlib.h>
#include <string.h>

struct Node {
  char* name;
  struct Node* childs[10];
};

typedef struct Node* Node;

Node tree_create_child(struct Node* parent, const char* name)
{
  for (int i = 0; i < 10; ++i) {
    if (NULL == parent->childs[i]) {
      parent->childs[i] = calloc(1, sizeof(struct Node));
      parent->childs[i]->name = strdup(name);
      return parent->childs[i];
    }
  }
  return NULL;
}

Node create_tree(const char* name)
{
  Node result = calloc(1, sizeof(struct Node));
  result->name = strdup(name);
  return result;
}

void tree_free(Node tree)
{
  free(tree->name);
  for (int i = 0; i < 10; ++i) {
    if (NULL != tree->childs[i]) {
      tree_free(tree->childs[i]);
    }
  }
  free(tree);
}

void break_here(Node tree)
{
  // Do nothing, set breakpoint here
}

int main(void)
{
  Node tree = create_tree("Root");
  for (int i = 0; i < 5; ++i) {
    Node child = tree_create_child(tree, "Child");
    for (int j = 0; j < 7; ++j) {
      tree_create_child(child, "Grandchild");
    }
  }
  break_here(tree);
  tree_free(tree);
  return 0;
}
