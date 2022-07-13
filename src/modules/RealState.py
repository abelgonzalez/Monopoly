
from asyncio.windows_events import NULL
from modules.Player import Player 

class RealState(object):
   
    def __init__(self):
        # Let's add some data to the [instance of the] class.
        self.name = ""
        self.costOfSale = float(200)
        self.rentalAmount = float(100)
        self.owner = ""
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

    def SetOwner(self, owner:Player):
        self.owner = owner

    def GetOwner(self):
        return self.owner

    def IsAvaliableToBuy(self):
        return self.avaliableToBuy 

    def SetAvaliableToBuy(self, avaliableToBuy: bool):
        self.avaliableToBuy = avaliableToBuy


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


