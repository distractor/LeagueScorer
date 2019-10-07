import os
from source.competition import Competition
from source.math import *
from source.result import Result
import pandas as pd
import numpy as np

class League:
    # Initializer
    def __init__(self, Name, Year, Nationality):
        self.Name = Name
        self.Year = Year
        self.Nationality = Nationality
        self.Pilots = []
        self.numberOfTasks = 0

    # Load all competitions from given year
    def loadCompetitions(self):
        directory = os.getcwd() + '/input/' + str(self.Year)        # directory with league fsdb files
        self.Competitions = []
        for file in os.listdir(directory):
            comp = Competition()                                    # initialize class
            comp.loadFromFSDB(directory + '/' + file)               # fill class
            self.Competitions.append(comp)                          # save comp to league

    # get all pilots and their results
    def getAllPilots(self):
        for comp in self.Competitions:
            numberOfTasks = len(comp.Tasks)
            self.numberOfTasks += numberOfTasks
            for p in comp.Pilots:
                if (p.Nationality != self.Nationality):
                    continue
                if (len(self.Pilots) == 0):
                    self.Pilots.append(p)
                else:
                    for compPilot in self.Pilots:
                        #print(compPilot.Name, p.Name)
                        alreadyIn = compareName(compPilot.Name, p.Name)
                        #print(alreadyIn)
                        if alreadyIn:
                            break

                    if alreadyIn:
                        pilotIndex = self.getPilotIndexByName(compPilot.Name)
                        for i in range(self.numberOfTasks - len(self.Pilots[pilotIndex].Result) - len(p.Result)):
                            self.Pilots[pilotIndex].Result.append(Result(-1, -1))
                        for result in p.Result:
                            self.Pilots[pilotIndex].Result.append(result)
                    else:
                        self.Pilots.append(p)

        for pilot in self.Pilots:
            for i in range(self.numberOfTasks - len(pilot.Result)):
                pilot.Result.append(Result(-1, -1))

        # normalization
        self.normalizeResults()
        # sums points
        self.sumPilotPoints()
        # order bs points
        self.orderPilotsByPoints()


    def getPilotIndexByName(self, Name):
        i = 0
        for i in range(len(self.Pilots) - 1):
            bSame = compareName(self.Pilots[i].Name, Name)
            if (bSame == True):
                break

        return i

    def sumPilotPoints(self):
        for pilot in self.Pilots:
            score = 0
            for result in pilot.Result:
                score += max(0, result.Points)

            pilot.setFinalResult(Result(score, -1))

    # order pilots by points
    def orderPilotsByPoints(self):
        ordered = False
        while (not ordered):
            ordered = True
            for i in range(1, len(self.Pilots)):
                currentPilot = self.Pilots[i]
                previousPilot = self.Pilots[i - 1]

                if (currentPilot.finalResult.Points > previousPilot.finalResult.Points):
                    self.Pilots[i] = previousPilot
                    self.Pilots[i - 1] = currentPilot
                    ordered = False

        # add ranking
        self.addPilotRank()


    # Add rank to pilots
    def addPilotRank(self):
        self.Pilots[0].finalResult = Result(self.Pilots[0].finalResult.Points, 1)  # winner
        for i in range(1, len(self.Pilots)):
            if (self.Pilots[i].finalResult.Points == self.Pilots[i - 1].finalResult.Points):
                # Same points for two (or more) pilots
                self.Pilots[i].setFinalResult(Result(self.Pilots[i].finalResult.Points, self.Pilots[i - 1].finalResult.Rank))
            else:
                self.Pilots[i].setFinalResult(Result(self.Pilots[i].finalResult.Points, i + 1))

    def normalizeResults(self):
        for i in range(self.numberOfTasks - 1):
            highestScore = 0
            for pilot in self.Pilots:
                highestScore = max(highestScore, pilot.Result[i].Points)

            if (highestScore > 500):
                Scale = 1000 / highestScore
            elif (highestScore > 250):
                Scale = 500 / highestScore
            else:
                Scale = 250 / highestScore

            print(Scale)
            for pilot in self.Pilots:
                pilot.Result[i].setPoints(max(int(pilot.Result[i].Points * Scale), 0)) # without the max, the value is negative??

    # create pandas array and save it to HMTL
    def saveResultsToHTML(self, fileName):
        pilots = [p.Name for p in self.Pilots]
        ranks = [p.finalResult.Rank for p in self.Pilots]
        points = [p.finalResult.Points for p in self.Pilots]
        data = pd.DataFrame({'Rank' : ranks, 'Name' : pilots, 'Points' : points})

        for iTask in range(self.numberOfTasks - 1):
            taskResults = [p.Result[iTask].Points if p.Result[iTask].Points != -1 else 0 for p in self.Pilots]

            d = pd.DataFrame({'T%d' % (iTask + 1) : taskResults})
            data = pd.concat([data, d], axis = 1)

        filePath = os.getcwd() + '/results/' + fileName
        data.to_html(filePath)
        print('File saved to %s.' % (filePath))