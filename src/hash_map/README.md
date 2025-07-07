Design a hash map or hash set

Key point is to avoid collision and don't use built-in dict


### using array for chaining
- hash slot + hash function (simple module operation)
- PUT(key) o(n//capacity)
- GET(key)
- REMOVE(key)

### using linked list for chaining
-> collision -> chaining: linked list or array
linked list -> BST -> build a BST and add / delete / search a node in BST





How to implement an ordered hash table?
- hash table for fast lookup
- doubly linked list  -> LRU cache

