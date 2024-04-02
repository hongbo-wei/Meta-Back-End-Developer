# sock solution
# each number represents a sock with a color
socks = [1, 2, 2, 1, 1, 3, 5, 1, 4, 4]
print(socks)

sock_dict = {}

for sock in socks:
    if sock in sock_dict:
        sock_dict[sock] += 1
    else:
        sock_dict[sock] = 1

for key, value in sock_dict.items():
    if value % 2 != 0:
        print(key, value)