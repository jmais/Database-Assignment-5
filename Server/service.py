from model import Sightings
from model import Flowers


class sightingsService:
    def __init__(self):
        self.model = Sightings()

    def topTen(self, name):
        return self.model.getTop10(name)

    def create(self,params):
        return self.model.create(params)


class flowerService:
    def __init__(self):
        self.model = Flowers()

    def getNames(self):
        return self.model.getNames()
    
    def update(self,params):
        return self.model.update(params)
    
    def select(self):
        return self.model.select()
    