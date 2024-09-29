"""
Design your implementation of the circular double-ended queue (deque).
Implement the MyCircularDeque class:
MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the
operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the
operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if
the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if
the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque
is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is
empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.

Example 1:
Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront",
"getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]
Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4

Constraints:
1 <= k <= 1000
0 <= value <= 1000
At most 2000 calls will be made to insertFront, insertLast, deleteFront,
deleteLast, getFront, getRear, isEmpty, isFull.
"""

from collections import deque
from typing import Callable


class MyCircularDeque:

    def __init__(self, k: int):
        self._k = k
        self._deque = deque()
        self._length = 0

    def _insert(self, function: Callable, value: int) -> bool:
        if self._length < self._k:
            function(value)
            self._length += 1
            return True
        return False

    def _delete(self, function: Callable) -> bool:
        if self._length:
            function()
            self._length -= 1
            return True
        return False

    def _get(self, idx: int) -> int:
        if not self._length:
            return -1
        return self._deque[idx]

    def insertFront(self, value: int) -> bool:
        return self._insert(self._deque.appendleft, value)

    def insertLast(self, value: int) -> bool:
        return self._insert(self._deque.append, value)

    def deleteFront(self) -> bool:
        return self._delete(self._deque.popleft)

    def deleteLast(self) -> bool:
        return self._delete(self._deque.pop)

    def getFront(self) -> int:
        return self._get(0)

    def getRear(self) -> int:
        return self._get(-1)

    def isEmpty(self) -> bool:
        return not self._length

    def isFull(self) -> bool:
        return self._length == self._k


if __name__ == '__main__':
    myCircularDeque = MyCircularDeque(3)
    assert myCircularDeque.insertLast(1) == True
    assert myCircularDeque.insertLast(2) == True
    assert myCircularDeque.insertFront(3) == True
    assert myCircularDeque.insertFront(4) == False
    assert myCircularDeque.getRear() == 2
    assert myCircularDeque.isFull() == True
    assert myCircularDeque.deleteLast() == True
    assert myCircularDeque.insertFront(4) == True
    assert myCircularDeque.getFront() == 4
