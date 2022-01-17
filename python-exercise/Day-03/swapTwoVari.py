a = int(input("Enter your first Number: "))
b = int(input("Enter your second Number: "))

print('A, B', a, b)
# Swap thes two
# temp = a
# a = b
# b = temp

# Shortcut
# a, b = b, a

# Another solution
a = a + b
b = a - b
a = a - b
print('A, B', a, b)