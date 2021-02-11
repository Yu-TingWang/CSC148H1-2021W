"""CSC148 Lab 5: Linked Lists

=== CSC148 Winter 2021 ===
Department of Computer Science,
University of Toronto

=== Module description ===

This module runs timing experiments to determine how the time taken
to call `len` on a Python list vs. a LinkedList grows as the list size grows.
"""
from timeit import timeit
from lab5.linked_list import LinkedList
from lab5.augment_linked_list import LinkedList as betterList
from typing import List, Callable

SIZES = [1000, 2000, 4000, 8000, 16000]
#SIZES = [1,2,3,4,5]# The list sizes to try.
NUM_TRIALS = 20                        # The number of trials to run.


'''
Task 2: Timing __len__ for linked lists vs. array-based lists
1. Most methods take longer to run on large inputs than on small inputs, although this is not always the case. 
  Look at your code for your linked list method __len__. 
  Do you expect it to take longer to run on a larger linked list than on a smaller one?

2. Pick one the following terms to relate the growth of __len__'s running time vs. input size, and justify.
    # constant, logarithmic, linear, quadratic, exponential
3. Complete the code in time_lists.py to measure how running time for your __len__ method changes 
    as the size of the linked list grows. Is it as you predicted?

4. The if __name__ == '__main__' block runs the experiment on both a LinkedList and a list: 
    What do you notice about the behaviour of calling len on a built-in list?
'''
def _setup_lists(lsize: int, n: int, list_type: Callable) -> List[LinkedList]:
    """Return a list of <n> <list_type> objects, each with <lsize> elements.

    Precondition: list_type is a class (e.g. list or LinkedList)
                  list_type has the __len__ method implemented
                  list_type can be constructed by passing in a list of elements
                  e.g. list([1, 2, 3]) creates a list with items [1, 2, 3]
                       LinkedList([1, 2, 3]) creates a LinkedList with items
                        [1, 2, 3] as well.

    >>> lnks = _setup_lists(1, 2, LinkedList)
    >>> len(lnks)
    2
    >>> len(lnks[0])
    1
    >>> len(lnks[1])
    1
    >>> isinstance(lnks[0], LinkedList)
    True
    >>> lsts = _setup_lists(1, 2, list)
    >>> len(lsts)
    2
    >>> len(lsts[0])
    1
    >>> len(lsts[1])
    1
    >>> isinstance(lsts[0], list)
    True
    """
    # TODO: Implement this helper function.
    lists = []
    for i in range(n):
        lists.append(list_type(range(lsize)))
    return lists

def time_len(list_type: Callable) -> List[float]:
    """Run timing experiments for len on lists of type list_type, returning a
    list of times with the average time it took to run len on list_type objects
    with sizes SIZES over NUM_TRIALS trials.

    Precondition: list_type is either list or LinkedList."""
    times = []

    # We have given you the code for testing len on Python's built-in list below,
    # based on the code from Lab 4.
    for size in SIZES:
        time = 0
        lists = _setup_lists(size, NUM_TRIALS, list_type)
        for lst in lists:
            time += timeit('len(lst)', number=1, globals=locals())

        average_time = time / NUM_TRIALS * 1e6
        times.append(average_time)
        print(f'len: List size {size:>7}, time: {average_time}')

    return times


# TODO: Plot the timing experiment using matplotlib.
#       You may want to follow the pattern provided in Lab 4's starter code:
#       https://q.utoronto.ca/courses/204422/pages/lab-4-abstract-data-types

import matplotlib
def plot_time()->None:
    import matplotlib.pyplot as plt
    lst_times = time_len(list) # var1
    linkedlist_times = time_len(LinkedList)
    betterList_times = time_len(betterList)

    lst_plt, = plt.plot(SIZES,lst_times,'ro')
    lst_plt.set_label('len(lst)')

    lnk_plt, = plt.plot(SIZES, linkedlist_times, 'bo')
    lnk_plt.set_label('len(linkedlist)')

    betterlst_plt, = plt.plot(SIZES,betterList_times,'kx')
    betterlst_plt.set_label("len(betterlist)")

    plt.legend()
    plt.xlabel("List Size")
    plt.ylabel('time')
    plt.show()

if __name__ == '__main__':
    print("Running len(lst) experiments...")
    time_len(list)

    print("Running len(LinkedList) experiments...")
    time_len(LinkedList)

    # TODO: After you implement a function to run the timing experiment,
    #       Add a call to that function below.
    plot_time()