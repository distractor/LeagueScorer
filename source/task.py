from source.scoring import Scoring

class Task:
    # Empty initializer
    def __init__(self):
        pass

    # Set ID
    def setID(self, ID):
        self.ID = ID

    # Set name
    def setName(self, Name):
        self.Name = Name

    # Set pilots
    def setPilots(self, Pilots):
        self.Pilots = Pilots

    # Score task
    def Score(self, Type, Scale):
        if Type == 'default':
            self.Pilots = Scoring(self.Pilots, Type, Scale).Score()