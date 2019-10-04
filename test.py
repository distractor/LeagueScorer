from source.pilot import Pilot
from source.FSDB import FSDB
from source.competition import Competition
from source.task import Task
from source.league import League
from source.math import *
from source.result import Result

#Test = Pilot()
#Test.setName("Mitja")




#data = FSDB('input/2019/AdrenalinCup2019.fsdb')
#pilots = data.getCompetitionParticipants()
#print(pilots)

#comp = Competition()
#comp.loadFromFSDB('input/2019/WinterCup2019-2.fsdb')
#comp.Score()
#for task in comp.Tasks:
#    for pilot in task.Pilots:
#        for result in pilot.Result:
#            print('%d: %d %d' % (pilot.ID, result.Rank, result.Points))


#for t in comp.Tasks:
#    print(t.Name)
#    print(t.ID)
#    print(len(t.Pilots))
#    for p in t.Pilots:
#        print(p.ID)

#comp.getResults()

league = League('SLO liga', 2019, 'SLO', False)
league.loadCompetitions()
league.Score('default')
for result in league.Pilots:
    print(result.Name, result.Result[0].Points)
#league.findPilots()
#league.getResultsByTotalPoints()
#for p in league.Pilots:
#    print(p.Rank, p.Name, p.Points)
#league.saveResultsToHTML('Original.html')
#
#scores = [25, 20, 16, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#
#league.getResultsByRank(scores)
#for p in league.Pilots:
#    print(p.Rank, p.Name, p.Points)
#league.saveResultsToHTML('MotoGP.html')
#
#oroz = [7,2,2,7,6,2,2,17,2,3,1,18,2,3,6,3,0,0,3,4]
#bojc = [2,3,3,8,5,0,0,0,1,1,6,12,4,5,3,4,3,2,4,18]
#
#b = 0
#o = 0
#for i in range(len(oroz)):
#    if (oroz[i] > len(scores)) or (oroz[i] == 0):
#        o = o + 0
#    else:
#        o = o + scores[oroz[i] - 1]
#    if (bojc[i] > len(scores)) or (bojc[i] == 0):
#        b = b + 0
#    else:
#        b = b + scores[bojc[i] - 1]
#
#print(o, b)

#print(comp.Name)
#print(comp.Dates)
#print(comp.Location)
#print(comp.FAISanctioned)