from typing import List    # Python library for expressing complex types
from typing import Dict, List
class Player:

    name: str
    scores: List[int]
    #top_score: int

    def __init__(self,name:str):
        '''
        create a new player whose name is 'name' and no scores history
        '''
        self.name = name
        self.scores = []

    def add_score(self,new_score:int):
        '''
        if 100 screos and already records, remove the oldest score
        :param new_score:
        :return:
        '''
        # check if we hae more than 100 scores
        if len(self.scores)== 100:
            # remove the oldest score
            self.scores.pop(0) # this will remove the first element in the list
            # for more information , go to python console and type help(list) check documetation of pop
        self.scores.append(new_score)

    def top_score(self)->int:

        return max(self.scores)
        #return self.top_score # if you choose this way, you have to deal wiht the param in add_score

    def average_score(self,n:int)->float:
        '''
        return the average score of the most n recents games of this player
        Precondition : this player has at least n scores
        :param n:
        :return:
        '''
        # we have to get the total score of the most n recents games
        total = sum(self.scores[-n:])
        return total/n