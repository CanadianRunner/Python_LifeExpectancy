Python Journal Template 
Directions: Follow the directions for each part of the journal template. Include in your response all the elements listed under the Requirements section. Prompts in the Inspiration section are not required; however, they may help you to fully think through your response.
Remember to review the Touchstone page for entry requirements, examples, and grading specifics.

Name: Sean Keane
Date: 1/13/2023
Final Replit Program Share Link: https://replit.com/join/lalbklquyw-canadianrunner
Complete the following template. Fill out all entries using complete sentences.

 
PART 1: Defining Your Problem

Task
State the problem you are planning to solve.

Requirements
●	Describe the problem you are trying to solve for.
●	Describe any input data you expect to use. 
●	Describe what the program will do to solve the problem. 
●	Describe any outputs or results the program will provide.

Inspiration
When writing your entry below ask yourself the following questions:
●	Why do you want to solve this particular problem?
●	What source(s) of data do you believe you will need? Will the user need to supply that data, or will you get it from an external file or another source?
●	Will you need to interact with the user throughout the program? Will users continually need to enter data in and see something to continue?
●	What are your expected results or what will be the end product? What will you need to tell a user of your program when it is complete?

I would like to create a calculator that will determine a person’s life expectancy on other planets.  I would like to add parameters into the calculation, that would tell the user if they exceeded the average life expectancy on their planet.  The input data will be if the user is born on Earth, if they are human, their sex, and their initial age.  I will need to look up what a year on each planet is equivalent to a year on Earth.  I will output multiple lines to the console (with space between sections for a clearer user experience).  I will show the surpassed life expectancy for four planets, the users age on Earth, and the equivalent age on all four planets.

To show the calculator is functioning correctly I will “Import random” to create a new user on each instance of running the program on Replit.  I will need to create this additional logic so my random user is instantiated on each run.

 
PART 2: Working Through Specific Examples

Task
Write down clear and specific steps to solve a simple version of your problem you identified in Part 1.


Requirements
Complete the three steps below for at least two distinct examples/scenarios.
●	State any necessary input data for your simplified problem. 
●	Write clear and specific steps in English (not Python) detailing what the program will do to solve the problem. 
●	Describe the specific result of your example/scenario.

Inspiration
When writing your entry below ask yourself the following questions:
●	Are there any steps that you don’t fully understand? These are places to spend more time working out the details. Consider adding additional smaller steps in these spots.
●	Remember that a computer program is very literal. Are there any steps that are unclear? Try giving the steps of your example/scenario to a friend or family member to read through and ask you questions about parts they don’t understand. Rewrite these parts as clearly as you can.
●	Are there interesting edge cases for your program? Try to start one of your examples/scenarios with input that matches this edge case. How does it change how your program might work?

This is my first program in Python.  So going in I know I will need to refer to documentation/Sophia lessons to get my program up and running.  I know proper syntax won’t come naturally, but through error handling/patience this application will perfectly manageable.  

I will need to input the age on Earth, if the person was born on Earth, if the person is human, if the person is male or female.  I can then feed this information to into each planets class to determine if the user surpasses the average life expectancy.  I will add or deduct life expectancy based on the users inputs. ie: “This person born on Jupiter surpassed their life expectancy by 49 years.”

A different scenario I’d like to develop for is based on the inputted users Earth age, what the age of the user is in Earth years. ie: Someone born on Earth is 100 years old and would be 53 Mars years old.
 
PART 3: Generalizing Into Pseudocode

Task
Write out the general sequence your program will use, including all specific examples/scenarios you provided in Part 2.

Requirements
●	Write pseudocode for the program in English but refer to Python program elements where they are appropriate. The pseudocode should represent the full functionality of the program, not just a simplified version. Pseudocode is broken down enough that the details of the program are no longer in any paragraph form.  One statement per line is ideal.

Help with writing pseudocode
●	Here are a few links that can help you write pseudocode with examples.  Remember to check out part 3 of the Example Journal Template Submission if you have not already.  Note: everyone will write pseudocode differently.  There is no right or wrong way to write it other than to make sure you write it clearly and in as much detail as you can so that it should be easy to convert it to code later.
○	https://www.geeksforgeeks.org/how-to-write-a-pseudo-code/ 
○	https://www.wikihow.com/Write-Pseudocode 

