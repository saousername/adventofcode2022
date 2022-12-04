# ALGO EXPLAINED
# Load in data and parse into pairs
# Loop through each pair and see if the first number of pair 2 is bigger than first number of pair 1
# Do the same for the second number but for if its smaller
# If it meets both conditions, add 1 to the total ranges

total = 0

dataFile = open("data.txt", "r")
pairLines = dataFile.readlines()

for pair in pairLines:
    pair = pair.rstrip("\n").split(",")

    add = False

    elf1 = range(int(pair[0].split("-")[0]), int(pair[0].split("-")[1])+1)
    elf2 = range(int(pair[1].split("-")[0]), int(pair[1].split("-")[1])+1)

    for num in elf1:
        print(num)

    for num in elf2:
        print(num)

    for area in elf1:
        if area in elf2:
            # print(area)
            add = True

    if add == True:
        total += 1

print(total)