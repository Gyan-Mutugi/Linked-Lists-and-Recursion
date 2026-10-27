
class Node:
    """
    Stores data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that uses recursion.
    """

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        """Insert a new node at the beginning in O(1) time."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def recursive_sum(self):
        """Return the sum of all nodes using recursion."""

        def calculate(node):
            if node is None:
                return 0

            return node.data + calculate(node.next)

        return calculate(self.head)

    def recursive_reverse(self):
        """Reverse the list in-place using recursion."""

        def reverse_nodes(previous, current):
            if current is None:
                return previous

            next_node = current.next
            current.next = previous

            return reverse_nodes(current, next_node)

        self.head = reverse_nodes(None, self.head)

    def recursive_search(self, target):
        """Return True if target exists, otherwise False."""

        def search(node):
            if node is None:
                return False

            if node.data == target:
                return True

            return search(node.next)

        return search(self.head)

    def display(self):
        """Print the list in a readable format."""
        values = []
        current = self.head

        while current is not None:
            values.append(str(current.data))
            current = current.next

        values.append("None")
        print(" -> ".join(values))
