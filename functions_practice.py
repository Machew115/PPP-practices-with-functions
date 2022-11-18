#Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    list = [a, b, c]
    return max(list)

print(max_num(1, 5, 10))
#Write a Python function called mult_list() to multiply all the numbers in a list.
def multiply(*num):
    total = 1
    for x in num:
        total *= x
    return total
print(multiply(1, 3, 9, 12))
#Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    text = string[::-1]
    print(text)

rev_string("hello")
#Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(num):
    if num > 10 and num <20:
        print(num)
    else:
        print("say what?")

num_within(12)
#The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
def num_within(x,a,b):
  return x in range(a,b+1)

#Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

#The function accepts the number n, the number of rows to print
triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1
    for row in triangle:
      print(row)
#Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
