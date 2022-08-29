# Write a function called max_num() to find the maximum of three numbers


def max_num(a, b, c):
    list = [a, b, c]
    return max(list)

a = 10
b = 14
c = 12
print(max(a, b, c))

# Write a function called mult_list() to muiltiply all the numbers in a list

def mult_list(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

list1 = [2, 6, 9]
list2 = [3, 2, 5]

print(mult_list(list1))
print(mult_list(list2))

# Write a function called rev_string() to reverse a string

def rev_string(string):
    string = string[::-1]
    return string

s = "Hello from the outside!"

print("The original string is : ", end="")
print(s)

print("The reversed string is : ", end="")
print(rev_string(s))

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(n):
    if n in range (3,9):
        print("true")
    else :
        print("false")

num_within(4) # true
num_within(1) # false

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

def pascal(numRows):
    for n in range(numRows):
        print(' '*(numRows-n), end='')
        print(' '.join(str(11**n)))

pascal(5)