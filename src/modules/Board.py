
from collections import deque

from modules.RealState import RealState


class Board(object):
   
    def __init__(self):
        self.name = ""      
        self.realStateList = deque()

    def GetBoardName(self):
        return self.name

    def SetBoardName(self, name: str):
        self.name = name

    def GetBoardRealStateList(self):
        return self.realStateList

    def SetBoardRealStateList(self, realStateList: list):
        self.realStateList = realStateList

    def AddRealStateToBoard(self, realState: RealState):
        self.realStateList.append(realState)


   