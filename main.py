l = ["moye", "skibidi", "fanum", "tax"]

l.clear()  # Removes all elements from the list
print(l)

l_copy = l.copy()  # Returns a shallow copy of the list
print(l_copy)

l.append("carol fernandes")  # Adds an element to the end of the list
print(l)

print(l.count("a"))  # Counts occurrences of "a" in the list

l.extend(["new", "elements"])  # Extends the list with multiple elements
print(l)

print(l.index("new"))  # Returns the index of "new"

l.insert(1, "inserted")  # Inserts an element at index 1
print(l)

print(l.pop())  # Removes and returns the last element

l.remove("inserted")  # Removes the first occurrence of "inserted"
print(l)

l.reverse()  # Reverses the order of elements
print(l)

l.sort()  # Sorts the list in ascending order
print(l)

print(sorted(l)) # sorted() is same as sort() function for lists