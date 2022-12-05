# Algorithm
# Parse each box from input into its group which would be an ordered list

# prod
stacks = [[], [], [], [], [], [], [], [], []]

# example
# stacks = [[], [], []]

puzzleInput = open("data.txt", "r").readlines()

for line in puzzleInput:
    line = line.rstrip()
    if "[" in line:
        boxesIndexs = list(range(0, len(line), 4))
        for boxIndex in boxesIndexs:
            box = line[boxIndex:boxIndex+3]
            if box != "   ":
                stacks[int(boxIndex/4)].append(box)
    if "move" in line:
        # "move 1 from 2 to 1"
        # "move [qty] from [subject] to [target]""
        words = line.split(" ")
        qty = int(words[1])
        subject = int(words[3])-1
        target = int(words[5])-1

        print(stacks[target])
        for i in range(0, qty):
            print(i)
            stacks[target].insert(0, stacks[subject][0])
            del stacks[subject][0]
        print(stacks[target])
        print("-")

msg = ""

for stack in stacks:
    if len(stack) > 0:
        msg += str(stack[0]).split("[")[1].split("]")[0]

print(msg)