Lab 5: Linked Lists
Learning outcomes
By the end of this lab, you will be able to:

- Implement linked list methods using iteration.
- Run timing experiments to compare multiple implementations of an interface.
- Augment the implementation of a class by adding new private attributes

<h1>Task 1: Practice with linked lists</h1>
1. In the starter code, find and read the docstring of the method __len__, and then implement it.

You already implemented this method in this week's prep, but it's good practice to implement it again. 
(And if you missed this week's prep, do it now!)

2. Then, implement the methods count, index, and __setitem__.

3. You might have noticed that all the doctests were commented out in the previous part. 
This is because they use a more powerful initializer than the one we've started with.

Your final task in this section is to implement a new initializer with the following interface:

def __init__(self, items: list) -> None:
    """
    
    Initialize a new linked list containing the given items.

    The first node in the linked list contains the first item
    in <items>.
    """
The lecture notes suggest one way to do this using append; 
however, here we want you to try doing this without using append (or any other helper method).

There are many different ways you could implement this method, but the key idea is that you need to loop through items,
 create a new _Node for each item, link the nodes together, and initialize self._first.

Spend time drawing some pictures before writing any code!


Take subway for example

list: Given the subway line, you can go to whichever station you like
[Union,King,Queen]

linkedlist: When given the subway line, you only have the start station( head node),
in order to get to Queen Station, you have to traverse from Union to King, King to Queen, you can't jump from Union to Queen directly.
| Union|King|  Queen |

<h1>Task 2: Timing __len__ for linked lists vs. array-based lists</h1>
1. Most methods take longer to run on large inputs than on small inputs, although this is not always the case. 
  Look at your code for your linked list method __len__. 
  Do you expect it to take longer to run on a larger linked list than on a smaller one?

2. Pick one the following terms to relate the growth of __len__'s running time vs. input size, and justify.
    - constant
    - logarithmic
    - linear
    - quadratic
    - exponential
3. Complete the code in time_lists.py to measure how running time for your __len__ method changes 
    as the size of the linked list grows. Is it as you predicted?

4. The if __name__ == '__main__' block runs the experiment on both a LinkedList and a list: 
    What do you notice about the behaviour of calling len on a built-in list?
    
<h1>Task 3: Augmenting our linked list implementation</h1>
It makes sense that our implementation of LinkedList.__len__ is so slow; 
but how is the built-in list.__len__ so much faster? 
It turns out that built-in Python lists use an additional attribute to store their length,
 so that whenever list.__len__ is called, it simply returns the value of this attribute.

The process of adding an extra attribute to an existing data structure is known as augmentation, 
and is very common in computer science. Every data structure augmentation poses a question of trade-offs:

- The benefit of augmenting is that the extra attribute makes certain operations simpler and/or more efficient to implement.
- The cost of augmenting is that this extra attribute increases the complexity of the data structure implementation. 
In particular, such attributes often have representation invariants associated with them 
that must be maintained every time the data structure is mutated.

1. Create a copy of your LinkedList class (you can pick a name for the copy), 
and add a new private attribute _length to the class documentation and initializer.



Write down a representation invariant for this new attribute; you can use English here, 
but try to be precise without using the word "length" in your description. 
(Hint: how do we define length in terms of the nodes of a list?)

2. Update each mutating method to preserve your representation invariant for this new attribute. 
(Why don't we need to worry about the non-mutating methods?)

3. Now let's enjoy the benefit of this augmentation! Modify your new class' __len__ method to simply return 
this new attribute. Use doctests wisely to ensure you've made the correct changes for this and the previous step.

4. Finally, perform some additional timing tests to demonstrate that you really have improved the efficiency of __len__.

