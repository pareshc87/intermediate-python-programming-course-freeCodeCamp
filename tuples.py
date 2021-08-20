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