Inspiration
When writing your entry below ask yourself the following questions:
●	Do you see common program elements and patterns in your specific examples/scenarios in Part 2, like variables, conditionals, functions,  loops, and classes? These should be part of your pseudocode for the general sequence as well.
●	Are there places where the steps for your examples/scenarios in Part 2 diverged? These may be places where errors may occur later in the project. Make note of them.
●	When you are finished with your pseudocode, does it make sense, even to a person that does not know Python? Aim for the clearest description of the steps, as this will make it easier to convert into program code later.
This program calculates the user exceeds the life expectancy of four different planets.  It will solve for Jupiter, Mars, Mercury, and Venus.  It will also calculate the age of the user on each planet in their local years.

#Import Random statement to test/show functioning program (logic to follow)

1.	Create a class called "LifeExpectancyAverage"
2.	Define a method called "init" that takes in three parameters: "bornOnEarth", "humanSpecies", and "sex"
3.	Within the "init" method, create class variables "bornOnEarth", "humanSpecies", "sex", and "lifeExpectancyAverage" and set them equal to the parameters passed in.
4.	Create a method called "calculateLifeExpectancyAverage" that takes in one parameter "initialAge"
5.	Within the "calculateLifeExpectancyAverage" method, create an if statement that checks if "self.bornOnEarth" is true, and if so, add 1 to "initialAge"
6.	Within the "calculateLifeExpectancyAverage" method, create an else statement that subtracts 10 from "initialAge" if "self.bornOnEarth" is false
7.	Within the "calculateLifeExpectancyAverage" method, create an if statement that checks if "self.humanSpecies" is true, and if so, add 1 to "initialAge"
8.	Within the "calculateLifeExpectancyAverage" method, create an else statement that subtracts 5 from "initialAge" if "self.humanSpecies" is false
9.	Within the "calculateLifeExpectancyAverage" method, create an if statement that checks if "self.sex" is "female", and if so, add 7 to "initialAge"
10.	Within the "calculateLifeExpectancyAverage" method, create an else statement that adds 1 to "initialAge" if "self.sex" is not "female"
11.	Within the "calculateLifeExpectancyAverage" method, return "initialAge"
12.	Create a method called "calcExpectedAgePerPlanet" that takes in one parameter "planetNum"
13.	Within the "calcExpectedAgePerPlanet" method, return the value of "self.lifeExpectancyAverage" divided by "planetNum"
14.	Define a class called "JupiterLifeExpectancy"
15.	In the class, define an initializer method that takes in an argument "ageOnEarth"
16.	Inside the initializer method, set the instance variable "ageOnEarth" to the value passed in as an argument
17.	Set the instance variable "ageOnJupiter" to 0
18.	Set the instance variable "jupiterYear" to 11.86
19.	Set the instance variable "surpassedExpect" to 0
20.	Define a method called "jupiterAgeCalc"
21.	Inside the "jupiterAgeCalc" method, set the "ageOnJupiter" instance variable to the result of rounding (ageOnEarth / jupiterYear)
22.	Define a method called "surpassedLifeExpectancy"
23.	Inside the "surpassedLifeExpectancy" method, set the "differenceInAge" instance variable to the result of rounding the absolute value of (LifeExpectancyAverage - ageOnJupiter)
24.	I will do steps 14-23 three more times and utilize the exsisting logic for my other three planets.  The variable that will change is the year on each planet.  For mars I’ll set self.marsYear = 1.88.  For Mercury I will set self.mercuryYear = 0.24.  For Venus I’ll set the self.VenusYear = 0.62.
25.	Here I will create a randomized “person” by importing and using the random method to determine what the persons parameters are equal to.
26.	Set a variable "ageOnEarth" to a random integer between 1 and 100 using the random.randint method
27.	Set a variable "bornOnEarth" to a random boolean value chosen from the list [True, False] using the random.choice method
28.	Set a variable "humanSpecies" to a random boolean value chosen from the list [True, False] using the random.choice method
29.	Set a variable "sex" to a random string value chosen from the list ["male", "female"] using the random.choice method
30.	Create an instance of the LifeExpectancyAverage class, using the variables "bornOnEarth", "humanSpecies", and "sex" as arguments
31.	Print the string "Life Expectancy outcomes based on a randomized person:"
32.	Print an empty line to create a space between the text and the next output.
33.	Next I will create four instances of lifeExpectancy for each planet and print the results.
34.	Create a variable "jupiterLifeExpectancy" and set it equal to an instance of the JupiterLifeExpectancy class, passing in the variable "ageOnEarth"
35.	Call the "jupiterAgeCalc" method on the "jupiterLifeExpectancy" variable
36.	Call the "surpassedLifeExpectancy" method on the "jupiterLifeExpectancy" variable, passing in the "lifeExpectancyAverage.lifeExpectancyAverage" variable
37.	Print a message including the text "This person born on Jupiter surpassed their life expectancy by" and the value of the "differenceInAge" attribute of the "jupiterLifeExpectancy" variable followed by the text "years"
38.	I will reuse this logic and apply it to all four planets and print their result. I will need to call on the specific AgeCalc() based on the planet I need to calculate.
39.	Print an empty line to create a space between the text and the next output.
40.	Print the text "Age on Earth:" followed by the variable ageOnEarth
41.	Print an empty line to create a space between the text and the next output.
42.	Print the text "Age on each planet in Earth years:"
43.	Print the text "Age on Jupiter:" followed by the attribute ageOnJupiter from the instance of JupiterLifeExpectancy
44.	Print the text "Age on Mars:" followed by the attribute ageOnMars from the instance of MarsLifeExpectancy
45.	Print the text "Age on Mercury:" followed by the attribute ageOnMercury from the instance of MercuryLifeExpectancy
46.	Print the text "Age on Venus:" followed by the attribute ageOnVenus from the instance of VenusLifeExpectancy




 
PART 4: Testing Your Program

