class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
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


def initialize() -> Stack:
    return Stack()


def isEmpty(data: Stack) -> bool:
    if data is None:
        return True
    else:
        return False


def push(data: Stack, value: int) -> Stack:
    if data.first is None:
        return Node(value, None)
    else:
        if data.first is not None:   
    raise NotImplementedError("Stack.push() not defined")


def pop(data: Stack) -> tuple[Node, Stack]:
    return data.first, data.first.next


def peek(data: Stack) -> Node:
    return data.first.value


def clear(data: Stack) -> Stack:
    if data.first is not None:
        clear(data.first.next)
    else:
        return data
    
