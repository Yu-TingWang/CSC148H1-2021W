**Learning goals**

By the end of this lab, you will be able to:
- Write recursive functions to solve problems on recursive structures (like nested lists)
- Implement the List ADT using a recursive approach

**Review of Recursion**

Recall from lecture and the prep exercise that recursion consists of 2 main cases:

1. A base case: where no recursive calls are needed
2. A general case: where you combine recursive calls to return the desired result.

As you work on recursive functions, keep these cases in mind.

Before starting the lab, consider this example: suppose we want to write a function that takes a nested list and returns the total number of lists in it (i.e. the number of [...]s we see).

```
def count_lists(obj: Union[int, List]) -> int:
    """Return the number of lists in obj. If obj is an int, return 0.
    >>> count_lists(1)
    0
    >>> count_lists([1, [2, 3], [[4]]])
    4
    """
```
To write the body of this function: start by identifying the base case. What's the simplest case that wouldn't require any recursive calls?

This would be the case of obj being an int: there's nothing to recurse on, after all. The docstring itself tells us what to do in this case: return 0.

Now, this means our general case is the case where obj is a list. In our general case, we make our recursive calls: in the case of count_lists(), we're making recursive calls on each element in our list, obj. Ideally, we would expect that:

- Calling count_lists() on an int should return 0.
- Calling count_lists() on a list should return the number of lists.

Consider the example count_lists([1, [2, 3], [[4]]]) and the recursive calls made:

- count_lists(1) should return 0.
- count_lists([2, 3]) should return 1.
- count_lists([[4]]) should return 2.

And for count_lists([1, [2, 3], [[4]]]) as a whole, we would expect 4 to be returned: this is the sum of the recursive calls (i.e. the number of lists in each element of obj) + 1 to account for the current list [1, [2, 3], [[4]]].

If you write code to match these steps, you should find your recursive function works. When writing a recursive function, you should assume your recursive calls work as expected. This assumption may feel strange, but take of faith and believe in it. Afterwards, you simply need to figure out how to use the results of those recursive calls and work accordingly!

Note: You might have also come to the conclusion that "a list of only ints" could be a base case, but you can make recursive calls on each of the elements. For such a base case, you would have to check to make sure that such a list doesn't contain any other lists. Does our general case handle this for us?

**Task 1: Practice with nested lists**

Open the file nested.py that contains a few nested list functions for you to implement.

To help you, the doctest examples illustrate

- a base case, where no recursive calls are needed, and
- a general case where you combine recursive calls to return the desired result.

For each of the functions, read the docstring and implement it using recursion.
Follow these four design steps:

1. Identify the recursive structure and write down the code template for nested lists:
```
def f(obj: Union[int, List]) -> ...:
    if isinstance(obj, int):
        ...
    else:
        for sublist in obj:
            ... f(lst_i) ...
```
2. Implement the base case(s) directly.

3. Write down a concrete example with a somewhat complex argument, and then write down the relevant recursive calls and what they should return.

greater_than_all(obj:[1, 2, [1, 2], 4], 10)
obj:[1, 2, [1, 2], 4]
 - sublist = 1
    - greater_than_all(1,10) = True
 - sublist = 2
    - greater_than_all(2,10) = True
 - sublist = [1,2]
    - greater_than_all([1,2],10)
        - sublist = 1
            - greater_than_all(1,10) = True
        - sublist = 2
            - greater_than_all(2,10) = True
 - sublist = 4
    - greater_than_all(4,10) = True

- Return True
    
greater_than_all(obj:[1, 2, [11, 2], 4], 10)
obj:[1, 2, [11, 2], 4]
 - sublist = 1
    - greater_than_all(1,10) = True
 - sublist = 2
    - greater_than_all(2,10) = True
 - sublist = [11,2]
    - sublist = 11
        - greater_than_all(11,10) = False


return False

---------------------- from line 51
add_n(obj:[1, 2, [1, 2], 4], 10)
- obj:[1, 2, [1, 2], 4]
    - i = 0
        - obj[0] = 1
            - obj[0] = add_n(1,10) = 11
-> obj:[11, 2, [1, 2], 4]
    - i = 1
        - obj[1] = 2
            - obj[1] = add_n(2,10) = 12
