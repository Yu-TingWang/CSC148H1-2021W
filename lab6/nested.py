"""Lab 6: Recursion

=== CSC148 Winter 2021 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains a few nested list functions for you to practice recursion.
"""
from typing import Union, List

def greater_than_all(obj: Union[int, List], n: int) -> bool:
    """Return True iff there is no int in <obj> that is larger than or
    equal to <n> (or, equivalently, <n> is greater than all ints in <obj>).
    Return False if there exists at least on int that is larger or equal to <n>
    >>> greater_than_all(10, 3)
    False
    >>> greater_than_all([1, 2, [1, 2], 4], 10)
    True
    >>> greater_than_all([], 0)
    True
    """
    if isinstance(obj, int):
        return obj<n
    else: # then obj is a class of class
        for sublist in obj:
            if not greater_than_all(sublist,n): # found a value that is ≥ n
                return False

        return True



def add_n(obj: Union[int, List], n: int) -> Union[int, List]:
    """Return a new nested list where <n> is added to every item in <obj>.

    >>> add_n(10, 3)
    13
    >>> add_n([1, 2, [1, 2], 4], 10)
    [11, 12, [11, 12], 14]
    """
    if isinstance(obj, int):
        return obj + n
    else:
        ### this will return a new list
        result = []
        for sublist in obj:
            result.append(add_n(sublist,n))
        return result
        # this will modify the original list
        for i in range(len(obj)):
            obj[i] = add_n(obj[i],n)
        return obj
        # this won't work
        for sublist in obj:
            sublist = add_n(obj[i],n)
        return obj
def nested_list_equal(obj1: Union[int, List], obj2: Union[int, List]) -> bool:
    """Return whether two nested lists are equal, i.e., have the same value.

    Note: order matters.
    You should only use == in the base case. Do NOT use it to compare
    otherwise (as that defeats the purpose of this exercise)!

    >>> nested_list_equal(17, [1, 2, 3])
    False
    >>> nested_list_equal([1, 2, [1, 2], 4], [1, 2, [1, 2], 4])
    True
    >>> nested_list_equal([1, 2, [1, 2], 4], [4, 2, [2, 1], 3])
    False
    >>>nested_list_equal(1,2)
    False
    >>>nested_list_equal([1],2)
    False
    """
    # HINT: You'll need to modify the basic pattern to loop over indexes,
    # so that you can iterate through both obj1 and obj2 in parallel.

    if isinstance(obj1, int) and isinstance(obj2, int):
        return obj1==obj2
    elif isinstance(obj1, list) and isinstance(obj2, list):
       if len(obj1)!=len(obj2):
           return False
       for i in range(len(obj1)):
           if not nested_list_equal(obj1[i],obj2[i]):
               return False
        return True
    else:
        return False



def duplicate(obj: Union[int, List]) -> Union[int, List]:
    """Return a new nested list with all numbers in <obj> duplicated.

    Each integer in <obj> should appear twice *consecutively* in the
    output nested list. The nesting structure is the same as the input,
    only with some new numbers added. See doctest examples for details.

    If <obj> is an int, return a list containing two copies of it.

    >>> duplicate(1)
    [1, 1]
    >>> duplicate([])
    []
    >>> duplicate([1, 2])
    [1, 1, 2, 2]
    >>> duplicate([1, [2, 3]])  # NOT [1, 1, [2, 2, 3, 3], [2, 2, 3, 3]]
    [1, 1, [2, 2, 3, 3]]
    """
    # HINT: in the recursive case, you'll need to distinguish between
    # a <sublist> that is an int and a <sublist> that is a list
    # (put an isinstance check inside the loop).

    ######### check the function description extend v.s. append ################

    if isinstance(obj, int):
        return [obj,obj]
    else:
        result = []
        for sub in obj:
            if isinstance(sub,int):
                result.extend(duplicate(sub))
            else:
                result.append(duplicate(sub))
        return result



if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # import python_ta
    # python_ta.check_all()
