# ALGO DESCRIPTION
# Parse backpacks into groups of 3 in chronological order
# Find common character between all three backpacks of group
# Calculate priority and add to total
# Output total

dataFile = open("data.txt", "r")

backpacks = dataFile.readlines()

# output var
totalPriority = 0

def findMutualCharacter(s1, s2, s3):
    for char in s1:
        if char in s2:
            if char in s3:
                return char

for groupIndex in range(int(len(backpacks)/3)):
    groupBackpacks = [backpacks[groupIndex*3].rstrip(), backpacks[(groupIndex*3)+1].rstrip(), backpacks[(groupIndex*3)+2].rstrip()]

    print(groupBackpacks)

    mutual = findMutualCharacter(groupBackpacks[0], groupBackpacks[1], groupBackpacks[2])

    print(mutual)

    if mutual == str(mutual):
        if mutual == mutual.lower():
            totalPriority += int(ord(mutual)-96)
        elif mutual == mutual.upper():
            totalPriority += int(ord(mutual)-38)
    else:
        print("No mutual on "+str(groupIndex))

print(totalPriority)