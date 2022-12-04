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

    stop = False
    
    # 2nd elfs 1st number is bigger than 1st elfs 1st number
    if int(pair[1].split("-")[0]) >= int(pair[0].split("-")[0]):
        # 2nd elfs 2nd number is smaller than 1st elfs 2nd number
        if int(pair[1].split("-")[1]) <= int(pair[0].split("-")[1]):
            total += 1
            continue

    # 1st elfs 1st number is bigger than 2nd elfs 1st number
    if int(pair[0].split("-")[0]) >= int(pair[1].split("-")[0]):
        # 1st elfs second number is smaller than 2nd elfs second number
        if int(pair[0].split("-")[1]) <= int(pair[1].split("-")[1]):
            total += 1
            continue

print(total)