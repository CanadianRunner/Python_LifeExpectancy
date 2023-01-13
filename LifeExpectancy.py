#File One
import math

class LifeExpectancyAverage:
  def __init__(self, bornOnEarth, humanSpecies, sex):
    self.bornOnEarth = bornOnEarth
    self.humanSpecies = humanSpecies
    self.sex = sex
    self.lifeExpectancyAverage = self.calculateLifeExpectancyAverage(71)
  
  def calculateLifeExpectancyAverage(self, initialAge):
    if self.bornOnEarth:
      initialAge += 1
    else:
      initialAge -= 10
    if self.humanSpecies:
      initialAge += 1
    else:
      initialAge -= 5
    if self.sex == "female":
      initialAge += 7
    else:
      initialAge += 1
    return initialAge
  
  def calcExpectedAgePerPlanet(self, planetNum):
    return math.round(self.lifeExpectancyAverage / planetNum)

#File 2

def jupiterAgeCalc(self):
    self.ageOnJupiter = round(self.ageOnEarth / self.jupiterYear)

def surpassedLifeExpectancy(self, LifeExpectancyAverage):
    self.differenceInAge = round(abs(LifeExpectancyAverage - self.ageOnJupiter))

#File 3

def marsAgeCalc(self):
    self.ageOnMars = round(self.ageOnEarth / self.marsYear)
    
def surpassedLifeExpectancy(self, LifeExpectancyAverage):
    self.differenceInAge = round(abs(LifeExpectancyAverage - self.ageOnMars))

#File 4

def mercuryAgeCalc(self):
    self.ageOnMercury = round(self.ageOnEarth / self.mercuryYear)

def surpassedLifeExpectancy(self, LifeExpectancyAverage):
    self.differenceInAge = round(abs(LifeExpectancyAverage - self.ageOnMercury))

#File 5


