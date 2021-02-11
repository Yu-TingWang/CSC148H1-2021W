"""Object-Oriented Programming: Twitter example

=== CSC148 Winter 2021 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains two sample classes Tweet and User that we developed
as way to introduce the major concepts of object-oriented programming.
"""
from __future__ import annotations # Allows forward references in type annotations.
from datetime import date  # Python library for working with dates (and times)
from typing import List    # Python library for expressing complex types


class Tweet:
    """A tweet, like in Twitter.

    === Attributes ===
    content: the contents of the tweet.
    userid: the id of the user who wrote the tweet.
    created_at: the date the tweet was written.
    likes: the number of likes this tweet has received.

    === Sample Usage ===

    Creating a tweet:
    >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
    >>> t.userid
    'Rukhsana'
    >>> t.created_at
    datetime.date(2017, 9, 16)
    >>> t.content
    'Hey!'

    Tracking likes for a tweet:
    >>> t.likes
    0
    >>> t.like(1)
    >>> t.likes
    1
    >>> t.like(10)
    >>> t.likes
    11
    """
    # Attribute types
    content: str
    userid: str
    created_at: date
    likes: int

    def __init__(self, who: str, when: date, what: str) -> None:
        """Initialize a new Tweet.

        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.userid
        'Rukhsana'
        >>> t.created_at
        datetime.date(2017, 9, 16)
        >>> t.content
        'Hey!'
        >>> t.likes
        0
        """
        self.content = what
        self.userid = who
        self.created_at = when
        self.likes = 0

    def like(self, n: int) -> None:
        """Record the fact that this tweet received <n> likes.

        These likes are in addition to the ones <self> already has.

        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.like(3)
        >>> t.likes
        3
        """
        self.likes += n

    def edit(self, new_content: str) -> None:
        """Replace the contents of this tweet with the new message.

        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.edit('Rukhsana is cool')
        >>> t.content
        'Rukhsana is cool'
        """
        self.content = new_content

    def retweet(self,new_user:User,new_date:date) -> Tweet:
        '''Return a copy of the given tweet with the new user and date.

        The new tweet has 0 likes, regardless of the number of likes of the
        original tweet.
        :param self: tweet
        :param new_userid: the userid of the user that is going to retweet
        :param new_date: the date that the new user retweet this tweet
        :return:
        >>> t1 = Tweet('David', date(2017, 8, 19), 'David is so cool!')
        >>> u1 = User('apple','macbook')
        >>> t2 = t1.retweet(u1,date.today())
        >>> t2.userid
        'apple'
        >>> t2.content
        'David is so cool!'
        '''
        # create a new Tweet with different created_at date, and different user that create the new Tweet
        # but the content of the tweet is still the same
        new_tweet = Tweet(new_user.userid,new_date,self.content)
        # create connection with new_user
        new_user.tweets.append(new_tweet)
        return new_tweet




