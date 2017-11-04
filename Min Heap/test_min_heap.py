from MinHeap import *

# Test Case 1
heap1 = MinHeap()
assert len(heap1) == 0
assert heap1.is_empty() == True
IN = lambda x : heap1.insert(x)
RM = lambda: heap1.delete()
AST = lambda x, l : len(heap1) == x and str(heap1) == str(l)
IN(4); assert AST(1, [4])
assert heap1.is_empty() == False
IN(7); assert AST(2, [4, 7])
IN(3); assert AST(3, [3, 7, 4])
IN(8); assert AST(4, [3, 7, 4, 8])
assert heap1.peek() == 3
IN(10); assert AST(5, [3, 7, 4, 8, 10])
RM(); assert AST(4, [4, 7, 10, 8])
IN(6); assert AST(5, [4, 6, 10, 8, 7])
RM(); assert AST(4, [6, 7, 10, 8])
assert heap1.peek() == 6
RM(); assert AST(3, [7, 8, 10])
IN(20); assert AST(4, [7, 8, 10, 20])
IN(4); assert AST(5, [4, 7, 10, 20, 8])
IN(7); assert AST(6, [4, 7, 7, 20, 8, 10])
IN(12); assert AST(7, [4, 7, 7, 20, 8, 10, 12])
IN(11); assert AST(8, [4, 7, 7, 11, 8, 10, 12, 20])
assert heap1.peek() == 4
IN(8); assert AST(9, [4, 7, 7, 8, 8, 10, 12, 20, 11])
IN(11); assert AST(10, [4, 7, 7, 8, 8, 10, 12, 20, 11, 11])
IN(5); assert AST(11, [4, 5, 7, 8, 7, 10, 12, 20, 11, 11, 8])
RM(); assert AST(10, [5, 7, 7, 8, 8, 10, 12, 20, 11, 11])
RM(); assert AST(9, [7, 8, 7, 11, 8, 10, 12, 20, 11])
RM(); assert AST(8, [7, 8, 10, 11, 8, 11, 12, 20])
assert heap1.peek() == 7
RM(); assert AST(7, [8, 8, 10, 11, 20, 11, 12])
IN(11); assert AST(8, [8, 8, 10, 11, 20, 11, 12, 11])
IN(7); assert AST(9, [7, 8, 10, 8, 20, 11, 12, 11, 11])
RM(); assert AST(8, [8, 8, 10, 11, 20, 11, 12, 11])
RM(); assert AST(7, [8, 11, 10, 11, 20, 11, 12])
RM(); assert AST(6, [10, 11, 11, 11, 20, 12])
RM(); assert AST(5, [11, 11, 11, 12, 20])
assert heap1.peek() == 11
RM(); assert AST(4, [11, 12, 11, 20])
RM(); assert AST(3, [11, 12, 20])
assert heap1.is_empty() == False
[RM() for _ in range(3)]
assert heap1.is_empty() == True
CAT = False
try:
    RM()
except ValueError:
    CAT = True
finally:
    pass
if not CAT:
    raise ValueError("expect an exception - heap.delete should fail when heap is empty")

# All Test Cases Passed
print("All tests passed!")

