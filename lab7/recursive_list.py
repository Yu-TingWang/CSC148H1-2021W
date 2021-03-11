"""Lab 6: Recursion

=== CSC148 Winter 2021 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains a new *recursive* implementation of the List ADT
called RecursiveList. Study it carefully, and then try implementing the
methods in this class.
"""
from __future__ import annotations
from typing import Any, Callable, Optional


class RecursiveList:
    """A recursive implementation of the List ADT.

    Note the structural differences between this implementation and the
    node-based implementation of linked lists from the past few weeks.
    Even though both classes have the same public interface,
    how they implement their methods are quite different!
    """
    # === Private Attributes ===
    # _first:
    #     The first item in the list.
    # _rest:
    #     A list containing the items that come after
    #     the first one.
    _first: Optional[Any]
    _rest: Optional[RecursiveList]

    # === Representation Invariants ===
    # _first is None if and only if _rest is None.
    #     This represents an empty list.

    def __init__(self, items: list) -> None:
        """Initialize a new list containing the given items.

        The first node in the list contains the first item in <items>.
        """
        if items == []:
            self._first = None
            self._rest = None
        else:
            self._first = items[0]
            self._rest = RecursiveList(items[1:])

    def is_empty(self) -> bool:
        """Return whether this list is empty.

        >>> lst1 = RecursiveList([])
        >>> lst1.is_empty()
        True
        >>> lst2 = RecursiveList([1, 2, 3])
        >>> lst2.is_empty()
        False
        """
        return self._first is None

    def __str__(self) -> str:
        """Return a string representation of this list.

        >>> lst = RecursiveList([1, 2, 3])
        >>> str(lst) # Equivalent to lst.__str__()
        '1 -> 2 -> 3'
        """
        if self.is_empty():
            return ''
        elif self._rest.is_empty():
            return str(self._first)
        else:
            return str(self._first) + ' -> ' + str(self._rest)

    def __len__(self) -> int:
        """Return the number of elements in this list.

        >>> lst = RecursiveList([])
        >>> len(lst) # Equivalent to lst.__len__()
        0
        >>> lst = RecursiveList([1, 2, 3])
        >>> len(lst)
        3
        """
        if self.is_empty():
            return 0
        else:
            return 1 + len(self._rest)


    def __eq__(self,other):
        if not isinstance(other,RecursiveList):
            raise TypeError
        if self._first != other._first:
            return False
        else:
            return self._rest == other._rest # __eq__(self._rest,other._rest)

    def __contains__(self, item: Any) -> bool:
        """Return whether <item> is in this list.

        Use == to compare items.

        >>> lst = RecursiveList([1, 2, 3])
        >>> 2 in lst # Equivalent to lst.__contains__(2)
        True
        >>> 4 in lst
        False
        """
        if self.is_empty():
            return False
        elif self._first == item:
            return True
        else:
            return self._rest.__contains__(item)
            # Equivalently, item in self._rest

    def count(self, item: Any) -> int:
        """Return the number of times <item> occurs in this list.

        Use == to compare items.

        >>> lst = RecursiveList([1, 2, 1, 3, 2, 1])
        >>> lst.count(1)
        3
        >>> lst.count(2)
        2
        >>> lst.count(3)
        1
        """
        if self.is_empty():
            return 0
        if self._first == item:
            return 1 + self._rest.count(item)
        else:
            return self._rest.count(item)



        pass

    def __getitem__(self, index: int) -> Any:
        """Return the item at position <index> in this list.

        Precondition: index >= 0.

        Raise IndexError if <index> is >= the length of this list.

        >>> lst = RecursiveList([1, 2, 3])
        >>> lst[0] # Equivalent to lst.__getitem__(0)
        1
        >>> lst[1]
        2
        >>> lst[2]
        3
        >>> lst[3]
        Traceback (most recent call last):
        ...
        IndexError
        """
        pass

    ###########################################################################
    # Mutating methods: these methods modify the the list
    ###########################################################################
    def __setitem__(self, index: int, item: Any) -> None:
        """Store item at position <index> in this list.

        Precondition: index >= 0.
        Raise IndexError if index is >= the length of this list.

        >>> lst = RecursiveList([1, 2, 3])
        >>> lst[0] = 100 # Equivalent to lst.__setitem__(0, 100)
        >>> lst[1] = 200
        >>> lst[2] = 300
        >>> lst[3] = 400
        Traceback (most recent call last):
        ...
        IndexError
        >>> str(lst)
        '100 -> 200 -> 300'
        """

    def insert_first(self, item: object) -> None:
        """Insert item at the front of this list.

        This should work even if this list is empty.
        """
        pass

    def pop(self, index: int) -> Any:
        """Remove and return the item at position <index> in this list.

        Precondition: index >= 0.
        Raise IndexError if <index> is >= the length of this list.

        >>> lst = RecursiveList([1, 2, 3])
        >>> lst.pop(2)
        3
        >>> str(lst)
        '1 -> 2'
        >>> lst.pop(1)
        2
        >>> str(lst)
        '1'
        >>> lst.pop(0)
        1
        >>> str(lst)
        ''
        >>> lst.pop(0)
        Traceback (most recent call last):
        ...
        IndexError
        """
        # edge cases : to check if precondition is met
        if self.is_empty():
            raise IndexError
        # base case : ground level of our recursive calls
        elif index == 0:
            return self._pop_first()
        else:
            return self._rest.pop(index-1)

    '''
    l = RecursiveList([1,2,3,4,5])
    l._first = 1
    l._rest = RecursiveList([2,3,4,5])
        l._rest._first = 2
        l._rest._rest = RecursiveList([3,4,5])
            l._rest._rest._first = 3
            l._rest._rest._rest = RecursiveList([4,5])
                l._rest._rest._rest._first = 4
                l._rest._rest._rest._rest = RecursiveList([5])
                    l._rest._rest._rest._rest._first = 5
                    l._rest._rest._rest._rest._rest = RecursiveList([])
                       
    l.pop(2)
    index ==2
    return l._rest.pop(2-1) = RecursiveList([2,3,4,5]).pop(1)
    
    return l._rest._rest.pop(1-1) = RecursiveList([3,4,5]).pop(0)
    return l._rest._rest._pop_first() = 3
    '''

    def _pop_first(self) -> Any:
        """Remove and return the first item in this list.

        Raise an IndexError if this list is empty.
        """
        if self.is_empty():
            raise IndexError
        else:
            stored_first = self._first
            # replace
            self._first, self._rest = self._rest._first, self._rest._rest
            return stored_first



    def insert(self, index: int, item: Any) -> None:
        """Insert the given item in to this list at position <index>.

        Precondition: index >= 0.
        Raise an IndexError if index is > the length of the list.
        Note that it is possible to add to the end of the list
        (when index == len(self)).

        >>> lst = RecursiveList(['c'])
        >>> lst.insert(0, 'a')
        >>> str(lst)
        'a -> c'
        >>> lst.insert(1, 'b')
        >>> str(lst)
        'a -> b -> c'
        >>> lst.insert(3, 'd')
        >>> str(lst)
        'a -> b -> c -> d'
        >>> lst.insert(5, 'd')
        Traceback (most recent call last):
        ...
        IndexError
        """
        pass



    def _insert_first(self, item: Any) -> None:
        """Insert item at the front of this list.

        This should work even if this list is empty.
        """
        pass

    ###########################################################################
    # Additional Exercises
    ###########################################################################
    def map(self, f: Callable[[Any], Any]) -> RecursiveList:
        """Return a new recursive list storing the items that are
        obtained by applying f to each item in this recursive list.

        >>> func = str.upper
        >>> func('hi')
        'HI'
        >>> lst = RecursiveList(['Hello', 'Goodbye'])
        >>> str(lst.map(func))
        'HELLO -> GOODBYE'
        >>> str(lst.map(len))
        '5 -> 7'
        """
        pass



    def selections(self) -> [RecursiveList]:
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
            return [RecursiveList([])]
        else:
            rest_selections = self._rest.selections()
            select_first = []
            for lst in rest_selections:
                # to take the first item
                first_item = RecursiveList([self._first])
                first_item._rest = lst.copy()
                select_first.append(first_item)
            return rest_selections + select_first

    def copy(self) -> RecursiveList:
        if self.is_empty():
            return RecursiveList([])
        else:
            new_list = RecursiveList([])
            new_list._first = self._first
            new_list._rest = self._rest
            return new_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # import python_ta
    # python_ta.check_all()