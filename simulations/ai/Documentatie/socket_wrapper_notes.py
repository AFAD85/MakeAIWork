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

import socket as sc
import json as js
# interpreter om met JSON (javascript over network) data om te kunnen gaan. Dit zijn stukjes data binnen {} tekens die afhankelijk van de context betekenis krijgen. Het gaat hier om de meest efficiente manier van data versturen als je de data niet comprimeert/abstracter maakt. (maar zou het niet sneller gaan als je een interpreter op lager niveau bouwt, die dan bijvoorbeeld weet dat A of D betekent stuur bijdraaien naar links of rechts, niet relevant of binnen de scope van deze opleiding, maar leuk om te weten... i guess). 


address = 'localhost', 50012
socketType = sc.AF_INET, sc.SOCK_STREAM
maxNrOfConnectionRequests = 5
maxMessageLength = 2048

class SocketWrapper:
# 
    def __init__ (self, clientSocket):
        self.clientSocket = clientSocket

    def send (self, anObject):
        buffer = bytes (f'{js.dumps (anObject):<{maxMessageLength}}', 'ascii')

        totalNrOfSentBytes = 0

        while totalNrOfSentBytes < maxMessageLength:
            nrOfSentBytes = self.clientSocket.send (buffer [totalNrOfSentBytes:])

            if not nrOfSentBytes:
                self.raiseConnectionError ()
                #wordt er niets verstuurd dan wordt er een connection error weergegeven
            totalNrOfSentBytes += nrOfSentBytes

    def recv (self):
        totalNrOfReceivedBytes = 0
        receivedChunks = []

        while totalNrOfReceivedBytes < maxMessageLength:
            receivedChunk = self.clientSocket.recv (maxMessageLength - totalNrOfReceivedBytes)

            if not receivedChunk:
                self.raiseConnectionError ()

            receivedChunks.append (receivedChunk)
            totalNrOfReceivedBytes += len (receivedChunk)
            
        return js.loads (b''.join (receivedChunks) .decode ('ascii'))

    def raiseConnectionError (self):
        raise RuntimeError ('Socket connection broken')
