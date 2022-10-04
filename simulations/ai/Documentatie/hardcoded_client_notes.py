'''
====== Legal notices

Copyright (C) 2013 - 2021 GEATEC engineering

This program is free software.
You can use, redistribute and/or modify it, but only under the terms stated in the QQuickLicense.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY, without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the QQuickLicense for details.

The QQuickLicense can be accessed at: http://www.qquick.org/license.html

__________________________________________________________________________


 THIS PROGRAM IS FUNDAMENTALLY UNSUITABLE FOR CONTROLLING REAL SYSTEMS !!

__________________________________________________________________________

It is meant for training purposes only.

Removing this header ends your license.
'''

import time as tm
# deze library kan vanaf een vast punt de delta tijd meten (dus met gelijke stappen en dus voorspelbaar)



import traceback as tb
# zoals ik deze lees zou het voor het bijhouden van de oorsprong van aanroepen?? Helaas wordt deze in dit bestand in elk geval niet meer aangeroepen hij zou dus weg kunnen... Maar ik heb niet de massief stale balen om dat uit te proberen... dus ik laat em lekker staan



import math as mt
# de clue zit in de naam, wiskundige functies constanten enzovoorts, kan ook via numpy maar waarom makkelijk doen als het ook moeilijk kan.


import sys as ss
# super toffe library waarmee je veel dingen kan oproepen zoals bijvoorbeeld de maximale bestandsgrootte die je systeem kan gebruiken voor een integer (sys.maxsize). Wij gebruiken em om te kijken waar python staat... 


import os
# heeft te maken met het wegschrijven van bestanden op de juiste plek (kan bijv met os.path de directory waarin je werkt oproepen).


import socket as sc
# laag level networking interface (uuuhghh......) 
# je hebt een client en server (s. voor server commandos c. voor client commandos). Als ik het goed snap kan alles vanaf de client worden aangestuurd... maaruh nog ff doorzoeken
# Je zet als het ware de server aan (s.listen en dan; while true : c, addr = s.accept()  ) en dan kan je commandos sturen vanaf je eigen addr (adres) c.send, c.close en vast nog veel meer keigave dingen.
#  



ss.path +=  [os.path.abspath (relPath) for relPath in  ('..',)] 
# dusch als ik het goed snap is dit gewoon een manier om de directory waarin dit bestand staat en de bovenliggende te gebruiken om te zoeken naar de volgende twee bestanden (modules)
import socket_wrapper as sw
# verwijst dus naar het bestand socket_wrapper, niet een library

import parameters as pm

class HardcodedClient:
    def __init__ (self):
        self.steeringAngle = 0

        with open (pm.sampleFileName, 'w') as self.sampleFile:
            with sc.socket (*sw.socketType) as self.clientSocket:
                self.clientSocket.connect (sw.address)
                self.socketWrapper = sw.SocketWrapper (self.clientSocket)
                self.halfApertureAngle = False

                while True:
                    self.input ()
                    self.sweep ()
                    self.output ()
                    self.logTraining ()
                    tm.sleep (0.02)
# deze functie 
    def input (self):
        sensors = self.socketWrapper.recv ()

        if not self.halfApertureAngle:
            self.halfApertureAngle = sensors ['halfApertureAngle']
            self.sectorAngle = 2 * self.halfApertureAngle / pm.lidarInputDim
            self.halfMiddleApertureAngle = sensors ['halfMiddleApertureAngle']
            
        if 'lidarDistances' in sensors:
            self.lidarDistances = sensors ['lidarDistances']
        else:
            self.sonarDistances = sensors ['sonarDistances']
# deze functie bevat de werking van de Lidar sensor, met name hoe deze vanuit de sensor data de stuurhoek aanstuurt
# finity staat in parameters en staat standaard op 20 geeft aan dat de meet afstand alleen wordt doorgegeven als deze onder de 20 valt.
# halfapatureangle staat in visualisations onder de scanner class en wordt verkregen door de apature angle met een floor deling door 2 te delen (lekker duidelijk!) hier komt de 22% van de sonar vandaan (45 graden delen door 2 en dan alles achter de komma weghalen).
# 

    def lidarSweep (self):
        nearestObstacleDistance = pm.finity
        nearestObstacleAngle = 0
        
        nextObstacleDistance = pm.finity
        nextObstacleAngle = 0

        for lidarAngle in range (-self.halfApertureAngle, self.halfApertureAngle):
            lidarDistance = self.lidarDistances [lidarAngle]
            
            if lidarDistance < nearestObstacleDistance:
                nextObstacleDistance =  nearestObstacleDistance
                nextObstacleAngle = nearestObstacleAngle
                
                nearestObstacleDistance = lidarDistance 
                nearestObstacleAngle = lidarAngle

            elif lidarDistance < nextObstacleDistance:
                nextObstacleDistance = lidarDistance
                nextObstacleAngle = lidarAngle
           
        targetObstacleDistance = (nearestObstacleDistance + nextObstacleDistance) / 2

        self.steeringAngle = (nearestObstacleAngle + nextObstacleAngle) / 2
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)
# deze functie 
    def sonarSweep (self):
        obstacleDistances = [pm.finity for sectorIndex in range (3)]
        obstacleAngles = [0 for sectorIndex in range (3)]
        
        for sectorIndex in (-1, 0, 1):
            sonarDistance = self.sonarDistances [sectorIndex]
            sonarAngle = 2 * self.halfMiddleApertureAngle * sectorIndex
            
            if sonarDistance < obstacleDistances [sectorIndex]:
                obstacleDistances [sectorIndex] = sonarDistance
                obstacleAngles [sectorIndex] = sonarAngle

        if obstacleDistances [-1] > obstacleDistances [0]:
            leftIndex = -1
        else:
            leftIndex = 0
           
        if obstacleDistances [1] > obstacleDistances [0]:
            rightIndex = 1
        else:
            rightIndex = 0
           
        self.steeringAngle = (obstacleAngles [leftIndex] + obstacleAngles [rightIndex]) / 2
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)
# deze functie 
    def sweep (self):
        if hasattr (self, 'lidarDistances'):
            self.lidarSweep ()
        else:
            self.sonarSweep ()
# deze functie 
    def output (self):
        actuators = {
            'steeringAngle': self.steeringAngle,
            'targetVelocity': self.targetVelocity
        }

        self.socketWrapper.send (actuators)
# deze functie 
    def logLidarTraining (self):
        sample = [pm.finity for entryIndex in range (pm.lidarInputDim + 1)]

        for lidarAngle in range (-self.halfApertureAngle, self.halfApertureAngle):
            sectorIndex = round (lidarAngle / self.sectorAngle)
            sample [sectorIndex] = min (sample [sectorIndex], self.lidarDistances [lidarAngle])

        sample [-1] = self.steeringAngle
        print (*sample, file = self.sampleFile)
# deze functie 
    def logSonarTraining (self):
        sample = [pm.finity for entryIndex in range (pm.sonarInputDim + 1)]

        for entryIndex, sectorIndex in ((2, -1), (0, 0), (1, 1)):
            sample [entryIndex] = self.sonarDistances [sectorIndex]

        sample [-1] = self.steeringAngle
        print (*sample, file = self.sampleFile)
# deze functie 
    def logTraining (self):
        if hasattr (self, 'lidarDistances'):
            self.logLidarTraining ()
        else:
            self.logSonarTraining ()

HardcodedClient ()
