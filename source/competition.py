from source.FSDB import FSDB
from source.scoring import Scoring

class Competition:
    # Empty initializer
    def __init__(self):
        pass

    # Load from FSDB file
    def loadFromFSDB(self, filePath):
        print('Loading FSDB file from: %s' % filePath)
        self.fsdbFilePath = filePath                                # Save filePath to class
        self.FSDB = FSDB(self.fsdbFilePath)                         # Create FSDB class

        self.Name = FSDB.getCompetitionName(self.FSDB)              # Get Competition name
        self.Dates = FSDB.getCompetitionDates(self.FSDB)            # Get Competition dates
        self.Location = FSDB.getCompetitionLocation(self.FSDB)      # Get Competition location
        self.FAISanctioned = FSDB.getFAIsanctioning(self.FSDB)      # Boolean for FAI sanctioned comp

        self.Pilots = FSDB.getCompetitionParticipants(self.FSDB)    # Gets participants at comp

        self.Tasks = FSDB.getCompetitionTasks(self.FSDB)            # Gets tasks flown at comp

    # Get pilot Name from pilot ID
    def getPilotFromID(self, ID):
        for p in self.Pilots:
            if (p.ID == ID):
                return p

        return None

    # Get pilots by nation
    def getPilotsByNation(self, Nation):
        pilots = []
        for pilot in self.Pilots:
            if pilot.Nationality == Nation:
                pilots.append(pilot)

        self.PilotsByNation = pilots