Task
While writing and testing your program code, describe your tests, record any errors, and state your approach to fixing the errors.

Requirements
●	For at least one of your test cases, describe how your choices for the test helped you understand whether the program was running correctly or not.
For each error that occurs while writing and testing your code:
●	Record the details of the error from Replit. A screenshot or copy-and-paste of the text into the journal entry is acceptable.
●	Describe what you attempted in order to fix the error. Clearly identify what approach was the one that worked.

Inspiration
When writing your entry below ask yourself the following questions:
●	Have you tested edge cases and special cases for the inputs of your program code? Often these unexpected values can cause errors in the operation of your program.
●	Have you tested opportunities for user error? If a user is asked to provide an input, what happens when they give the wrong type of input, like a letter instead of a number, or vice versa?
●	Did the outcome look the way you expected? Was it formatted correctly? 
●	Does your output align with the solution to the problem you coded for?
Test Case 1:
1.	I will create an instance of the LifeExpectancyAverage class with the following values: bornOnEarth = True, humanSpecies = True, sex = "female"
2.	I will pass in an age of 20 for the ageOnEarth variable
3.	I will call the calcExpectedAgePerPlanet function with the value of 2 (Jupiter)
4.	I expect the output to be round((20 + 1 + 1 + 7) / 2) = 14
This was a good first test because it “gut  checked” whether my logic would work throughout the program.  It picked at the math I was hoping to solve for and successfully rounded the result as intended. Thankfully the test passed.
Test Case 2:
1.	I will create an instance of the LifeExpectancyAverage class with the following values: bornOnEarth = False, humanSpecies = False, sex = "male"
2.	I will pass in an age of 50 for the ageOnEarth variable
3.	I will call the calcExpectedAgePerPlanet function with the value of 0.24 (Mercury)
4.	I expect the output to be round((50 - 10 - 5 + 1) / 0.24) = 208
Test Case 3:
1.	I will create an instance of the JupiterLifeExpectancy class with the ageOnEarth = 75
2.	I will call the jupiterAgeCalc function
3.	I will call the surpassedLifeExpectancy function with the lifeExpectancyAverage object from Test Case 1
4.	I expect the output of the differenceInAge attribute to be round(75 / 11.86 - 14) = 4
Test Case 4:
1.	I will create an instance of the MarsLifeExpectancy class with the ageOnEarth = 40
2.	I will call the marsAgeCalc function
3.	I will call the surpassedLifeExpectancy function with the lifeExpectancyAverage object from Test Case 2
4.	I expect the output of the differenceInAge attribute to be round(40 / 1.88 - 208) = -168
Test Case 5:
1.	I will create an instance of the VenusLifeExpectancy class with the ageOnEarth = 60
2.	I will call the venusAgeCalc function
3.	I will call the surpassedLifeExpectancy function with the lifeExpectancyAverage object from Test Case 1
4.	I expect the output of the differenceInAge attribute to be round(60 / 0.62 - 14) = -9
Test Case 6:
1.	I will create an instance of the MercuryLifeExpectancy class with the ageOnEarth = 90
2.	I will call the mercuryAgeCalc function
3.	I will call the surpassedLifeExpectancy function with the lifeExpectancyAverage object from Test Case 2
4.	I expect the output of the differenceInAge attribute to be round(90 / 0.24 - 208) = 271
Test Case 7:
1.	I will pass in an empty list for the input list
2.	I will expect the program to return an error message "please provide valid input"

