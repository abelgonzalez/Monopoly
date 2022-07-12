
from asyncio.windows_events import NULL
import Player as Player

class RealState(object):
   
    def __init__(self):
        # Let's add some data to the [instance of the] class.
        self.name = ""
        self.costOfSale = float(200)
        self.rentalAmount = float(100)
        self.owner = NULL
        self.avaliableToBuy = True

    # Getter and setters

    def GetName(self):
        return self.name

    def SetName(self, name: str):
        self.name = name

    def GetCostOfSale(self):
        return self.costOfSale

    def SetCostOfSale(self, costOfSale: float):
        self.costOfSale = costOfSale
    
    def GetRentalAmount(self):
        return self.rentalAmount

    def SetRentalAmount(self, rentalAmount: float):
        self.rentalAmount = rentalAmount
    
    def GetOwner(self):
        return self.owner

    def SetOwner(self, owner: Player):
        self.owner = owner

    def GetOwner(self):
        return self.avaliableToBuy

    def IsAvaliableToBuy(self, avaliableToBuy: bool):
        self.avaliableToBuy = avaliableToBuy



realState = RealState()
realState.SetName("Edificio 1")
realState.SetRentalAmount(100)


print(realState.GetName())
