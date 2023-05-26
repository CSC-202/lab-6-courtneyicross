class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class List:
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


def initialize() -> List:
    return List()


def isEmpty(data: List) -> bool:
    if data is None:
        return True
    else:
        return False


def addAtIndex(data: List, index: int, value: int) -> List:
    if data is None and index == 0:
        return Node(value, None)
    elif index == 0:
        return Node(value, data)
    else:
        return Node(data.value, addAtIndex(data.next, index - 1, value))


def removeAtIndex(data: List, index: int) -> tuple[Node, List]:
    if index == 0:
        return data.value, data.next
    else:
        deleted = removeAtIndex(data.next, index - 1)
        return deleted[0], Node(data.value, deleted[1])


def addToFront(data: List, value: int) -> List:
    return Node(value, data)


def addToBack(data: List, value: int) -> List:
    return Node(data.value, value)


def getElementAtIndex(data: List, index: int) -> Node:
    if data is None:
        raise IndexError
    if index > len(data) - 1:
        raise IndexError
    else:
        if index == 0:
            return data.value
        else:
            return getElementAtIndex(data.next, index - 1)


def clear(data: List) -> List:
    if data is not None:
        return clear(data.next)
    else:
        return data
    