All of my tests are now passing.  I had a number of syntax errors during development (a couple referenced in the images below).  I also had a few variables I mistyped ie: “mercury vs merury”.
When I console indicated an error I read through the entire error message.  Then I check to see what line the error occurred on and jumped to that area of the file.  Sometimes the error was simple like syntax.  Other times it required a more nuanced approach with a “Traceback error” occurring a few times.  My scope was off and I needed to reshuffle my logic because with my past structure the variable was not defined.  

I referenced documentation multiple times to address my errors and discovered helpful solutions.  Many times the console clearly identify the line the error occurred on and I was able to quickly fix the issue on Replit.


    


PART 5: Commenting Your Program

Task
Submit your full program code, including thorough comments describing what each portion of the program should do when working correctly.

Requirements
●	The purpose of the program and each of its parts should be clear to a reader that does not know the Python programming language. 

Inspiration
When writing your entry, you are encouraged to consider the following:
●	Is each section or sub-section of your code commented to describe what the code is doing?
●	Give your code with comments to a friend or family member to review. Add additional comments to spots that confuse them to make it clearer.

#This project is designed to determine a user's life expectancy on different planets, including Jupiter, Mars, Mercury, and Venus. It also calculates whether the user has exceeded the average life expectancy on the planet they have selected.
#Importing random to show application functions without manually entering info. 
#I also added print statements at the bottom of the page to take these random values and return the age on each planet.
import random
# The LifeExpectancyAverage class calculates the average life expectancy based on the input values of bornOnEarth, humanSpecies, and sex
class LifeExpectancyAverage:
    # The constructor initializes the variables and calls the calculateLifeExpectancyAverage function
    def __init__(self, bornOnEarth, humanSpecies, sex):
        self.bornOnEarth = bornOnEarth
        self.humanSpecies = humanSpecies
        self.sex = sex
        self.lifeExpectancyAverage = self.calculateLifeExpectancyAverage(71)

    # The calculateLifeExpectancyAverage function takes in an initialAge value and calculates the average life expectancy based on the user inputs
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

    # The calcExpectedAgePerPlanet function takes in a planetNum variable and calculates the expected age on that planet
    def calcExpectedAgePerPlanet(self, planetNum):
        return  self.lifeExpectancyAverage / planetNum


class JupiterLifeExpectancy:
    # The constructor initializes the ageOnEarth, ageOnJupiter, jupiterYear, and surpassedExpect variables
    def __init__(self, ageOnEarth):
        self.ageOnEarth = ageOnEarth
        self.ageOnJupiter = 0
        self.jupiterYear = 11.86
        self.surpassedExpect = 0

    # The jupiterAgeCalc function calculates the age of the person on Jupiter in Earth years
    def jupiterAgeCalc (self):
        self.ageOnJupiter = round(self.ageOnEarth / self.jupiterYear)

    # The surpassedLifeExpectancy function takes in a LifeExpectancyAverage object and calculates the difference between that and the ageOnJupiter
    def surpassedLifeExpectancy(self, LifeExpectancyAverage):
        self.differenceInAge = round(abs(LifeExpectancyAverage - self.ageOnJupiter))


class MarsLifeExpectancy:
    # The constructor initializes the ageOnEarth, ageOnMars, marsYear, and surpassedExpect variables
    def __init__ (self, ageOnEarth):
        self.ageOnEarth = ageOnEarth
        self.ageOnMars = 0
        self.marsYear = 1.88
        self.surpassedExpect = 0

    # The marsAgeCalc function calculates the age of the person on Mars in Earth years
    def marsAgeCalc (self):
        self.ageOnMars = round(self.ageOnEarth / self.marsYear)

    # The surpassedLifeExpectancy function takes in a LifeExpectancyAverage object and calculates the difference between that and the ageOnMars
    def surpassedLifeExpectancy(self, LifeExpectancyAverage):
        self.differenceInAge = round(abs(LifeExpectancyAverage - self.ageOnMars))


class MercuryLifeExpectancy:
    # The constructor initializes the ageOnEarth, ageOnMercury, mercuryYear, and surpassedExpect variables
    def __init__ (self, ageOnEarth):
        self.ageOnEarth = ageOnEarth
        self.ageOnMercury = 0
        self.mercuryYear = 0.24
        self.surpassedExpect = 0

    # The mercuryAgeCalc function calculates the age of the person on Mercury in Earth Years
    def mercuryAgeCalc (self):
        self.ageOnMercury = round(self.ageOnEarth / self.mercuryYear)

    # The surpassedLifeExpectancy function takes in a LifeExpectancyAverage object and calculates the difference between that and the ageOnMercury
    def surpassedLifeExpectancy(self, LifeExpectancyAverage):
        self.differenceInAge = round(abs(LifeExpectancyAverage - self.ageOnMercury))


