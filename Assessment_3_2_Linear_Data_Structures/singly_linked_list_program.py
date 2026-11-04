# Assessment 3.2 - Singly Linked List
# Based on Assessment 3.1: ENONSAON
# Nodes are added at the end and removed from the head.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_first(self):
        if self.head is None:
            return None

        removed_data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return removed_data

    def display(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values


def main():
    letters = "ENONSAON"
    linked_list = SinglyLinkedList()

    print("=== SINGLY LINKED LIST PROGRAM ===")
    print("Adding letters to the linked list:")
    for letter in letters:
        linked_list.append(letter)
        print(f"Added {letter}: {linked_list.display()}")

    print("\nRemoving nodes from the head:")
    while linked_list.head is not None:
        removed = linked_list.remove_first()
        print(f"Removed: {removed} | Remaining: {linked_list.display()}")

    print("\nLinked list is empty.")


if __name__ == "__main__":
    main()