-> obj:[11, 12, [1, 2], 4]
    - i = 2
        - obj[2] = [1,2]
            - obj[2] = add_n([1,2],10)
                - obj' = [1,2]
                    - i' = 0
                        - obj'[0] = 1
                        - obj'[0] = add_n(1,10) = 11
                -> obj' = [11,2]
                    - i' = 1
                        - obj'[1] = 2
                        - obj'[1] = add_n(2,10) = 12
                -> obj' = [11,12]
            - obj[2] = [11,12]       
-> obj:[11, 12, [11, 12], 4]             
    - i = 3
        - obj[3] = 4
            - obj[3] = add_n(4,10) =14
->- obj:[11, 12, [11, 12], 14]









4. Think about how to combine the recursive calls to compute the correct output.


**Task 2: Recursive implementation of the List ADT**

Now, you will use your growing comfort with recursion to implement the List ADT recursively.
This will be the third implementation of the List ADT that we have covered in this course.
Remember that implementations can have the same public interface, even though they implement their methods quite differently!
This guarantees that if client code switches to using the new implementation, it will work exactly as it did before. We get “plug-out plug-in compatability”.

Open the file recursive_list.py that contains a partial implementation of a recursive list class RecursiveList.
In this task you will implement the rest of its methods.

There are two important things to note before you begin:

- A recursive list has two attributes:

    - the first item in the list. This is actual list content, and can be of any type.
    - the rest of the list, which is itself a list!
- An empty list is represented by having its _first and _rest attributes be None.
This is expanded upon in a representation invariant in the class documentation.

When you are ready, follow these steps to learn and work with this new recursive structure.

1. Study this memory model diagram showing a RecursiveList containing four integers:
    - Review the attributes of the class and see how they appear in the diagram.
    - Confirm that this is a valid instance of the class, in other words, that it satisfies the representation invariants.
2. Make your own diagram showing what an empty recursive list looks like in this implementation.
3. Read the docstring and code for the ```__init__```, ```is_empty```, and ```__str__``` methods and understand how each of these three methods works on these instances.
4. Read the docstring for ```__len__ ```and implement the method.

lst = RecursiveList([1, 2, 3])
    - self.is_empty() = False
    - 1+ len(self._rest)
    - 1+ len(RecursiveList([2,3])) 
        - self = RecursiveList([2,3])
        - self.is_empty()=False
        - 1 + len(self._rest)
        - 1 + len(RecursiveList([3]))
            - self = RecursiveList([3])
            - self.is_emptu() = False
            - 1 + len(self._rest)
            - 1 + len(RecursiveList([]))
                - self = RecursiveList([])
                - self.is_empty() = True
            -> 1 + len(RecursiveList([])) = 1 + 0  ... line 183
        -> 1 + len(RecursiveList([3])) = 1 + 1 = 2 ... line 179
    -> 1+ len(RecursiveList([2,3]))  = 1 + 2 = 3 ... line 175   






Your implementation should handle the base case, where the list is empty, and the recursive case, where the list definitely has one item, and possibly more items.
Remember that even if a ```RecursiveList``` has just one item, its ```_rest``` attribute still refers to a ```RecursiveList``` object!
5. Read the docstring and implementation for ```__contains__```.

x = RecursiveList([1,2,3])
y = RecursiveList([None,2,3,4,5])

x._first = 1
x._rest = RecursiveList([2,3])
let's call x._rest = w
w = RecursiveList([2,3])
w._first = 2
w._rest = RecursiveList([3])
let's call w._rest = h
h = RecursiveList([3])
h._first = 3
h._rest = RecursiveList([]) = None

Again, ```__contains__``` has two base cases.
Then read the docstring for count, which is similar to ```__contains__```, and implement the method.
6. Read the docstring for ```__getitem__```. ```__getitem__``` should have two base cases:
      - the list is empty,
      - the index is 0, referring to the first item in the list. 
      - Then, implement the method.
7. Read the docstring for ```__setitem__```, which is similar to ```__getitem__```, and implement the method.
8. Read the docstring for the methods ```insert``` and ```pop```, that mutate a list at a specified index.
For each method, write down the base case(s), and then implement it using recursion.

You may find implementing the methods ```_pop_first``` and ```_insert_first``` helpful.
