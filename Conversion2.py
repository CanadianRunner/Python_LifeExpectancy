import random

class LifeExpectancyAverage:
    def __init__(self, bornOnEarth, humanSpecies, sex):
        self.bornOnEarth = bornOnEarth
        self.humanSpecies = humanSpecies
        self.sex = sex
        self.lifeExpectancyAverage = self.calculateLifeExpectancyAverage(71)

    def calculateLifeExpectancyAverage(self, initialAge):
        if self.bornOnEarth is True:
            initialAge += 1
        else:
            initialAge -= 10

        if self.humanSpecies == True:
            initialAge += 1
        else:
            initialAge -= 5

        if self.sex == "female":
            initialAge += 7
        else:
            initialAge += 1

        return initialAge

    def calcExpectedAgePerPlanet(self, planetNum):
        return  self.lifeExpectancyAverage / planetNum


class JupiterLifeExpectancy:
    def __init__(self, ageOnEarth):
        self.ageOnEarth = ageOnEarth
        self.ageOnJupiter = 0
        self.jupiterYear = 11.86
        self.surpassedExpect = 0

    def jupiterAgeCalc (self):
        self.ageOnJupiter = round(self.ageOnEarth / self.jupiterYear)

    def surpassedLifeExpectancy(self, LifeExpectancyAverage):
        self.differenceInAge = round(abs(LifeExpectancyAverage - self.ageOnJupiter))


class MarsLifeExpectancy:
    def __init__ (self, ageOnEarth):
        self.ageOnEarth = ageOnEarth
        self.ageOnMars = 0
        self.marsYear = 1.88
        self.surpassedExpect = 0

    def marsAgeCalc (self):
        self.ageOnMars = round(self.ageOnEarth / self.marsYear)

    def surpassedLifeExpectancy(self, LifeExpectancyAverage):
        self.differenceInAge = round(abs(LifeExpectancyAverage - self.ageOnMars))


class MercuryLifeExpectancy:
    def __init__ (self, ageOnEarth):
        self.ageOnEarth = ageOnEarth
        self.ageOnMercury = 0
        self.mercuryYear = 0.24
        self.surpassedExpect = 0

    def mercuryAgeCalc (self):
        self.ageOnMercury = round(self.ageOnEarth / self.meruryYear)

    def surpassedLifeExpectancy(self, LifeExpectancyAverage):
        self.differenceInAge = round(abs(LifeExpectancyAverage - self.ageOnMercury))


class VenusLifeExpectancy:
    def __init__ (self, ageOnEarth):
        self.ageOnEarth = ageOnEarth
        self.ageOnVenus = 0
        self.venusYear = 0.62
        self.surpassedExpect = 0

    def venusAgeCalc (self):
        self.ageOnVenus = round(self.ageOnEarth / self.venusYear)

    def surpassedLifeExpectancy(self, LifeExpectancyAverage):
        self.differenceInAge = round(abs(LifeExpectancyAverage - self.ageOnVenus))


# create a random age on Earth
ageOnEarth = random.randint(1, 100)

# create a random value for whether the person was born on Earth
bornOnEarth = random.choice([True, False])

# create a random value for whether the person is human
humanSpecies = random.choice([True, False])

# create a random value for the person's sex
sex = random.choice(["male", "female"])

# create an instance of the LifeExpectancyAverage class
lifeExpectancyAverage = LifeExpectancyAverage(bornOnEarth, humanSpecies, sex)

# create an instance of the JupiterLifeExpectancy class
jupiterLifeExpectancy = JupiterLifeExpectancy(ageOnEarth)
jupiterLifeExpectancy.jupiterAgeCalc()

# create an instance of the MarsLifeExpectancy class
marsLifeExpectancy = MarsLifeExpectancy(ageOnEarth)
marsLifeExpectancy.marsAgeCalc()

# create an instance of the MercuryLifeExpectancy class
mercuryLifeExpectancy = MercuryLifeExpectancy(ageOnEarth)
mercuryLifeExpectancy.mercuryAgeCalc()

# create an instance of the VenusLifeExpectancy class
venusLifeExpectancy = VenusLifeExpectancy(ageOnEarth)
venusLifeExpectancy.venusAgeCalc()


# print the age on each planet
print("Age on Earth:", ageOnEarth)
print("Age on Jupiter:", jupiterLifeExpectancy.ageOnJupiter)
print("Age on Mars:", marsLifeExpectancy.ageOnMars)
print("Age on Mercury:", mercuryLifeExpectancy.ageOnMercury)
print("Age on Venus:", venusLifeExpectancy.ageOnVenus)
