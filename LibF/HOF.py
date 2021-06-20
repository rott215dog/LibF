def product(x,y):
  return x * y

def compose(f, g):
  return lambda x: f(g(x))

square = lambda x: x ** 2

sqrt = lambda x: x ** (1/2)

mod_2 = lambda x: x % 2

harmonic = lambda x: 1 / x

def concat(l1,l2):
  return l1 + l2

def find_big(a,b):
  if a > b:
    return a
  return b

def find_lil(a,b):
  if a < b:
    return a
  return b

import math

def is_prime(n):
  if n < 2:
    return False
  for f in range(2, int(math.sqrt(n)) + 1):
    if n % f == 0:
      return False
  return True

sum_two = lambda x, y: x + y

def longer(s, t):
    # Take two strings
    # Return the longer
    # Return the first if equal in length
    if len(s) >= len(t):
        return s
    else:
        return t

def sum_lst(l):
  return fold(sum_two,l)

def square_lst(l):
  return map(square,l)

#FUNCTION LIST

def map(f,l):
  T = []
  for elem in l:
    T.append(f(elem))
  return T

def filter(f, l):
  T = []
  for elem in l:
    if f(elem) == True:
      T.append(elem)
  return T

def fold(f,l):
  if l == []:
    #print('Error: Empty List')
    return []
  if len(l) == 1:
    return l[0]
  x = f(l[0],l[1])
  for i in range(len(l) - 2):
    x = f(x,l[i + 2])
  return x

def repeat(f, x, y):
  if y == 0:
    return x
  return repeat(f, f(x), y - 1)

def factorial(n):
  return fold(product, range(1, n + 1))

def harmonic_series(n):
  l = []
  for i in range(1, n + 1):
    l.append(i)
    
  return fold(sum_two, map(harmonic, l))

def find_max(l):
  return fold(find_big,l)

def find_min(l):
  return fold(find_lil,l)

def flatten(l):
  return fold(concat,l)

sum_sq = compose(sum_lst,square_lst)

sq_sum = compose(square,sum_lst)

def self_compose(f,n):
  x = f
  for i in range(1, n):
    x = compose(x,f)
  return x

def prime_factorization(n):
  lst = []
  if is_prime(n) == True:
    lst.append(n)
    return lst
  else:
    for i in range(2, n // 2):
      while n % i == 0:
        lst.append(i)
        n //= i
  return lst