class VenusLifeExpectancy:
    # The constructor initializes the ageOnEarth, ageOnVenus, venusYear, and surpassedExpect variables
    def __init__ (self, ageOnEarth):
        self.ageOnEarth = ageOnEarth
        self.ageOnVenus = 0
        self.venusYear = 0.62
        self.surpassedExpect = 0

    # The venusAgeCalc function calculates the age of the person on Venus in Earth years
    def venusAgeCalc (self):
        self.ageOnVenus = round(self.ageOnEarth / self.venusYear)

    # The surpassedLifeExpectancy function takes in a LifeExpectancyAverage object and calculates the difference between that and the ageOnVenus
    def surpassedLifeExpectancy(self, LifeExpectancyAverage):
        self.differenceInAge = round(abs(LifeExpectancyAverage - self.ageOnVenus))


# I am instantiating a new random person in this code block.  This allows the user to test the application without any inputs.  Simply run the app and it will create a new person with the logic below
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
# Print an empty line to create a space between the text and the next output.
print("")

# create an instance of the JupiterLifeExpectancy class
jupiterLifeExpectancy = JupiterLifeExpectancy(ageOnEarth)
#Calculate the age on Jupiter
jupiterLifeExpectancy.jupiterAgeCalc()
#Calculate the difference between life expectancy and age on Jupiter
jupiterLifeExpectancy.surpassedLifeExpectancy(lifeExpectancyAverage.lifeExpectancyAverage)
#Print out the difference in years.
print("This person born on Jupiter surpassed their life expectancy by", jupiterLifeExpectancy.differenceInAge,"years")
# create an instance of the MarsLifeExpectancy class
marsLifeExpectancy = MarsLifeExpectancy(ageOnEarth)
#Calculate the age on Mars
marsLifeExpectancy.marsAgeCalc()
#Calculate the difference in life expectancy and age on Mars
marsLifeExpectancy.surpassedLifeExpectancy(lifeExpectancyAverage.lifeExpectancyAverage)
#Print out the difference in years
print("This person born on Mars surpassed their life expectancy by", marsLifeExpectancy.differenceInAge,"years")

# create an instance of the MercuryLifeExpectancy class
mercuryLifeExpectancy = MercuryLifeExpectancy(ageOnEarth)
#Calculate the age on Mercury
mercuryLifeExpectancy.mercuryAgeCalc()
#Calculate the difference in life expectancy and age on Mercury
mercuryLifeExpectancy.surpassedLifeExpectancy(lifeExpectancyAverage.lifeExpectancyAverage)
#Print out the difference in years
print("This person born on Mercury surpassed their life expectancy by", mercuryLifeExpectancy.differenceInAge,"years")

# create an instance of the VenusLifeExpectancy class
venusLifeExpectancy = VenusLifeExpectancy(ageOnEarth)
#Calculate the age on Venus
venusLifeExpectancy.venusAgeCalc()
#Calculate the difference in life expectancy and age on Venus
venusLifeExpectancy.surpassedLifeExpectancy(lifeExpectancyAverage.lifeExpectancyAverage)
#Print out the difference in years
print("This person born on Venus surpassed their life expectancy by", venusLifeExpectancy.differenceInAge,"years")

#Empy string for spacing (better user experience)
print("")

#Printing a string and the value of the users age on Earth
print("Age on Earth:", ageOnEarth)

#Printing a space for console styling
print("")

#String explaining to the user the values below
print("Age on each planet in Earth years:")


# These print statements provide a string and the rounded age on each planet in Earth Years
print("Age on Jupiter:", jupiterLifeExpectancy.ageOnJupiter)
print("Age on Mars:", marsLifeExpectancy.ageOnMars)
print("Age on Mercury:", mercuryLifeExpectancy.ageOnMercury)
print("Age on Venus:", venusLifeExpectancy.ageOnVenus)


PART 6: Your Completed Program

Task
Provide the Replit link to your full program code.

Requirements
●	The program must work correctly with all the comments included in the program.

Inspiration
●	Check before submitting your touchstone that your final version of the program is running successfully.

https://replit.com/@CanadianRunner/SophiaPytonTouchStone#main.py

