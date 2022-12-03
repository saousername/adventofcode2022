# ALGO DESCRIPTION
# Parse all backpacks from data.txt
# Loop through backpacks and split into compartment 1 and 2
# Find common characters (case-sensitive)
# Check common character's importance rating and add it to a sum variable
# Next backpack
# At end of loop, print out the sum total

dataFile = open("data.txt", "r")

backpacks = dataFile.readlines()

# output var
totalPriority = 0

def findMutualCharacter(s1, s2):
    for char in s1:
        if char in s2:
            return char

for backpack in backpacks:
    # remove \n from lines
    backpack = backpack.rstrip()

    compartmentOne = backpack[0:int(len(backpack)/2)]
    compartmentTwo = backpack[int(len(backpack)/2):len(backpack)]

    mutual = findMutualCharacter(compartmentOne, compartmentTwo)

    if mutual == mutual.lower():
        totalPriority += int(ord(mutual)-96)
    elif mutual == mutual.upper():
        totalPriority += int(ord(mutual)-38)

print(totalPriority)