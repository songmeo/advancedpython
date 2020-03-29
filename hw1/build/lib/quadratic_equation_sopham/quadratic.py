#!/usr/bin/python3
import cmath, math

def quadratic():
  while True:
    try:
      a, b, c = map(int, input("Please type a, b, c: ").split())
      if a == 0:
        raise Exception("a could not be 0. Please try again.")
      break
    except ValueError:
      print("Illegal input.")
    except Exception:
      print("a could not be zero.")
  d = b**2 - 4*a*c
  if d >= 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
  else:
    x1 = (-b + cmath.sqrt(d)) / (2*a)
    x2 = (-b - cmath.sqrt(d)) / (2*a)
  print('x1 = {} x2 = {}'.format(x1, x2))
