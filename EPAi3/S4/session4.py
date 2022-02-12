import numbers
import random
from decimal import *

getcontext().rounding = ROUND_HALF_EVEN
TEN_PLACES = Decimal(10) ** -10

class Qualean:
    """
    Quantum boolean numbers
    """
    def __init__(self, real: int = 1):
        if real not in [1, 0, -1]:
            raise ValueError("Invalid state: state should be one of [1, 0, -1]")
        self.real = real
        self.imaginary = random.uniform(-1, 1)
        if real:
            self.number = (Decimal(self.real) * Decimal(self.imaginary)).quantize(TEN_PLACES)
        else:
            self.number = Decimal((0, (0, 0), -1)) # 0.0

    # object representation
    def __repr__(self):
        return "Qualean Class Instance"

    # text for print
    def __str__(self):
        return "Qualean String for number: " + str(self.number)

    # interface with outside
    def return_qualean(self):
        if self.number:
            return round(float(self.number), 10)
        else:
            return float(self.number)

    # arithmetic operations
    def __add__(self, other):
        if not isinstance(other, (numbers.Number, Qualean)):
            raise TypeError("Invalid operand: operand should be a number")
        if isinstance(other, Qualean):
            operand = other.return_qualean()
        else:
            operand = other
        return self.return_qualean() + operand

    def __mul__(self, other):
        if not isinstance(other, (numbers.Number, Qualean)):
            raise TypeError("Invalid operand: operand should be a number")
        if isinstance(other, Qualean):
            operand = other.return_qualean()
        else:
            operand = other
        return self.return_qualean() * operand

    def __sqrt__(self):
        if self.number >= 0:
            return self.number.sqrt()
        else:
            return str(round((-self.number).sqrt(), 10)) + 'i'

    def __invertsign__(self):
        if self.number:
            return round(float(-self.number), 10)
        else:
            return float(self.number)

    # logical operations
    def __and__(self, other):
        if self.number:
            return bool(other)
        else:
            return False

    def __or__(self, other):
        if self.number:
            return True
        else:
            return bool(other)

    # relational operations
    def __eq__(self, other):
        if not isinstance(other, (numbers.Number, Qualean)):
            raise TypeError("Invalid operand: operand should be a number")
        return self.return_qualean() == other.return_qualean()

    def __ge__(self, other):
        if not isinstance(other, (numbers.Number, Qualean)):
            raise TypeError("Invalid operand: operand should be a number")
        if isinstance(other, Qualean):
            operand = other.return_qualean()
        else:
            operand = other
        return self.return_qualean() >= operand

    def __gt__(self, other):
        if not isinstance(other, (numbers.Number, Qualean)):
            raise TypeError("Invalid operand: operand should be a number")
        if isinstance(other, Qualean):
            operand = other.return_qualean()
        else:
            operand = other
        return self.return_qualean() > operand

    def __le__(self, other):
        if not isinstance(other, (numbers.Number, Qualean)):
            raise TypeError("Invalid operand: operand should be a number")
        if isinstance(other, Qualean):
            operand = other.return_qualean()
        else:
            operand = other
        return self.return_qualean() <= operand

    def __lt__(self, other):
        if not isinstance(other, (numbers.Number, Qualean)):
            raise TypeError("Invalid operand: operand should be a number")
        if isinstance(other, Qualean):
            operand = other.return_qualean()
        else:
            operand = other
        return self.return_qualean() < operand

    # type conversions
    def __float__(self):
        return float(self.number)

    def __bool__(self):
        return self.number != 0
