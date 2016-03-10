import math
from ..util import egcd, gcd, modinv, is_prime
from ..abstract.Field import Field, FieldElement
from Zmod import Zmod, ZmodElement

class FiniteField(Zmod):
  def __init__(s, p):
    Zmod.__init__(s, p)
    if s.element_class != FiniteFieldElement:
      raise ArithmeticError("Invalid Prime : %d" % p)
    s.p = p

  def __str__(s):
    return Zmod.__str__(s, "p")

class FiniteFieldElement(ZmodElement):
  def __init__(s, field, x):
    ZmodElement.__init__(s, field, x)