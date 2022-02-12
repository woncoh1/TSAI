# Session 3 assignment of EPAi3.0
Numeric Types - I

##########

    'int',
    'encoded_from_base10',
    'digit_map',
    'ValueError',
    'math',
    'isclose',
    'absolute',
    'relative',
    'tolerance',
    'bin(',
    'hex(',
    'round',
    'truncation',
    'error',
    'equality',
    'zero',
    'away'

## 0. Assignment Instructions

1. Garbage collection of cyclical reference
    - Here in this code we will be leaking memory because we are creating cyclic reference. 
    - Find that we are indeed making cyclic references. 
    - Eventually memory will be released, but that is currently not happening immediately. 
    - We have added a function called "clear_memory" but it is not able to do it's job. Fix it. 
    - Refer to test_clear_memory Test in test_session2.py to see how we're crudely finding that this code is sub-optimal.

2. Efficient equality and membership testing of strings
    - Here we are suboptimally testing whether two strings are exactly same or not. 
    - After that we are trying to see if we have a particular character in that string or not. 
    - Currently the code is suboptimal. 
    - Write it in such a way that it takes 1/10 the current time.

<a name="cyclical"/>

## 1. Garbage Collection of Cyclical Reference

### 1-1 Parts List

#### Classes

1. `Something`
    - This is a simple class with a constructor that assigns `None` to the sole class variable `something_new`.
    
2. `SomethingNew`
    - Here the `__init__` constructor accepts an argument of type `Something`, whose default is set to `None`.
    - The assignment `self.something = something` forebodes potential cyclical reference. 

#### Functions

1. `add_something`
    - Clear cyclical reference: 
        - `something = Something()`
        - `something.something_new = SomethingNew(i, something)`
    - The resulting `something` gets added to the collection.

2. `clear_memory`
    - This functions is intended to delete all elements from the list and free up memory.
    - But we need to modify the body of this function in order to make it work properly.

3. `critical_function`
    - This is the function at brings together all the ingredients, namely `collection`, `add_something` and `clear_memory`, and put them to heavy work.

### 1-2 Major Steps

1. Locate cyclical reference: `something.something_new = SomethingNew(i, something)`
    1. `add_something(collection, i)` in the body of `critical_function()`
    2. `something = Something()` in the body of `add_something(collection, i)` creates an instance of the class `Something`
    3. `something.something_new = SomethingNew(i, something)` creates a cyclical reference back to the instance `something`, because of `self.something = something` in the constructor of the class `SomethingNew`.

2. Free up memory by explicitly calling the gabage collector: `gc.collect()`
    ```
    def clear_memory(collection: List[Something]):
        # clear all elements in the list
        collection.clear()
        # force garbage collection
        gc.collect()
    ```
    1. `collection.clear()` is equivalent to `del collection[:]`, which frees up all elements (i.e. pointers to cyclical references) of the list `collection`.
        - Note here that reference counts of the cyclically referred objects are not 0
    2. `gc.collect()` forces deallocation of cyclical references right after clearing `collection`.

<a name="testing"/>

## 2. Efficient Equality and Membership Testing

### 2-1 Parts List

1. `compare_strings_old`
    - Part 1: Equality testing
    - Part 2: Membership testing
    - `char_list` should be replaced by something more efficient to iteratively test for membership

2. `compare_strings_new`
    - We need to change this function from sleeping (`time.sleep(6)`) to doing the exact same thing as `compare_strings_old`, but order-of-magnitude more efficiently.

### 2-2 Major Steps

1. Equality testing
    - Forcing interning allows us to use physical identity check (i.e memory address comparison) instead of logical equality check.
    - We thus use `sys.intern` to forcfully intern all variables, and compare the memory location using `is`.

2. Membership testing
    - Sets are preferred over lists and tuples when checking for membership because sets are hashed better than lists and tuples.  
    - Here all we have to do is to change `char_list` to `char_set` by using a set in place of the list.
