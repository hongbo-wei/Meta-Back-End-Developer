'''
FOR numer in 1 to 40
    if multiple of 3 and 5
        print FizzBuzz
    else if multiple of 3
        print Fizz
    else if multiple of 5
        print Buzz
    else
        print number
'''

for number in range(1, 41):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)