from source.pilot import Pilot
from source.FSDB import FSDB
from source.competition import Competition
from source.task import Task
from source.league import League
from source.math import *
from source.result import Result
import os

# Load all competitions
directory = os.getcwd() + '/input/' + str(2019)        # directory with league fsdb files
league = League('SLO LIGA 2019', 2019, 'SLO')
league.loadCompetitions()
league.getAllPilots()

for pilot in league.Pilots:
    if pilot.Nationality == league.Nationality:
        print(pilot.Name, pilot.finalResult.Points)

print('number of tasks:', league.numberOfTasks)
league.saveResultsToHTML('default.html')