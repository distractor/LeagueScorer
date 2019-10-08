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
            self.Competitions.append(comp)                          # save comp to self

    # gets all pilots and their results
    def getAllPilots(self):
        for comp in self.Competitions:
            numberOfTasks = len(comp.Tasks)
            self.numberOfTasks += numberOfTasks                 # number of tasks in league
            for p in comp.Pilots:
                if (p.Nationality != self.Nationality):
                    # continue if pilot is not of interest
                    continue

                if (len(self.Pilots) == 0):
                    # first pilot of interest is appened
                    self.Pilots.append(p)
                else:
                    # pilots already in the league: check if current pilot is already in
                    for compPilot in self.Pilots:
                        alreadyIn = compareName(compPilot.Name, p.Name)
                        if alreadyIn:
                            break

                    if alreadyIn:
                        # pilot is already in, so just append results
                        pilotIndex = self.getPilotIndexByName(compPilot.Name)
                        # append missing results
                        for i in range(self.numberOfTasks - len(self.Pilots[pilotIndex].Result) - len(p.Result)):
                            self.Pilots[pilotIndex].Result.append(Result(-1, -1))
                        for result in p.Result:
                            self.Pilots[pilotIndex].Result.append(result)
                    else:
                        # pilot is first time in.
                        # prepend missing results
                        result = []
                        if (self.numberOfTasks - len(p.Result) != 0):
                            for i in range(self.numberOfTasks - len(p.Result)):
                                result.append(Result(-1, -1))
                        for r in p.Result:
                            result.append(r)

                        p.setResult(result)
                        self.Pilots.append(p)


        # make sure all pilots have same number of tasks
        for pilot in self.Pilots:
            for i in range(self.numberOfTasks - len(pilot.Result)):
                pilot.Result.append(Result(-1, -1))

        # normalization
        self.normalizeResults()
        # sums points
        self.sumPilotPoints()
        # order bs points
        self.orderPilotsByPoints()

    # Finds pilot index in list from name
    def getPilotIndexByName(self, Name):
        i = 0
        for i in range(len(self.Pilots) - 1):
            bSame = compareName(self.Pilots[i].Name, Name)
            if (bSame == True):
                break
        return i

    # sums points from all tasks and saves in final result
    def sumPilotPoints(self):
        for pilot in self.Pilots:
            score = 0
            pilot.setFinalResult(Result(-1, -1))
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

    # normalizes task points
    def normalizeResults(self):
        for i in range(self.numberOfTasks - 1):
            highestScore = 0
            for pilot in self.Pilots:
                highestScore = max(highestScore, pilot.Result[i].Points)

            # get scaling factor
            if (highestScore > 500):
                Scale = 1000 / highestScore
            elif (highestScore > 250):
                Scale = 500 / highestScore
            else:
                Scale = 250 / highestScore

            # multiply results
            for pilot in self.Pilots:
                pilot.Result[i].setPoints(max(round(pilot.Result[i].Points * Scale), 0)) # without the max, the value is negative??

    # create pandas array and save it to HMTL
    def saveResultsToHTML(self, fileName):
        pilots = [p.Name for p in self.Pilots]
        ranks = [p.finalResult.Rank for p in self.Pilots]
        points = [p.finalResult.Points for p in self.Pilots]
        data = pd.DataFrame({'Rank' : ranks, 'Name' : pilots, 'Points' : points})

        for iTask in range(self.numberOfTasks):
            taskResults = [p.Result[iTask].Points if p.Result[iTask].Points != -1 else 0 for p in self.Pilots]

            d = pd.DataFrame({'T%d' % (iTask + 1) : taskResults})
            data = pd.concat([data, d], axis = 1)

        filePath = os.getcwd() + '/results/' + fileName
        data.to_html(filePath)
        print('File saved to %s.' % (filePath))

    def useMotoGPScoring(self, Scores):
        rewardPlaces = len(Scores)
        for iTask in range(self.numberOfTasks):
            pilotNames = [p.Name for p in self.Pilots]
            pilotScore = [p.Result[iTask].Points for p in self.Pilots]

            pilotScore, pilotNames = (list(t) for t in zip(*sorted(zip(pilotScore, pilotNames), reverse = True)))
            pilotScore = Scores + [0] * (len(pilotScore) - rewardPlaces)
            for i in range(len(pilotScore) - 1):
                pilotIndex = self.getPilotIndexByName(pilotNames[i])
                self.Pilots[pilotIndex].Result[iTask] = Result(pilotScore[i], -1)

        # sums points
        self.sumPilotPoints()
        # order bs points
        self.orderPilotsByPoints()