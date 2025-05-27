example_set = {1, 2, 3, 4, 5}

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

union = set_a.union(set_b)
print(f"Union of set_a and set_b: {union}")
# Will return a new set with all unique elements from both sets.

intersection = set_a.intersection(set_b)
print(f"Intersection of set_a and set_b: {intersection}")
# Will return a new set with elements that are common to both sets.

difference = set_a.difference(set_b)
print(f"Difference of set_a and set_b: {difference}")
# Will return a new set with elements that are in set_a but not in set_b.
print(f"Difference of set_b and set_a: {set_b.difference(set_a)}")


example_set.add(6)
print(f"Set after adding 6: {example_set}")
example_set.remove(2)
print(f"Set after removing 2: {example_set}")

# Practical Application: Removing duplicates from collection, membership testing, performing mathematical set operations, etc.

# Update an existing set
example_set.update({7, 8})
print(f"Set after updating with {7, 8}: {example_set}")


