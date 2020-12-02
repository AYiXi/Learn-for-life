from typing import Any, Sized


class Node:
    def __init__(self, item: Any, _next: Any) -> None:
        self.item = item
        self.next = _next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def add(self, item: Any):
        self.head = Node(item, self.head)
        self.size += 1
    
    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            self.size -= 1
            return item
    
    def is_empty(self) -> bool:
        return self.head is None

    def __str__(self) -> str:
        iterate = self.head
        item_str = ''
        item_list = []
        while iterate:
            item_list.append(str(iterate.item))
            iterate = iterate.next
        
        item_str = ' --> '.join(item_list)
        return item_str
        
    def __len__(self) -> int:
        return self.size

if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.add(1)
    linkedlist.add(1)
    linkedlist.add(1)
    print(linkedlist)