import os
from source.competition import Competition
from source.result import Result
from source.scoring import Scoring
import pandas as pd

class League:
    # Initializer
    def __init__(self, Name, Year, Nationality, Scale):
        self.Name = Name
        self.Year = Year
        self.Nationality = Nationality
        self.Scale = Scale

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
                pilotCompeted, pilotIndex = self.pilotParticipated(pilot.Name)
                if (pilot.Nationality == self.Nationality) and not pilotCompeted:
                    self.Pilots.append(pilot)

    def getAllPilotResult(self):
        for comp in self.Competitions:
            for task in comp.Tasks:
                for taskPilot in task.Pilots:
                    pilotCompeted, pilotIndex = self.pilotParticipated(comp.getPilotFromID(taskPilot.ID).Name)
                    if pilotCompeted:
                        result = Result(taskPilot.Result[0].Points, taskPilot.Result[0].Rank)
                    else:
                        result = Result(0, 0)
                    self.Pilots[pilotIndex].addResult(result)

    # returns boolean if pilot participated
    def pilotParticipated(self, Name):
        if (len(self.Pilots) == 0):
            # Empty list
            return [False, 0]
        else:
            pilotFound = False
            i = 0
            while (not pilotFound and (i < len(self.Pilots))):
                nameParts = Name.split(' ')
                pilotFound = True
                # Loop in case pilots last and first name are switched anytime
                for part in nameParts:
                    pilotFound = pilotFound and (part in self.Pilots[i].Name)
                i = i + 1

            return [pilotFound, i - 1]

    #Score
    def Score(self, Type):
        self.findPilots()
        self.getAllPilotResult()
        scoring = Scoring(self.Pilots, Type, self.Scale)
        self.Pilots = scoring.sumPoints()
        self.Pilots = scoring.Score()

    # create pandas array and save it to HMTL
    def saveResultsToHTML(self, fileName):
        pilots = [p.Name for p in self.Pilots]
        ranks = [p.Rank for p in self.Pilots]
        points = [p.Points for p in self.Pilots]
        data = pd.DataFrame({'Rank' : ranks, 'Name' : pilots, 'Points' : points})

        filePath = os.getcwd() + '/results/' + fileName
        data.to_html(filePath)
        print('File saved to %s.' % (filePath))
