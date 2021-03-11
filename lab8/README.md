<h1>Learning outcomes</h1>
By the end of this lab, you will be able to:

- Write recursive methods to perform non-mutating and mutating tasks on trees.
- Augment a tree data structure (add a new attribute) to improve the efficiency
 of one or more tree operations.
 
 <h1>Task 0: Setup and review</h1>
 
 <h2> Review</h2>
Recall that we have introduced a new data structure, the Tree

We often use trees to represent data which falls naturally into a hierarchical, 
non-linear structure (like a family tree or corporate hierarchy), 
and we will soon see an application of trees to efficiently storing ordered data.

We have implemented a tree using a class with two private attributes, ` _root , _subtrees,` 
which represent the value at the root of the tree and the list of subtrees of that tree, respectively. 
Since the subtrees are themselves trees, we call trees a recursive data structure: 
it is built out of parts which have the same structure as the whole. 
This is reflected in our code: we tend to compute on trees using recursive functions and methods, 
whose code tends to follow the same structure as the tree itself:
```
def my_tree_method(self) -> ...:
    if self.is_empty():
        ...
    else:
        ...
        for subtree in self._subtrees:
            ... subtree.my_tree_method() ...
        ...
```

Of course, the hard work is figuring out how to fill in and modify this template to get the desired behaviour.
But keep this code pattern in mind as you work through the lab exercises.

 <h2> Get some paper!</h2>
Before starting the exercises, make sure you do the following. Trust us, it will make reasoning about your code much easier later on.

Take a blank sheet of paper, and draw the following three trees:
- An empty tree (just write the word “Empty” or something similar).
- A tree with just one value.
- A tree with at least three subtrees, which each have height >= 3.
- Draw triangles around each of the subtrees.

You can draw these abstractly, with just a circle (and a value inside it) for each node, rather than a detailed memory model diagram.


 <h1>Task 1: Non-mutating tree methods</h1>
 
  <h2> Branching Factors</h2>
Consider the following definition.

The **branching factor** of an item in a tree is its number of children (or equivalently, its number of subtrees).

In Artificial Intelligence, one of the most important properties of a tree is the average branching factor of 
its internal values (i.e., its non-leaf values).

Your first task is to implement the method `Tree.branching_factor` that computes the average branching factor of 
the internal values in a tree.

_Hint_: similar to the method `Tree.average` we covered in lecture, it’s not enough simply to recursively compute 
the average branching factor of each subtree.
Instead, you and your partner should write a recursive helper method that returns two values that 
together can be used to compute this average branching factor, and where the values can be computed recursively.

  <h2> Items at depth</h2>
  
The **depth** of an item in a tree is the distance (counting values) between the item and the root of the tree, inclusive.

So the root of the tree has depth 1, its children have depth 2, the children of its children have depth 3, etc.

Before jumping right to the code, practice thinking recursively by doing the following:

1. If you haven’t done so already, draw a tree of height 4 that has at least three subtrees.
2. Circle all of the items in your tree at depth 3.
3. Redraw each subtree of your tree separately (leave space between them).
4. On each subtree, circle the same items that you circles in step 2.
5. What is the depth of the items you circled, relative to the subtree (hint: it’s not depth 3)?

After you’ve answered the last part, you’re ready to implement `Tree.items_at_depth`!

```t = 
                    1
            2                 3
        4     5       6   7   8   9   10

t.items_at_depth(3) = 
    values = []
    self._subtrees = [Tree(2),Tree(3)]
    values.extend(Tree(2).items_at_depth(3-1=2))
        Tree(2).items_at_depth(2) = [4,5]
            values' =[]
            Tree(2)._subtrees = [Tree(4),Tree(5)]
            values'.extend(Tree(4).items_at_depth(1))
                Tree(4).items_at_depth(1) = [4]
            values' = [4]
            values'.extend(Tree(5).items_at_depth(1))
                Tree(5).items_at_depth(1) = [5]
            values' = [4,5]
        Tree(2).items_at_depth(2) = [4,5]
    values = [4,5]
    values.extend(Tree(3).items_at_depth(3-1=2))  
          Tree(3).items_at_depth(2) =
               
 
t.items_at_depth(4) = 
    values = []
    self._subtrees = [Tree(2),Tree(3)]
    values.extend(Tree(2).items_at_depth(4-1=3))
        Tree(2).items_at_depth(4-1=3)
            values' =[]
            Tree(2)._subtrees = [Tree(4),Tree(5)]
            values'.extend(Tree(4).items_at_depth(2))
                Tree(4).items_at_depth(2) = []
                Tree(4)._subtrees = []
                values'' = []
            values' = []
            values'.extend(Tree(5).items_at_depth(2))
                Tree(5).items_at_depth(2)=[]
    values = []
    values.extend(Tree(3).items_at_depth(4-1=3))
    ```
        


 <h1>Task 2: A mutating method (insert)</h1>
 
Here, we’re going to write a mutating method, one that inserts a value into a tree.

Since an instance of `Tree` can have any number of subtrees, we can add a new leaf at any spot in the tree simply 
by appending a new subtree to a `_subtree`s list. To make things a bit more interesting, you’re going to explore 
Python’s built-in `random `module to generate random choices as you go down the tree.

Implement the `Tree.insert` method by following the algorithm in its docstring.

Thought question: If you didn’t randomly choose where to insert a new item, where would you put it? 
Would any problems ensue?

 <h1>Task 3: Augmenting the Tree</h1>
 
As we saw with linked lists a few weeks ago, our current implementation of ```Tree.__len__``` is rather inefficient:
 it must recalculate the size of each subtree (recursively) every time it is called.

Your final task in this lab is to augment your ```Tree``` class by adding a new ```size``` instance attribute that 
represents the size of a tree.
You might be tempted to jump right to using it in ```Tree.__len__```, but remember that every new attribute 
we add must be taken into account in the implementations for the _initializer_ and every mutating method!

- For the initializer, you receive a list of `Tree`s as input.

    You should _assume_ that their size attributes are set properly, 
    and simply use each input subtree’s size to initialize `self.size`.
- For the insertion and deletion algorithms you developed in lecture and this lab, make sure to update `self.size` 
when an item is inserted/removed.

You might be nervous about modifying your existing `Tree` class implementation.
If you do this task properly, you shouldn’t have to delete any of the existing code you wrote, but instead add new code to a few methods to keep the size attribute up to date!
 

 