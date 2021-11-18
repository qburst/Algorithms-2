class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        """Add value at the end of the list
        :param value: float
        :return: None
        """
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            cursor = self.head
            while cursor.val:
                if cursor.next is None:
                    cursor.next = node
                    cursor = cursor.next
                    return
                else:
                    cursor = cursor.next

    def exist(self, value: float) -> bool:
        """Find whether the value in the linked list
        :param value: float
        :return: bool
        """
        cursor = self.head
        while cursor:
            if cursor.val == value:
                return True
            cursor = cursor.next
        return False

    def remove(self, value: float) -> None:
        """Remove element from the linked list
        :param value: float
        :return: None
        """
        current = self.head
        prev = None
        while current:
            if current.val == value:
                prev.next = current.next
                current.next = None
            prev = current
            current = current.next

    def index(self, value: float) -> int:
        """Find value index position in linked list
        :param value: float
        :return: index position
        """
        cursor = self.head
        index = 0
        while cursor:
            if cursor.val == value:
                return index
            cursor = cursor.next
            index += 1
        return -1

    def insert(self, value: float, pos: int) -> None:
        """Insert value into the specified index position
        :param value: float
        :param pos: int
        :return: LinkedList
        """
        node = Node(value)
        current = self.head
        prev = None
        index = 0
        while current:
            if index == pos:
                node.next = current
                prev.next = node
                return
            prev = current
            current = current.next
            index += 1

    def print_list(self) -> None:
        """Print a linked list
        :return: None
        """
        output = ""
        format = "[val = {}] -> "
        cursor = self.head
        while cursor:
            output += format.format(cursor.val)
            cursor = cursor.next
        print(output + "None")


linked = LinkedList()
linked.add(1)  # 0
linked.add(2)  # 1
linked.add(3)  # 2
linked.add(4)  # 4
print(linked.exist(4))
print(linked.exist(3))
print(linked.exist(0))
print(linked.index(4))
print(linked.index(3))
print(linked.index(0))
print(linked.insert(10, 2))
linked.print_list()
print(linked.remove(2))
linked.print_list()
