from source.pilot import Pilot
from source.FSDB import FSDB
from source.competition import Competition
from source.task import Task

#Test = Pilot()
#Test.setName("Mitja")

#Test.getName()

#data = FSDB('input/2019/AdrenalinCup2019.fsdb')
#pilots = data.getCompetitionParticipants()
#print(pilots)

comp = Competition()
comp.loadFromFSDB('input/2019/WinterCup2019-2.fsdb')
#for p in comp.Pilots:
    #print(p.Nationality)

#for t in comp.Tasks:
#    print(t.Name)
#    print(t.ID)
#    print(len(t.Pilots))
#    for p in t.Pilots:
#        print(p.ID)

comp.getResults()
for p in comp.Pilots:
    print(p.Name, p.Points, p.Rank)


#print(comp.Name)
#print(comp.Dates)
#print(comp.Location)
#print(comp.FAISanctioned)