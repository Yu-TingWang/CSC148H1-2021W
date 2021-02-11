Task 1: Play a game
In this lab you'll write code to play a simple number game. This game can be played with two or more players.
When the game starts, there is a count that begins at 0.
On a player's turn, they add to the count an integer that must be between a set minimum and a set maximum.
The player whose move causes the count to be greater than or equal to a set goal amount is the winner.

Here's a sample game with two players, where the goal is 21, the minimum move is 1, and the maximum move is 3.
David is the winner.




| Player1  |      Player2      |  count |
|----------|:-------------:|------:|
|  |   | 0 |
| 2 |       |   2|
| | 3 |   5 |
| 3|  |   8 |
||  1	  |     9|
|3	  |	      |     12|
|      |  3	  |     15|
|1  	  |	      |     16|
|      |   1	  |     17|
|3	  |	      |     20|
|	  |    1  |     21|

Download module nim_no_classes.py into your lab3 folder.
This is a simple version of the number game (named Nim) that you can play by yourself.
This implementation does not use any classes, and is very limited in its functionality.

Try to play the game yourself, or with a partner. Use the goal 21, minimum move 1, and maximum move 3.

Does a good strategy emerge?
(Even if it doesn't, move on after a few minutes when you understand the game. We'll come back to strategies later!)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Task 2: Become familiar with class

Download module lab3.py into your lab3 folder.

Read the NumberGame class carefully and answer the following questions about it.
Note that the entire class is provided for you, and your job here is to understand it-- in other words,
you're practicing your code reading skills.

1. What attribute stores the players of the game?
    - self.players
 
2. If turn is 15, whose turn is it?
    self.players[1]

3. Write a line of code that would create an instance of NumberGame that violates one of the representation invariants.
Which of the representation invariants is it possible to violate by constructing a NumberGame improperly?
    ex. min_step > max_step . NumerGame(goal, 5,3,current,players)
    ex. min_step > goal : NumberGame(0,-3, max_step,current,players)
    

4. List all the places in this class where a Player is stored, an instance attribute of Player is accessed or set,
or a method is called on a Player.

** Minimum requirement **
Players
attribute:
name, 
-- steps,

methods:
move



++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Task 3: Become familiar with function main
Now look at function main and answer these questions:

1. Where is a NumberGame constructed?
2. This function calls g.play repeatedly in a loop.
 What parts of the game can change each time g.play is called: the goal, the min or max move, the players, the moves?

 
3. List all the places in this function where a Player is stored, an instance attribute of Player is accessed or set,
 or a method is called on a Player.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Task 4: Plan a Player class and 3 subclasses
Since you have found all the places where a Player is used, you know the attributes and methods it must provide
as its public interface. You could complete the program by writing a single class Player with methods that provide these.
But we're going to have three different kinds of player. They will have some things in common,
but they will differ on how they choose a move:

* A random player will pick a random move from among the legal possibilities.
* A user player will prompt the user to select a move rather than having the computer choose the move.
* A strategic player will choose the best possible move. (Did you come up with a good strategy earlier?)
Rather than make three unrelated classes, we are going to define a parent class called Player and make three child classes.

1. Get out some paper and write down the four class names Player, RandomPlayer, StrategicPlayer, and UserPlayer with
   lots of space below each in which to describe their data and their methods.
   You are going to make a simple diagram like this one.
2. You already identified which methods are needed based on your reading of the starter code.
   Decide which methods belong in which class and add them to the appropriate spot in your diagram.
3. What information must be stored in order in order for these methods to provide their services?
   Don't worry about attribute names or types yet, just describe the information in plain English.
   Decide which pieces of information belong in which class and add them to the appropriate spot in your diagram.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Task 5: Write class Player
Now write the abstract class Player. You will probably be able to implement some methods completely.
Other methods you won't be able to complete at all-- they are abstract. In those methods, the body should simply say
    raise NotImplementedError
Be sure to include a complete class docstring. (You can look at class NumberGame for a reminder of what they look like.)
Your docstring should warn that the Player class is abstract and should not be instantiated.
You do not need to include doctest examples.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Task 6: Implement class RandomPlayer
Now that we have a Player class, we need one or more child classes that can complete its unimplemented method(s).

Implement class RandomPlayer as a subclass of Player (review how to do this if you aren't sure).
Any Player methods that were not implemented must be overridden here in class RandomPlayer.

We have imported module random for you. You will find the function random.randint handy--
if you aren't sure how to use it, import it in the Python console and call help on it to learn more!
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Task 7: Make the whole thing run
Even though you only have one kind of player, you can still make the program run.
Fill in the missing part in make_player to so that it creates a RandomPlayer.
(Later, we'll let the user choose from among the three types of player.)

Run your game! It should be fun to watch two random players battle it out.

There will likely be small glitches to fix, but they will be things like forgetting an argument,
and shouldn't be hard to fix.
Read the error messages carefully-- they include very precise information about what's wrong.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Task 8: Add class UserPlayer
Now implement UserPlayer. If you have time, ensure that the user's moves are legal. But if you are running out of time,
don't bother with that. It's not important to the learning goals for this lab.

Once you have UserPlayer done, update make_player so it gives the user a choice between the two kinds of player
that you have implemented.

Try playing your game with one user player and one random player. We hope you can beat the random player!