class User:
    """A Twitter user.

    === Attributes ===
    userid: the userid of this Twitter user.
    bio: the bio of this Twitter user.
    follows: a list of the other users who this Twitter user follows.
    tweets: a list of the tweets that this user has made.
    """
    # Attribute types
    userid: str
    bio: str
    follows: List[User]
    tweets: List[Tweet]

    def __init__(self, id_: str, bio: str) -> None:
        """Initialize this User.

        >>> u = User('Rukhsana', 'Roller coaster fanatic')
        >>> u.userid
        'Rukhsana'
        >>> u.bio
        'Roller coaster fanatic'
        >>> u.follows
        []
        >>> u.tweets
        []
        """
        self.userid = id_
        self.bio = bio
        self.follows = []
        self.tweets = []

    def tweet(self, message: str) -> None:
        """Record that this User made a tweet with the given content.

        Use date.today() to get the current date for the newly created tweet.

        >>> u1 = User('Rukhsana', 'Roller coaster fanatic')
        >>> u1.tweet('Wheeeeee!')
        >>> u1.tweet('Again! Again!')
        >>> len(u1.tweets)
        2
        """
        new_tweet = Tweet(self.userid, date.today(), message)
        self.tweets.append(new_tweet)

    def follow(self, other: User) -> None:
        """Record that this User follows <other>.

        >>> u1 = User('Rukhsana', 'Roller coaster fanatic')
        >>> u2 = User('POTUS', 'USA!!!')
        >>> u1.follow(u2)
        >>> len(u1.follows)
        1
        >>> len(u2.follows)
        0
        """
        self.follows.append(other)

    def verbosity(self, y: int) -> int:
        """Return the number of characters in this User's tweets in year <y>.

        >>> u1 = User('Rukhsana', 'Roller coaster fanatic')
        >>> u1.tweet('The comet!!')
        >>> u1.tweet('Leviathan!!!!!')
        >>> u1.verbosity(date.today().year)
        25
        >>> u1.verbosity(2015)
        0
        """
        # TODO: Implement this!
        # Hint: look up the attributes of date, found here:
        # https://docs.python.org/3/library/datetime.html#date-objects
        total = 0 # record the total number of characters in the users' tweets created at year y
        for x in self.tweets: # x: is an object Tweet
            # x:Tweet , Tweet has an attribute created_at, which is an object of date
            # x.created_at: date, date has an attribute year
            # x.created_at.year: int, indicating the year in the date object
            if x.created_at.year == y:
                total += len(x.content)
        return total

    def hack(self) -> None:
        """Make every tweet made by every user this user follows say
        'mwahahaha'.

        Use the <edit> method from the Tweet class.

        >>> u1 = User('Diane', 'amazing laugh')
        >>> u2 = User('David', 'okay laugh')
        >>> u1.follow(u2)
        >>> u2.tweet('David is so cool')
        >>> u2.tweets[0].content
        'David is so cool'
        >>> u1.hack()
        >>> u2.tweets[0].content
        'mwahahaha'
        """
        # TODO: implement this!
        for u in self.follows: # follows: List[User]
            # u : User
            for t in u.tweets: # t: Tweet
                t.edit('mwahahaha')

    def retweet(self,tweet:Tweet,new_date:date) -> Tweet:
        '''Return a copy of the given tweet with the new user and date.

        The new tweet has 0 likes, regardless of the number of likes of the
        original tweet.
        :param self : user
        :param tweet: an object of tweet whose content we need to copy
        :param new_date: the date of this tweet we are going to copy
        :return:
        >>> u1 = User('Diane', 'amazing laugh')
        >>> u2 = User('David', 'okay laugh')
        >>> t1 = Tweet('Diane',date.today(),'hello world')
        >>> t2 = u2.retweet(t1,date(2021,7,31))
        >>> t2.userid
        'David'
        >>> t2 = u2.retweet(t1,date(2021,7,31))
        >>> t2.created_at
        datetime.date(2021, 7, 31)
        >>> t2 = u2.retweet(t1,date(2021,7,31))
        >>> t2.content
        'hello world'
        '''
        # create a new Tweet with the content in tweet but with the date of new_date
        new_tweet = Tweet(self.userid,new_date,tweet.content)
        # add this newly created Tweet to our list of tweets
        self.tweets.append(new_tweet)
        # return the newly created Tweet
        return new_tweet

# TODO: Suppose we want to turn this function into a method.
# Which class should we put it into? Once you've decided, move it.
def retweet(new_user: str, tweet: Tweet, new_date: date) -> Tweet:
    """Return a copy of the given tweet with the new user and date.

    The new tweet has 0 likes, regardless of the number of likes of the
    original tweet.

    >>> t1 = Tweet('David', date(2017, 8, 19), 'David is so cool!')
    >>> t2 = retweet('Diane', t1, date(2017, 8, 20))
    >>> t2.content
    'David is so cool!'
    >>> t2.userid
    'Diane'
    >>> t2.created_at
    datetime.date(2017, 8, 20)
    """
    return Tweet(new_user, new_date, tweet.content)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Optionally, check your work with python_ta!
    # import python_ta
    # python_ta.check_all(config={'extra-imports': ['datetime']})
