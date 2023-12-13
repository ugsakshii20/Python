# Create empty sets
engineers = set()
managers = set()

# Add elements to sets using input
print("Enter names of engineers (separated by space): ")
names = input().split()
engineers.update(names)

print("Enter names of managers (separated by space): ")
names = input().split()
managers.update(names)

# Display engineers
print("\nEngineers:")
for engineer in engineers:
    print(f"Name of Engineer is: {engineer}")

# Copy managers as a tuple and list
myManagers = tuple(managers)
myEngineers = list(engineers)

# Add new manager
managers.add('Jenifer')

# Merge sets
engineer_manager = engineers | managers

# Display engineers not managers
print("\nEngineers not managers:")
for engineer in engineers:
    if engineer not in managers:
        print(engineer)

# Display engineers also managers
print("\nEngineers who are also managers:")
for engineer in engineers:
    if engineer in managers:
        print(engineer)

# Display person who is either engineer or manager but not both
both_roles = engineers & managers
only_engineers = engineers - both_roles
only_managers = managers - both_roles

print("\nPerson who is either engineer or manager but not both:")
if only_engineers:
    print("Only engineers:", only_engineers.pop())
elif only_managers:
    print("Only manager:", only_managers.pop())
else:
    print("No one fits this criteria.")
