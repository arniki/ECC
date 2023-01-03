import math

"""
Constructor for EllipticCurvePoint class.

Parameters:
x (int): The x coordinate of the point.
y (int): The y coordinate of the point.
a (int): The a parameter of the curve.
b (int): The b parameter of the curve.
p (int): The prime modulus of the curve.
"""

class EllipticCurvePoint:
  def __init__(self, x, y, a, b, p):
    self.x = x
    self.y = y
    self.a = a
    self.b = b
    self.p = p

  def __add__(self, other):

"""
Overloads the '+' operator for EllipticCurvePoint objects.
Performs point addition on elliptic curves.

Parameters:
other (EllipticCurvePoint): The point to be added.

Returns:
EllipticCurvePoint: The result of adding the two points.
"""

    if self.x == other.x and self.y == other.y:
      s = (3 * self.x * self.x + self.a) % self.p
      s = (s * (2 * self.y)) % self.p
    else:
      s = (other.y - self.y) % self.p
      s = (s * (other.x - self.x)) % self.p
      s = (s * pow(other.x - self.x, -1, self.p)) % self.p
    x = (s * s - self.x - other.x) % self.p
    y = (s * (self.x - x) - self.y) % self.p
    return EllipticCurvePoint(x, y, self.a, self.b, self.p)

  def __mul__(self, scalar):

"""
Overloads the '*' operator for EllipticCurvePoint objects.
Performs point multiplication.


Parameters:
scalar (int): The scalar to multiply the point by.

Returns:
EllipticCurvePoint: The result of multiplying the point by the scalar.
"""

    result = self
    for i in range(scalar - 1):
      result = result + self
    return result

  def order(self):

"""
Returns the order of the point.
Returns:
int: The order of the point, or None if the point is not of finite order.
"""

    i = 1
    result = self
    while result.x != None and result.y != None:
      result = result + self
      i += 1
    return i
