# write code to determine if a given number n is even or odd. Think of this as a function that returns 0 if the number is even, and 1 if it is odd.


def checkParity(n):
  result = (n % 2)
  return result
  
print("Odd parity", checkParity(2))
print("Even parity", checkParity(2))