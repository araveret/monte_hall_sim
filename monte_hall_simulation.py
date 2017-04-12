s# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:15:03 2016

@author: araveret
"""

###############################################################################
############################# Intro to Python #################################
###############################################################################

# Expressions evaludate to a value

# Numeric
3
3 + 4
4 - 2
2 * 6
6 / 3

# String
A                                   
'A'
'A' + 'B'                          

# Variables
A = 'A'
B = 'The dog ran across the park'
C = '!'                               
B + C 

B[0]
B[0:3]
B[3:]

D = A + B[3:] + C

# Lists
list_A = [1,2,3,4,5]
list_B = [2,4,5]

list_A[0]
list_A[:3]
list_B.append(7)

list_A + list_B
(list_A + list_B).count(5)
list(set(list_A + list_B))

list_C = []

for item in list_A:
    if item in list_B:
        x = 1
    else:
        list_C.append(item)
        


# Truth statements
1 == 2
1 != 2
1 < 2
1 <= 2

# if statements 
x=0
if x==0:
    print('Hurray!')

# for loops
x=[2,3,4,5,6]
for item in x:
    if item==4 or item==6:
        print(item)

# while statements
n=0
while n < len(x):
    if x[n] in [4,6]:
        print(x[n])
    n+=1
    
n=0
while n < len(x):
    if x[n] in [4,6]:
        x.pop(n)
    n+=1
    

#Built in functions
min([1,2,3,4])
max([1,2,3,4])
sum([1,2,3,4])
len([1,2,3,4])
[1,2,3,4].count(3)
[1,2,3,4].append(5)

#Importing a library
from math import pi
from random import randint

# Expressions can use function call notation
def add_5(a_list):
    a_list.append(5)

x=[1,2,3,4]
add_5(x)

def dice_roll():
    print(randint(1,6))

dice_roll()

all_rolls=[]
def dice_roll():
    all_rolls.append(randint(1,6))
dice_roll()



###############################################################################
###################### Monte Hall Simulation Lesson ###########################
###############################################################################


# Import a function called 'randint' from the library 'random.'




# Define a function called 'game_show' to simulate one game. Remember anything
# after this line of code should be indented to keep it part of the function.



    
# Set the scene by creating a string of numbers 1-3, each number representing 
# a door. Call this string 'doors.' 



    
# Create two empty strings called 'doorwithcar' and 'doorswithgoats', which 
# will be randomly assigned with door numbers. These door assignments will 
# represent information only known to the game show host.



    
# Select a random number called 'number' between 1-3 using randint, which will 
# be used to identify which door contains the car, and which remaining doors 
# will contain the goats.




# Add the randomly generated number to 'doorwithcar' using the append function




# Create an if statement to remaining numbers to 'doorswithgoats' using the 
# append function (ex. if 'number' is 2, we want to add 1,3)




# Create a second set of variables representing doors from the perspective of 
# the game show player. The variable 'firstchoice' will represent the first 
# door selected by the player. The variable 'remainingdoors' will represent
# the doors that were not selected by the player. The variable 'openeddoor' 
# will respresent the door that the game show host decided to open. And the 
# varaible 'secondchoice' will represent the door that the player decides to
# switch to. For now, set them all equal to empty lists.




# Select a random number called 'number2' between 1-3 using randint, which will 
# be used to identify which door is first selected by the player. Append that 
# number to the 'firstchoice' list. Use an if statemetn to append the remaining
# door numbers to the 'remainingdoors' list.




# Next we will need to choose a remaining door to be opened. This door cannot
# be the door first selected by the player, or the door containing the car.
# Create a for loop with a nested if statement to identify an item in 
# 'doorswithgoats' that is also in 'remainingdoors'. Define the 'openeddoor'
# list to equal a list with only this item in it.



    
# Next we will need to simulate the player switching to the remaining door. 
# This is one of the doors in 'remainingdoors' but must not be the one that was
# opened. Create an if statement to check if the the first number in the 
# remaining doors list is equal to the opened door. If so, append the second
# remaining door to the list 'secondchoice'. Else, add the first remaining door
# to 'secondchoice.'



        
# Next we will need to check to see if the player won the game, and save the 
# game outcome. Create an if statement to check if 'secondchoice' is equal to 
# 'doorwithcar.' If so, append 'Win' to a list called 'game_outcomes.' Else, 
# append 'Loss' to 'game_outcomes.'
    
    
    

# This is the end of the function 'game_show.' Do not indent anything after 
# this line, unless it is part of a new function or loop.

# Create a list called 'game_outcomes'




# Create a while loop that runs 'game_show' 10,000 times. Do not forget to set
# n = 0 before the loop and have n += 1 inside the loop.



    
# Print a string that says 'Player wins X% of the time.' where X is a 
# calculated value counting the percent of 'Wins' in 'game_outcomes.'





###############################################################################
##################### Monte Hall Simulation Solution ##########################
###############################################################################


from random import randint

def game_show():
    doors = [1,2,3]    
    doorwithcar = []
    doorswithgoats = []
    
    number = randint(1,3)

    doorwithcar.append(number)

    if number == 1:
        doorswithgoats.append(2)
        doorswithgoats.append(3)
    elif number == 2:
        doorswithgoats.append(1)
        doorswithgoats.append(3)
    else:
        doorswithgoats.append(1)
        doorswithgoats.append(2)

    firstchoice = []
    remainingdoors = []
    openeddoor = []
    secondchoice = []

    number2 = randint(1,3)
    firstchoice.append(number2)
    
    if number2 == 1:
        remainingdoors.append(2)
        remainingdoors.append(3)
    elif number2 == 2:
        remainingdoors.append(1)
        remainingdoors.append(3)
    else:
        remainingdoors.append(1)
        remainingdoors.append(2)

    for item in doorswithgoats:
        if item in remainingdoors:
            openeddoor = [item]

    if openeddoor[0] == remainingdoors[0]:
        secondchoice.append(remainingdoors[1])
    else:
        secondchoice.append(remainingdoors[0])
        
    if secondchoice == doorwithcar:
        game_outcomes.append('Win')
    else:
        game_outcomes.append('Loss')
         

game_outcomes = []

n = 0
while n < 10000:
    game_show()
    n+=1

print('Player wins '+ str(game_outcomes.count('Win')/100) + '% of the time.')
