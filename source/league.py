import os
from source.competition import Competition

class League:
    # Initializer
    def __init__(self, Name, Year, Nationality):
        self.Name = Name
        self.Year = Year
        self.Nationality = Nationality

    # Load all competitions from given year
    def loadCompetitions(self):
        directory = os.getcwd() + '/input/' + str(self.Year)        # directory with league fsdb files
        self.Competitions = []
        for file in os.listdir(directory):
            comp = Competition()                                    # initialize class
            comp.loadFromFSDB(directory + '/' + file)               # fill class
            self.Competitions.append(comp)                          # save comp to league

    # sets all pilots from league
    def findPilots(self):
        self.Pilots = []
        for comp in self.Competitions:
            for pilot in comp.Pilots:
                if (pilot.Nationality == self.Nationality) and not self.pilotParticipated(pilot.Name):
                    self.Pilots.append(pilot)

    # returns boolean if pilot participated
    def pilotParticipated(self, Name):
        if (len(self.Pilots) == 0):
            # Empty list
            return False
        else:
            pilotFound = False
            i = 0
            while (not pilotFound and (i < len(self.Pilots))):
                pilotFound = (self.Pilots[i].Name == Name)
                i = i + 1

            return pilotFound

