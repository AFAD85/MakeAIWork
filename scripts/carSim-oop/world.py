

import time as tm
from car import Car


class World:

  # Constructor:
  def __init__(self):
    self.t = 0.0
    self.dT = 0.1
    self.running = True
    self.carTesla = Car("Tesla", 800.0, 600.0)
    self.carBMW = Car("BMW", 600.0, 800.0)

  def bang(self):
    while self.running:
      self.t += self.dT
      self.carTesla.move(self.dT)
      self.carBMW.move(self.dT)
      if self.carTesla.x > 100:
        print ("Tesla winnar!")
        self.running = False
      if self.carBMW.x > 100:
        print ("BMW HAT ES GESHAFT!")
        self.running = False
      print("Time: ", self.t)
      tm.sleep(self.dT)

  def stop(self):
    self.running = False