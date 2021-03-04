**Learning goals**

By the end of this lab, you will be able to:

- Understand how for-loop iteration is implemented in Python
- Write recursive functions to solve problems on recursive structures (like nested lists or RecursiveList)

Please note that while this lab looks a bit shorter than previous ones, the material covered is more technically challenging than past labs.
Don’t be afraid to ask questions to make sure you understand what’s going on before writing any code!

<h1>Task 0: Setup</h1>

Download the following file, and save it to your labs/lab7 folder.

- linked_list.py
- Also, copy-and-paste your recursive_list.py file from last week into your labs/lab7 folder, as you’ll be building on that in Task 2 this week.

<h1>Task 1: Understanding iteration</h1>
In our study of linked lists, we have striven to implement as much of the functionality of the Python list class as possible.
However, one fundamental feature of Python lists has eluded us: the easy way we can iterate through lists using for loops:

```
s = 0
for n in [1, 2, 3, 4, 5]:
    s += n
print(s)
```

Though our Linked List traversal pattern plays the same role, it sure would be nice to be able to use for loops with linked lists!

The key to supporting for loop iteration is through a Python concept called iterators.

An iterator is a Python object that provides access to a sequence of items one at a time.

There are two steps to enabling our LinkedList objects to be used in for loops using an iterator:

1. Inside ```LinkedList```, implement a special method called ```__iter__```, which returns an iterator for the linked list.
We’ll use a new class ```LinkedListIterator``` to represent this type of object.
2. Inside ```LinkedListIterator```, implement the special method ```__next__```, which returns the next item in the linked list.
Each subsequent call to ```__next__``` should return a new item in the linked list, until it reaches the end of the list.
If ```__next__``` is called after the end of the list has been reached, it
should raise a ```StopIteration``` error.
Here’s how these two special methods are used when we encounter a for loop like the following:

```
lst = LinkedList([1, 2, 3])
for i in lst:
    print(i)
```

1. When the ```for``` loop is first reached, Python calls ```lst.__iter__()```, obtaining a new ```LinkedListIterator``` object associated with ```lst```.

2. At each iteration (including the first one), Python calls ```__next__``` on the iterator object, and stores the returned value in ```i```.
Then the loop body executes with this value of i.

Every single time Python start a new iteration, ```__next__``` is called again, and a new value is bound to i.
So it’s the responsibility of the iterator’s ```__next__``` method to make sure that it continually returns new values in the linked list lst.

How does the ```for``` loop stop? By catching and handling a ```StopIteration``` error!

Your task is to take these ideas, and complete the code in ```linked_list.py```.
As usual, more technical details can be found within the starter code.

Once you are done, go back and see if the new for syntax makes it easier to implement ```__contains__```, ```count```, and other methods for ```LinkedList```.
Note that depending on your implementations, using a ```for``` loop might not always be appropriate!

<h1>Task 2: Recursive lists revisited</h1>

First, if you didn’t get a chance to complete the all of the ```RecursiveList``` method from last week’s lab, you can go back and do so now!
This is excellent preparation for the more complex recursive data structures we’ll begin studying next week.

Next, we’ll look at one particularly famous example of using recursion to elegantly solve a problem that is hard to solve non-recursively.

Consider a list lst = ```[x_1, x_2, ..., x_n]```.
We define a **selection of** ```lst``` to be a list that contains some of the items in ```lst```, in the same order they appeared in ```lst```.
For example, the list ```[1, 2, 3]``` has eight selections:
```
[1], [1, 2], [1, 3], [1, 2, 3]
[], [2], [3], [2, 3]
```
Your task is to implement a ```RecursiveList``` method which returns all possible selections of a list.
Each selection should be stored as a new ```RecursiveList``` object.

Copy-and-paste the following starter code for this method into the ```RecursiveList``` class definition from the previous lab.

```
def selections(self) -> List[RecursiveList]:
        """Return a list of all selections from this list.

        You can return the selections in any order.

        >>> lst1 = RecursiveList([])
        >>> selections1 = lst1.selections()
        >>> len(selections1)
        1
        >>> selections1[0].is_empty()
        True
        >>> lst2 = RecursiveList([1, 2, 3])
        >>> len(lst2.selections())
        8
        """
        if self.is_empty():
            ...
        else:
            rest_selections = self._rest.selections()
            ...
```
Hints:

1. In our example above of ```lst = [1, 2, 3]```, the “rest” of the list is ```[2, 3]```, and the selections of the rest are ```[], [2], [3], [2, 3]```.
How does that compare to the total selections of ```[1, 2, 3]```?
To prevent accidental aliasing, you’ll want to define a helper method ```RecursiveList.copy``` that returns a new recursive list that’s a copy of ```self```.

<h1>Additional exercises</h1>
<h2>Permutations</h2>
We define a permutation of a list to be another list with exact same elements as the original list, but which may or may not be in the same order as the original.

For example, the list `[1, 2, 3]` has six permutations:

```
[1, 2, 3], [1, 3, 2],
[2, 1, 3], [3, 1, 2],
[2, 3, 1], [3, 2, 1]
```

Write a ```RecursiveList``` method called ```permutations``` that returns a list of all of the permutations of a recursive list.
As with ```selections```, each permutation should be represented as a brand new ```RecursiveList``` object.


Make ```RecursiveList``` iterable

Even though our implementation of ```RecursiveList``` is fundamentally recursive, we can use the same ideas from Task 1 to be able to iterate through this type of list as well.
Try doing this for some extra practice!