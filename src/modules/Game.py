from asyncio.windows_events import NULL
from unicodedata import decimal, name
# Python doesn't directly support abstract classes.
from abc import ABC, abstractmethod
# the abc (abstract base class) module provides you with the infrastructure for defining abstract base classes

from modules.RealState import RealState

class Game(object):
    # __init__ is a special method called whenever you try to make
    # an instance of a class. As you heard, it initializes the object.
    # Here, we'll initialize some of the data.
    def __init__(self):
        # Let's add some data to the [instance of the] class.
        self.name = ""

    def StartGame(self):
        return self.name

    def InitRandomPlayerOrder(self, name: str):
        self.name = name

    def InitBoard(self):
        return self.realStateList

    def ThrowDice(self, realStateList: list):
        self.realStateList = realStateList
    
    def GetPlayersOnBoard(self, realState: RealState):
        self.realStateList.append(realState) 

