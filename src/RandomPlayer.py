
import math
from unicodedata import decimal
from Player import Player
import random

class RandomPlayer(Player):

    def BuyRealState(self, realStateCost):
        if (random.choice([True, False]) == True):
            self.WithdrawMoney(realStateCost)


player4 = RandomPlayer()

player4.SetName("Jogador3 - Aleatório")
print(player4.GetName())

print(player4.CheckBalance())

realStateCost = 90
player4.BuyRealState(realStateCost)

print(player4.CheckBalance())
