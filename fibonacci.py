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
  sequence = []
  a, b = 0, 1
  
  for i in range(n):
    sequence.append(a)
    a, b = b, a + b
  return sequence

def print_sequence(sequence):
  print("Fibonacci Sequence:")
  print(" ".join(map(str, sequence)))
  

n = user_input()
sequence = fibonacci_sequence(n)
print_sequence(sequence)



# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
