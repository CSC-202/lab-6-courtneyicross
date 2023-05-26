class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:
    first: Node
    last: Node

    def __init__(self):
        self.first = None
        self.last = None

    def __len__(self):
        n: int = 0
        current = self.first
        while current != None:
            n += 1
            current = current.next
        return n

    def toPythonList(self):
        result: list = []
        current = self.first
        while current != None:
            result.append(current.value)
            current = current.next
        return result


def initialize() -> Queue:
    return Queue()
    


def isEmpty(data: Queue) -> bool:
    if data.first is None:
        return True
    else:
        return False


def enqueue(data: Queue, value: int) -> Queue:
    if data.first is None:
        return Node(value, None)
    else:
        pass
    


def dequeue(data: Queue) -> tuple[Node, Queue]:
    return data.first, data.first.next
    


def peek(data: Queue) -> Node:
    return data.first.value


def clear(data: Queue) -> Queue:
    if data is not None:
        clear(data.first.next)
    else:
        return data
