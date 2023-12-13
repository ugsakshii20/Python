def print_duplicates(s):
    duplicates = [char for char in s if s.count(char) > 1]
    return list(set(duplicates))

s=input("Enter the string:")
print("Duplicate charaters are:",print_duplicates(s))
