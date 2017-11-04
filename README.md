# Python Storage
*data structures, algorithms*

## Binary Tree (BST)
### BinNode
- init
- str
- bool isLeaf(self)
### BinarySearchTree
- init
- void insert(self, data)
- void preorderPrint(self) -> stdout
- str preorder__str__(self)
- void inorderPrint(self) -> stdout
- str inorder__str__(self)
- void postorderPrint(self) -> stdout
- str postorder__str__(self)
- bool search(self, data)
- BinNode addressOf(self, data)
- data min(self)
- BinNode minAddress(self)
- data max(self)
- int height(self)
- void levelorderPrint(self) -> stdout
- void delete(self, data)
- BinNode successor(self, data)

## Graph (use BinTree)
### Graph
- init
- void addVertex(self, data)
- void addEdge(self, start, end)
- void deleteVertex(self, data)
- void deleteEdge(self, start, end)
- void isAdjacent(self, start, end)
- list neighborsOf(self, start)

## Linked List
see documentation

## Min Heap
### MinHeap
- init
- str
- len
- void clear(self)
- bool is_empty(self)
- data peek(self)
- void insert(self, value)
- void delete(self)
### HeapSort
- list heap_sort(list)

## Trie
### Node
- init
- void addChild(self, data)
### Trie
- init
- void addWord(self, word)
- bool isWord(self, word)
- bool isPrefix(self, word)

