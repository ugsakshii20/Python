def set_operations():
    # Creating a set
    my_set = {1, 2, 3, 4, 5}

    # Add an element
    my_set.add(6)

    # Remove an element
    my_set.remove(1)

    # Check if an element exists
    exists = 1 in my_set

    # Get the number of elements
    count = len(my_set)

    # Clear the set
    my_set.clear()

    # Union of two sets
    union = my_set.union({6, 7, 8})

    # Intersection of two sets
    intersection = my_set.intersection({2, 3, 4})

    # Difference of two sets
    difference = my_set.difference({2, 3, 4})

    # Symmetric difference of two sets
    sym_difference = my_set.symmetric_difference({2, 3, 4})

    print(my_set)

set_operations()
