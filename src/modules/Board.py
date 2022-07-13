from asyncio.windows_events import NULL
from unicodedata import decimal, name
# Python doesn't directly support abstract classes.
from abc import ABC, abstractmethod
from collections import deque
# the abc (abstract base class) module provides you with the infrastructure for defining abstract base classes

from modules.RealState import RealState


class Board(object):
    # __init__ is a special method called whenever you try to make
    # an instance of a class. As you heard, it initializes the object.
    # Here, we'll initialize some of the data.
    def __init__(self):
        # Let's add some data to the [instance of the] class.
        self.name = ""
        #self.realStateList = []*20
        # linked list
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


if __name__ == "__main__":
    # Real state init
    realState1 = RealState()
    realState1.SetName("Edificio 1")
    realState1.SetRentalAmount(100)
    realState1.SetOwner("")

    realState2 = RealState()
    realState2.SetName("Edificio 2")
    realState2.SetRentalAmount(150)
    realState1.SetOwner("")

    realState3 = RealState()
    realState3.SetName("Edificio 3")
    realState3.SetRentalAmount(40)
    realState1.SetOwner("")

    # Board init
    board1 = Board()
    board1.AddRealStateToBoard(realState1)
    board1.AddRealStateToBoard(realState2)
    board1.AddRealStateToBoard(realState3)

    print(board1.GetBoardRealStateList())
