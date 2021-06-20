def __GCF(p,q):
      if p == q:
        return p
      elif p > q:
        m = q
        n = p
      elif p < q:
        m = p
        n = q
      while n % m > 0:
        n2 = m
        m = n % m
        n = n2
      return m

def __LCM(p,q):
  m = p
  n = q
  while m != n:
    if m < n:
       m = m + p
    elif n < m:
      n = n + q
  return m





class frac():

  def __init__(self,n, d=1):

    if not isinstance(n*d, int):
      raise TypeError

    if n * d < 0:  
      n, d = -1 * abs(n), abs(d)
    else:
      n, d = abs(n), abs(d)

    if n != 0:
      toDiv = __GCF(abs(n),abs(d))
      n,d = n // toDiv, d // toDiv

    self.n = n
    self.d = d

  def __repr__(self):
    return str(self.n) +'/'+ str(self.d)

  def __neg__(self):
    return frac(-1 * self.n,self.d)

  def __add__(self,other):
    # __add__ needs to take care of cases where other is not a frac
    # if other is an int, make it a frac
    if isinstance(other, int):
      other = frac(other)
    # if other is a float, convert self to float and return a float
    if isinstance(other, float):
      return self.n/self.d + other

    if self.d != other.d:
      toMult = __LCM(self.d,other.d)
      xy = toMult // self.d
      n1 = self.n * xy

      d1 = toMult
      
      xy = toMult // other.d
      n2 = other.n * xy

    else:
      n1 = self.n
      n2 = other.n

      d1 = self.d

    n3 = n1 + n2

    if n3 != 0:
      xy = __GCF(abs(n3),abs(d1))      
      n3 /= xy
      d1 /= xy

    n = int(n3)
    d = int(d1)

    return frac(n,d)

  def __sub__(self,other):

    return self  + (-other)

  def __mul__(self, other):
    if isinstance(other, float):
      return other * float(self)

    if isinstance(other, int):
      other = frac(other)

    d = self.d * other.d
    n = self.n * other.n
    if n != 0:
      toDiv = __GCF(abs(n),abs(d))
      n,d = n // toDiv, d // toDiv

    return frac(n,d)

  def __truediv__(self,other):
    if isinstance(other, int):
      other = frac(other)

    if isinstance(other, float):
      return float(self) / other

    n = self.n * other.d
    d = self.d * other.n
    if n != 0:
      toDiv = __GCF(abs(n),abs(d))
      n,d = n // toDiv, d // toDiv

    return frac(n,d) 

  def __pow__(self, expo):
    if expo != abs(expo):
      return frac(self.d,self.n) ** abs(expo)

    if isinstance(expo, float):
      raise TypeError
    return frac(self.n ** expo, self.d ** expo)

  def __eq__(self, other):

    if isinstance(other, int):
      other = frac(other)

    if isinstance(other,float):
      return float(self) == other

    if self.n * other.d == self.d * other.n:
      return True
    return False

  def __ne__(self, other):
    return not self == other

  def __gt__(self,other):
    if other == self:
      return False

    if isinstance(other, int):
      other = frac(other)

    if isinstance(other, float):
      return float(self) > other

    if self.n/self.d > other.n/other.d:
      return True
    return False

  def __lt__(self,other):
    if other == self:
      return False

    return not self > other

  def __ge__(self,other):
    if self > other or self == other:
      return True
    return False

  def __le__(self,other):
    if self < other or self == other:
      return True
    return False
      
  def __float__(self):
    return self.n/self.d

  def __int__(self):
    return int(float(self))

  def __abs__(self):
    return frac(abs(self.n),abs(self.d))

  def __radd__(second, first):
    # __radd__ gets called only if the first operand
    # isn't a frac. Like for instance 1 + 1/2.
    # Moreover, "second" (which is the first parameter)
    # binds to the frac that comes second
    # and "first" (which is the second parameter) binds to the
    # first parameter. So for 1 + 1/2, first will be 1 and
    # second will be 1/2.
    # (Why? That's just how __radd__ is built to work.)
    # So all we need to do is this:
    return second + first
    # This calls the __add__ method, since second is a frac.

  def __rsub__(second, first):
    return (-second) + first

  def __rmul__(second, first):
    return second * first

  def __rtruediv__(second, first):

    if isinstance(first, float):
      return first / float(second)

    if isinstance(first, int):
      return frac(first) / second

  def __rpow__(second,first):
    return first ** float(second)