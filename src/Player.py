from asyncio.windows_events import NULL
from unicodedata import decimal, name
# Python doesn't directly support abstract classes.
from abc import ABC, abstractmethod
# the abc (abstract base class) module provides you with the infrastructure for defining abstract base classes

import RealState as RealState


class Player(object):
    # __init__ is a special method called whenever you try to make
    # an instance of a class. As you heard, it initializes the object.
    # Here, we'll initialize some of the data.
    def __init__(self):
        # Let's add some data to the [instance of the] class.
        self.name = ""
        self.accountBalance = float(300)
        self.realStateList = []

    # We can also add our own functions.
    #@property
    def BuyRealState(self):
        a = 1

    #@property
    def GetName(self):
        return self.name

    #@property
    def SetName(self, name: str):
        self.name = name

    #@property
    def CheckBalance(self):
        return self.accountBalance

    #@property
    def AddBalance(self, amount: float):
        self.accountBalance += amount

    #@property
    def WithdrawMoney(self, amount: float):
        self.accountBalance -= amount
