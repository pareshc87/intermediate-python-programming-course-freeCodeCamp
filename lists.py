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

# Using arithmetic operators on lists
# New list
my_list2 = [4, 3, 1, -1, -5, 10]
print("my_list2 =", my_list2)

# Multiply list with a scalar
my_list2 = [0] * 5
print("my_list2 =", my_list2)

# Add two lists
my_list2 = [1, 2, 3, 4, 5]
list3 = my_list1 + my_list2
print("list3 =", my_list2)

# Slicing lists - list[start:stop:step]
my_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
slice1 = my_list3[1:4]
print("slice1 = ", slice1)

slice2 = my_list3[2:9:2]
print("slice2 =", slice2)

slice3 = my_list3[::-1]
print('slice3 =', slice3)

# New list
my_list4 = ['banana', 'cherry', 'apple']
list_cpy = my_list4
list_cpy.append('lemon')

print('my_list4 =', my_list4)
print('list_cpy =', list_cpy)

# Copying list
my_list4 = ['banana', 'cherry', 'apple']
list_cpy = my_list4.copy()
list_cpy.append('lemon')

print('my_list4 =', my_list4)
print('list_cpy =', list_cpy)

# List comprehension
my_list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list5_squared = [num * num for num in my_list5]
print('my_list5 =', my_list5)
print('my_list5_squared =', my_list5_squared)
