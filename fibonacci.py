#!/usr/bin/env python3

print("Fibonacci! scuzi, babbada boopi? babbada boopi? bibadda boopada babada babada!")

n = 0

def user_input():
  while True:
    try:
      n = int(input("Enter how many numbers in the Fibonacci sequence you want: "))
      if n <= 0:
        print("Error: Enter a valid positive integer.")
      else:
        break
    except ValueError:
      print("Error: Please enter a valid integer.")
  return n



def fibonacci_sequence(n):
  a, b = 0, 1
  print("Fibonacci sequence: ")

  for i in range(n):
    print(a, end= " ")
    a, b = b, a + b

n = user_input()
fibonacci_sequence(n)



# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
