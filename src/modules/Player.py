from asyncio.windows_events import NULL
import random
from unicodedata import decimal, name
# Python doesn't directly support abstract classes.
from abc import ABC, abstractmethod
# the abc (abstract base class) module provides you with the infrastructure for defining abstract base classes


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
    # @property
    def BuyRealState(self):
        a = 1

    # @property
    def GetName(self):
        return self.name

    # @property
    def SetName(self, name: str):
        self.name = name

    # @property
    def CheckBalance(self):
        return self.accountBalance

    # @property
    def AddBalance(self, amount: float):
        self.accountBalance += amount

    # @property
    def WithdrawMoney(self, amount: float):
        self.accountBalance -= amount

    def DeclareBankrupt(self):
        for i in self.realStateList:
            i.SetOwner(NULL)

        self.realStateList = []


class CautiousPlayer(Player):

    def BuyRealState(self, realStateCost):
        if (self.CheckBalance() - realStateCost > 80):
            self.WithdrawMoney(realStateCost)


class DemandingPlayer(Player):

    def BuyRealState(self, rentalAmount):
        if (rentalAmount > 50):
            self.WithdrawMoney(rentalAmount)


class RandomPlayer(Player):

    def BuyRealState(self, realStateCost):
        if (random.choice([True, False]) == True):
            self.WithdrawMoney(realStateCost)


class ImpulsivePlayer(Player):

    def BuyRealState(self, realStateCost):
        if (realStateCost <= self.CheckBalance()):
            self.WithdrawMoney(realStateCost)
