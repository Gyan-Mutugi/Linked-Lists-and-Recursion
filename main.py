
from linked_list import LinkedList

# Create an empty linked list
employees = LinkedList()

# Insert employee IDs
employees.insert_at_front(30)
employees.insert_at_front(20)
employees.insert_at_front(10)

print("Original linked list:")
employees.display()

# Test recursive sum
print("Sum of IDs:", employees.recursive_sum())

# Test recursive search
print("Search for ID 20:", employees.recursive_search(20))
print("Search for ID 99:", employees.recursive_search(99))

# Test recursive reverse
employees.recursive_reverse()

print("Reversed linked list:")
employees.display()

# Test sum after reversing
print("Sum after reversing:", employees.recursive_sum())
