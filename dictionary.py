def dictionary_operations():
    # Creating a dictionary
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    # Get the value of a key
    value = my_dict.get('a')

    # Add a key-value pair
    my_dict['d'] = 4

    # Update a value
    my_dict.update({'a': 10})

    # Remove a key-value pair
    del my_dict['a']

    # Get all keys
    keys = my_dict.keys()

    # Get all values
    values = my_dict.values()

    # Get all key-value pairs
    items = my_dict.items()

    # Check if a key exists
    exists = 'a' in my_dict

    # Clear the dictionary
    my_dict.clear()

    print(my_dict)

dictionary_operations()
