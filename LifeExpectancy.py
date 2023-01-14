#This project is designed to determine a user's life expectancy on different planets, including Jupiter, Mars, Mercury, and Venus. It also calculates whether the user has exceeded the average life expectancy on the planet they have selected.
#Importing random to show application functions without manually entering info. 
#I also added print statements at the bottom of the page to take these random values and return the age on each planet.
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
        self.ageOnMercury = round(self.ageOnEarth / self.mercuryYear)

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

#Print the age of this instanced person (based on random parameters)

print("Life Expectancy outcomes based on a randomized person:")
print("")

# create an instance of the JupiterLifeExpectancy class
jupiterLifeExpectancy = JupiterLifeExpectancy(ageOnEarth)
jupiterLifeExpectancy.jupiterAgeCalc()
jupiterLifeExpectancy.surpassedLifeExpectancy(lifeExpectancyAverage.lifeExpectancyAverage)
print("This person born on Jupiter surpassed their life expectancy by", jupiterLifeExpectancy.differenceInAge,"years")

# create an instance of the MarsLifeExpectancy class
marsLifeExpectancy = MarsLifeExpectancy(ageOnEarth)
marsLifeExpectancy.marsAgeCalc()
marsLifeExpectancy.surpassedLifeExpectancy(lifeExpectancyAverage.lifeExpectancyAverage)
print("This person born on Mars surpassed their life expectancy by", marsLifeExpectancy.differenceInAge,"years")

# create an instance of the MercuryLifeExpectancy class
mercuryLifeExpectancy = MercuryLifeExpectancy(ageOnEarth)
mercuryLifeExpectancy.mercuryAgeCalc()
mercuryLifeExpectancy.surpassedLifeExpectancy(lifeExpectancyAverage.lifeExpectancyAverage)
print("This person born on Mercury surpassed their life expectancy by", mercuryLifeExpectancy.differenceInAge,"years")

# create an instance of the VenusLifeExpectancy class
venusLifeExpectancy = VenusLifeExpectancy(ageOnEarth)
venusLifeExpectancy.venusAgeCalc()
venusLifeExpectancy.surpassedLifeExpectancy(lifeExpectancyAverage.lifeExpectancyAverage)
print("This person born on Venus surpassed their life expectancy by", venusLifeExpectancy.differenceInAge,"years")

print("")

print("Age on Earth:", ageOnEarth)

print("")

print("Age on each planet in Earth years:")

# print the rounded age on each planet in Earth Years
print("Age on Jupiter:", jupiterLifeExpectancy.ageOnJupiter)
print("Age on Mars:", marsLifeExpectancy.ageOnMars)
print("Age on Mercury:", mercuryLifeExpectancy.ageOnMercury)
print("Age on Venus:", venusLifeExpectancy.ageOnVenus)
