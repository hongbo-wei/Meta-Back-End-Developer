# Reverse by slicing
s = 'Hello'
s = s[::-1]

print(s)

# Reverse by recursion
def reverse_str(str):
    if len(str) == 0:
        return str
    else:
        return reverse_str(str[1:]) + str[0]
    
s = 'Hello'
s = reverse_str(s)
print(s)
