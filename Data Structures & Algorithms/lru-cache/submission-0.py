class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # Map key to its corresponding node
        
        # Create dummy head and tail nodes.
        # New nodes will be inserted right after head, so head.next is always the MRU.
        # The node right before tail (tail.prev) is always the LRU.
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node) -> None:
        # Remove 'node' from the doubly-linked list.
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node: Node) -> None:
        # Insert 'node' right after head, making it the most recently used.
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        # If key is in cache, move the corresponding node to the MRU position.
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # If key already exists, remove the old node.
        if key in self.cache:
            self.remove(self.cache[key])
        # Create a new node and add it to the cache.
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)
        
        # If the cache exceeds capacity, remove the least recently used node.
        # The LRU node is the one right before tail (tail.prev).
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
