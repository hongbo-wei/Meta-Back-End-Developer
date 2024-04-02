'''
Check for hash collisions
'''

arr = [1,45,5,34,23,5,82,12,35,21,8,9]

def hash(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] % 7
    print(arr)

hash(arr)