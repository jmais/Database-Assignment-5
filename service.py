from model import Sightings


class sightingsService:
    def __init__(self):
        self.model = Sightings()

    def topTen(self, name):
        return self.model.getTop10(name)

    def create(self,params):
        return self.model.create(params)
    