# Session 4 - Numeric Types II & Functional Arguments

Table of Contents:  
- [Assignment Instruction](#inst)  
- [Function Implementation](#impl)    
    - [Initialization](#init)  
    - [Get Interface](#get)  
    - [Output Text](#text)  
    - [Type Conversion](#type)  
    - [Arithmetic Operation](#arithmetic)  
    - [Logical Operation](#logical)  
    - [Relational (comparison) Operation](#relational)  

<a name="inst"/>

## 1. Assignment Instruction

1. If you have not updated your GitHub username [on this sheet](https://docs.google.com/spreadsheets/d/1JDzWk_u-5A8zLx2fJdcWn22JYO1-l2k2NrqfDjCnu7k/edit?usp=sharing), your assignment will not be evaluated. 
    - From this assignment onwards, you cannot submit from any other github account, and you might directly receive the assignment to your GitHub account. 

2. Write a **Qualean** class that is inspired by Boolean+Quantum concepts. 
    - We can assign it only 3 possible **real** states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. 
    - The moment you assign it a real number, it immediately finds an imaginary number **`random.uniform(-1, 1)`** and multiplies with it and stores that number internally after using **Bankers rounding to 10th decimal place**. 
    - *To understand this further.. imagine picking 100 times any number from 1 or 0 or -1.* 
    - *You want to store this list.*
    - *But before you can store it, the quantum nature of this class is going to pick another number (`random.uniform(-1, 1)`) and multiply with the number you want to store.*
    - *So if I wanted to store 1, 0, 1, -1, -1.. it might get stored as 0.00123123, 0, -0.123123, 0.63463, -0.36343.*
    - It implements these functions (with exactly the same names):
      - `__and__`
      - `__or__` 
      - `__repr__`
      - `__str__`
      - `__add__`
      - `__eq__`
      - `__float__`
      - `__ge__`
      - `__gt__`
      - `__invertsign__`
      - `__le__`
      - `__lt__`
      - `__mul__`
      - `__sqrt__`
      - `__bool__`

3. Your task is to write the above class, and then write all the functions. 

4. Some of the tests in the test file will check for:
    - q + q + q ... 100 times = 100 * q
    - q.__sqrt__() = Decimal(q).sqrt
    - sum of 1 million different qs is very close to zero (use isclose)
    - q1 and q2 returns False when q2 is not defined as well and q1 is False
    - q1 or q2 returns True when q2 is not defined as well and q1 is not false

5. Upload your code and make use of GitHub Actions and submit the GitHub link. 

6. No README, no evaluation. README must explain each function and each test case. 
    - 420 points for clearing 42 test cases × quality of your code comments and README file.

<a name="impl"/>

## 2. Function Implementation

- We will rely on the `Decimal` class for internal representation of our qualean number.
- Before we define our `Qualean` class, we ensure Bankers rounding to 10th decimal place through the following:

    ``` python
    getcontext().rounding = ROUND_HALF_EVEN
    TEN_PLACES = Decimal(10) ** -10
    ```

<a name="init"/>

### Initialization

- `__init__`

    - Part 1: Function signiture & error handling 
        1. Receive one integer from the set {1, 0, -1} as arguement 
        2. Raise a `ValueError` if argument is not a member of the set {1, 0, -1}  
   
    ```python
    def __init__(self, real: int = 1):
        if real not in [1, 0, -1]:
            raise ValueError("Invalid state: state should be one of [1, 0, -1]")
    ```

    - Part 2: Prepare real and imaginary states
    
    ```python
        self.real = real
        self.imaginary = random.uniform(-1, 1)
    ```
    
    - Part 3: Initialize qualean state
    
    ```python
        if real:
            self.number = (Decimal(self.real) * Decimal(self.imaginary)).quantize(TEN_PLACES)
        else:
            self.number = Decimal((0, (0, 0), -1)) # 0.0
    ``` 

<a name="get"/>

### Get Interface

- `return_qualean`

    - This is our `get` interface with users in the outside world.
    - We use `float` for various operations (mathematical and logical) and other interactions.
    
    ```python
    def return_qualean(self):
        if self.number:
            return round(float(self.number), 10)
        else:
            return float(self.number)
    ```

<a name="text"/>

### Output Text
- `__repr__`
    
    - Simple text for object representation
     
    ```python
    def __repr__(self):
        return "Qualean Class Instance"
    ```
    
- `__str__`

    - Simple text to print with the `print` function
    
    ```python
    def __str__(self):
        return "Qualean String for number: " + str(self.number)
    ```

<a name="type"/>

### Type Conversion

These are simple wrappers for the pure Python `float` and `bool` functions.

- `__float__`
- `__bool__`

<a name="arithmetic"/>

### Arithmetic Operation
- `__add__`
    
    - Part 1: Function signiture & error handling
        1. We accept an argument `other`
        2. And check whether it's a number
        
    ```python
    def __add__(self, other):
        if not isinstance(other, (numbers.Number, Qualean)):
            raise TypeError("Invalid operand: operand should be a number")
    ```
    
    - Part 2: Initialize `operand`
    ```python
        if isinstance(other, Qualean):
            operand = other.return_qualean()
        else:
            operand = other
    ```
    
    - Part 3: Perform mathematical operation and return
    ```python
        return self.return_qualean() + operand
    ```
   
- `__mul__`: identical to `__add__` except it multiplies (`*`)

- `__sqrt__`

    - Simple squaring function, but returns a string appended with an 'i' for negative numbers
    
    ```python
    def __sqrt__(self):
        if self.number >= 0:
            return self.number.sqrt()
        else:
            return str(round((-self.number).sqrt(), 10)) + 'i'
    ```

- `__invertsign__`
    
    - Simple function that inverts the sign of a qualean number
    
    ```python
    def __invertsign__(self):
        if self.number:
            return round(float(-self.number), 10)
        else:
            return float(self.number)
    ```

<a name="logical"/>

### Logical Operation

These are simple wrappers for pure Python `and` and `or` functions with short-circuiting

- `__and__`
- `__or__` 

<a name="relational"/>

### Relational (comparison) Operation

These functions have exactly the same overall structure and implementation as the arithmetic operators, obviously except for the last part (Part 3) where actual operations are performed.

- `__ge__`
- `__gt__`
- `__le__`
- `__lt__`
- `__eq__`
