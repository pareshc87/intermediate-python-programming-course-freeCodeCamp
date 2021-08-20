# Tuples - ordered, immutable, allows duplicate elements
tuple1 = ('Max', 28, 'Boston')
print("tuple1 =", tuple1)

# To have only 1 item in a tuple use following syntax
tuple2 = ('Max',)
print(type(tuple2))

# Indexing items
item1 = tuple1[0]
print("Item at index=0 is", item1)

# Tuple is IMMUTABLE
# tuple1[0] = 'Maximus'

# Iterate over tuple
for i in tuple1:
    print(i)

# Check if item exists in a tuple
if 'Tim' in tuple1:
    print("Item 'Tim' exists in tuple1")
else:
    print("Item does not exists.")

# Create tuple2
tuple2 = tuple(list('apple'))
print('tuple2 =', tuple2)
print("Item count in tuple2 =", len(tuple2))

# tuple3
tuple3 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
slice1 = tuple3[:5:2]
print("tuple3 =", tuple3)
print("slice1 =", slice1)

# Tuple unpacking
i1, i2, *i3, i4 = tuple3
print("i1 =", i1)
print("i2 =", i2)
print("i3 =", i3)
print("i4 =", i4)

# Tuple vs Lists - Tuple is a efficient data structure that list in python.
# Efficiency in size
import sys

list1 = [0, 1, 2, 'Hello', True]
tuple4 = (0, 1, 2, 'Hello', True)
print("Size of list =", sys.getsizeof(list), "bytes")  # Size of list = 408 bytes
print("Size of tuples =", sys.getsizeof(tuple4), "bytes")  # Size of tuples = 80 bytes

# Efficiency in execution speed
import timeit

print("Exec. time =", timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))  # Exec. time = 0.056340389000979485
print("Exec. time =", timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))  # Exec. time = 0.008076303998677758
