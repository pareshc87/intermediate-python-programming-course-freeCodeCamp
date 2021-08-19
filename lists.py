# Lists are ordered, mutable and allows duplicate elements.
my_list1 = ['apple', 'banana', 'cherry']
print("my_list1 =", my_list1)

# Indexing lists
print("Item at index=2 is", my_list1[2])
print("Item at index=0 is", my_list1[0])

# Negative index
print("Item at index=-1 is", my_list1[-1])

# Iterate over list
print("Items in my_list1:")
for i in my_list1:
    print(i, sep=' ')

# Check if an item is in a list
if 'banana' in my_list1:
    print("Item 'banana' exists in the list.")
else:
    print("Item does not exist.")

# Get item count in list
print("Item count=", len(my_list1))

# Append an item at end of the list
my_list1.append('lemon')
print("Item 'lemon' was appended at the end of the list using list using list.append('<object>') method. my_list1 =",
      my_list1)

# Insert item at specific position
my_list1.insert(2, 'blueberry')
print(my_list1)

# Remove last item from the list
last_item = my_list1.pop()
print("Item", last_item, "was removed from the list using list.pop() method. my_list1 =", my_list1)

# Remove specific item
my_list1.remove('cherry')
print("Item 'cherry' was removed from the list using list.remove('<object>'). my_list1 =", my_list1)

# Clear the list
my_list1.clear()
print("my_list1 is empty.")

# Add list items
my_list1 = ['apple', 'banana', 'blueberry', 'cherry', 'lemon']
print("my_list1 =", my_list1)

# Reverse the list
my_list1.reverse()
print("Reverse item order in the list. my_list1=", my_list1)

# Sort list in place
my_list1.sort()
print("list.sort() =", my_list1)

# Sort list in memory
print("sorted(<list_object>) =", sorted(my_list1))
